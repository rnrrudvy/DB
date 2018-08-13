# 고객명 / ID(기본키) / PW / 나이 / 국적 / 거주지 / 가입날짜 / 등급

import sqlite3
import os
from tkinter import *
from functools import partial


def list_db():
    root = Tk()
    root.title("DB목록창")
    root.geometry("300x300")

    path_dir = 'D:/Users/kuk/OneDrive/01. repository/Python/DB_GUI/'
    dblist = os.listdir(path_dir)
    dblist.sort()

    varT = StringVar()
    varT.set(dblist)

    label_dblist = Label(root, textvariable=varT)
    label_dblist.pack(side=TOP)

    root.mainloop()


def save_quit(a, b, event):
    con = sqlite3.connect(b.get())
    cur = con.cursor()
    con.commit()
    con.close()

    a.destroy()  # 새로 열린 이 창만 닫기


def create_db():
    root = Tk()
    root.title("DB생성창")
    root.geometry("300x300")

    label_dbname = Label(root, text='DB이름')
    label_dbname.pack(side=LEFT)

    test = StringVar()
    textbox_dbname = Entry(root, textvariable=test)
    textbox_dbname.pack(side=LEFT)

    save_quit_arg = partial(save_quit, root, textbox_dbname)
    savebtn = Button(root, text='save')
    savebtn.pack(side=BOTTOM)
    savebtn.bind("<Button>", save_quit_arg)
    root.bind("<Return>", save_quit_arg)

    root.mainloop()


window = Tk()
window.title("DB Manager v1.0")  # 창 이름
window.geometry("200x500")  # 창 크기
window.resizable(width=TRUE, height=TRUE)  # 창 크기 변경 설정

# 사용자 UI
button1 = Button(window, text='DB목록', command=list_db)
button2 = Button(window, text='DB생성', command=create_db)
button3 = Button(window, text='DB삭제')
button4 = Button(window, text='DB수정')
button5 = Button(window, text='Table목록')
button6 = Button(window, text='Table생성')
button7 = Button(window, text='Table삭제')
button8 = Button(window, text='Table수정')
button9 = Button(window, text='프로그램종료', command=exit)
button1.place(x=40, y=30, width=100, height=30)
button2.place(x=40, y=80, width=100, height=30)
button3.place(x=40, y=130, width=100, height=30)
button4.place(x=40, y=180, width=100, height=30)
button5.place(x=40, y=230, width=100, height=30)
button6.place(x=40, y=280, width=100, height=30)
button7.place(x=40, y=330, width=100, height=30)
button8.place(x=40, y=380, width=100, height=30)
button9.place(x=40, y=430, width=100, height=30)
window.mainloop()


'''
con = sqlite3.connect("TestDB")
cur = con.cursor()

cur.execute("Create TABLE Customer")

con.commit()
con.close()


예제
cur.execute("CREATE TABLE kuk(id char(4), password int(4))")
    cur.execute("INSERT INTO kuk VALUES('john', 123)")
    cur.execute("INSERT INTO kuk VALUES('conn', 321)")
'''