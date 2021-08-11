from math import factorial

def  esPrimo(num):
    # flag = True
    # for i in range(2, num):
    #     if num % i == 0:
    #         flag = False
    #         break
    # if num == 1:
    #     flag = False
    # return flag
    if (factorial(num-1)+1) % num == 0:  #Utilizando el teorema de Wilson
        return True
    else:
        return False


def run():
    print("""Programa de prueba de primalidad

Dado un numero, el programa te devuelve si es un numero primo o no
""")
    num = int(input("Ingrese un numero \n"))
    if esPrimo(num):
        print("{} es un numero primo".format(num))
    else:
        print("{} No es un numero primo".format(num))

if __name__ == '__main__':
    run()
