import random
import re
import time

class DiceRoller:
    def __init__(self):
        self.dice_types = {
            'D4': 4,
            'D6': 6,
            'D8': 8,
            'D10': 10,
            'D12': 12,
            'D20': 20
        }
    
    def roll_dice(self, dice_type, count=1):
        """
        掷指定类型的骰子
        
        参数:
        dice_type -- 骰子类型 (D4, D6, D8, D10, D12, D20)
        count -- 骰子数量
        
        返回:
        骰子结果列表
        """
        if dice_type not in self.dice_types:
            raise ValueError(f"不支持的骰子类型: {dice_type}")
        
        sides = self.dice_types[dice_type]
        results = []
        
        for _ in range(count):
            result = random.randint(1, sides)
            results.append(result)
        
        return results
    
    def parse_input(self, input_str):
        """
        解析用户输入的骰子表达式
        
        参数:
        input_str -- 用户输入的骰子表达式，如 "2D6", "D20", "3D10+2D4"
        
        返回:
        解析后的骰子指令列表
        """
        # 使用正则表达式匹配骰子表达式
        pattern = r'(\d*)[dD](\d+)(?:\s*\+\s*(\d*)[dD](\d+))?'
        matches = re.findall(pattern, input_str)
        
        instructions = []
        
        for match in matches:
            # 处理第一个骰子组
            count1 = int(match[0]) if match[0] else 1
            dice_type1 = f"D{match[1]}"
            
            # 检查骰子类型是否支持
            if dice_type1 not in self.dice_types:
                raise ValueError(f"不支持的骰子类型: {dice_type1}")
            
            instructions.append((dice_type1, count1))
            
            # 处理第二个骰子组（如果有）
            if match[2] or match[3]:
                count2 = int(match[2]) if match[2] else 1
                dice_type2 = f"D{match[3]}"
                
                if dice_type2 not in self.dice_types:
                    raise ValueError(f"不支持的骰子类型: {dice_type2}")
                
                instructions.append((dice_type2, count2))
        
        return instructions
    
    def roll_from_instructions(self, instructions):
        """
        根据指令列表掷骰子
        
        参数:
        instructions -- 骰子指令列表，每个元素为(骰子类型, 数量)
        
        返回:
        包含所有骰子结果的字典
        """
        all_results = {}
        total = 0
        
        for dice_type, count in instructions:
            results = self.roll_dice(dice_type, count)
            all_results[f"{count}{dice_type}"] = results
            total += sum(results)
        
        all_results["总计"] = total
        return all_results
    
    def display_results(self, results):
        """
        显示骰子结果
        
        参数:
        results -- 骰子结果字典
        """
        print("\n🎲 骰子结果 🎲")
        print("=" * 30)
        
        for key, value in results.items():
            if key != "总计":
                if isinstance(value, list) and len(value) > 1:
                    print(f"{key}: {value} (总和: {sum(value)})")
                else:
                    print(f"{key}: {value}")
        
        print("-" * 30)
        print(f"总计: {results['总计']}")
        print("=" * 30)

def main():
    roller = DiceRoller()
    
    print("欢迎使用骰子模拟器!")
    print("支持的骰子类型: D4, D6, D8, D10, D12, D20")
    print("输入格式示例:")
    print("  - 单个骰子: D20")
    print("  - 多个骰子: 3D6")
    print("  - 组合骰子: 2D8+1D4")
    print("输入 'quit' 退出程序")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\n请输入骰子指令: ").strip()
            
            if user_input.lower() == 'quit':
                print("感谢使用骰子模拟器，再见!")
                break
            
            if not user_input:
                continue
            
            # 解析用户输入
            instructions = roller.parse_input(user_input)
            
            if not instructions:
                print("无法解析输入，请使用正确格式")
                continue
            
            # 模拟掷骰子动画
            print("掷骰子中", end="")
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.3)
            print()
            
            # 掷骰子并显示结果
            results = roller.roll_from_instructions(instructions)
            roller.display_results(results)
            
        except ValueError as e:
            print(f"错误: {e}")
        except Exception as e:
            print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()