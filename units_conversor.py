print("Unit conversor")

print()

def temp(opt):

    if opt == 1:
        x = int(input("Enter the value to be converted: "))
        y = x * 1.8 + 32
        print("Celsius (C) to Fahrenheit (F)")
        print(f"The final value is {y} Fahrenheit (F)")

    elif opt == 2:
        x = int(input("Enter the value to be converted: "))
        y = x - 273.15
        print("Kelvin (K) to Celsius (C)")
        print("The final value is {y} Celsius (C)")

    elif opt == 3:
        x = int(input("Enter the value to be converted: "))
        y = (x - 32) / 1.8
        print("Fahrenheit (F) to Celsius (C)")
        print(f"The final value is {y} Celsius (C)")

    elif opt == 4:
        x = int(input("Enter the value to be converted: "))
        y = x + 273.15
        print("Celsius (C) to Kelvin (K)")
        print(f"The final value is {y} Kelvin (K)")

def dist(opt):

    if opt == 1:
        x = int(input("Enter the value to be converted: "))
        y  = x / 1.6
        print("Kilometers (km) to Miles (mi)")
        print(f"The final value is {y} Miles (mi)")

    if opt == 2:
        x = int(input("Enter the value to be converted: "))
        y  = x / 0.3
        print("Meters (m) to Feets (ft)")
        print(f"The final value is {y} Feets (ft)")

    if opt == 3:
        x = int(input("Enter the value to be converted: "))
        y  = x / 2.54
        print("Centimeters (cm) to Inches (in)")
        print(f"The final value is {y} Inches (in)")

    if opt == 4:
        x = int(input("Enter the value to be converted: "))
        y  = x * 1.6
        print("Miles (mi) to  Kilometers (km)")
        print(f"The final value is {y} Kilometers (km)")

    if opt == 5:
        x = int(input("Enter the value to be converted: "))
        y  = x * 0.3
        print("Feet (ft) to Meters (m)")
        print(f"The final value is {y} Meters (m)")

    if opt == 6:
        x = int(input("Enter the value to be converted: "))
        y  = x * 2.54
        print("Inches (in) to Centimeters (cm)")
        print(f"The final value is {y} Centimeters (cm)")

def weig(opt):

    if opt == 1:
        x = int(input("Enter the value to be converted: "))
        y  = x / 2.2
        print("Kilograms (kg) to Libres (lb)")
        print(f"The final value is {y} Libres (lb)")

    if opt == 2:
        x = int(input("Enter the value to be converted: "))
        y  = x / 28.35
        print("Grams (g) to Ounces (oz)")
        print(f"The final value is {y} Ounces (oz)")

    if opt == 3:
        x = int(input("Enter the value to be converted: "))
        y  = x * 2.2
        print("KLibres (lb) to Kilograms (kg)")
        print(f"The final value is {y} Kilograms (kg)")

    if opt == 4:
        x = int(input("Enter the value to be converted: "))
        y  = x * 28.35
        print("Ounces (oz) to Grams (g)")
        print(f"The final value is {y} Grams (g)")


def vol(opt):

    if opt == 1:
        x = int(input("Enter the value to be converted: "))
        y  = x / 3.79
        print("Litters (L) to Gallons (gal)")
        print(f"The final value is {y} Gallons (gal)")

    if opt == 2:
        x = int(input("Enter the value to be converted: "))
        y  = x / 15
        print("Milliliters (mL) to Soup Spoons")
        print(f"The final value is {y} Soup Spoons")

    if opt == 3:
        x = int(input("Enter the value to be converted: "))
        y  = x / 5
        print("Milliliters (mL) to Teaspoons")
        print(f"The final value is {y} Teaspoons")

    if opt == 4:
        x = int(input("Enter the value to be converted: "))
        y  = x * 3.79
        print("Gallons (gal) to Litters (L)")
        print(f"The final value is {y} Litters (L)")

    if opt == 5:
        x = int(input("Enter the value to be converted: "))
        y  = x * 15
        print("Soup Spoons to Milliliters (mL)")
        print(f"The final value is {y} Milliliters (mL")

    if opt == 6:
        x = int(input("Enter the value to be converted: "))
        y  = x * 5
        print("Teaspoons to Milliliters (mL)")
        print(f"The final value is {y} Milliliters (mL)")

