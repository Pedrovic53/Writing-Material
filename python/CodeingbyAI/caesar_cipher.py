def caesar_cipher(text, shift, mode='encrypt'):
    """
    凯撒加密/解密函数
    
    参数:
    text -- 要加密/解密的文本
    shift -- 移位量 (整数)
    mode -- 'encrypt' 加密 或 'decrypt' 解密
    
    返回:
    加密或解密后的文本
    """
    result = ""
    
    # 确保移位量在0-25之间
    shift = shift % 26
    
    # 如果是解密模式，使用负移位量
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # 判断是大写字母还是小写字母
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # 应用凯撒移位
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # 非字母字符保持不变
            result += char
    
    return result

def main():
    """主函数，提供用户交互界面"""
    print("凯撒加密/解密工具")
    print("=" * 30)
    
    while True:
        # 获取用户输入
        mode = input("请选择模式 (1-加密, 2-解密, 0-退出): ").strip()
        
        if mode == '0':
            print("程序已退出。")
            break
        elif mode not in ['1', '2']:
            print("无效选择，请重新输入。")
            continue
        
        # 获取文本和移位量
        text = input("请输入文本: ")
        
        try:
            shift = int(input("请输入移位量 (0-25): "))
            if not 0 <= shift <= 25:
                print("移位量必须在0-25之间，请重新输入。")
                continue
        except ValueError:
            print("无效的移位量，请输入0-25之间的整数。")
            continue
        
        # 执行加密或解密
        if mode == '1':
            result = caesar_cipher(text, shift, 'encrypt')
            print(f"加密结果: {result}")
        else:
            result = caesar_cipher(text, shift, 'decrypt')
            print(f"解密结果: {result}")
        
        print()  # 空行分隔

# 暴力破解凯撒密码（当不知道移位量时）
def brute_force_caesar(cipher_text):
    """尝试所有可能的移位量来破解凯撒密码"""
    print("尝试所有可能的解密:")
    print("-" * 40)
    
    for shift in range(26):
        decrypted = caesar_cipher(cipher_text, shift, 'decrypt')
        print(f"移位量 {shift:2d}: {decrypted}")

if __name__ == "__main__":
    main()

# 使用示例
# brute_force_caesar("Khoor, Zruog!")