import random
import time

# 箴言和预言库
fortunes = [
    "今天将是你的幸运日",
    "耐心是一种美德，很快会有回报",
    "旅行会给你带来新的视角",
    "一个旧友会带来好消息",
    "你的创造力将得到认可",
    "信任你的直觉，它会引导你",
    "意想不到的机会即将出现",
    "微笑是打开许多门的钥匙",
    "善良的话语可以带来巨大的回报",
    "学习永远不会浪费",
    "你的坚韧将克服任何障碍",
    "新的冒险在等待着你"
]

# 中文诗词库
chinese_poems = [
    "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
    "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。",
    "千山鸟飞绝，万径人踪灭。孤舟蓑笠翁，独钓寒江雪。",
    "海上生明月，天涯共此时。情人怨遥夜，竟夕起相思。",
    "空山新雨后，天气晚来秋。明月松间照，清泉石上流。",
    "君自故乡来，应知故乡事。来日绮窗前，寒梅著花未？",
    "红豆生南国，春来发几枝。愿君多采撷，此物最相思。"
]

# 生成随机数字（幸运数字）
def generate_lucky_numbers():
    count = random.randint(3, 6)  # 生成3-6个幸运数字
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(1, 99))
    return numbers

# 显示ASCII艺术的幸运饼干
def display_fortune_cookie():
    print("""
          .----.
       .':::::::::.
      ::::::::::::::
      :'::::::::::::
       '.:::::::::'
         ':::::'
          '::'
           '
    """)
    print("   🥠 幸运饼干 🥠")
    print("=" * 30)

# 模拟打开饼干的过程
def open_fortune_cookie():
    print("正在打开幸运饼干...")
    for i in range(3):
        print("💥" * (i + 1))
        time.sleep(0.5)
    print("\n" + "=" * 30)

# 获取随机幸运信息
def get_fortune():
    # 随机选择信息类型：箴言、诗词或数字
    fortune_type = random.choice(["fortune", "poem", "numbers"])
    
    if fortune_type == "fortune":
        return random.choice(fortunes)
    elif fortune_type == "poem":
        return random.choice(chinese_poems)
    else:
        numbers = generate_lucky_numbers()
        return f"你的幸运数字是: {', '.join(map(str, numbers))}"

# 主程序
def main():
    print("欢迎来到幸运饼干程序!")
    print("每个饼干都包含一条特别的信息...\n")
    
    while True:
        input("按回车键打开一个幸运饼干 (输入 'quit' 退出): ")
        
        user_input = input()
        if user_input.lower() == 'quit':
            print("谢谢使用，再见!")
            break
        
        display_fortune_cookie()
        open_fortune_cookie()
        
        fortune = get_fortune()
        print(f"你的幸运信息是:\n{fortune}\n")
        
        print("=" * 30)
        print()

if __name__ == "__main__":
    main()