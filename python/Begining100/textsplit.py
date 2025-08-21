import re
from collections import Counter

def get_char(txt):
    # 使用更准确的正则表达式分割单词
    # 匹配一个或多个非字母数字字符作为分隔符
    words = re.split(r'[^\w]+', txt)
    
    # 过滤掉空字符串并将所有单词转为小写
    words = [word.lower() for word in words if word]
    
    # 使用Counter计数更高效
    word_count = Counter(words)
    
    # 按词频排序
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

if __name__ == '__main__':
    try:
        # 指定文件编码，避免编码问题
        with open('test.txt', 'r', encoding='utf-8') as file:
            vtxt = file.read()
        vlts = get_char(vtxt)
        print("单词统计结果:")
        for word, count in vlts:
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("错误: 找不到文件 'test.txt'")
    except Exception as e:
        print(f"发生错误: {e}")