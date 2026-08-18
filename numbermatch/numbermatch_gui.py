import numbermatch as a
import tkinter
window=tkinter.Tk()
window.title("Python GUI Practice")
window.geometry("700x400")
window.resizable(False,True)
a.Num=[]
a.Numcount=5
a.MakeNum()
a.score=0
a.level=1
b=[]
btn=[]
x1=0
y1=0
c=1
h=[]
line=0
def show():
    global h
    if a.Gameover()==True:
        window.destroy()
        print("레벨: ",a.level,"점수: ",a.score)
    else :
        for i in range(4):
            btn.append([0]*9)
        if len(a.Num)>=4:
            for i in range(4):
                for j in range(9):
                    if a.Num[i+line][j]==0:
                        btn[i][j] = tkinter.Button(window,relief='groove',width=8,height=2,text='',bg='gray',command=lambda x=i+line,y=j : ch(x,y))
                        btn[i][j].grid(row = i+2, column = j)
                    else:
                        btn[i][j] = tkinter.Button(window,relief='groove',width=8,height=2,text=a.Num[i+line][j],bg='navajo white',command=lambda x=i+line,y=j : ch(x,y))
                        btn[i][j].grid(row = i+2, column = j)
        if len(a.Num)<4:
            for i in range(len(a.Num)):
                for j in range(9):
                    if a.Num[i][j]==0:
                        btn[i][j] = tkinter.Button(window,relief='groove',width=8,height=2,text='',bg='gray',command=lambda x=i,y=j : ch(x,y))
                        btn[i][j].grid(row = i+2, column = j)
                    else:
                        btn[i][j] = tkinter.Button(window,relief='groove',width=8,height=2,text=a.Num[i+line][j],bg='navajo white',command=lambda x=i,y=j : ch(x,y))
                        btn[i][j].grid(row = i+2, column = j)
            for i in range(len(a.Num),4):
                for j in range(9):
                    btn[i][j] = tkinter.Button(window,relief='groove',width=8,height=2,text='',bg='gray',command=lambda x=i,y=j : ch(x,y))
                    btn[i][j].grid(row = i+2, column = j)
        if len(h)>1 and (h[0]-line)<4 and (h[0]-line) >= 0:
            btn[h[0]-line][h[1]].configure(bg="blue")
        if len(h)>1 and (h[2]-line)<4 and (h[2]-line) >= 0:
            btn[h[2]-line][h[3]].configure(bg="blue")
def up():
    global line
    if (line>=1 ):
        line-=1
        show()
def down():
    global line
    if ((len(a.Num)-line)>4):
        line+=1
        show()
def ch(x,y):
    global line, h
    btn[x-line][y].configure(bg="yellow")
    global x1,y1,c
    if c % 2 == 1:
        c+=1
        x1=x
        y1=y
    else :
        c+=1
        a.X1=x1
        a.Y1=y1
        a.X2=x
        a.Y2=y
        if a.score_match()==True:
            h=[]
        a.score_match()
        if a.remove()==True and line >=1:
            line-=1
        if a.remove()==False:
            if line==1:
                line-=1
            elif line>1:
                line-=2
        a.remove2()
        a.AllClear()
        Score_value.config(text=a.score)
        level_value.config(text=a.level)
        show()
def add():
    a.AppNum()
    show()
def hint():
    global h
    if (a.Hint()==True):
        h=a.Hintshow()
        show()
    else:
        print("힌트를 사용할 수 없습니다.")
addbtn=tkinter.Button(window,relief='groove', bg='white', text="추가",command=add)
addbtn.grid(row=12,column=0,columnspan=2)
hintbtn=tkinter.Button(window,relief='groove', bg='white', text="힌트",command=hint)
hintbtn.grid(row=12,column=7,columnspan=2)
a.up=tkinter.Button(window,relief='raised', bg='white', text="up",command=up)
a.up.grid(row=3,column=10)
a.down=tkinter.Button(window,relief='raised', bg='white', text="down",command=down)
a.down.grid(row=4,column=10)
Score=tkinter.Label(window, bg='white', text="현재점수")
Score.grid(row=1,column=0)
Score_value=tkinter.Label(window, bg='white', text="0")
Score_value.grid(row=1,column=1)
Level=tkinter.Label(window, bg='white', text="현재레벨")
Level.grid(row=1,column=5)
level_value=tkinter.Label(window, bg='white', text="1")
level_value.grid(row=1,column=6)
show()
window.mainloop()
