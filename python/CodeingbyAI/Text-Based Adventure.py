import os
import time
import random

class TextAdventureGame:
    def __init__(self):
        self.player_name = ""
        self.player_health = 100
        self.player_inventory = []
        self.current_room = "start"
        self.game_over = False
        self.rooms = self.create_rooms()
        self.map_data = self.create_map()
        
    def create_rooms(self):
        """创建游戏房间和它们的描述"""
        rooms = {
            "start": {
                "name": "起点房间",
                "description": "你处在一个昏暗的房间中。四周是石墙，墙上挂着火把。\n房间里有一张桌子和一把椅子。",
                "exits": {"east": "hallway", "south": "storage"},
                "items": ["火把", "钥匙"],
                "ascii_art": """
                ┌─────────────┐
                │             │
                │     🚪     │
                │             │
                │     🧍     │
                │             │
                └─────────────┘
                """
            },
            "hallway": {
                "name": "走廊",
                "description": "一条长长的走廊，墙上挂着古老的画作。\n走廊的尽头有一扇门。",
                "exits": {"west": "start", "east": "library", "south": "garden"},
                "items": ["画作"],
                "ascii_art": """
                ┌─────────────────┐
                │        🖼️       │
                │                 │
                │        🚶       │
                │                 │
                │        🖼️       │
                └─────────────────┘
                """
            },
            "library": {
                "name": "图书馆",
                "description": "一个满是灰尘的图书馆。书架上摆满了古老的书籍。\n房间中央有一张书桌，上面放着一本打开的书。",
                "exits": {"west": "hallway", "south": "study"},
                "items": ["古老的书", "魔法卷轴"],
                "ascii_art": """
                ┌─────────────┐
                │ 📚 📚 📚   │
                │             │
                │     🪑      │
                │     📖      │
                │             │
                └─────────────┘
                """
            },
            "study": {
                "name": "书房",
                "description": "一个小巧的书房，墙上挂着一张地图。\n书桌上有一盏油灯和一些文件。",
                "exits": {"north": "library", "east": "secret_room"},
                "items": ["地图", "油灯"],
                "ascii_art": """
                ┌─────────────┐
                │     🗺️      │
                │             │
                │     🪑      │
                │     💡      │
                │             │
                └─────────────┘
                """
            },
            "secret_room": {
                "name": "秘密房间",
                "description": "一个隐藏的房间！墙上闪烁着神秘的符文。\n房间中央有一个宝箱。",
                "exits": {"west": "study"},
                "items": ["宝箱", "神秘符文"],
                "ascii_art": """
                ┌─────────────┐
                │    ✨       │
                │   🧿 🧿     │
                │     🎁      │
                │   🧿 🧿     │
                │    ✨       │
                └─────────────┘
                """
            },
            "storage": {
                "name": "储藏室",
                "description": "一个杂乱的储藏室，堆满了箱子和桶。\n空气中弥漫着霉味。",
                "exits": {"north": "start", "east": "garden"},
                "items": ["桶", "绳子"],
                "ascii_art": """
                ┌─────────────┐
                │     🪣      │
                │   📦 📦    │
                │     🪣      │
                │   📦 📦    │
                │             │
                └─────────────┘
                """
            },
            "garden": {
                "name": "花园",
                "description": "一个荒废的花园，杂草丛生。\n中央有一口枯井，旁边有一把生锈的铲子。",
                "exits": {"north": "hallway", "west": "storage"},
                "items": ["铲子", "枯井"],
                "ascii_art": """
                ┌─────────────┐
                │    🌿 🌿   │
                │  🌿    🌿   │
                │     🕳️      │
                │  🌿    🌿   │
                │    🌿 🌿   │
                └─────────────┘
                """
            }
        }
        return rooms
    
    def create_map(self):
        """创建游戏地图的ASCII表示"""
        map_art = """
        🏰 文本冒险游戏地图 🏰
        
        ┌─────────┬─────────┬─────────┐
        │ 储藏室  │  起点   │  走廊   │
        │         │         │         │
        │    📦   │    🧍   │    🖼️   │
        ├─────────┼─────────┼─────────┤
        │  花园   │         │ 图书馆  │
        │         │         │         │
        │    🌿   │         │    📚   │
        ├─────────┴─────────┼─────────┤
        │     书房          │         │
        │                   │         │
        │       🗺️          │         │
        ├───────────────────┼─────────┤
        │     秘密房间      │         │
        │                   │         │
        │       🎁          │         │
        └───────────────────┴─────────┘
        
        使用方向命令移动 (north, south, east, west)
        """
        return map_art
    
    def clear_screen(self):
        """清空屏幕"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_intro(self):
        """显示游戏介绍"""
        self.clear_screen()
        print("""
        🏰 欢迎来到文本冒险游戏! 🏰
        
        在这个游戏中，你将探索一个神秘的城堡。
        使用命令移动、收集物品并解决谜题。
        
        可用命令:
        - north, south, east, west: 移动方向
        - look: 查看当前房间
        - take [物品]: 拾取物品
        - inventory: 查看背包
        - map: 显示地图
        - use [物品]: 使用物品
        - quit: 退出游戏
        
        按回车键开始游戏...
        """)
        input()
    
    def display_room(self):
        """显示当前房间的信息"""
        room = self.rooms[self.current_room]
        self.clear_screen()
        print(f"\n当前位置: {room['name']}")
        print("=" * 40)
        print(room['ascii_art'])
        print(room['description'])
        
        # 显示出口
        exits = ", ".join(room['exits'].keys())
        print(f"\n可用的出口: {exits}")
        
        # 显示物品
        if room['items']:
            items = ", ".join(room['items'])
            print(f"房间内的物品: {items}")
        
        print("=" * 40)
    
    def process_command(self, command):
        """处理玩家输入的命令"""
        command = command.lower().strip()
        
        if command in ["north", "south", "east", "west"]:
            self.move_player(command)
        elif command == "look":
            self.display_room()
        elif command.startswith("take "):
            item = command[5:]
            self.take_item(item)
        elif command == "inventory":
            self.show_inventory()
        elif command == "map":
            self.show_map()
        elif command.startswith("use "):
            item = command[4:]
            self.use_item(item)
        elif command == "quit":
            print("感谢游玩! 再见!")
            self.game_over = True
        else:
            print("我不明白这个命令。尝试 'north', 'south', 'east', 'west', 'look', 'take [物品]', 'inventory', 'map', 'use [物品]', 或 'quit'.")
    
    def move_player(self, direction):
        """移动玩家到新的房间"""
        room = self.rooms[self.current_room]
        
        if direction in room['exits']:
            self.current_room = room['exits'][direction]
            print(f"你向{direction}移动...")
            time.sleep(1)
            self.display_room()
            
            # 特殊房间事件
            if self.current_room == "secret_room" and "钥匙" not in self.player_inventory:
                print("\n门是锁着的! 你需要找到钥匙才能进入。")
                self.current_room = "study"  # 返回书房
                time.sleep(2)
                self.display_room()
        else:
            print("你不能往那个方向移动!")
    
    def take_item(self, item):
        """从房间中拾取物品"""
        room = self.rooms[self.current_room]
        
        if item in room['items']:
            room['items'].remove(item)
            self.player_inventory.append(item)
            print(f"你拾取了 {item}.")
            
            # 特殊物品事件
            if item == "钥匙":
                print("这把钥匙看起来很古老，可能能打开某扇门。")
        else:
            print(f"房间里没有 {item}.")
    
    def show_inventory(self):
        """显示玩家背包"""
        if self.player_inventory:
            print("你的背包:")
            for item in self.player_inventory:
                print(f"  - {item}")
        else:
            print("你的背包是空的.")
    
    def show_map(self):
        """显示游戏地图"""
        self.clear_screen()
        print(self.map_data)
        input("\n按回车键返回游戏...")
        self.display_room()
    
    def use_item(self, item):
        """使用物品"""
        if item in self.player_inventory:
            if item == "钥匙" and self.current_room == "study":
                print("你使用钥匙打开了秘密通道!")
                # 添加通往秘密房间的出口
                self.rooms["study"]["exits"]["east"] = "secret_room"
                self.player_inventory.remove(item)
                time.sleep(2)
                self.display_room()
            else:
                print(f"你使用了 {item}, 但似乎没什么发生。")
        else:
            print(f"你的背包里没有 {item}.")
    
    def play(self):
        """开始游戏"""
        self.display_intro()
        
        # 获取玩家名称
        self.player_name = input("请输入你的名字: ")
        print(f"欢迎, {self.player_name}!")
        time.sleep(1)
        
        # 显示起始房间
        self.display_room()
        
        # 游戏主循环
        while not self.game_over:
            command = input("\n你想做什么? ").strip()
            self.process_command(command)
            
            # 检查游戏结束条件
            if self.current_room == "secret_room" and "宝箱" in self.rooms["secret_room"]["items"]:
                print("\n恭喜! 你找到了宝藏! 游戏胜利!")
                self.game_over = True

# 启动游戏
if __name__ == "__main__":
    game = TextAdventureGame()
    game.play()