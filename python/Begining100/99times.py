#Asterisks
for i in range(1, 25) :
  print("* " * i)

#九九乘法表
for i in range(1,10): 
#循环会执行9次
    for j in range(1,i+1): 
    #不包含i+1
        print(f'{j} * {i} = {i*j}', end = ' ') 
    print()
    #空的print()的作用是换行

