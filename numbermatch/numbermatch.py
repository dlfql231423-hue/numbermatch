import random

def MakeNum():
    for i in range(4):
        Num.append([0]*9)
    count=0
    for i in range(len(Num)):
        for j in range(9):
            if count>=32:
                break
            Num[i][j]=random.randint(1,9)
            count+=1
def Draw():
    for i in range(len(Num)):
        print(Num[i])
def last_Line():
    a=0
    a=len(Num)
    return a

def last_Row():
    a=0
    for j in range(8,-1,-1):
        if Num[len(Num)-1][j]==0:
            continue
        else:
            a=j+1
            return a
    return a
def AppNum():
    global Numcount
    Num_copy=[]
    copy_count=0
    App_count=0
    Zero_Size=0
    last_line=last_Line()
    last_row=last_Row()
    if Numcount>0:
        Numcount-=1
        for i in range(len(Num)):
            for j in range(9):
                if Num[i][j]!=0:
                    Num_copy.append(Num[i][j])
                    copy_count+=1
        Zero_Size = (len(Num_copy) - (8 - last_row)) // 9
        if((len(Num_copy) - (8 - last_row)) % 9 > 1):
            Zero_Size += 1
        for i in range(len(Num)-1,len(Num)):
            for j in range(last_row,9):
                if App_count<copy_count:
                    Num[i][j]=Num_copy[App_count]
                    App_count+=1
        for i in range(Zero_Size):
            Num.append([0]*9)
        for i in range(last_line,len(Num)):
            for j in range(9):
                if App_count<copy_count:
                    Num[i][j]=Num_copy[App_count]
                    App_count+=1
def change():
    global X1,X2,Y1,Y2
    X=0
    Y=0
    if X1>X2:
        X=X1
        X1=X2
        X2=X
        Y=Y1
        Y1=Y2
        Y2=Y
    if X1==X2 and Y1>Y2:
        Y=Y1
        Y1=Y2
        Y2=Y
def tensame():
    global X1,X2,Y1,Y2
    t=bool
    if Num[X1][Y1]==Num[X2][Y2] or Num[X1][Y1]+Num[X2][Y2]==10:
        t=True
    else :
        t=False
    return t
def width():
    global X1,X2,Y1,Y2
    t=bool
    if X1==X2 and Y2-Y1==1:
        t=True
    else :
        t=False
    return t
def width_middle():
    global X1,X2,Y1,Y2
    t=bool
    if (width()):
        t=False
    else :
        if X1==X2:
            for i in range(Y1+1,Y2):
                if Num[X1][i]==0:
                    t=True
                else :
                    t=False
                    break
        else:
            t=False
    return t
def length():
    global X1,X2,Y1,Y2
    t=bool
    if Y1==Y2 and X2-X1==1:
        t=True
    else :
        t=False
    return t
def length_middle():
    global X1,X2,Y1,Y2
    t=bool
    if (length()):
        t=False
    else:
        if Y1==Y2:
            for i in range(X1+1,X2):
                if Num[i][Y1]==0:
                    t=True
                else:
                    t=False
                    break
        else:
            t=False
        
    return t
def slash():
    global X1,X2,Y1,Y2
    t=bool
    if X2-X1==1 and Y2-Y1==1:
        t=True
    else :
        t=False
    return t
def slash_middle():
    global X1,X2,Y1,Y2
    t=bool
    if (length()):
        t=False
    else:
        if X2-X1==Y2-Y1:
            for i in range(1,X2-X1):
                if Num[X1+i][Y1+i]==0:
                    t=True
                else:
                    t=False
                    break
        else:
            t=False
    return t
def re_slash():
    global X1,X2,Y1,Y2
    t=bool
    if X2-X1==1 and Y1-Y2==1:
        t=True
    else :
        t=False
    return t
def re_slash_middle():
    global X1,X2,Y1,Y2
    t=bool
    if (length()):
        t=False
    else:
        if X2-X1==Y1-Y2:
            for i in range(1,X2-X1):
                if Num[X1+i][Y1-i]==0:
                    t=True
                else:
                    t=False
                    break
        else:
            t=False
    return t
def gap():
    global X1,X2,Y1,Y2
    t=bool
    if X2-X1==1 and Y1==8 and Y2==0:
        t=True
    else :
        t=False
    return t
def gap_middle():
    global X1,X2,Y1,Y2
    t=bool
    a=bool
    b=bool
    if (gap()):
        t=False
    else:
        if X2-X1==1:
            for i in range(X1,X2):
                for j in range(Y1+1,9):
                    if Num[i][j]==0:
                        a=True
                    else:
                        a=False
                        break
            for i in range(X2,X2+1):
                for j in range(Y2):
                    if Num[i][j]==0:
                        b=True
                    else:
                        b=False
                        break
            if a!=False and b!=False :
                t=True
            else :
                t=False
        else:
            t=False
    return t
def score_match():
    global X1,X2,Y1,Y2,score,level
    t=True
    change()
    if (Num[X1][Y1]!=0 and Num[X2][Y2]!=0)and (X1!=X2 or Y1!=Y2):
        if tensame()==True and (length()==True or width()==True or slash()==True or re_slash()==True or gap()==True):
            Num[X1][Y1]=0
            Num[X2][Y2]=0
            score+=1*level
            return t
        elif tensame()==True and (length_middle()==True or width_middle()==True or slash_middle()==True or re_slash_middle()==True or gap_middle()==True):
            Num[X1][Y1]=0
            Num[X2][Y2]=0
            score+=4*level
            return t
def remove():
    global num_remove
    t=bool
    num_remove=[]
    for i in range(len(Num)):
        count=0
        for j in range(9):
            if Num[i][j]==0:
                count+=1
        if count>8:
            num_remove.append(i)
    if len(num_remove)==1:
        t=True
        return t
    elif len(num_remove)>=2:
        t=False
        return t
def remove2():
    global score,level, num_remove
    if remove()==True or remove()==False:
        for i in range(len(num_remove)):
            Num.remove(Num[num_remove[i]-i])
            score+=10*level
    
def Hint():
    global X1, Y1, X2, Y2, HintList
    HintList=[]
    Hintbox=[]
    t=True
    for i1 in range(len(Num)):
        for j1 in range(9):
            for i2 in range(len(Num)):
                for j2 in range(9):
                    X1=i1
                    Y1=j1
                    X2=i2
                    Y2=j2
                    change()
                    if (Num[X1][Y1]!=0 and Num[X2][Y2]!=0)and (X1!=X2 or Y1!=Y2):
                        if tensame() and (length() or width() or slash() or re_slash() or gap() or length_middle() or width_middle() or slash_middle() or re_slash_middle() or gap_middle()): 
                            Hintbox=[X1,Y1,X2,Y2]
                            if HintList.count(Hintbox)==0:
                                HintList.append(Hintbox)
                            Hintbox=[]
    if len(HintList)>0:
        return t
def Hintshow():
    Hint()
    if Hint()==True:  
        a= random.choice(HintList)
        return a
def AllClear():
    global score,level, Numcount
    if len(Num)==0:
        score+=100*level+10*Numcount
        level+=1
        Numcount=5
        MakeNum()
def Gameover():
    global Numcount
    t= True
    Hint()
    if Numcount==0 and len(HintList)==0:
        return t