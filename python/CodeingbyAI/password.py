def check_len(pwd):
    """检查密码长度是否至少为8个字符"""
    return len(pwd) >= 8

def check_chars(pwd):
    """检查密码是否包含小写字母、大写字母、数字和特殊字符"""
    has_lower = has_upper = has_digit = has_special = False
    
    for char in pwd:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isspace():  # 非字母数字且非空格的字符视为特殊字符
            has_special = True
    
    return has_lower and has_upper and has_digit and has_special

def check_repetition(pwd, min_length=3):
    """检查密码中是否有重复的子串"""
    n = len(pwd)
    # 检查所有可能长度的重复子串
    for length in range(min_length, n//2 + 1):
        for i in range(n - 2*length + 1):
            substring = pwd[i:i+length]
            if substring in pwd[i+length:]:
                return False
    return True

def get_password_feedback(pwd):
    """提供详细的密码强度反馈"""
    feedback = []
    
    # 检查长度
    if len(pwd) < 8:
        feedback.append("密码长度至少需要8个字符")
    
    # 检查字符类型
    has_lower = has_upper = has_digit = has_special = False
    for char in pwd:
        if char.islower(): has_lower = True
        elif char.isupper(): has_upper = True
        elif char.isdigit(): has_digit = True
        elif not char.isspace(): has_special = True
    
    if not has_lower:
        feedback.append("需要至少一个小写字母")
    if not has_upper:
        feedback.append("需要至少一个大写字母")
    if not has_digit:
        feedback.append("需要至少一个数字")
    if not has_special:
        feedback.append("需要至少一个特殊字符（如!@#$%等）")
    
    # 检查重复模式
    if not check_repetition(pwd):
        feedback.append("密码中包含重复模式")
    
    return feedback

if __name__ == '__main__':
    print("请输入密码进行验证（输入'q'退出）:")
    
    while True:
        pwd = input('请输入密码: ')
        if pwd.lower() == 'q':
            print('再见!')
            break
        
        # 获取详细反馈
        feedback = get_password_feedback(pwd)
        
        if not feedback:
            print('密码强度足够! 欢迎!')
            break
        else:
            print('密码不符合要求:')
            for item in feedback:
                print(f"- {item}")
            print("请重新输入密码。")