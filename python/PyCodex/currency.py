pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))
CNY = pesos*0.13 + soles*1.98 + reais*1.24
print(CNY)