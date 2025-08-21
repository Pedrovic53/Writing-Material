import calendar
import datetime
import json
import os

class ElectronicCalendar:
    def __init__(self, filename='events.json'):
        self.filename = filename
        self.events = self.load_events()

    def load_events(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}  # 事件格式: {'YYYY-MM-DD': [{'time': 'HH:MM', 'description': '事件描述'}]}

    def save_events(self):
        with open(self.filename, 'w') as f:
            json.dump(self.events, f, indent=4)

    def display_calendar(self, year, month):
        print(calendar.month(year, month))

    def add_event(self, date_str, time_str, description):
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        date_key = date.strftime('%Y-%m-%d')
        if date_key not in self.events:
            self.events[date_key] = []
        self.events[date_key].append({'time': time_str, 'description': description})
        self.save_events()
        print(f"事件已添加: {date_str} {time_str} - {description}")

    def view_events(self, date_str):
        date_key = date_str
        if date_key in self.events:
            print(f"{date_key} 的事件:")
            for event in self.events[date_key]:
                print(f"  {event['time']} - {event['description']}")
        else:
            print("没有事件。")

    def delete_event(self, date_str, index):
        date_key = date_str
        if date_key in self.events and 0 <= index < len(self.events[date_key]):
            del self.events[date_key][index]
            if not self.events[date_key]:
                del self.events[date_key]
            self.save_events()
            print("事件已删除。")
        else:
            print("无效的索引或日期。")

def main():
    cal = ElectronicCalendar()
    while True:
        print("\n电子日历菜单:")
        print("1. 显示日历")
        print("2. 添加事件")
        print("3. 查看事件")
        print("4. 删除事件")
        print("5. 退出")
        choice = input("选择操作: ")
        if choice == '1':
            year = int(input("输入年份: "))
            month = int(input("输入月份: "))
            cal.display_calendar(year, month)
        elif choice == '2':
            date_str = input("输入日期 (YYYY-MM-DD): ")
            time_str = input("输入时间 (HH:MM): ")
            desc = input("输入事件描述: ")
            cal.add_event(date_str, time_str, desc)
        elif choice == '3':
            date_str = input("输入日期 (YYYY-MM-DD): ")
            cal.view_events(date_str)
        elif choice == '4':
            date_str = input("输入日期 (YYYY-MM-DD): ")
            cal.view_events(date_str)  # 先显示以选择索引
            index = int(input("输入要删除的事件索引 (从0开始): "))
            cal.delete_event(date_str, index)
        elif choice == '5':
            break
        else:
            print("无效选择。")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkcalendar import Calendar  # 注意: 需要 pip install tkcalendar (如果环境允许)

# ... (继承上面的 ElectronicCalendar 类)

class GUICalendar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("电子日历")
        self.cal = ElectronicCalendar()
        self.calendar = Calendar(self, selectmode='day')
        self.calendar.pack()
        self.event_list = tk.Listbox(self)
        self.event_list.pack()
        tk.Button(self, text="查看事件", command=self.view_selected_events).pack()

    def view_selected_events(self):
        date = self.calendar.get_date()
        self.event_list.delete(0, tk.END)
        date_key = datetime.datetime.strptime(date, '%m/%d/%y').strftime('%Y-%m-%d')  # 格式调整
        if date_key in self.cal.events:
            for event in self.cal.events[date_key]:
                self.event_list.insert(tk.END, f"{event['time']} - {event['description']}")

if __name__ == "__main__":
    app = GUICalendar()
    app.mainloop()