def vel(opt):

    if opt == 1:
        x = int(input("Enter the value to be converted: "))
        y  = x * 0.62
        print("Kilometers per Hour (km/h) to Miles per Hour (mph)")
        print(f"The final value is {y} Miles per Hour (mph)")

    if opt == 2:
        x = int(input("Enter the value to be converted: "))
        y  = x * 0.28
        print("Meter per Second (m/s) to Kilometers per Hour (km/h)")
        print(f"The final value is {y} Kilometers per Hour (km/h)")

    if opt == 3:
        x = int(input("Enter the value to be converted: "))
        y  = x / 0.62
        print("Miles per Hour (mph) to  Kilometers per Hour (km/h)")
        print(f"The final value is {y} Kilometers per Hour (km/h)")

    if opt == 4:
        x = int(input("Enter the value to be converted: "))
        y  = x / 0.28
        print("Kilometers per Hour (km/h) to Meter per Second (m/s)")
        print(f"The final value is {y} Meter per Second (m/s)")

n = int(input("Choose the desired conversion: \n"
              "1. Temperature\n"
              "2. Distance\n"
              "3. Weight\n"
              "4. Volume\n"
              "5. Velocity\n"
              "Enter: "))

if n == 1:
    m = int(input("Now choose: \n"
                  "1. Celsius (C) ⟷ Fahrenheit (F)\n"
                  "2. Celsius (C) ⟷ Kelvin (K)\n"
                  "3. Fahrenheit (F) ⟷  Celsius (C)\n"
                  "4. Kelvin (K) ⟷ Celsius (C)\n"
                  "Enter: "))
    temp(m)

elif n == 2:
    m = int(input("Now choose: \n"
                  "1. Kilometers (km) ⟷ Miles (mi)\n"
                  "2. Meters (m) ⟷ Feets (ft)\n"
                  "3. Centimeters (cm) ⟷ Inches (in)\n"
                  "4. Miles (mi) ⟷  Kilometers (km)\n"
                  "5. Feet (ft) ⟷ Meters (m)\n"
                  "6. Inches (in) ⟷ Centimeters (cm)\n"
                  "Enter: "))
    dist(m)

elif n == 3:
    m = int(input("Now choose: \n"
                  "1. Kilograms (kg) ⟷ Libres (lb)\n"
                  "2. Grams (g) ⟷ Ounces (oz)\n"
                  "3. Libres (lb) ⟷ Kilograms (kg)\n"
                  "4. Ounces (oz) ⟷ Grams (g)\n"
                  "Enter: "))
    weig(m)

elif n == 4:
    m = int(input("Now choose: \n"
                  "1. Litters (L) ⟷ Gallons (gal)\n"
                  "2. Milliliters (mL) ⟷ Soup Spoons\n"
                  "3. Milliliters (mL) ⟷ Teaspoons\n"
                  "4. Gallons (gal) ⟷ Litters (L)\n"
                  "5. Soup Spoons ⟷ Milliliters (mL)\n"
                  "6. Teaspoons ⟷ Milliliters (mL)\n"
                  "Enter: "))
    vol(m)

elif n == 5:
    m = int(input("Now choose: \n"
                  "1. Kilometers per Hour (km/h) ⟷ Miles per Hour (mph)\n"
                  "2. Meter per Second (m/s) ⟷ Kilometers per Hour (km/h)\n"
                  "3. Miles per Hour (mph) ⟷  Kilometers per Hour (km/h)\n"
                  "4. Kilometers per Hour (km/h) ⟷ Meter per Second (m/s)\n"
                  "Enter: "))
    vel(m)

