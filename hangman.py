def hangman():
	stage =0
	wrong_guesses = ['','_______    ', '|     |     ', '|     O     ', '|     /|\    ', '|     /\    ', '|         ']
	word = 'cat'
	score_board = ['__'] * len(word)
	win = False
	print('welcome to hangman')
	while stage<len(wrong_guesses)-1:
		print('\n')
		guess = input('guess a letter')
		if guess in word:
			score_board[word.index(guess)]=guess
		else:
			stage+=1
		print(''.join(score_board))
		print('\n'.join(wrong_guesses[0:stage+1]))
		if '__' not in score_board:
			print('You win, the word was:')
			print(' '.join(score_board))
			win = True
			break
	if not win:
		print('\n'.join(wrong_guesses[0:stage]))
		print('you lose')

hangman()
			