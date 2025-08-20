#第一种解法
def fab(n):
# n表示第n项
    if n <= 0:
        return '非法数据'
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        a,b = 0,1
        # 第一项是0, 第二项是1
        fab_lst = [0,1]
        for i in range(n-2):
        # n-2的原因是：列表中已经有两项了
            a,b = b, a+b
            fab_lst.append(b)
        return fab_lst
print(fab(n=11))

# 第二种解法
def fibonacci(n):
    a = 0
    b = 1
    
    # Check if n is less than 0
    if n < 0:
        print("Incorrect input")
        
    # Check if n is equal to 0
    elif n == 0:
        return 0
      
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(9))