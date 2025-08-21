i = 0
while True:
    reply = input('Enter text')
    if reply == 'stop': break
    print(reply.upper())
    i = i+1
    print('You have tired', i, 'times')