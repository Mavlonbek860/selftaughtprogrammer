class Word:
	
	def __init__(self, word, turkum, translations=[]):
		self._word = word
		self._turkum = turkum
		self._translations = translations
	
	def __str__(self):
		string = self._word + ': ' + self._turkum + '\n\t'
		for s in self._translations:
			string += s + '\n\t'
		return string
	
	def add_translation(self, tra):
		self._translations.append(tra)

word = open('word.txt', 'r')
