def esPalindromo(word):
	word = (word.replace(' ', '')).lower()
	if word == word[::-1]:
		return True
	else:
		return False

def run():
	word = input("Ingrese una palabra: \n")
	if esPalindromo(word):
		print("Es Palindromo")
	else:
		print("No es Palindromo")


if __name__ == '__main__':
	run()