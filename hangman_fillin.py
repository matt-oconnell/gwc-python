# get original word. turn into a list
original_word = input('choose a word')
original_list = list(original_word)

# create underline list based off of original list
underline_list = []
original_list_length = ## FILL IN - length of original_list
for i in range(original_list_length):
  ##  FILL IN - create an array like ["_", "_", "_"] of length of original list

# total lives to start with
lives = 3

while True:
  ## FILL IN - check if lives are less than 1. If so, print a line about losing the game and break the loop
  
  # when there are no more letters to guess, there will be no underscores left
  if '_' not in underline_list:
    print('You win!', underline_list)
    break

  print(underline_list)
  guessed_letter = input('Choose a letter. You have ' + str(lives) + ' lives.')
  
  ## FILL IN - if guessed_letter is not in original list than subtract 1 from lives

  ## FILL IN - create a loop using range where we go through each letter in the original_list
    ## FILL IN - at each letter, check if the guessed_letter matches the current element from the original list
    ## FILL IN - if it does, update the underline_list at this index
