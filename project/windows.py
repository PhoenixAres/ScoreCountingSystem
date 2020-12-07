from tkinter import *
from file import *
from work import *

def start():
    #创建窗体
    window = Tk()
    window.title('学生成绩统计系统')
    window.geometry("400x400+200+50")

    #标签
    label = Label(window,
               text="请输入文件名：",
               fg="black",
               font=("黑体", 10),
               width=60,
               height=1,
               wraplength=1000,
               justify="left",
               anchor="center")
    label.pack()
    label = Label(window,
               text="(数据格式：学号 姓名 班级 平时成绩 期中成绩 期末成绩)",
               fg="black",
               font=("黑体", 10),
               width=60,
               height=1,
               wraplength=2000,
               justify="left",
               anchor="center")
    label.pack()

    #输入文本框
    def showinfo():
         # 获取输入的内容
         s = entry.get()
         txt = ''
         try:
            ls = ReadFile(s)
         except:
             txt = '文件格式错误\n'
         else:
             txt = show(ls, s.split('.')[0])
         finally:
             text.delete('1.0', 'end')
             text.insert(INSERT, txt)

    entry = Entry(window)
    entry.pack()

    button = Button(window, text="确认", command=showinfo)
    button.pack()

    #滚动文本框显示结果
    # 创建滚动条
    scroll = Scrollbar()
    text = Text(window, width=60, height=10)
    # side放到窗体的哪一侧,  fill填充
    scroll.pack(side=RIGHT, fill=Y)
    text.pack(side=LEFT, fill=Y)
    # 关联
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.pack()

    #顶层菜单
    menubar = Menu(window)
    window.config(menu=menubar)
    def func():
        ls = generate(100)
        txt = show(ls)
        text.delete('1.0', 'end')
        text.insert(INSERT, txt)
    # 创建一个菜单选项
    menu1 = Menu(menubar, tearoff=False)
    # 给菜单选项添加内容
    for item in ['创建测试样例(100个数据)', '退出']:
        if item == '退出':
            # 添加分割线
            menu1.add_separator()
            menu1.add_command(label=item, command=window.quit)
        else:
            menu1.add_command(label=item, command=func)

    # 向菜单条上添加菜单选项
    menubar.add_cascade(label='菜单', menu=menu1)

    window.mainloop()