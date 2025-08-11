ph_levels = int(input('Type a value between 0 and 14 '))

if ph_levels > 7:
  print('Basic')
elif ph_levels < 7:
  print('Acidic')
else:
  print('Neutral')