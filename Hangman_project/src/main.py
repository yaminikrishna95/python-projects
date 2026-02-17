
import random
from words_list import words

hangman_art={0:("  ","  ","  "),
			 1:("  o ","  ","  "),
			 2:("  o  ","  | ","  "),
			 3:("  o "," /| ","  "),
			 4:("  o "," /|\\ ","  "),
			 5:("  o "," /|\\"," / "),
			 6:("  o"," /|\\ "," / \\ ")}

def display_hangman(wrong_guesses):
	print("***********")
	for i in hangman_art[wrong_guesses]:
		print(i)
	print("***********")
def display_hints(hint):
	print(" ".join(hint))

def display_answer(answer):
	print(" ".join(answer))
def main():

	answer=random.choice(words)
	hint=["_"]*len(answer)
	wrong_guesses=0
	guessed_letters=set()
	is_running=True
	while is_running:
		display_hangman(wrong_guesses)
		display_hints(hint)

		guess = input("Enter a word: ").lower()
		if len(guess)!=1 or not guess.isalpha():
			print("Invalid input")
			continue
		elif guess in guessed_letters:
			print(f"You already guessed this letter {guess}")
			continue

		if guess in answer:
			for i in range(len(answer)):
				if answer[i]==guess:
					hint[i]=guess
		else:
			wrong_guesses += 1
		if "_" not in hint:
			display_hangman(wrong_guesses)
			display_answer(answer)
			print("You win!")
			is_running=False
		elif wrong_guesses >= len(hangman_art)-1:
			display_hangman(wrong_guesses)
			display_answer(answer)
			print("You lost!")
			is_running=False



if __name__ == "__main__":
	main()

