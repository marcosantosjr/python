#
# Paste the data you wish to graph in tab-delimited rows in the format:
#
#       xdata <tab> ydata
#
# In this example the xdata is time (s) and y data is y position (cm)
#


data = """
0.000000000E0	-2.688162330E0
3.336670003E-2	-4.301059729E0
6.673340007E-2	-5.376324661E0
1.001001001E-1	-6.989222059E0
1.334668001E-1	-1.129028179E1
1.668335002E-1	-1.451607658E1
2.002002002E-1	-2.043003371E1
2.335669002E-1	-2.526872591E1
2.669336003E-1	-3.118268303E1
3.003003003E-1	-3.870953756E1
3.336670003E-1	-4.623639208E1
3.670337004E-1	-5.430087907E1
4.004004004E-1	-6.236536606E1
4.337671004E-1	-7.150511799E1
4.671338005E-1	-8.010723744E1
5.005005005E-1	-8.924698937E1
5.338672005E-1	-9.892437376E1
5.672339006E-1	-1.080641257E2
6.006006006E-1	-1.177415101E2
6.339673006E-1	-1.274188945E2
6.673340007E-1	-1.370962788E2
7.007007007E-1	-1.467736632E2
7.340674007E-1	-1.575263126E2
7.674341008E-1	-1.672036969E2
8.008008008E-1	-1.768810813E2
8.341675008E-1	-1.865584657E2
8.675342009E-1	-1.973111150E2
9.009009009E-1	-2.075261319E2
9.342676009E-1	-2.182787812E2
9.676343010E-1	-2.284937981E2
""".split('\n')  # split this string on the "newline" character.

# print len(data)


#
# The data is stored in a single string. Now, split the data and store
# each column in a list. Convert the data from a string to a float.
#

tlist = []
ylist = []
for s in data:
    if s:
        t, y = s.split()  # split the string in two
        t = float(t)  # convert time to float
        y = float(y) / 100.0  # convert y-position (cm) to float in meters
        tlist.append(t)  # append to the list for time data
        ylist.append(y)  # append to the list for y-position data

# print "tlist=",tlist
# print "ylist=",ylist

import matplotlib.pyplot as plt

plt.title('y-position vs. time for falling cupcake paper')
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.plot(tlist, ylist, 'm.')
plt.show()

def _MultiDeviceAddN(tensor_list, gradient_uid):
  """Adds tensors from potentially multiple devices."""
  # Basic function structure comes from control_flow_ops.group().
  # Sort tensors according to their devices.
  tensors_on_device = collections.defaultdict(lambda: [])
  for tensor in tensor_list:
    tensors_on_device[tensor.device].append(tensor)

  # For each device, add the tensors on that device first.
  # Then gather the partial sums from multiple devices.
  # TODO(sjhwang): Create hierarchical aggregation tree as pbar's suggestion.
  # E.g., aggregate per GPU, then per task, and so on.
  summands = []

  def DeviceKey(dev):
    return "" if dev is None else dev

  for dev in sorted(tensors_on_device, key=DeviceKey):
    tensors = tensors_on_device[dev]
    with ops._colocate_with_for_gradient(  # pylint: disable=protected-access
        tensors[0].op,
        gradient_uid,
        ignore_existing=True):
      summands.append(math_ops.add_n(tensors))

  return math_ops.add_n(summands)


@tf_export("AggregationMethod")
class AggregationMethod(object):
  """A class listing aggregation methods used to combine gradients.
  Computing partial derivatives can require aggregating gradient
  contributions. This class lists the various methods that can
  be used to combine gradients in the graph.
  The following aggregation methods are part of the stable API for
  aggregating gradients:
  *  `ADD_N`: All of the gradient terms are summed as part of one
     operation using the "AddN" op (see `tf.add_n`). This
     method has the property that all gradients must be ready and
     buffered separately in memory before any aggregation is performed.
  *  `DEFAULT`: The system-chosen default aggregation method.
  The following aggregation methods are experimental and may not
  be supported in future releases:
  * `EXPERIMENTAL_TREE`: Gradient terms are summed in pairs using
    using the "AddN" op. This method of summing gradients may reduce
    performance, but it can improve memory utilization because the
    gradients can be released earlier.
  """
  ADD_N = 0
  DEFAULT = ADD_N
  # The following are experimental and may not be supported in future releases.
  EXPERIMENTAL_TREE = 1
  EXPERIMENTAL_ACCUMULATE_N = 2  # An alias for EXPERIMENTAL_ADD_N = 1


