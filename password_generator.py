import random

n = int(input("Digite o comprimento da senha: "))
password = ''

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"
                   "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
simbols = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-" ".",
            "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`",
            "{", "|", "}", "~", " ", "/"]

list_of_lists = [numbers, capital_letters, lowercase_letters, simbols]

cont = 0

while cont < n:

    random_inner_list = random.choice(list_of_lists)

    random_element = random.choice(random_inner_list)

    password += random_element

    cont += 1

print(password)