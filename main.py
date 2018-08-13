# 고객명 / ID(기본키) / PW / 나이 / 국적 / 거주지 / 가입날짜 / 등급

import sqlite3
from tkinter import *
from functools import partial


def _save_quit(a, b):
    # DB 연결
    # TestDB 대신에 Entry를 사용하여 사용자 입력으로 DB이름을 입력
    # 입력받은 값으로 connect하여 DB 생성할 예정
    print(b)
    #con = sqlite3.connect("TestDB")
    #cur = con.cursor()
    #con.commit()
    #con.close()

    a.destroy()  # 새로 열린 이 창만 닫기


def create_db():
    root = Tk()
    root.title("DB생성창")
    root.geometry("300x300")

    # Entry 만들어서 DB이름 받고 그 값을 함수로 넘겨줄 것
    test = StringVar()
    label1 = Label(root, text='DB이름').pack(side=LEFT)
    textbox = Entry(root, textvariable=test).pack(side=LEFT)
    test = test.set('default')
    save_quit_arg = partial(_save_quit, root, test)
    savebtn = Button(root, text='save', command=save_quit_arg).pack(side=BOTTOM)


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


예제
cur.execute("CREATE TABLE kuk(id char(4), password int(4))")
    cur.execute("INSERT INTO kuk VALUES('john', 123)")
    cur.execute("INSERT INTO kuk VALUES('conn', 321)")
'''