def _AggregatedGrads(grads,
                     op,
                     gradient_uid,
                     loop_state,
                     aggregation_method=None):
  """Get the aggregated gradients for op.
  Args:
    grads: The map of memoized gradients.
    op: The op to get gradients for.
    gradient_uid: A unique identifier within the graph indicating
      which invocation of gradients is being executed. Used to cluster
      ops for compilation.
    loop_state: An object for maintaining the state of the while loops in the
                graph. It is of type ControlFlowState. None if the graph
                contains no while loops.
    aggregation_method: Specifies the method used to combine gradient terms.
      Accepted values are constants defined in the class `AggregationMethod`.
  Returns:
    A list of gradients, one per each output of `op`. If the gradients
      for a particular output is a list, this function aggregates it
      before returning.
  Raises:
    TypeError: if the incoming grads are not Tensors or IndexedSlices.
    ValueError: if the arguments are invalid.
  """
  if aggregation_method is None:
    aggregation_method = AggregationMethod.DEFAULT
  if aggregation_method not in [
      AggregationMethod.ADD_N, AggregationMethod.EXPERIMENTAL_TREE,
      AggregationMethod.EXPERIMENTAL_ACCUMULATE_N
  ]:
    raise ValueError(
        "Invalid aggregation_method specified %s." % aggregation_method)
  out_grads = _GetGrads(grads, op)
  for i, out_grad in enumerate(out_grads):
    if loop_state:
      if isinstance(out_grad, (ops.Tensor, ops.IndexedSlices)):
        assert control_flow_util.IsLoopSwitch(op)
        continue
    # Grads have to be Tensors or IndexedSlices
    if (isinstance(out_grad, collections_abc.Sequence) and not all(
        isinstance(g, (ops.Tensor, ops.IndexedSlices))
        for g in out_grad
        if g is not None)):
      raise TypeError("gradients have to be either all Tensors "
                      "or all IndexedSlices")
    # Aggregate multiple gradients, and convert [] to None.
    if out_grad:
      if len(out_grad) < 2:
        used = "nop"
        out_grads[i] = out_grad[0]
      elif all(isinstance(g, ops.Tensor) for g in out_grad if g is not None):
        tensor_shape = _AccumulatorShape(out_grad)
        if aggregation_method in [
            AggregationMethod.EXPERIMENTAL_TREE,
            AggregationMethod.EXPERIMENTAL_ACCUMULATE_N
        ]:
          # Aggregate all gradients by doing pairwise sums: this may
          # reduce performance, but it can improve memory because the
          # gradients can be released earlier.
          #
          # TODO(vrv): Consider replacing this with a version of
          # tf.AddN() that eagerly frees its inputs as soon as they are
          # ready, so the order of this tree does not become a problem.
          used = "tree"
          with ops.name_scope(op.name + "_gradient_sum"):
            running_sum = out_grad[0]
            for grad in out_grad[1:]:
              running_sum = math_ops.add_n([running_sum, grad])
            out_grads[i] = running_sum
        else:
          used = "add_n"
          out_grads[i] = _MultiDeviceAddN(out_grad, gradient_uid)
        logging.vlog(2, "  _AggregatedGrads %d x %s using %s", len(out_grad),
                     tensor_shape, used)
      else:
        out_grads[i] = backprop.aggregate_indexed_slices_gradients(out_grad)  # pylint: disable=protected-access
    else:  # not out_grad
      # out_grads[i] is [], thus its aggregation is simply None.
      out_grads[i] = None
  return out_grads


# Represents the output of TFE_Py_TapeSetPossibleGradientTypes. Real enums are
# unfortunately too slow to use here.
POSSIBLE_GRADIENT_TYPES_NONE = 0
POSSIBLE_GRADIENT_TYPES_FIRST_ORDER = 1
POSSIBLE_GRADIENT_TYPES_HIGHER_ORDER = 2


def PossibleTapeGradientTypes(tensors):
  """Determines whether and how `args` may require tape gradients."""
  return pywrap_tfe.TFE_Py_TapeSetPossibleGradientTypes(tensors)
