# Примитивный калькуляхтор

print ("калькулятор")
a = input ("Введите число затем нажмите \"Enter\"\n")
simbol = input ("Введите символ +, -, *, /.\n затем нажмите \"Enter\"\n")
b = input ("Введите число\n затем нажмите \"Enter\"\n")
if simbol == ("+"):
    print (int (a) + int (b))
if simbol == ("-"):
    print (int (a) - int (b))
if simbol == ("*"):
    print (int (a) * int (b))
if simbol == ("/"):
    print (int (a) / int (b))
