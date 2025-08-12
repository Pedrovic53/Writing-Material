height = int(input('What is Ur height(cm)?'))
credits = int(input('How many credits do U have?'))

if height >= 137 and credits >= 10:
    print('Enjoy the ride!')
elif height < 137 and credits >= 10:
    print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
    print('You don\'t have enough credits.')
else:
    print('Fuck off!')