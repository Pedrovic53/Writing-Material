num = int(input('Type an integer: '))

total = 0

for i in range(1,num + 1):
  total += i ** 2
  print(total)