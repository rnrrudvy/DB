# 고객명 / ID(기본키) / PW / 나이 / 국적 / 거주지 / 가입날짜 / 등급

import sqlite3
from tkinter import *
from functools import partial

def quit_(a):
    a.destroy()

def create_db():
    root = Tk()
    root.title("DB생성창")
    root.geometry("300x300")
    # savebtn = Button(root, text='save', command=root.destroy).pack()
    arg = root,
    quit_arg = partial(quit_, arg)
    savebtn = Button(root, text='save', command=quit_arg).pack()

    root.mainloop()


window = Tk()
window.title("DB Manager v1.0")  # 창 이름
window.geometry("200x450")  # 창 크기
window.resizable(width=TRUE, height=TRUE)  # 창 크기 변경 설정

# 사용자 UI
button1 = Button(window, text='DB목록')
button2 = Button(window, text='DB생성', command=create_db)
button3 = Button(window, text='DB삭제')
button4 = Button(window, text='DB수정')
button5 = Button(window, text='Table목록')
button6 = Button(window, text='Table생성')
button7 = Button(window, text='Table삭제')
button8 = Button(window, text='Table수정')
button1.place(x=40, y=30, width=100, height=30)
button2.place(x=40, y=80, width=100, height=30)
button3.place(x=40, y=130, width=100, height=30)
button4.place(x=40, y=180, width=100, height=30)
button5.place(x=40, y=230, width=100, height=30)
button6.place(x=40, y=280, width=100, height=30)
button7.place(x=40, y=330, width=100, height=30)
button8.place(x=40, y=380, width=100, height=30)
window.mainloop()


'''
con = sqlite3.connect("TestDB")
cur = con.cursor()

cur.execute("Create TABLE Customer")

con.commit()
con.close()

def create_table():
    pass


def delete_table():
    pass


def alter_table():
    pass
'''