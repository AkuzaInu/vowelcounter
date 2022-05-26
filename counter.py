# This is a vowel and consonants counter
# Enter a word and it will start counting
# Made by Akuza

class Run:
	def __init__(self):
		self.vowels = ['a','o','u','e','i','y']
		self.vowelcount = 0
		self.consonantcount = 0

	def counter(self, word):
		for i in word:
			if i in self.vowels:
				self.vowelcount += 1
			else:
				self.consonantcount += 1

		print("Vowels:", self.vowelcount)
		print("Consonants:", self.consonantcount)

	def run(self):
		menu = """Vowel and consonants counter

Please enter a word to start the counting:
"""

		print(menu)
		self.word()

	def word(self):
		uinput = input(">> ")

		try:
			int(uinput)
		except:
			self.counter(uinput)
		else:
			print("You can't enter numbers.")

Run().run()