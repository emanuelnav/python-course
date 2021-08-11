def palindromo(string):
    string = (string.replace(' ', '')).lower()
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    op = input("Ingrese una palabra: ")
    try:
        print(palindromo(op))
    except TypeError:
        print("Solo se pueden ingresar strings")


if __name__ == "__main__":
    run()