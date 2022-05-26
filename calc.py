# Примитивный калькуляхтор
def calc():
    print ("калькулякТор'т")
    a = input ("Введите число затем нажмите \"Enter\"\n")
    simbol = input ("Введите символ +, -, *, /.\nзатем нажмите \"Enter\"\n")
    b = input ("Введите число\nзатем нажмите \"Enter\"\n")
    if simbol == ("+"):
        print (int (a) + int (b))
    if simbol == ("-"):
        print (int (a) - int (b))
    if simbol == ("*"):
        print (int (a) * int (b))
    if simbol == ("/"):
        print (int (a) / int (b))
        
    calc()
    
while True:
    q = input ("запустить калькуляхтр? (да/нет): ")
    
    if q == ("да"):
        calc()
    else:
        break
