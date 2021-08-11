def divisors(n):
    # divisors = []
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         divisors.append(i)
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors


def run():
    # try:
    #     num = int(input("Ingrese un numero: "))
    #     if num < 0:
    #         raise ValueError("Ingrese un valor entero positivo")
    #     print(divisors(num))
    # except ValueError as ve:
    #     print(ve)
    num = input("Ingrese un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero entero"
    num = int(num)
    print(divisors(num))


if __name__ == "__main__":
    run()