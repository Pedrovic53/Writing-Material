import string

def passwd_pre(pwd):
    """将密码中的字符按照特定规则替换"""
    vret = []
    for char in pwd:
        if char in 'abc':
            char = '!'
        elif char in 'def':
            char = '@'
        elif char in 'ghi':
            char = '#'
        elif char in 'jkl':
            char = '$'
        elif char in 'mno':  # 添加缺失的映射
            char = '%'
        elif char in 'pqr':
            char = '^'
        elif char in 'stu':
            char = '&'
        elif char in 'vwx':
            char = '*'
        elif char in 'yz':
            char = '('
        elif char == 'Z':  # 单独处理大写Z
            char = 'a'
        elif char.isupper():
            # 将大写字母转换为小写并后移一位
            char = chr(ord(char.lower()) + 1)
        vret.append(char)
    return ''.join(vret)  # 修正缩进，在循环结束后返回

def change_txt(pwd, str1, str2):
    """根据映射表替换文本中的字符"""
    vret = ''
    pwd = pwd.lower()
    for char in pwd:
        j = str1.find(char)
        if j == -1:
            vret = vret + char
        else:
            vret = vret + str2[j]  # 修正：使用索引而不是函数调用
    return vret

if __name__ == '__main__':
    # 测试 passwd_pre 函数
    test_password = "HelloWorldZ"
    print("Original:", test_password)
    print("Processed:", passwd_pre(test_password))
    
    # 测试 change_txt 函数
    result = change_txt('Python', string.ascii_letters, 'qwerdagsjdgajhkjhhosadk')
    print("Change txt result:", result)