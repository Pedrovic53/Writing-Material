import json
import os
import datetime
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
try:
    from waveshare_epd import epd2in13  # Waveshare e-ink library (adjust for your model)
except ImportError:
    epd2in13 = None  # Fallback if library not installed

class XiaoLiuRen:
    def __init__(self, filename='divinations.json'):
        self.filename = filename
        self.palaces = [
            {"name": "大安 (Da An)", "meaning": "吉祥，事情顺利，平安无事。 (Good fortune, things proceed smoothly, safe and sound.)"},
            {"name": "留连 (Liu Lian)", "meaning": "迟滞，事情进展缓慢，需耐心等待。 (Delay, things progress slowly, patience required.)"},
            {"name": "速喜 (Su Du)", "meaning": "快速喜讯，事情很快有好结果。 (Quick joy, things will soon yield good results.)"},
            {"name": "赤口 (Chi Kou)", "meaning": "口舌是非，需谨慎言行。 (Gossip or disputes, be cautious with words and actions.)"},
            {"name": "小吉 (Xiao Ji)", "meaning": "小有吉利，事情有小成。 (Minor good fortune, small success in matters.)"},
            {"name": "空亡 (Kong Wang)", "meaning": "不利，事情可能落空，需重新计划。 (Unfavorable, things may fail, need to replan.)"}
        ]
        self.divinations = self.load_divinations()

    def load_divinations(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_divination(self, question, palace_index, timestamp):
        divination = {
            "timestamp": timestamp,
            "question": question,
            "palace": self.palaces[palace_index]["name"],
            "meaning": self.palaces[palace_index]["meaning"]
        }
        self.divinations.append(divination)
        with open(self.filename, 'w') as f:
            json.dump(self.divinations, f, indent=4, ensure_ascii=False)

    def calculate_palace(self, month, day, hour):
        return (month + day + hour - 1) % 6

    def divine(self, question, month, day, hour):
        palace_index = self.calculate_palace(month, day, hour)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.save_divination(question, palace_index, timestamp)
        return self.palaces[palace_index]

    def render_to_image(self, question, palace):
        image = Image.new('1', (250, 122), 255)  # 250x122 for 2.13-inch e-ink
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
        except:
            font = ImageFont.load_default()
        y = 10
        draw.text((10, y), "小六壬占卜", font=font, fill=0)
        y += 20
        draw.text((10, y), f"问题: {question[:20]}", font=font, fill=0)  # Truncate for space
        y += 20
        draw.text((10, y), f"结果: {palace['name']}", font=font, fill=0)
        y += 20
        draw.text((10, y), f"释义: {palace['meaning'][:30]}", font=font, fill=0)  # Truncate for space
        return image

    def display_on_eink(self, image):
        if epd2in13 is None:
            print("E-ink library not available. Image saved as 'divination.png'.")
            image.save('divination.png')
            return
        try:
            epd = epd2in13.EPD()
            epd.init()
            epd.display(epd.getbuffer(image))
            epd.sleep()
        except Exception as e:
            print(f"E-ink display error: {e}")
            image.save('divination.png')

class XiaoLiuRenGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("小六壬占卜")
        self.geometry("400x500")
        self.xlr = XiaoLiuRen()
        
        # GUI Elements
        tk.Label(self, text="小六壬占卜程序", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self, text="问题:").pack()
        self.question_entry = tk.Entry(self, width=30)
        self.question_entry.pack()
        
        tk.Label(self, text="农历月 (1-12，留空随机):").pack()
        self.month_entry = tk.Entry(self, width=10)
        self.month_entry.pack()
        
        tk.Label(self, text="农历日 (1-30，留空随机):").pack()
        self.day_entry = tk.Entry(self, width=10)
        self.day_entry.pack()
        
        tk.Label(self, text="时辰 (1-12，留空随机):").pack()
        self.hour_entry = tk.Entry(self, width=10)
        self.hour_entry.pack()
        
        tk.Button(self, text="占卜", command=self.perform_divination).pack(pady=10)
        tk.Button(self, text="显示到墨水屏", command=self.display_to_eink).pack(pady=5)
        
        self.result_label = tk.Label(self, text="", wraplength=350, justify="left")
        self.result_label.pack(pady=10)
        
        self.last_image = None  # Store last rendered image for e-ink

    def perform_divination(self):
        question = self.question_entry.get().strip()
        if not question:
            messagebox.showerror("错误", "请输入一个问题！")
            return
        
        try:
            month = self.month_entry.get().strip()
            month = int(month) if month else random.randint(1, 12)
            day = self.day_entry.get().strip()
            day = int(day) if day else random.randint(1, 30)
            hour = self.hour_entry.get().strip()
            hour = int(hour) if hour else random.randint(1, 12)
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字（或留空使用随机数）！")
            return
        
        result = self.xlr.divine(question, month, day, hour)
        self.result_label.config(text=f"结果: {result['name']}\n释义: {result['meaning']}")
        self.last_image = self.xlr.render_to_image(question, result)

    def display_to_eink(self):
        if self.last_image is None:
            messagebox.showerror("错误", "请先进行占卜！")
            return
        self.xlr.display_on_eink(self.last_image)
        messagebox.showinfo("成功", "已尝试显示到墨水屏（或保存为divination.png）。")

if __name__ == "__main__":
    app = XiaoLiuRenGUI()
    app.mainloop()