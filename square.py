from functools import reduce

def run():
    numbers = [1, 2, 3, 4, 5, 6]
    # square = [i**2 for i in numbers]
    square = list(map(lambda x: x**2, numbers))
    print(square)


if __name__ == "__main__":
    run()
