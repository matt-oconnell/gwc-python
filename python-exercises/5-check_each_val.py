word = 'coolio'
output_list = []

for char in word:
  if char == 'o':
    output_list.append('_')
  else:
    output_list.append(char)

print(output_list)
