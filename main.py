# 고객명 / ID(기본키) / PW / 나이 / 국적 / 거주지 / 가입날짜 / 등급

import sqlite3
import os
from tkinter import *
from tkinter import messagebox
from functools import partial


# DB목록 출력 윈도우창 ################################################################################
def list_db():
    path_dir = 'C:/Users/kuk/OneDrive/01. repository/Python/DB_GUI/db/'
    dblist = os.listdir(path_dir)
    dblist.sort()
    dblist_str = '' # 그냥 리스트로 바로 넣으려고 햇더니 {TestDB} {a} 요따구로 돼서 출력시 그지같이 나와서 스트링 변수만들고 여기다 한 줄로 저장해서 씀
    for i in range(0, len(dblist), 1):
        dblist_str += dblist[i] + '\n\n'    # 개행 한 줄만 하니까 간격 좁아서 별로라서 두 줄로 함

    root = Tk()
    root.title("DB목록창")
    root.geometry("300x300")
    root.resizable(width=TRUE, height=TRUE)

    label_dblist = Label(root, text=dblist_str, font=20)
    label_dblist.pack(anchor=CENTER, expand=TRUE)

    quitbtn = Button(root, text='닫기', font=20, bg='green', command=root.destroy)
    quitbtn.pack(anchor=SE, expand=TRUE, ipadx=10, ipady=10)

    root.mainloop()


# DB생성 윈도우창 ################################################################################
def create_db():
    root = Tk()
    root.title("DB생성창")
    root.geometry("300x300")

    label_dbname = Label(root, text='DB이름')
    label_dbname.grid(row=0, column=0)

    test = StringVar()
    textbox_dbname = Entry(root, textvariable=test)
    textbox_dbname.grid(row=0, column=1)
    textbox_dbname.focus()  # 엔트리에 마우스 클릭없이 커서 깜빡이게 해줌

    save_quit_arg = partial(save_quit, root, textbox_dbname)
    save_btn = Button(root, text='생성')
    save_btn.grid(row=0, column=2)

    quit_btn = Button(root, text='취소', command=root.destroy)
    quit_btn.grid(row=0, column=3)

    save_btn.bind("<Button>", save_quit_arg)
    root.bind("<Return>", save_quit_arg)
#    root.bind("<Escape>", root.destroy)  # 구현실패함 안됨 오류만 뜸

    root.mainloop()


# DB생성 후 종료버튼 이벤트 ################################################################################
def save_quit(a, b, event):
    path = 'C:/Users/kuk/OneDrive/01. repository/Python/DB_GUI/db/'+b.get()
    path_dir = 'C:/Users/kuk/OneDrive/01. repository/Python/DB_GUI/db/'
    dblist = os.listdir(path_dir)
    if b.get() in dblist:
        messagebox.showinfo("오류", "이미 있는 이름입니다")
    else:
         con = sqlite3.connect(path)
         con.close()

    a.destroy()  # 새로 열린 이 창만 닫기


# DB삭제 윈도우창 ################################################################################
def delete_db():
    root = Tk()
    root.title("DB삭제창")
    root.geometry("300x300")

    label_dbname = Label(root, text='DB이름')
    label_dbname.grid(row=0, column=0)

    test = StringVar()  # 이 객체는 음, 그러니까 위젯에 변수를 사용하게 해준다(?)
    textbox_dbname = Entry(root, textvariable=test) # 이 명령으로 저 객체를 지정해야 사용가능
    textbox_dbname.grid(row=0, column=1)
    textbox_dbname.focus()  # 엔트리에 마우스 클릭없이 커서 깜빡이게 해줌

    delete_quit_arg = partial(delete_quit, root, textbox_dbname)    # 함수에 매개변수 넣는 것임 lambda써도 되지만 이게 맘에 듬
    save_btn = Button(root, text='삭제')
    save_btn.grid(row=0, column=2)

    quit_btn = Button(root, text='취소', command=root.destroy)
    quit_btn.grid(row=0, column=3)

    save_btn.bind("<Button>", delete_quit_arg)
    root.bind("<Return>", delete_quit_arg)

    root.mainloop()


# DB삭제 후 종료버튼 이벤트 ################################################################################
def delete_quit(a, b, event):
    path_dir = 'C:/Users/kuk/OneDrive/01. repository/Python/DB_GUI/db/'
    dblist = os.listdir(path_dir)   # 경로에 있는 파일들 목록을 리스트로 반환해줌
    if b.get() in dblist:   # 엔트리에서 받아온 값이 리스트에 있으면 삭제 없으면 메시지 띄움
        os.remove(path_dir+b.get())
    else:
        messagebox.showinfo("오류", "그런 DB가 없음")

    a.destroy()  # 새로 열린 이 창만 닫기


# main 시작 ################################################################################
def main():
    window = Tk()
    window.title("DB Manager v1.0")  # 창 이름
    window.geometry("300x700")  # 창 크기
    window.resizable(width=TRUE, height=TRUE)  # 창 크기 변경 설정

    # 사용자 UI
    button1 = Button(window, text='DB목록', bg='magenta', command=list_db)
    button2 = Button(window, text='DB생성', bg='magenta', command=create_db)
    button3 = Button(window, text='DB삭제', bg='magenta', command=delete_db)
    button4 = Button(window, text='Table목록', bg='green')
    button5 = Button(window, text='Table생성', bg='green')
    button6 = Button(window, text='Table삭제', bg='green')
    button7 = Button(window, text='Table수정', bg='green')
    button8 = Button(window, text='프로그램종료', bg='magenta', command=exit)

    for i in range(8):
        Grid.rowconfigure(window, i, weight=1)  # 가중치를 1로 주면 span 사용이 가능해지는 것 같음
        Grid.columnconfigure(window, i, weight=1)   # 그냥 span만 줘봤는데 그러면 아무 변화 없음
                                                    # 가운데 i는 그 grid하는 index를 선택하는 것 같음

    button1.grid(row=0, column=0, sticky=E+W+S+N, columnspan=10)    # 동서남북을 다 지정하면 딱 모양 맞춰가지고 중간에 채울수 있음
    button2.grid(row=1, column=0, sticky=E+W+S+N, columnspan=10)    # span은 잘 모르겠지만 남는 부분들을 채우는 것 같음
    button3.grid(row=2, column=0, sticky=E+W+S+N, columnspan=10)
    button4.grid(row=3, column=0, sticky=E+W+S+N, columnspan=10)
    button5.grid(row=4, column=0, sticky=E+W+S+N, columnspan=10)
    button6.grid(row=5, column=0, sticky=E+W+S+N, columnspan=10)
    button7.grid(row=6, column=0, sticky=E+W+S+N, columnspan=10)
    button8.grid(row=7, column=0, sticky=E+W+S+N, columnspan=10)

    window.bind("<Escape>", exit)
    window.mainloop()


# 모듈화(?) ################################################################################
if __name__ == "__main__":
    main()


'''
DB 관련 참조 명령어들 
연결
con = sqlite3.connect("TestDB")
커서(통로) 생성
cur = con.cursor()
실행문 입력
cur.execute("Create TABLE Customer")
내용 전송
con.commit()
연결 해제
con.close()

실행문 예제
cur.execute("CREATE TABLE kuk(id char(4), password int(4))")
cur.execute("INSERT INTO kuk VALUES('john', 123)")
cur.execute("INSERT INTO kuk VALUES('conn', 321)")
'''