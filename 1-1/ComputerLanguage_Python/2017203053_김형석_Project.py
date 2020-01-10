# 파일이름: 2017203053-김형석-프로그램
# 파일 내용: FCS(Football Club Simulater)
# 학번: 2017203053
# 이름: 김형석
# 제출일자: 2018.6.7

# 게임오류 : 양쪽에서 키 입력 시 한쪽에서 이동 중복, 골인 했을 때 메세지, 게임 시작 화면 텍스트, 충돌 처리 조건식
# 메뉴오류 : 영입/방출

from tkinter import* # 라이브러리 pillow, pygame 설치 필요
from PIL import Image,ImageTk
from tkinter import messagebox    
import pygame

def price(): # 텍스트 파일에서 파일 읽기(초기 구단 자본 및 선수 이적료
    infile = open('transfer_fee.txt', 'r')
    for line in infile :
        line = line.rstrip()
        print(line)
    infile.close()

def pickClub(): # 구단 선택 메뉴
    global BarClubMoney,RealClubMoney,ManCClubMoney,ManUClubMoney,LivClubMoney
    global BarM,RealM,ManCM,ManUM,LivM
    global BarP,RealP,ManCP,ManUP,LivP
    win = Toplevel() 
    win.geometry('800x600') # 윈도우 창 사이즈 설정

    
    backgnd=PhotoImage(file="laliga.gif") # 윈도우 창 배경 설정
    w=Label(win,image=backgnd)
    w.pack()

    # 메뉴 버튼
    Button(win, text='1.Barcelona',command=pickBar).place(x=100,y=50)
    Button(win, text='2.Real Madrid',command=pickReal).place(x=100,y=90)
    Button(win, text='3.Manchester City',command=pickManC).place(x=100,y=130)
    Button(win, text='4.Manchester United',command=pickManU).place(x=100,y=170)
    Button(win, text='5.Liverpool',command=pickLiv).place(x=100,y=210)
    Button(win, text='초기 구단 자본 및 선수 이적료 확인',command=price).place(x=100,y=260)
     # 완료 버튼을 누르면 자식 윈도우를 닫고 부모 윈도우로 돌아감 
    Button(win, text='완료', command=win.destroy).place(x=100, y=310)

    win.mainloop()

def PresentBar():# 구단 현황 리스트로 프린트
    global BarClubMoney
    global BarM
    global BarP
    print('Barcelona : ',BarP)
    print('현재 잔여 자본 : ',BarClubMoney)

def PresentReal():
    global RealClubMoney
    global RealM
    global RealP
    print('Real Madird : ',RealP)
    print('현재 잔여 자본 : ',RealClubMoney)

def PresentManC():
    global ManCClubMoney
    global ManCM
    global ManCP
    print('Manchester City : ',ManCP)
    print('현재 잔여 자본 : ',ManCClubMoney)
    
def PresentManU():
    global ManUClubMoney
    global ManUM
    global ManUP
    print('Manchester United : ',ManUP)
    print('현재 잔여 자본 : ',ManUClubMoney)

def PresentLiv():
    global LivClubMoney
    global LivM
    global LivP
    print('Liverpool : ',LivP)
    print('현재 잔여 자본 : ',LivClubMoney)
    
    
def pickBar(): # 바르셀로나 메뉴
    global BarClubMoney
    global BarM
    global BarP
    
    win = Toplevel()
    
    photo2 = PhotoImage(file="Bar.gif")
    label2 = Label(win, image=photo2)
    label2.grid(row=0, column=1)
    
    Button(win, text='영입', command=Barrecruit).grid(row=4,column=0)
    Button(win, text='방출', command=Barrelease).grid(row=5,column=0)
    Button(win, text='완료', command=win.destroy).grid(row=6,column=0)
    Button(win, text='구단 현황', command=PresentBar).grid(row=5,column=1)
    win.mainloop()

def pickReal(): # 레알 마드리드 메뉴
    global RealClubMoney
    global RealM
    global RealP
    
    win = Toplevel()
    
    photo2 = PhotoImage(file="Real.gif")
    label2 = Label(win, image=photo2)
    label2.grid(row=0, column=1)
    
    Button(win, text='영입', command=Realrecruit).grid(row=4,column=0)
    Button(win, text='방출', command=Realrelease).grid(row=5,column=0)
    Button(win, text='완료', command=win.destroy).grid(row=6,column=0)
    Button(win, text='구단 현황', command=PresentReal).grid(row=5,column=1)

    win.mainloop()

def pickManC(): # 맨시티 메뉴
    global ManCClubMoney
    global ManCM
    global ManCP
    
    win = Toplevel()
    
    photo2 = PhotoImage(file="ManC.gif")
    label2 = Label(win, image=photo2)
    label2.grid(row=0, column=1)
    
    Button(win, text='영입', command=ManCrecruit).grid(row=4,column=0)
    Button(win, text='방출', command=ManCrelease).grid(row=5,column=0)
    Button(win, text='완료', command=win.destroy).grid(row=6,column=0)
    Button(win, text='구단 현황', command=PresentManC).grid(row=5,column=1)

    win.mainloop()

def pickManU(): # 맨유 메뉴
    global ManUClubMoney
    global ManUM
    global ManUP
    win = Toplevel()
    
    photo2 = PhotoImage(file="ManU.gif")
    label2 = Label(win, image=photo2)
    label2.grid(row=0, column=1)
    
    Button(win, text='영입', command=ManUrecruit).grid(row=4,column=0)
    Button(win, text='방출', command=ManUrelease).grid(row=5,column=0)
    Button(win, text='완료', command=win.destroy).grid(row=6,column=0)
    Button(win, text='구단 현황', command=PresentManU).grid(row=5,column=1)

    win.mainloop()

def pickLiv(): # 리버풀 메뉴
    global LivClubMoney
    global LivM
    global LivP
    win = Toplevel()
    
    photo2 = PhotoImage(file="Liv.gif")
    label2 = Label(win, image=photo2)
    label2.grid(row=0, column=1)
    
    Button(win, text='영입', command=Livrecruit).grid(row=4,column=0)
    Button(win, text='방출', command=Livrelease).grid(row=5,column=0)
    Button(win, text='완료', command=win.destroy).grid(row=6,column=0)
    Button(win, text='구단 현황', command=PresentLiv).grid(row=5,column=1)

    win.mainloop()


    
def Barrecruit(): # 바르셀로나 영입
    global BarClubMoney
    global BarM
    global BarP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Button(win, text='공격수', command=BarFWrecruit).place(x=120,y=60)
    Button(win, text='미드필더', command=BarMFrecruit).place(x=120,y=100)
    Button(win, text='수비수', command=BarDEFrecruit).place(x=120,y=140)
    Button(win, text='골키퍼', command=BarGKrecruit).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
def Barrelease(): # 바르셀로나 방출
    global BarClubMoney
    global BarM
    global BarP
    
    win = Toplevel()
    
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Button(win, text='공격수', command=BarFWrelease).place(x=120,y=60)
    Button(win, text='미드필더', command=BarMFrelease).place(x=120,y=100)
    Button(win, text='수비수', command=BarDEFrelease).place(x=120,y=140)
    Button(win, text='골키퍼', command=BarGKrelease).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
    
def BarFWrecruit(): # 바르셀로나 공격수 영입
    global BarClubMoney
    global BarM
    global BarP
                            
    def BarPlayerFWrecruit():
        global BarClubMoney
        global BarM
        global BarP
        global usedMoney
        
        usedMoney=0
                
        if value1.get()==1: # 체크버튼이 체크되었을 때
            if ('Messi' in BarP) != 1: # 체크된 선수가 구단 리스트 안에 없을 때
                usedMoney+=300000000
            else: # 체크된 선수가 구단 리스트 안에 이미 있을 때
                messagebox.showinfo('','Messi 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value2.get()==1:
            if ('L.Suarez' in BarP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value3.get()==1:
            if ('Ronaldo' in BarP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 이미 해당 구단에 있습니다.')
                 
                    
        if value4.get()==1:
            if ('Bale' in BarP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Bale 선수는 이미 해당 구단에 있습니다.')
                   
        if value5.get()==1:
            if ('Benzema' in BarP) != 1:
                usedMoney+=46000000
            else:
                messagebox.showinfo('','Benzema 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value6.get()==1:
            if ('Neymar' in BarP) != 1:
                usedMoney+=222000000
            else:
                messagebox.showinfo('','Neymar 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value7.get()==1:
            if ('Lewandowski' in BarP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 이미 해당 구단에 있습니다.')
                   
                    
        if value8.get()==1:
            if ('Muller' in BarP) != 1:
                usedMoney+=97500000
            else:
                messagebox.showinfo('','Muller 선수는 이미 해당 구단에 있습니다.')
                   
                    
        if value9.get()==1:
            if ('Ronaldinho' in BarP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value10.get()==1:
            if ('C.Ronaldo' in BarP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value11.get()==1:
            if ('SON' in BarP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','SON 선수는 이미 해당 구단에 있습니다.')
                    
                   
                
        if value12.get()==1:
            if ('R.Carlos' in BarP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value13.get()==1:
            if ('Mbappe' in BarP) != 1:
                usedMoney+=180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value14.get()==1:
            if ('Rooney' in BarP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Rooney 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value15.get()==1:
            if ('M.Salah' in BarP) != 1:
                usedMoney+=39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 이미 해당 구단에 있습니다.')
                   
                    
        if value16.get()==1:
            if ('Kane' in BarP) != 1:
                usedMoney+=198000000
            else:
                messagebox.showinfo('','Kane 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value17.get()==1:
            if ('Griezmann' in BarP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Greizmann 선수는 이미 해당 구단에 있습니다.')
                    
        if usedMoney>BarClubMoney: # 체크된 선수들의 영입료가 남아있는 자본보다 클 때
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
            
        elif usedMoney<=BarClubMoney: # 체크된 선수들의 영입료가 남아있는 자본 이하 일 때
            if value1.get()==1:
                if ('Messi' in BarP) != 1:
                    BarP.append('Messi') # 구단 리스트에 선수 추가
                    BarClubMoney=BarClubMoney-300000000 # 자본에서 선수 영입료만큼 지출
                    
                    
            if value2.get()==1:
                if ('L.Suarez' in BarP) != 1:
                    BarP.append('L.Suarez')
                    BarClubMoney=BarClubMoney-86000000
                    
                    
            if value3.get()==1:
                if ('Ronaldo' in BarP) != 1:
                    BarP.append('Ronaldo')
                    BarClubMoney=BarClubMoney-45000000
                    
                    
            if value4.get()==1:
                if ('Bale' in BarP) != 1:
                    BarP.append('Bale')
                    BarClubMoney=BarClubMoney-100000000
                    
            if value5.get()==1:
                if ('Benzema' in BarP) != 1:
                    BarP.append('Benzema')
                    BarClubMoney=BarClubMoney-46000000
                    
                    
            if value6.get()==1:
                if ('Neymar' in BarP) != 1:                    
                    BarP.append('Neymar')
                    BarClubMoney=BarClubMoney-222000000
                    
                    
            if value7.get()==1:
                if ('Lewandowski' in BarP) != 1:                   
                    BarP.append('Lewandowski')
                    BarClubMoney=BarClubMoney-86000000
                    
                    
            if value8.get()==1:
                if ('Muller' in BarP) != 1:                    
                    BarP.append('Muller')
                    BarClubMoney=BarClubMoney-97500000
                    
                    
            if value9.get()==1:
                if ('Ronaldinho' in BarP) != 1:                    
                    BarP.append('Ronaldinho')
                    BarClubMoney=BarClubMoney-25000000
                    
                    
            if value10.get()==1:
                if ('C.Ronaldo' in BarP) != 1:                    
                    BarP.append('C.Ronaldo')
                    BarClubMoney=BarClubMoney-100000000
                    
                    
            if value11.get()==1:
                if ('SON' in BarP) != 1:                    
                    BarP.append('SON')
                    BarClubMoney=BarClubMoney-90000000
                    
                
            if value12.get()==1:
                if ('R.Carlos' in BarP) != 1:                    
                    BarP.append('R.Carlos')
                    BarClubMoney=BarClubMoney-6000000
                    
                    
            if value13.get()==1:
                if ('Mbappe' in BarP) != 1:                    
                    BarP.append('Mbappe')
                    BarClubMoney=BarClubMoney-180000000
                    
                    
            if value14.get()==1:
                if ('Rooney' in BarP) != 1:                    
                    BarP.append('Rooney')
                    BarClubMoney=BarClubMoney-30000000
                    
                    
            if value15.get()==1:
                if ('M.Salah' in BarP) != 1:                    
                    BarP.append('M.Salah')
                    BarClubMoney=BarClubMoney-39000000
                    
                    
            if value16.get()==1:
                if ('Kane' in BarP) != 1:                    
                    BarP.append('Kane')
                    BarClubMoney=BarClubMoney-198000000
                   
                    
            if value17.get()==1:
                if ('Griezmann' in BarP) != 1:                    
                    BarP.append('Griezmann')
                    BarClubMoney=BarClubMoney-30000000
 
            
            messagebox.showinfo('','영입이 완료되었습니다.')
            
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()

    
    
    Label(win, text="영입할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar() # 체크 버튼이 체크되면 value 값 1, 체크 안되면 value값 0
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='영입',command=BarPlayerFWrecruit).place(x=500,y=60)
    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    
    win.mainloop()
def BarMFrecruit(): # 바르셀로나 미드필더 영입 
    global BarClubMoney
    global BarM
    global BarP
    
    
    def BarPlayerMFrecruit():
        global BarClubMoney
        global BarM
        global BarP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('J.S.Park' in BarP) != 1:
                usedMoney+=7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('Pogba' in BarP) != 1:
                usedMoney+=102000000
            else:
                messagebox.showinfo('','Pogba 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('A.Iniesta' in BarP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Modric' in BarP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Modric 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Sergio Busquets' in BarP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Eriksen' in BarP) != 1:
                usedMoney+=62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Kroos' in BarP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Kroos 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('De Bruyne' in BarP) != 1:
                usedMoney+=74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Silva' in BarP) != 1:
                usedMoney+=50000000
            else:
                messagebox.showinfo('','Silva 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Isco' in BarP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Isco 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('Vidal' in BarP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Vidal 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('Casemiro' in BarP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Coutinho' in BarP) != 1:
                usedMoney+=163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Mane' in BarP) != 1:
                usedMoney+=34000000
            else:
                messagebox.showinfo('','Mane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('J.Rodriguez' in BarP) != 1:
                usedMoney+=80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 이미 해당 구단에 있습니다.')
        
                        
        if usedMoney>BarClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=BarClubMoney:
        
            if value1.get()==1:
                if ('J.S.Park' in BarP) != 1:
                    BarP.append('J.S.Park')
                    BarClubMoney=BarClubMoney-7300000
                    
            if value2.get()==1:
                if ('Pogba' in BarP) != 1:
                    BarP.append('Pogba')
                    BarClubMoney=BarClubMoney-102000000
                    
            if value3.get()==1:
                if ('A.Iniesta' in BarP) != 1:
                    BarP.append('A.Iniesta')
                    BarClubMoney=BarClubMoney-35000000
                    
            if value4.get()==1:
                if ('Modric' in BarP) != 1:
                    BarP.append('Modric')
                    BarClubMoney=BarClubMoney-35000000
                    
            if value5.get()==1:
                if ('Sergio Busquets' in BarP) != 1:
                    BarP.append('Sergio Busquets')
                    BarClubMoney=BarClubMoney-100000000
                    
            if value6.get()==1:
                if ('Eriksen' in BarP) != 1:
                    BarP.append('Eriksen')
                    BarClubMoney=BarClubMoney-62000000
                    
            if value7.get()==1:
                if ('Kroos' in BarP) != 1:
                    BarP.append('Kroos')
                    BarClubMoney=BarClubMoney-25000000
                    
            if value8.get()==1:
                if ('De Bruyne' in BarP) != 1:
                    BarP.append('De Bruyne')
                    BarClubMoney=BarClubMoney-74000000
                    
            if value9.get()==1:
                if ('Silva' in BarP) != 1:
                    BarP.append('Silva')
                    BarClubMoney=BarClubMoney-50000000
                    
            if value10.get()==1:
                if ('Isco' in BarP) != 1:
                    BarP.append('Isco')
                    BarClubMoney=BarClubMoney-40000000
                    
            if value11.get()==1:
                if ('Vidal' in BarP) != 1:
                    BarP.append('Vidal')
                    BarClubMoney=BarClubMoney-35000000
                    
            if value12.get()==1:
                if ('Casemiro' in BarP) != 1:
                    BarP.append('Casemiro')
                    BarClubMoney=BarClubMoney-6000000
                    
            if value13.get()==1:
                if ('Coutinho' in BarP) != 1:
                    BarP.append('Coutinho')
                    BarClubMoney=BarClubMoney-163000000
                    
            if value14.get()==1:
                if ('Mane' in BarP) != 1:
                    BarP.append('Mane')
                    BarClubMoney=BarClubMoney-34000000
                    
            if value15.get()==1:
                if ('J.Rodriguez' in BarP) != 1:
                    BarP.append('J.Rodriguez')
                    BarClubMoney=BarClubMoney-80000000
                    
            
            messagebox.showinfo('','영입이 완료되었습니다.')
                
            
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='영입',command=BarPlayerMFrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
def BarDEFrecruit(): # 바르셀로나 수비수 영입
    global BarClubMoney
    global BarM
    global BarP
    
    

    def BarPlayerDEFrecruit():
        global BarClubMoney
        global BarM
        global BarP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Marcelo' in BarP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value2.get()==1:
            if ('Pique' in BarP) != 1:
                usedMoney+=7000000
            else:
                messagebox.showinfo('','Pique 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value3.get()==1:
            if ('Sergio Ramos' in BarP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 이미 해당 구단에 있습니다.')
                 
                    
        if value4.get()==1:
            if ('Jordi Alba' in BarP) != 1:
                usedMoney+=14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 이미 해당 구단에 있습니다.')
                   
        if value5.get()==1:
            if ('Hummels' in BarP) != 1:
                usedMoney+=41000000
            else:
                messagebox.showinfo('','Hummels 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value6.get()==1:
            if ('Otamendi' in BarP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 이미 해당 구단에 있습니다.')
        
                    
        if usedMoney>BarClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
            
        elif usedMoney<=BarClubMoney:
      
        
            if value1.get()==1:
                if ('Marcelo' in BarP) != 1:
                    BarP.append('Marcelo')
                    BarClubMoney=BarClubMoney-6000000
                    
            if value2.get()==1:
                if ('Pique' in BarP) != 1:
                    BarP.append('Pique')
                    BarClubMoney=BarClubMoney-7000000
                    
            if value3.get()==1:
                if ('Sergio Ramos' in BarP) != 1:
                    BarP.append('Serigio Ramos')
                    BarClubMoney=BarClubMoney-90000000
                    
            if value4.get()==1:
                if ('Jordi Alba' in BarP) != 1:
                    BarP.append('Jordi Alba')
                    BarClubMoney=BarClubMoney-14000000
                    
            if value5.get()==1:
                if ('Hummels' in BarP) != 1:
                    BarP.append('Hummels')
                    BarClubMoney=BarClubMoney-41000000
                    
            if value6.get()==1:
                if ('Otamendi' in BarP) != 1:
                    BarP.append('Otamendi')
                    BarClubMoney=BarClubMoney-45000000
            
            messagebox.showinfo('','영입이 완료되었습니다.')
            
    
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='영입',command=BarPlayerDEFrecruit).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
def BarGKrecruit(): # 바르셀로나 골키퍼 영입 
    global BarClubMoney
    global BarM
    global BarP
       
    

    def BarPlayerGKrecruit():
        global BarClubMoney
        global BarM
        global BarP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Casillas' in BarP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casillas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('De Gea' in BarP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','De Gea 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Neuer' in BarP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Neuer 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Buffon' in BarP) != 1:
                usedMoney+=53500000
            else:
                messagebox.showinfo('','Buffon 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Navas' in BarP) != 1:
                usedMoney+=10000000
            else:
                messagebox.showinfo('','Navas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Van der Sar' in BarP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Oblak' in BarP) != 1:
                usedMoney+=16000000
            else:
                messagebox.showinfo('','Oblak 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Ederson' in BarP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Ederson 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Lloris' in BarP) != 1:
                usedMoney+=19000000
            else:
                messagebox.showinfo('','Lloris 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Ter Stegen' in BarP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>BarClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=BarClubMoney:
        
            if value1.get()==1:
                if ('Casillas' in BarP) != 1:
                    BarP.append('Casillas')
                    BarClubMoney=BarClubMoney-6000000
                    
            if value2.get()==1:
                if ('De Gea' in BarP) != 1:
                    BarP.append('De Gea')
                    BarClubMoney=BarClubMoney-40000000
                    
            if value3.get()==1:
                if ('Neuer' in BarP) != 1:
                    BarP.append('Neuer')
                    BarClubMoney=BarClubMoney-30000000
                    
            if value4.get()==1:
                if ('Buffon' in BarP) != 1:
                    BarP.append('Navas')
                    BarClubMoney=BarClubMoney-53500000
                    
            if value5.get()==1:
                if ('Navas' in BarP) != 1:
                    BarP.append('Navas')
                    BarClubMoney=BarClubMoney-10000000
                    
            if value6.get()==1:
                if ('Van der Sar' in BarP) != 1:
                    BarP.append('Van der Sar')
                    BarClubMoney=BarClubMoney-23000000
                    
            if value7.get()==1:
                if ('Oblak' in BarP) != 1:
                    BarP.append('Oblak')
                    BarClubMoney=BarClubMoney-16000000
                    
            if value8.get()==1:
                if ('Ederson' in BarP) != 1:
                    BarP.append('Ederson')
                    BarClubMoney=BarClubMoney-40000000
                    
            if value9.get()==1:
                if ('Lloris' in BarP) != 1:
                    BarP.append('Lloris')
                    BarClubMoney=BarClubMoney-19000000
                   
            if value10.get()==1:
                if ('Ter Stegen' in BarP) != 1:
                    BarP.append('Ter Stegen')
                    BarClubMoney=BarClubMoney-23000000
                    
            
            
            messagebox.showinfo('','영입이 완료되었습니다.')
                
           
            
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='영입',command=BarPlayerGKrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    
    win.mainloop()
    
def BarFWrelease(): # 바르셀로나 공격수 방출
    global BarClubMoney
    global BarM
    global BarP
    

    def BarPlayerFWrelease():
        global BarClubMoney
        global BarM
        global BarP
      
        
        if value1.get()==1: # 체크 버튼이 체크되었을 때
            if ('Messi' in BarP) == 1: # 체크된 선수가 구단 리스트에 있으면
                BarP.remove('Messi') # 체크된 선수를 리스트에서 삭제
                BarClubMoney=BarClubMoney+300000000 # 삭제된 선수의 영입료만큼 환불
            else: # 체크 버튼이 체크되지 않았을 때 
                messagebox.showinfo('','Messi 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('L.Suarez' in BarP) == 1:
                BarP.remove('L.Suarez')
                BarClubMoney=BarClubMoney+86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Ronaldo' in BarP) == 1:
                BarP.remove('Ronaldo')
                BarClubMoney=BarClubMoney+45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Bale' in BarP) == 1:
                BarP.remove('Bale')
                BarClubMoney=BarClubMoney+100000000
            else:
                messagebox.showinfo('','Bale 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Benzema' in BarP) == 1:
                BarP.remove('Benzema')
                BarClubMoney=BarClubMoney+46000000
            else:
                messagebox.showinfo('','Benzema 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Neymar' in BarP) == 1:
                BarP.remove('Neymar')
                BarClubMoney=BarClubMoney+222000000
            else:
                messagebox.showinfo('','Neymar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Lewandowski' in BarP) == 1:
                BarP.remove('Lewandowski')
                BarClubMoney=BarClubMoney+86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Muller' in BarP) == 1:
                BarP.remove('Muller')
                BarClubMoney=BarClubMoney+97500000
            else:
                messagebox.showinfo('','Muller 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Ronaldinho' in BarP) == 1:
                BarP.remove('Ronaldinho')
                BarClubMoney=BarClubMoney+25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('C.Ronaldo' in BarP) == 1:
                BarP.remove('C.Ronaldo')
                BarClubMoney=BarClubMoney+100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('SON' in BarP) == 1:
                BarP.remove('SON')
                BarClubMoney=BarClubMoney+90000000
            else:
                messagebox.showinfo('','SON 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('R.Carlos' in BarP) == 1:
                BarP.remove('R.Carlos')
                BarClubMoney=BarClubMoney+6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Mbappe' in BarP) == 1:
                BarP.remove('Mbappe')
                BarClubMoney=BarClubMoney+180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Rooney' in BarP) == 1:
                BarP.remove('Rooney')
                BarClubMoney=BarClubMoney+30000000
            else:
                messagebox.showinfo('','Rooney 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('M.Salah' in BarP) == 1:
                BarP.remove('M.Salah')
                BarClubMoney=BarClubMoney+39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 해당 구단에 속해 있지 않습니다.')
        if value16.get()==1:
            if ('Kane' in BarP) == 1:
                BarP.remove('Kane')
                BarClubMoney=BarClubMoney+198000000
            else:
                messagebox.showinfo('','Kane 선수는 해당 구단에 속해 있지 않습니다.')
        if value17.get()==1:
            if ('Griezmann' in BarP) == 1:
                BarP.remove('Griezmann')
                BarClubMoney=BarClubMoney+30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 해당 구단에 속해 있지 않습니다.')
            
        messagebox.showinfo('','방출이 완료되었습니다.')
        
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Label(win, text="방출할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='방출',command=BarPlayerFWrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def BarMFrelease(): # 바르셀로나 미드필더 방출
    global BarClubMoney
    global BarM
    global BarP
    

    def BarPlayerMFrelease():
        global BarClubMoney
        global BarM
        global BarP
      
        
        if value1.get()==1:
            if ('J.S.Park' in BarP) == 1:
                BarP.remove('J.S.Park')
                BarClubMoney=BarClubMoney+7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pogba' in BarP) == 1:
                BarP.remove('Pogba')
                BarClubMoney=BarClubMoney+102000000
            else:
                messagebox.showinfo('','Pogba 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('A.Iniesta' in BarP) == 1:
                BarP.remove('A.Iniesta')
                BarClubMoney=BarClubMoney+35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Modric' in BarP) == 1:
                BarP.remove('Modric')
                BarClubMoney=BarClubMoney+35000000
            else:
                messagebox.showinfo('','Modric 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Sergio Busquets' in BarP) == 1:
                BarP.remove('Sergio Busquets')
                BarClubMoney=BarClubMoney+100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Eriksen' in BarP) == 1:
                BarP.remove('Eriksen')
                BarClubMoney=BarClubMoney+62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Kroos' in BarP) == 1:
                BarP.remove('Kroos')
                BarClubMoney=BarClubMoney+25000000
            else:
                messagebox.showinfo('','Kroos 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('De Bruyne' in BarP) == 1:
                BarP.remove('De Bruyne')
                BarClubMoney=BarClubMoney+74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Silva' in BarP) == 1:
                BarP.remove('Silva')
                BarClubMoney=BarClubMoney+50000000
            else:
                messagebox.showinfo('','Silva 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Isco' in BarP) == 1:
                BarP.remove('Isco')
                BarClubMoney=BarClubMoney+40000000
            else:
                messagebox.showinfo('','Isco 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('Vidal' in BarP) == 1:
                BarP.remove('Vidal')
                BarClubMoney=BarClubMoney+35000000
            else:
                messagebox.showinfo('','Vidal 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('Casemiro' in BarP) == 1:
                BarP.remove('Casemiro')
                BarClubMoney=BarClubMoney+6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Coutinho' in BarP) == 1:
                BarP.remove('Coutinho')
                BarClubMoney=BarClubMoney+163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Mane' in BarP) == 1:
                BarP.remove('Mane')
                BarClubMoney=BarClubMoney+34000000
            else:
                messagebox.showinfo('','Mane 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('J.Rodriguez' in BarP) == 1:
                BarP.remove('J.Rodriguez')
                BarClubMoney=BarClubMoney+80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='방출',command=BarPlayerMFrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def BarDEFrelease(): # 바르셀로나 수비수 방출
    global BarClubMoney
    global BarM
    global BarP
    

    def BarPlayerDEFrelease():
        global BarClubMoney
        global BarM
        global BarP
      
        
        if value1.get()==1:
            if ('Marcelo' in BarP) == 1:
                BarP.remove('Marcelo')
                BarClubMoney=BarClubMoney+6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pique' in BarP) == 1:
                BarP.remove('Pique')
                BarClubMoney=BarClubMoney+7000000
            else:
                messagebox.showinfo('','Pique 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Sergio Ramos' in BarP) == 1:
                BarP.remove('Sergio Ramos')
                BarClubMoney=BarClubMoney+90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Jordi Alba' in BarP) == 1:
                BarP.remove('Jordi Alba')
                BarClubMoney=BarClubMoney+14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Hummels' in BarP) == 1:
                BarP.remove('Hummels')
                BarClubMoney=BarClubMoney+41000000
            else:
                messagebox.showinfo('','Hummels 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Otamendi' in BarP) == 1:
                BarP.remove('Otamendi')
                BarClubMoney=BarClubMoney+45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='방출',command=BarPlayerDEFrelease).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def BarGKrelease(): # 바르셀로나 골키퍼 방출
    
    
    global BarClubMoney
    global BarM
    global BarP
    

    def BarPlayerGKrelease():
        global BarClubMoney
        global BarM
        global BarP
      
        
        if value1.get()==1:
            if ('Casillas' in BarP) == 1:
                BarP.remove('Casillas')
                BarClubMoney=BarClubMoney+6000000
            else:
                messagebox.showinfo('','Casillas 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('De Gea' in BarP) == 1:
                BarP.remove('De Gea')
                BarClubMoney=BarClubMoney+40000000
            else:
                messagebox.showinfo('','De Gea 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Neuer' in BarP) == 1:
                BarP.remove('Neuer')
                BarClubMoney=BarClubMoney+30000000
            else:
                messagebox.showinfo('','Neuer 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Buffon' in BarP) == 1:
                BarP.remove('Buffon')
                BarClubMoney=BarClubMoney+53500000
            else:
                messagebox.showinfo('','Buffon 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Navas' in BarP) == 1:
                BarP.remove('Navas')
                BarClubMoney=BarClubMoney+10000000
            else:
                messagebox.showinfo('','Navas 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Van der Sar' in BarP) == 1:
                BarP.remove('Van der Sar')
                BarClubMoney=BarClubMoney+23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Oblak' in BarP) == 1:
                BarP.remove('Oblak')
                BarClubMoney=BarClubMoney+16000000
            else:
                messagebox.showinfo('','Oblak 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Ederson' in BarP) == 1:
                BarP.remove('Ederson')
                BarClubMoney=BarClubMoney+40000000
            else:
                messagebox.showinfo('','Ederson 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Lloris' in BarP) == 1:
                BarP.remove('Lloris')
                BarClubMoney=BarClubMoney+19000000
            else:
                messagebox.showinfo('','Lloris 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Ter Stegen' in BarP) == 1:
                BarP.remove('Ter Stegen')
                BarClubMoney=BarClubMoney+23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Bar2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='방출',command=BarPlayerGKrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    
    
    
    win.mainloop()
    
def Realrecruit(): # 레알 마드리드 영입
    global RealClubMoney
    global RealM
    global RealP
    
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=RealFWrecruit).place(x=120,y=60)
    Button(win, text='미드필더', command=RealMFrecruit).place(x=120,y=100)
    Button(win, text='수비수', command=RealDEFrecruit).place(x=120,y=140)
    Button(win, text='골키퍼', command=RealGKrecruit).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
def Realrelease(): # 레알 마드리드 방출
    global RealClubMoney
    global RealM
    global RealP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=RealFWrelease).place(x=120,y=60)
    Button(win, text='미드필더', command=RealMFrelease).place(x=120,y=100)
    Button(win, text='수비수', command=RealDEFrelease).place(x=120,y=140)
    Button(win, text='골키퍼', command=RealGKrelease).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
    
def RealFWrecruit(): # 레알 마드리드 공격수 영입
    global RealClubMoney
    global RealM
    global RealP

                            
    def RealPlayerFWrecruit():
        global RealClubMoney
        global RealM
        global RealP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Messi' in RealP) != 1:
                usedMoney+=300000000
            else:
                messagebox.showinfo('','Messi 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('L.Suarez' in RealP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Ronaldo' in RealP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Bale' in RealP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Bale 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Benzema' in RealP) != 1:
                usedMoney+=46000000
            else:
                messagebox.showinfo('','Benzema 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Neymar' in RealP) != 1:
                usedMoney+=222000000
            else:
                messagebox.showinfo('','Neymar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Lewandowski' in RealP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Muller' in RealP) != 1:
                usedMoney+=97500000
            else:
                messagebox.showinfo('','Muller 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Ronaldinho' in RealP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('C.Ronaldo' in RealP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('SON' in RealP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','SON 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('R.Carlos' in RealP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Mbappe' in RealP) != 1:
                usedMoney+=180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Rooney' in RealP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Rooney 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('M.Salah' in RealP) != 1:
                usedMoney+=39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value16.get()==1:
            if ('Kane' in RealP) != 1:
                usedMoney+=198000000
            else:
                messagebox.showinfo('','Kane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value17.get()==1:
            if ('Griezmann' in RealP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>RealClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
                
        elif usedMoney<=RealClubMoney: 
            if value1.get()==1:
                if ('Messi' in RealP) != 1:
                    RealP.append('Messi')
                    RealClubMoney=RealClubMoney-300000000
                    
            if value2.get()==1:
                if ('L.Suarez' in RealP) != 1:
                    RealP.append('L.Suarez')
                    RealClubMoney=RealClubMoney-86000000
                    
            if value3.get()==1:
                if ('Ronaldo' in RealP) != 1:
                    RealP.append('Ronaldo')
                    RealClubMoney=RealClubMoney-45000000
                    
            if value4.get()==1:
                if ('Bale' in RealP) != 1:
                    RealP.append('Bale')
                    RealClubMoney=RealClubMoney-100000000
                    
            if value5.get()==1:
                if ('Benzema' in RealP) != 1:
                    RealP.append('Benzema')
                    RealClubMoney=RealClubMoney-46000000
                    
            if value6.get()==1:
                if ('Neymar' in RealP) != 1:
                    RealP.append('Neymar')
                    RealClubMoney=RealClubMoney-222000000
                    
            if value7.get()==1:
                if ('Lewandowski' in RealP) != 1:
                    RealP.append('Lewandowski')
                    RealClubMoney=RealClubMoney-86000000
                    
            if value8.get()==1:
                if ('Muller' in RealP) != 1:
                    RealP.append('Muller')
                    RealClubMoney=RealClubMoney-97500000
                    
            if value9.get()==1:
                if ('Ronaldinho' in RealP) != 1:
                    RealP.append('Ronaldinho')
                    RealClubMoney=RealClubMoney-25000000
                    
            if value10.get()==1:
                if ('C.Ronaldo' in RealP) != 1:
                    RealP.append('C.Ronaldo')
                    RealClubMoney=RealClubMoney-100000000
                    
            if value11.get()==1:
                if ('SON' in RealP) != 1:
                    RealP.append('SON')
                    RealClubMoney=RealClubMoney-90000000
                    
            if value12.get()==1:
                if ('R.Carlos' in RealP) != 1:
                    RealP.append('R.Carlos')
                    RealClubMoney=RealClubMoney-6000000
                    
            if value13.get()==1:
                if ('Mbappe' in RealP) != 1:
                    RealP.append('Mbappe')
                    RealClubMoney=RealClubMoney-180000000
                    
            if value14.get()==1:
                if ('Rooney' in RealP) != 1:
                    RealP.append('Rooney')
                    RealClubMoney=RealClubMoney-30000000
                    
            if value15.get()==1:
                if ('M.Salah' in RealP) != 1:
                    RealP.append('M.Salah')
                    RealClubMoney=RealClubMoney-39000000
                    
            if value16.get()==1:
                if ('Kane' in RealP) != 1:
                    RealP.append('Kane')
                    RealClubMoney=RealClubMoney-198000000
                    
            if value17.get()==1:
                if ('Griezmann' in RealP) != 1:
                    RealP.append('Griezmann')
                    RealClubMoney=RealClubMoney-30000000

            
            messagebox.showinfo('','영입이 완료되었습니다.')
                
            
    
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='영입',command=RealPlayerFWrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def RealMFrecruit(): # 레알 마드리드 미드필더 영입
    global RealClubMoney
    global RealM
    global RealP
    
    def RealPlayerMFrecruit():
        global RealClubMoney
        global RealM
        global RealP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('J.S.Park' in RealP) != 1:
                usedMoney+=7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('Pogba' in RealP) != 1:
                usedMoney+=102000000
            else:
                messagebox.showinfo('','Pogba 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('A.Iniesta' in RealP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Modric' in RealP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Modirc 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Sergio Busquets' in RealP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Eriksen' in RealP) != 1:
                usedMoney+=62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Kroos' in RealP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Kroos 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('De Bruyne' in RealP) != 1:
                usedMoney+=74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Silva' in RealP) != 1:
                usedMoney+=50000000
            else:
                messagebox.showinfo('','Silva 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Isco' in RealP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Isco 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('Vidal' in RealP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Vidal 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('Casemiro' in RealP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Coutinho' in RealP) != 1:
                usedMoney+=163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Mane' in RealP) != 1:
                usedMoney+=34000000
            else:
                messagebox.showinfo('','Mane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('J.Rodriguez' in RealP) != 1:
                usedMoney+=80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 이미 해당 구단에 있습니다.')
        
                        
        if usedMoney>RealClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=RealClubMoney:
      
        
            if value1.get()==1:
                if ('J.S.Park' in RealP) != 1:
                    RealP.append('J.S.Park')
                    RealClubMoney=RealClubMoney-7300000
                    
            if value2.get()==1:
                if ('Pogba' in RealP) != 1:
                    RealP.append('Pogba')
                    RealClubMoney=RealClubMoney-102000000
                    
            if value3.get()==1:
                if ('A.Iniesta' in RealP) != 1:
                    RealP.append('A.Iniesta')
                    RealClubMoney=RealClubMoney-35000000
                    
            if value4.get()==1:
                if ('Modric' in RealP) != 1:
                    RealP.append('Modric')
                    RealClubMoney=RealClubMoney-35000000
                    
            if value5.get()==1:
                if ('Sergio Busquets' in RealP) != 1:
                    RealP.append('Sergio Busquets')
                    RealClubMoney=RealClubMoney-100000000
                    
            if value6.get()==1:
                if ('Eriksen' in RealP) != 1:
                    RealP.append('Eriksen')
                    RealClubMoney=RealClubMoney-62000000
                    
            if value7.get()==1:
                if ('Kroos' in RealP) != 1:
                    RealP.append('Kroos')
                    RealClubMoney=RealClubMoney-25000000
                    
            if value8.get()==1:
                if ('De Bruyne' in RealP) != 1:
                    RealP.append('De Bruyne')
                    RealClubMoney=RealClubMoney-74000000
                    
            if value9.get()==1:
                if ('Silva' in RealP) != 1:
                    RealP.append('Silva')
                    RealClubMoney=RealClubMoney-50000000
                    
            if value10.get()==1:
                if ('Isco' in RealP) != 1:
                    RealP.append('Isco')
                    RealClubMoney=RealClubMoney-40000000
                    
            if value11.get()==1:
                if ('Vidal' in RealP) != 1:
                    RealP.append('Vidal')
                    RealClubMoney=RealClubMoney-35000000
                    
            if value12.get()==1:
                if ('Casemiro' in RealP) != 1:
                    RealP.append('Casemiro')
                    RealClubMoney=RealClubMoney-6000000
                    
            if value13.get()==1:
                if ('Coutinho' in RealP) != 1:
                    RealP.append('Coutinho')
                    RealClubMoney=RealClubMoney-163000000
                    
            if value14.get()==1:
                if ('Mane' in RealP) != 1:
                    RealP.append('Mane')
                    RealClubMoney=RealClubMoney-34000000
                    
            if value15.get()==1:
                if ('J.Rodriguez' in RealP) != 1:
                    RealP.append('J.Rodriguez')
                    RealClubMoney=RealClubMoney-80000000

            
            messagebox.showinfo('','영입이 완료되었습니다.')
            
                
            
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='영입',command=RealPlayerMFrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def RealDEFrecruit(): # 레알 마드리드 수비수 영입
    global RealClubMoney
    global RealM
    global RealP
    

    def RealPlayerDEFrecruit():
        global RealClubMoney
        global RealM
        global RealP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Marcelo' in RealP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value2.get()==1:
            if ('Pique' in RealP) != 1:
                usedMoney+=7000000
            else:
                messagebox.showinfo('','Pique 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value3.get()==1:
            if ('Sergio Ramos' in RealP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 이미 해당 구단에 있습니다.')
                 
                    
        if value4.get()==1:
            if ('Jordi Alba' in RealP) != 1:
                usedMoney+=14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 이미 해당 구단에 있습니다.')
                   
        if value5.get()==1:
            if ('Hummels' in RealP) != 1:
                usedMoney+=41000000
            else:
                messagebox.showinfo('','Hummels 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value6.get()==1:
            if ('Otamendi' in RealP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 이미 해당 구단에 있습니다.')
        
                    
        if usedMoney>RealClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
            
        elif usedMoney<=RealClubMoney:
      
        
            if value1.get()==1:
                if ('Marcelo' in RealP) != 1:
                    RealP.append('Marcelo')
                    RealClubMoney=RealClubMoney-6000000
                    
            if value2.get()==1:
                if ('Pique' in RealP) != 1:
                    RealP.append('Pique')
                    RealClubMoney=RealClubMoney-7000000
                    
            if value3.get()==1:
                if ('Sergio Ramos' in RealP) != 1:
                    RealP.append('Serigio Ramos')
                    RealClubMoney=RealClubMoney-90000000
                    
            if value4.get()==1:
                if ('Jordi Alba' in RealP) != 1:
                    RealP.append('Jordi Alba')
                    RealClubMoney=RealClubMoney-14000000
                    
            if value5.get()==1:
                if ('Hummels' in RealP) != 1:
                    RealP.append('Hummels')
                    RealClubMoney=RealClubMoney-41000000
                    
            if value6.get()==1:
                if ('Otamendi' in RealP) != 1:
                    RealP.append('Otamendi')
                    RealClubMoney=RealClubMoney-45000000

            
            messagebox.showinfo('','영입이 완료되었습니다.')
           
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='영입',command=RealPlayerDEFrecruit).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def RealGKrecruit(): # 레알 마드리드 골키퍼 영입
    global RealClubMoney
    global RealM
    global RealP
    

    def RealPlayerGKrecruit():
        global RealClubMoney
        global RealM
        global RealP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Casillas' in RealP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casillas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('De Gea' in RealP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','De Gea 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Neuer' in RealP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Neuer 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Buffon' in RealP) != 1:
                usedMoney+=53500000
            else:
                messagebox.showinfo('','Buffon 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Navas' in RealP) != 1:
                usedMoney+=10000000
            else:
                messagebox.showinfo('','Navas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Van der Sar' in RealP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Oblak' in RealP) != 1:
                usedMoney+=16000000
            else:
                messagebox.showinfo('','Oblak 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Ederson' in RealP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Ederson 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Lloris' in RealP) != 1:
                usedMoney+=19000000
            else:
                messagebox.showinfo('','Lloris 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Ter Stegen' in RealP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>RealClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=RealClubMoney:
          
        
            if value1.get()==1:
                if ('Casillas' in RealP) != 1:
                    RealP.append('Casillas')
                    RealClubMoney=RealClubMoney-6000000
                    
            if value2.get()==1:
                if ('De Gea' in RealP) != 1:
                    RealP.append('De Gea')
                    RealClubMoney=RealClubMoney-40000000
                    
            if value3.get()==1:
                if ('Neuer' in RealP) != 1:
                    RealP.append('Neuer')
                    RealClubMoney=RealClubMoney-30000000
                    
            if value4.get()==1:
                if ('Buffon' in RealP) != 1:
                    RealP.append('Navas')
                    RealClubMoney=RealClubMoney-53500000
                    
            if value5.get()==1:
                if ('Navas' in RealP) != 1:
                    RealP.append('Navas')
                    RealClubMoney=RealClubMoney-10000000
                    
            if value6.get()==1:
                if ('Van der Sar' in RealP) != 1:
                    RealP.append('Van der Sar')
                    RealClubMoney=RealClubMoney-23000000
                    
            if value7.get()==1:
                if ('Oblak' in RealP) != 1:
                    RealP.append('Oblak')
                    RealClubMoney=RealClubMoney-16000000
                    
            if value8.get()==1:
                if ('Ederson' in RealP) != 1:
                    RealP.append('Ederson')
                    RealClubMoney=RealClubMoney-40000000
                   
            if value9.get()==1:
                if ('Lloris' in RealP) != 1:
                    RealP.append('Lloris')
                    RealClubMoney=RealClubMoney-19000000
                    
            if value10.get()==1:
                if ('Ter Stegen' in RealP) != 1:
                    RealP.append('Ter Stegen')
                    RealClubMoney=RealClubMoney-23000000

            messagebox.showinfo('','영입이 완료되었습니다.')
           
            
         
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='영입',command=RealPlayerGKrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def RealFWrelease(): # 레알 마드리드 공격수 방출
    global RealClubMoney
    global RealM
    global RealP
    

    def RealPlayerFWrelease():
        global RealClubMoney
        global RealM
        global RealP
          
        
        if value1.get()==1:
            if ('Messi' in RealP) == 1:
                RealP.remove('Messi')
                RealClubMoney=RealClubMoney+300000000
            else:
                messagebox.showinfo('','Messi 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('L.Suarez' in RealP) == 1:
                RealP.remove('L.Suarez')
                RealClubMoney=RealClubMoney+86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Ronaldo' in RealP) == 1:
                RealP.remove('Ronaldo')
                RealClubMoney=RealClubMoney+45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Bale' in RealP) == 1:
                RealP.remove('Bale')
                RealClubMoney=RealClubMoney+100000000
            else:
                messagebox.showinfo('','Bale 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Benzema' in RealP) == 1:
                RealP.remove('Benzema')
                RealClubMoney=RealClubMoney+46000000
            else:
                messagebox.showinfo('','Benzema 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Neymar' in RealP) == 1:
                RealP.remove('Neymar')
                RealClubMoney=RealClubMoney+222000000
            else:
                messagebox.showinfo('','Neymar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Lewandowski' in RealP) == 1:
                RealP.remove('Lewandowski')
                RealClubMoney=RealClubMoney+86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Muller' in RealP) == 1:
                RealP.remove('Muller')
                RealClubMoney=RealClubMoney+97500000
            else:
                messagebox.showinfo('','Muller 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Ronaldinho' in RealP) == 1:
                RealP.remove('Ronaldinho')
                RealClubMoney=RealClubMoney+25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('C.Ronaldo' in RealP) == 1:
                RealP.remove('C.Ronaldo')
                RealClubMoney=RealClubMoney+100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('SON' in RealP) == 1:
                RealP.remove('SON')
                RealClubMoney=RealClubMoney+90000000
            else:
                messagebox.showinfo('','SON 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('R.Carlos' in RealP) == 1:
                RealP.remove('R.Carlos')
                RealClubMoney=RealClubMoney+6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Mbappe' in RealP) == 1:
                RealP.remove('Mbappe')
                RealClubMoney=RealClubMoney+180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Rooney' in RealP) == 1:
                RealP.remove('Rooney')
                RealClubMoney=RealClubMoney+30000000
            else:
                messagebox.showinfo('','Rooney 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('M.Salah' in RealP) == 1:
                RealP.remove('M.Salah')
                RealClubMoney=RealClubMoney+39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 해당 구단에 속해 있지 않습니다.')
        if value16.get()==1:
            if ('Kane' in RealP) == 1:
                RealP.remove('Kane')
                RealClubMoney=RealClubMoney+198000000
            else:
                messagebox.showinfo('','Kane 선수는 해당 구단에 속해 있지 않습니다.')
        if value17.get()==1:
            if ('Griezmann' in RealP) == 1:
                RealP.remove('Griezmann')
                RealClubMoney=RealClubMoney+30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 해당 구단에 속해 있지 않습니다.')
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='방출',command=RealPlayerFWrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def RealMFrelease(): # 레알 마드리드 미드필더 방출
    global RealClubMoney
    global RealM
    global RealP
    

    def RealPlayerMFrelease():
        global RealClubMoney
        global RealM
        global RealP
      
        
        if value1.get()==1:
            if ('J.S.Park' in RealP) == 1:
                RealP.remove('J.S.Park')
                RealClubMoney=RealClubMoney+7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pogba' in RealP) == 1:
                RealP.remove('Pogba')
                RealClubMoney=RealClubMoney+102000000
            else:
                messagebox.showinfo('','Pogba 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('A.Iniesta' in RealP) == 1:
                RealP.remove('A.Iniesta')
                RealClubMoney=RealClubMoney+35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Modric' in RealP) == 1:
                RealP.remove('Modric')
                RealClubMoney=RealClubMoney+35000000
            else:
                messagebox.showinfo('','Modric 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Sergio Busquets' in RealP) == 1:
                RealP.remove('Sergio Busquets')
                RealClubMoney=RealClubMoney+100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Eriksen' in RealP) == 1:
                RealP.remove('Eriksen')
                RealClubMoney=RealClubMoney+62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Kroos' in RealP) == 1:
                RealP.remove('Kroos')
                RealClubMoney=RealClubMoney+25000000
            else:
                messagebox.showinfo('','Kroos 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('De Bruyne' in RealP) == 1:
                RealP.remove('De Bruyne')
                RealClubMoney=RealClubMoney+74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Silva' in RealP) == 1:
                RealP.remove('Silva')
                RealClubMoney=RealClubMoney+50000000
            else:
                messagebox.showinfo('','Silva 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Isco' in RealP) == 1:
                RealP.remove('Isco')
                RealClubMoney=RealClubMoney+40000000
            else:
                messagebox.showinfo('','Isco 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('Vidal' in RealP) == 1:
                RealP.remove('Vidal')
                RealClubMoney=RealClubMoney+35000000
            else:
                messagebox.showinfo('','Vidal 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('Casemiro' in RealP) == 1:
                RealP.remove('Casemiro')
                RealClubMoney=RealClubMoney+6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Coutinho' in RealP) == 1:
                RealP.remove('Coutinho')
                RealClubMoney=RealClubMoney+163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Mane' in RealP) == 1:
                RealP.remove('Mane')
                RealClubMoney=RealClubMoney+34000000
            else:
                messagebox.showinfo('','Mane 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('J.Rodriguez' in RealP) == 1:
                RealP.remove('J.Rodriguez')
                RealClubMoney=RealClubMoney+80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='방출',command=RealPlayerMFrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def RealDEFrelease(): # 레알 마드리드 수비수 방출
    global RealClubMoney
    global RealM
    global RealP
    

    def RealPlayerDEFrelease():
        global RealClubMoney
        global RealM
        global RealP
      
        
        if value1.get()==1:
            if ('Marcelo' in RealP) == 1:
                RealP.remove('Marcelo')
                RealClubMoney=RealClubMoney+6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pique' in RealP) == 1:
                RealP.remove('Pique')
                RealClubMoney=RealClubMoney+7000000
            else:
                messagebox.showinfo('','Pique 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Sergio Ramos' in RealP) == 1:
                RealP.remove('Sergio Ramos')
                RealClubMoney=RealClubMoney+90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Jordi Alba' in RealP) == 1:
                RealP.remove('Jordi Alba')
                RealClubMoney=RealClubMoney+14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Hummels' in RealP) == 1:
                RealP.remove('Hummels')
                RealClubMoney=RealClubMoney+41000000
            else:
                messagebox.showinfo('','Hummels 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Otamendi' in RealP) == 1:
                RealP.remove('Otamendi')
                RealClubMoney=RealClubMoney+45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='방출',command=RealPlayerDEFrelease).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def RealGKrelease(): # 레알 마드리드 골키퍼 방출
    global RealClubMoney
    global RealM
    global RealP
    

    def RealPlayerGKrelease():
        global RealClubMoney
        global RealM
        global RealP
      
        
        if value1.get()==1:
            if ('Casillas' in RealP) == 1:
                RealP.remove('Casillas')
                RealClubMoney=RealClubMoney+6000000
            else:
                messagebox.showinfo('','Casillas 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('De Gea' in RealP) == 1:
                RealP.remove('De Gea')
                RealClubMoney=RealClubMoney+40000000
            else:
                messagebox.showinfo('','De Gea 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Neuer' in RealP) == 1:
                RealP.remove('Neuer')
                RealClubMoney=RealClubMoney+30000000
            else:
                messagebox.showinfo('','Neuer 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Buffon' in RealP) == 1:
                RealP.remove('Buffon')
                RealClubMoney=RealClubMoney+53500000
            else:
                messagebox.showinfo('','Buffon 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Navas' in RealP) == 1:
                RealP.remove('Navas')
                RealClubMoney=RealClubMoney+10000000
            else:
                messagebox.showinfo('','Navas 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Van der Sar' in RealP) == 1:
                RealP.remove('Van der Sar')
                RealClubMoney=RealClubMoney+23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Oblak' in RealP) == 1:
                RealP.remove('Oblak')
                RealClubMoney=RealClubMoney+16000000
            else:
                messagebox.showinfo('','Oblak 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Ederson' in RealP) == 1:
                RealP.remove('Ederson')
                RealClubMoney=RealClubMoney+40000000
            else:
                messagebox.showinfo('','Ederson 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Lloris' in RealP) == 1:
                RealP.remove('Lloris')
                RealClubMoney=RealClubMoney+19000000
            else:
                messagebox.showinfo('','Lloris 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Ter Stegen' in RealP) == 1:
                RealP.remove('Ter Stegen')
                RealClubMoney=RealClubMoney+23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Real2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='방출',command=RealPlayerGKrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCrecruit(): # 맨시티 영입
    global ManCClubMoney
    global ManCM
    global ManCP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=ManCFWrecruit).place(x=120,y=60)
    Button(win, text='미드필더', command=ManCMFrecruit).place(x=120,y=100)
    Button(win, text='수비수', command=ManCDEFrecruit).place(x=120,y=140)
    Button(win, text='골키퍼', command=ManCGKrecruit).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
def ManCrelease(): # 맨시티 방출
    global ManCClubMoney
    global ManCM
    global ManCP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=ManCFWrelease).place(x=120,y=60)
    Button(win, text='미드필더', command=ManCMFrelease).place(x=120,y=100)
    Button(win, text='수비수', command=ManCDEFrelease).place(x=120,y=140)
    Button(win, text='골키퍼', command=ManCGKrelease).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
    
def ManCFWrecruit(): # 맨시티 공격수 영입
    global ManCClubMoney
    global ManCM
    global ManCP
                            
    def ManCPlayerFWrecruit():
        global ManCClubMoney
        global ManCM
        global ManCP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Messi' in ManCP) != 1:
                usedMoney+=300000000
            else:
                messagebox.showinfo('','Messi 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('L.Suarez' in ManCP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Ronaldo' in ManCP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Bale' in ManCP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Bale 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Benzema' in ManCP) != 1:
                usedMoney+=46000000
            else:
                messagebox.showinfo('','Benzema 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Neymar' in ManCP) != 1:
                usedMoney+=222000000
            else:
                messagebox.showinfo('','Neymar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Lewandowski' in ManCP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Muller' in ManCP) != 1:
                usedMoney+=97500000
            else:
                messagebox.showinfo('','Muller 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Ronaldinho' in ManCP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('C.Ronaldo' in ManCP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','C..Ronaldo 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('SON' in ManCP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','SON 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('R.Carlos' in ManCP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Mbappe' in ManCP) != 1:
                usedMoney+=180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Rooney' in ManCP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Rooney 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('M.Salah' in ManCP) != 1:
                usedMoney+=39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value16.get()==1:
            if ('Kane' in ManCP) != 1:
                usedMoney+=198000000
            else:
                messagebox.showinfo('','Kane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value17.get()==1:
            if ('Griezmann' in ManCP) !=1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>ManCClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
                
        elif usedMoney<=ManCClubMoney:
            if value1.get()==1:
                if ('Messi' in ManCP) != 1:
                    ManCP.append('Messi')
                    ManCClubMoney=ManCClubMoney-300000000
                    
            if value2.get()==1:
                if ('L.Suarez' in ManCP) != 1:
                    ManCP.append('L.Suarez')
                    ManCClubMoney=ManCClubMoney-86000000
                    
            if value3.get()==1:
                if ('Ronaldo' in ManCP) != 1:
                    ManCP.append('Ronaldo')
                    ManCClubMoney=ManCClubMoney-45000000
                    
            if value4.get()==1:
                if ('Bale' in ManCP) != 1:
                    ManCP.append('Bale')
                    ManCClubMoney=ManCClubMoney-100000000
                    
            if value5.get()==1:
                if ('Benzema' in ManCP) != 1:
                    ManCP.append('Benzema')
                    ManCClubMoney=ManCClubMoney-46000000
                    
            if value6.get()==1:
                if ('Neymar' in ManCP) != 1:
                    ManCP.append('Neymar')
                    ManCClubMoney=ManCClubMoney-222000000
                    
            if value7.get()==1:
                if ('Lewandowski' in ManCP) != 1:
                    ManCP.append('Lewandowski')
                    ManCClubMoney=ManCClubMoney-86000000
                    
            if value8.get()==1:
                if ('Muller' in ManCP) != 1:
                    ManCP.append('Muller')
                    ManCClubMoney=ManCClubMoney-97500000
                    
            if value9.get()==1:
                if ('Ronaldinho' in ManCP) != 1:
                    ManCP.append('Ronaldinho')
                    ManCClubMoney=ManCClubMoney-25000000
                    
            if value10.get()==1:
                if ('C.Ronaldo' in ManCP) != 1:
                    ManCP.append('C.Ronaldo')
                    ManCClubMoney=ManCClubMoney-100000000
                    
            if value11.get()==1:
                if ('SON' in ManCP) != 1:
                    ManCP.append('SON')
                    ManCClubMoney=ManCClubMoney-90000000
                    
            if value12.get()==1:
                if ('R.Carlos' in ManCP) != 1:
                    ManCP.append('R.Carlos')
                    ManCClubMoney=ManCClubMoney-6000000
                    
            if value13.get()==1:
                if ('Mbappe' in ManCP) != 1:
                    ManCP.append('Mbappe')
                    ManCClubMoney=ManCClubMoney-180000000
                    
            if value14.get()==1:
                if ('Rooney' in ManCP) != 1:
                    ManCP.append('Rooney')
                    ManCClubMoney=ManCClubMoney-30000000
                    
            if value15.get()==1:
                if ('M.Salah' in ManCP) != 1:
                    ManCP.append('M.Salah')
                    ManCClubMoney=ManCClubMoney-39000000
                    
            if value16.get()==1:
                if ('Kane' in ManCP) != 1:
                    ManCP.append('Kane')
                    ManCClubMoney=ManCClubMoney-198000000
                    
            if value17.get()==1:
                if ('Griezmann' in ManCP) != 1:
                    ManCP.append('Griezmann')
                    ManCClubMoney=ManCClubMoney-30000000
                    


            
            messagebox.showinfo('','영입이 완료되었습니다.')
            
           
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='영입',command=ManCPlayerFWrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCMFrecruit(): # 맨시티 미드필더 영입
    global ManCClubMoney
    global ManCM
    global ManCP
    
    def ManCPlayerMFrecruit():
        global ManCClubMoney
        global ManCM
        global ManCP
        usedMoney=0
        if value1.get()==1:
            if ('J.S.Park' in ManCP) != 1:
                usedMoney+=7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('Pogba' in ManCP) != 1:
                usedMoney+=102000000
            else:
                messagebox.showinfo('','Pogba 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('A.Iniesta' in ManCP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Modric' in ManCP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Modric 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Sergio Busquets' in ManCP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Eriksen' in ManCP) != 1:
                usedMoney+=62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Kroos' in ManCP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Kroos 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('De Bruyne' in ManCP) != 1:
                usedMoney+=74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Silva' in ManCP) != 1:
                usedMoney+=50000000
            else:
                messagebox.showinfo('','Silva 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Isco' in ManCP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Isco 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('Vidal' in ManCP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Vidal 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('Casemiro' in ManCP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Coutinho' in ManCP) != 1:
                usedMoney+=163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Mane' in ManCP) != 1:
                usedMoney+=34000000
            else:
                messagebox.showinfo('','Mane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('J.Rodriguez' in ManCP) != 1:
                usedMoney+=80000000
            else:
                messagebox.showinfo('','J.Rodirguez 선수는 이미 해당 구단에 있습니다.')
        
                        
        if usedMoney>ManCClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=ManCClubMoney:
            if value1.get()==1:
                if ('J.S.Park' in ManCP) != 1:
                    ManCP.append('J.S.Park')
                    ManCClubMoney=ManCClubMoney-7300000
                    
            if value2.get()==1:
                if ('Pogba' in ManCP) != 1:
                    ManCP.append('Pogba')
                    ManCClubMoney=ManCClubMoney-102000000
                    
            if value3.get()==1:
                if ('A.Iniesta' in ManCP) != 1:
                    ManCP.append('A.Iniesta')
                    ManCClubMoney=ManCClubMoney-35000000
                    
            if value4.get()==1:
                if ('Modric' in ManCP) != 1:
                    ManCP.append('Modric')
                    ManCClubMoney=ManCClubMoney-35000000
                    
            if value5.get()==1:
                if ('Sergio Busquets' in ManCP) != 1:
                    ManCP.append('Sergio Busquets')
                    ManCClubMoney=ManCClubMoney-100000000
                    
            if value6.get()==1:
                if ('Eriksen' in ManCP) != 1:
                    ManCP.append('Eriksen')
                    ManCClubMoney=ManCClubMoney-62000000
                    
            if value7.get()==1:
                if ('Kroos' in ManCP) != 1:
                    ManCP.append('Kroos')
                    ManCClubMoney=ManCClubMoney-25000000
                    
            if value8.get()==1:
                if ('De Bruyne' in ManCP) != 1:
                    ManCP.append('De Bruyne')
                    ManCClubMoney=ManCClubMoney-74000000
                    
            if value9.get()==1:
                if ('Silva' in ManCP) != 1:
                    ManCP.append('Silva')
                    ManCClubMoney=ManCClubMoney-50000000
                    
            if value10.get()==1:
                if ('Isco' in ManCP) != 1:
                    ManCP.append('Isco')
                    ManCClubMoney=ManCClubMoney-40000000
                    
            if value11.get()==1:
                if ('Vidal' in ManCP) != 1:
                    ManCP.append('Vidal')
                    ManCClubMoney=ManCClubMoney-35000000
                    
            if value12.get()==1:
                if ('Casemiro' in ManCP) != 1:
                    ManCP.append('Casemiro')
                    ManCClubMoney=ManCClubMoney-6000000
                    
            if value13.get()==1:
                if ('Coutinho' in ManCP) != 1:
                    ManCP.append('Coutinho')
                    ManCClubMoney=ManCClubMoney-163000000
                    
            if value14.get()==1:
                if ('Mane' in ManCP) != 1:
                    ManCP.append('Mane')
                    ManCClubMoney=ManCClubMoney-34000000
                    
            if value15.get()==1:
                if ('J.Rodriguez' in ManCP) != 1:
                    ManCP.append('J.Rodriguez')
                    ManCClubMoney=ManCClubMoney-80000000

            
            messagebox.showinfo('','영입이 완료되었습니다.')
            
                
           
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='영입',command=ManCPlayerMFrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCDEFrecruit(): # 맨시티 수비수 영입
    global ManCClubMoney
    global ManCM
    global ManCP
    

    def ManCPlayerDEFrecruit():
        global ManCClubMoney
        global ManCM
        global ManCP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Marcelo' in ManCP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value2.get()==1:
            if ('Pique' in ManCP) != 1:
                usedMoney+=7000000
            else:
                messagebox.showinfo('','Pique 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value3.get()==1:
            if ('Sergio Ramos' in ManCP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 이미 해당 구단에 있습니다.')
                 
                    
        if value4.get()==1:
            if ('Jordi Alba' in ManCP) != 1:
                usedMoney+=14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 이미 해당 구단에 있습니다.')
                   
        if value5.get()==1:
            if ('Hummels' in ManCP) != 1:
                usedMoney+=41000000
            else:
                messagebox.showinfo('','Hummels 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value6.get()==1:
            if ('Otamendi' in ManCP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 이미 해당 구단에 있습니다.')
        
                    
        if usedMoney>ManCClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
            
        elif usedMoney<=ManCClubMoney:
        
            if value1.get()==1:
                if ('Marcelo' in ManCP) != 1:
                    ManCP.append('Marcelo')
                    ManCClubMoney=ManCClubMoney-6000000
            if value2.get()==1:
                if ('Pique' in ManCP) != 1:
                    ManCP.append('Pique')
                    ManCClubMoney=ManCClubMoney-7000000
            if value3.get()==1:
                if ('Sergio Ramos' in ManCP) != 1:
                    ManCP.append('Serigio Ramos')
                    ManCClubMoney=ManCClubMoney-90000000
            if value4.get()==1:
                if ('Jordi Alba' in ManCP) != 1:
                    ManCP.append('Jordi Alba')
                    ManCClubMoney=ManCClubMoney-14000000
            if value5.get()==1:
                if ('Hummels' in ManCP) != 1:
                    ManCP.append('Hummels')
                    ManCClubMoney=ManCClubMoney-41000000
            if value6.get()==1:
                if ('Otamendi' in ManCP) != 1:
                    ManCP.append('Otamendi')
                    ManCClubMoney=ManCClubMoney-45000000

            
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='영입',command=ManCPlayerDEFrecruit).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCGKrecruit(): # 맨시티 골키퍼 영입
    global ManCClubMoney
    global ManCM
    global ManCP
    

    def ManCPlayerGKrecruit():
        global ManCClubMoney
        global ManCM
        global ManCP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Casillas' in ManCP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casillas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('De Gea' in ManCP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','De Gea 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Neuer' in ManCP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Neuer 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Buffon' in ManCP) != 1:
                usedMoney+=53500000
            else:
                messagebox.showinfo('','Buffon 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Navas' in ManCP) != 1:
                usedMoney+=10000000
            else:
                messagebox.showinfo('','Navas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Van der Sar' in ManCP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Oblak' in ManCP) != 1:
                usedMoney+=16000000
            else:
                messagebox.showinfo('','Oblak 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Ederson' in ManCP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Ederson 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Lloris' in ManCP) != 1:
                usedMoney+=19000000
            else:
                messagebox.showinfo('','Lloris 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Ter Stegen' in ManCP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>ManCClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=ManCClubMoney:
        
            if value1.get()==1:
                if ('Casillas' in ManCP) != 1:
                    ManCP.append('Casillas')
                    ManCClubMoney=ManCClubMoney-6000000
            if value2.get()==1:
                if ('De Gea' in ManCP) != 1:
                    ManCP.append('De Gea')
                    ManCClubMoney=ManCClubMoney-40000000
            if value3.get()==1:
                if ('Neuer' in ManCP) != 1:
                    ManCP.append('Neuer')
                    ManCClubMoney=ManCClubMoney-30000000
            if value4.get()==1:
                if ('Buffon' in ManCP) != 1:
                    ManCP.append('Navas')
                    ManCClubMoney=ManCClubMoney-53500000
            if value5.get()==1:
                if ('Navas' in ManCP) != 1:
                    ManCP.append('Navas')
                    ManCClubMoney=ManCClubMoney-10000000
            if value6.get()==1:
                if ('Van der Sar' in ManCP) != 1:
                    ManCP.append('Van der Sar')
                    ManCClubMoney=ManCClubMoney-23000000
            if value7.get()==1:
                if ('Oblak' in ManCP) != 1:
                    ManCP.append('Oblak')
                    ManCClubMoney=ManCClubMoney-16000000
            if value8.get()==1:
                if ('Ederson' in ManCP) != 1:
                    ManCP.append('Ederson')
                    ManCClubMoney=ManCClubMoney-40000000
            if value9.get()==1:
                if ('Lloris' in ManCP) != 1:
                    ManCP.append('Lloris')
                    ManCClubMoney=ManCClubMoney-19000000
            if value10.get()==1:
                if ('Ter Stegen' in ManCP) != 1:
                    ManCP.append('Ter Stegen')
                    ManCClubMoney=ManCClubMoney-23000000
           
            
                
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='영입',command=ManCPlayerGKrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCFWrelease(): # 맨시티 공격수 방출
    global ManCClubMoney
    global ManCM
    global ManCP
    

    def ManCPlayerFWrelease():
        global ManCClubMoney
        global ManCM
        global ManCP
      
        
        if value1.get()==1:
            if ('Messi' in ManCP) == 1:
                ManCP.remove('Messi')
                ManCClubMoney=ManCClubMoney+300000000
            else:
                messagebox.showinfo('','Messi 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('L.Suarez' in ManCP) == 1:
                ManCP.remove('L.Suarez')
                ManCClubMoney=ManCClubMoney+86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Ronaldo' in ManCP) == 1:
                ManCP.remove('Ronaldo')
                ManCClubMoney=ManCClubMoney+45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Bale' in ManCP) == 1:
                ManCP.remove('Bale')
                ManCClubMoney=ManCClubMoney+100000000
            else:
                messagebox.showinfo('','Bale 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Benzema' in ManCP) == 1:
                ManCP.remove('Benzema')
                ManCClubMoney=ManCClubMoney+46000000
            else:
                messagebox.showinfo('','Benzema 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Neymar' in ManCP) == 1:
                ManCP.remove('Neymar')
                ManCClubMoney=ManCClubMoney+222000000
            else:
                messagebox.showinfo('','Neymar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Lewandowski' in ManCP) == 1:
                ManCP.remove('Lewandowski')
                ManCClubMoney=ManCClubMoney+86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Muller' in ManCP) == 1:
                ManCP.remove('Muller')
                ManCClubMoney=ManCClubMoney+97500000
            else:
                messagebox.showinfo('','Muller 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Ronaldinho' in ManCP) == 1:
                ManCP.remove('Ronaldinho')
                ManCClubMoney=ManCClubMoney+25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('C.Ronaldo' in ManCP) == 1:
                ManCP.remove('C.Ronaldo')
                ManCClubMoney=ManCClubMoney+100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('SON' in ManCP) == 1:
                ManCP.remove('SON')
                ManCClubMoney=ManCClubMoney+90000000
            else:
                messagebox.showinfo('','SON 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('R.Carlos' in ManCP) == 1:
                ManCP.remove('R.Carlos')
                ManCClubMoney=ManCClubMoney+6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Mbappe' in ManCP) == 1:
                ManCP.remove('Mbappe')
                ManCClubMoney=ManCClubMoney+180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Rooney' in ManCP) == 1:
                ManCP.remove('Rooney')
                ManCClubMoney=ManCClubMoney+30000000
            else:
                messagebox.showinfo('','Rooney 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('M.Salah' in ManCP) == 1:
                ManCP.remove('M.Salah')
                ManCClubMoney=ManCClubMoney+39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 해당 구단에 속해 있지 않습니다.')
        if value16.get()==1:
            if ('Kane' in ManCP) == 1:
                ManCP.remove('Kane')
                ManCClubMoney=ManCClubMoney+198000000
            else:
                messagebox.showinfo('','Kane 선수는 해당 구단에 속해 있지 않습니다.')
        if value17.get()==1:
            if ('Griezmann' in ManCP) == 1:
                ManCP.remove('Griezmann')
                ManCClubMoney=ManCClubMoney+30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 해당 구단에 속해 있지 않습니다.')
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='방출',command=ManCPlayerFWrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCMFrelease(): # 맨시티 미드필더 방출
    global ManCClubMoney
    global ManCM
    global ManCP
    

    def ManCPlayerMFrelease():
        global ManCClubMoney
        global ManCM
        global ManCP
        
        if value1.get()==1:
            if ('J.S.Park' in ManCP) == 1:
                ManCP.remove('J.S.Park')
                ManCClubMoney=ManCClubMoney+7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pogba' in ManCP) == 1:
                ManCP.remove('Pogba')
                ManCClubMoney=ManCClubMoney+102000000
            else:
                messagebox.showinfo('','Pogba 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('A.Iniesta' in ManCP) == 1:
                ManCP.remove('A.Iniesta')
                ManCClubMoney=ManCClubMoney+35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Modric' in ManCP) == 1:
                ManCP.remove('Modric')
                ManCClubMoney=ManCClubMoney+35000000
            else:
                messagebox.showinfo('','Modric 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Sergio Busquets' in ManCP) == 1:
                ManCP.remove('Sergio Busquets')
                ManCClubMoney=ManCClubMoney+100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Eriksen' in ManCP) == 1:
                ManCP.remove('Eriksen')
                ManCClubMoney=ManCClubMoney+62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Kroos' in ManCP) == 1:
                ManCP.remove('Kroos')
                ManCClubMoney=ManCClubMoney+25000000
            else:
                messagebox.showinfo('','Kroos 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('De Bruyne' in ManCP) == 1:
                ManCP.remove('De Bruyne')
                ManCClubMoney=ManCClubMoney+74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Silva' in ManCP) == 1:
                ManCP.remove('Silva')
                ManCClubMoney=ManCClubMoney+50000000
            else:
                messagebox.showinfo('','Silva 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Isco' in ManCP) == 1:
                ManCP.remove('Isco')
                ManCClubMoney=ManCClubMoney+40000000
            else:
                messagebox.showinfo('','Isco 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('Vidal' in ManCP) == 1:
                ManCP.remove('Vidal')
                ManCClubMoney=ManCClubMoney+35000000
            else:
                messagebox.showinfo('','Vidal 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('Casemiro' in ManCP) == 1:
                ManCP.remove('Casemiro')
                ManCClubMoney=ManCClubMoney+6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Coutinho' in ManCP) == 1:
                ManCP.remove('Coutinho')
                ManCClubMoney=ManCClubMoney+163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Mane' in ManCP) == 1:
                ManCP.remove('Mane')
                ManCClubMoney=ManCClubMoney+34000000
            else:
                messagebox.showinfo('','Mane 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('J.Rodriguez' in ManCP) == 1:
                ManCP.remove('J.Rodriguez')
                ManCClubMoney=ManCClubMoney+80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='방출',command=ManCPlayerMFrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCDEFrelease(): # 맨시티 수비수 방출
    global ManCClubMoney
    global ManCM
    global ManCP
    

    def ManCPlayerDEFrelease():
        global ManCClubMoney
        global ManCM
        global ManCP
      
        
        if value1.get()==1:
            if ('Marcelo' in ManCP) == 1:
                ManCP.remove('Marcelo')
                ManCClubMoney=ManCClubMoney+6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pique' in ManCP) == 1:
                ManCP.remove('Pique')
                ManCClubMoney=ManCClubMoney+7000000
            else:
                messagebox.showinfo('','Pique 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Sergio Ramos' in ManCP) == 1:
                ManCP.remove('Sergio Ramos')
                ManCClubMoney=ManCClubMoney+90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Jordi Alba' in ManCP) == 1:
                ManCP.remove('Jordi Alba')
                ManCClubMoney=ManCClubMoney+14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Hummels' in ManCP) == 1:
                ManCP.remove('Hummels')
                ManCClubMoney=ManCClubMoney+41000000
            else:
                messagebox.showinfo('','Hummels 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Otamendi' in ManCP) == 1:
                ManCP.remove('Otamendi')
                ManCClubMoney=ManCClubMoney+45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='방출',command=ManCPlayerDEFrelease).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManCGKrelease(): # 맨시티 골키퍼 방출
    global ManCClubMoney
    global ManCM
    global ManCP
    

    def ManCPlayerGKrelease():
        global ManCClubMoney
        global ManCM
        global ManCP
      
        
        if value1.get()==1:
            if ('Casillas' in ManCP) == 1:
                ManCP.remove('Casillas')
                ManCClubMoney=ManCClubMoney+6000000
            else:
                messagebox.showinfo('','Casillas 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('De Gea' in ManCP) == 1:
                ManCP.remove('De Gea')
                ManCClubMoney=ManCClubMoney+40000000
            else:
                messagebox.showinfo('','De Gea 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Neuer' in ManCP) == 1:
                ManCP.remove('Neuer')
                ManCClubMoney=ManCClubMoney+30000000
            else:
                messagebox.showinfo('','Neuer 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Buffon' in ManCP) == 1:
                ManCP.remove('Buffon')
                ManCClubMoney=ManCClubMoney+53500000
            else:
                messagebox.showinfo('','Buffon 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Navas' in ManCP) == 1:
                ManCP.remove('Navas')
                ManCClubMoney=ManCClubMoney+10000000
            else:
                messagebox.showinfo('','Navas 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Van der Sar' in ManCP) == 1:
                ManCP.remove('Van der Sar')
                ManCClubMoney=ManCClubMoney+23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Oblak' in ManCP) == 1:
                ManCP.remove('Oblak')
                ManCClubMoney=ManCClubMoney+16000000
            else:
                messagebox.showinfo('','Oblak 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Ederson' in ManCP) == 1:
                ManCP.remove('Ederson')
                ManCClubMoney=ManCClubMoney+40000000
            else:
                messagebox.showinfo('','Ederson 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Lloris' in ManCP) == 1:
                ManCP.remove('Lloris')
                ManCClubMoney=ManCClubMoney+19000000
            else:
                messagebox.showinfo('','Lloris 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Ter Stegen' in ManCP) == 1:
                ManCP.remove('Ter Stegen')
                ManCClubMoney=ManCClubMoney+23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManC2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='방출',command=ManCPlayerGKrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUrecruit(): # 맨유 영입
    global ManUClubMoney
    global ManUM
    global ManUP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=ManUFWrecruit).place(x=120,y=60)
    Button(win, text='미드필더', command=ManUMFrecruit).place(x=120,y=100)
    Button(win, text='수비수', command=ManUDEFrecruit).place(x=120,y=140)
    Button(win, text='골키퍼', command=ManUGKrecruit).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
def ManUrelease(): # 맨유 방출
    global ManUClubMoney
    global ManUM
    global ManUP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=ManUFWrelease).place(x=120,y=60)
    Button(win, text='미드필더', command=ManUMFrelease).place(x=120,y=100)
    Button(win, text='수비수', command=ManUDEFrelease).place(x=120,y=140)
    Button(win, text='골키퍼', command=ManUGKrelease).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
    
def ManUFWrecruit(): # 맨유 공격수 영입
    global ManUClubMoney
    global ManUM
    global ManUP
                            
    def ManUPlayerFWrecruit():
        global ManUClubMoney
        global ManUM
        global ManUP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Messi' in ManUP) != 1:
                usedMoney+=300000000
            else:
                messagebox.showinfo('','Messi 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('L.Suarez' in ManUP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Ronaldo' in ManUP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Bale' in ManUP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Bale 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Benzema' in ManUP) != 1:
                usedMoney+=46000000
            else:
                messagebox.showinfo('','Benzema 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Neymar' in ManUP) != 1:
                usedMoney+=222000000
            else:
                messagebox.showinfo('','Neymar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Lewandowski' in ManUP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Muller' in ManUP) != 1:
                usedMoney+=97500000
            else:
                messagebox.showinfo('','Muller 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Ronaldinho' in ManUP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('C.Ronaldo' in ManUP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('SON' in ManUP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','SON 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('R.Carlos' in ManUP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Mbappe' in ManUP) != 1:
                usedMoney+=180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Rooney' in ManUP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Rooney 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('M.Salah' in ManUP) != 1:
                usedMoney+=39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value16.get()==1:
            if ('Kane' in ManUP) != 1:
                usedMoney+=198000000
            else:
                messagebox.showinfo('','Kane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value17.get()==1:
            if ('Griezmann' in ManUP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>ManUClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=ManUClubMoney:
            if value1.get()==1:
                if ('Messi' in ManUP) != 1:
                    ManUP.append('Messi')
                    ManUClubMoney=ManUClubMoney-300000000
            if value2.get()==1:
                if ('L.Suarez' in ManUP) != 1:
                    ManUP.append('L.Suarez')
                    ManUClubMoney=ManUClubMoney-86000000
            if value3.get()==1:
                if ('Ronaldo' in ManUP) != 1:
                    ManUP.append('Ronaldo')
                    ManUClubMoney=ManUClubMoney-45000000
            if value4.get()==1:
                if ('Bale' in ManUP) != 1:
                    ManUP.append('Bale')
                    ManUClubMoney=ManUClubMoney-100000000
            if value5.get()==1:
                if ('Benzema' in ManUP) != 1:
                    ManUP.append('Benzema')
                    ManUClubMoney=ManUClubMoney-46000000
            if value6.get()==1:
                if ('Neymar' in ManUP) != 1:
                    ManUP.append('Neymar')
                    ManUClubMoney=ManUClubMoney-222000000
            if value7.get()==1:
                if ('Lewandowski' in ManUP) != 1:
                    ManUP.append('Lewandowski')
                    ManUClubMoney=ManUClubMoney-86000000
            if value8.get()==1:
                if ('Muller' in ManUP) != 1:
                    ManUP.append('Muller')
                    ManUClubMoney=ManUClubMoney-97500000
            if value9.get()==1:
                if ('Ronaldinho' in ManUP) != 1:
                    ManUP.append('Ronaldinho')
                    ManUClubMoney=ManUClubMoney-25000000
            if value10.get()==1:
                if ('C.Ronaldo' in ManUP) != 1:
                    ManUP.append('C.Ronaldo')
                    ManUClubMoney=ManUClubMoney-100000000
            if value11.get()==1:
                if ('SON' in ManUP) != 1:
                    ManUP.append('SON')
                    ManUClubMoney=ManUClubMoney-90000000
            if value12.get()==1:
                if ('R.Carlos' in ManUP) != 1:
                    ManUP.append('R.Carlos')
                    ManUClubMoney=ManUClubMoney-6000000
            if value13.get()==1:
                if ('Mbappe' in ManUP) != 1:
                    ManUP.append('Mbappe')
                    ManUClubMoney=ManUClubMoney-180000000
            if value14.get()==1:
                if ('Rooney' in ManUP) != 1:
                    ManUP.append('Rooney')
                    ManUClubMoney=ManUClubMoney-30000000
            if value15.get()==1:
                if ('M.Salah' in ManUP) != 1:
                    ManUP.append('M.Salah')
                    ManUClubMoney=ManUClubMoney-39000000
            if value16.get()==1:
                if ('Kane' in ManUP) != 1:
                    ManUP.append('Kane')
                    ManUClubMoney=ManUClubMoney-198000000
            if value17.get()==1:
                if ('Griezmann' in ManUP) != 1:
                    ManUP.append('Griezmann')
                    ManUClubMoney=ManUClubMoney-30000000
            
           
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='영입',command=ManUPlayerFWrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUMFrecruit(): # 맨유 미드필더 영입
    global ManUClubMoney
    global ManUM
    global ManUP
    
    def ManUPlayerMFrecruit():
        global ManUClubMoney
        global ManUM
        global ManUP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('J.S.Park' in ManUP) != 1:
                usedMoney+=7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('Pogba' in ManUP) != 1:
                usedMoney+=102000000
            else:
                messagebox.showinfo('','Pogba 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('A.Iniesta' in ManUP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Modric' in ManUP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Modric 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Sergio Busquets' in ManUP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Eriksen' in ManUP) != 1:
                usedMoney+=62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Kroos' in ManUP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Kroos 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('De Bruyne' in ManUP) != 1:
                usedMoney+=74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Silva' in ManUP) != 1:
                usedMoney+=50000000
            else:
                messagebox.showinfo('','Silva 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Isco' in ManUP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Isco 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('Vidal' in ManUP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Vidal 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('Casemiro' in ManUP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Coutinho' in ManUP) != 1:
                usedMoney+=163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Mane' in ManUP) != 1:
                usedMoney+=34000000
            else:
                messagebox.showinfo('','Mane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('J.Rodriguez' in ManUP) != 1:
                usedMoney+=80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 이미 해당 구단에 있습니다.')
        
                        
        if usedMoney>ManUClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=ManUClubMoney:
        
            if value1.get()==1:
                if ('J.S.Park' in ManUP) != 1:
                    ManUP.append('J.S.Park')
                    ManUClubMoney=ManUClubMoney-7300000
            if value2.get()==1:
                if ('Pogba' in ManUP) != 1:
                    ManUP.append('Pogba')
                    ManUClubMoney=ManUClubMoney-102000000
            if value3.get()==1:
                if ('A.Iniesta' in ManUP) != 1:
                    ManUP.append('A.Iniesta')
                    ManUClubMoney=ManUClubMoney-35000000
            if value4.get()==1:
                if ('Modric' in ManUP) != 1:
                    ManUP.append('Modric')
                    ManUClubMoney=ManUClubMoney-35000000
            if value5.get()==1:
                if ('Sergio Busquets' in ManUP) != 1:
                    ManUP.append('Sergio Busquets')
                    ManUClubMoney=ManUClubMoney-100000000
            if value6.get()==1:
                if ('Eriksen' in ManUP) != 1:
                    ManUP.append('Eriksen')
                    ManUClubMoney=ManUClubMoney-62000000
            if value7.get()==1:
                if ('Kroos' in ManUP) != 1:
                    ManUP.append('Kroos')
                    ManUClubMoney=ManUClubMoney-25000000
            if value8.get()==1:
                if ('De Bruyne' in ManUP) != 1:
                    ManUP.append('De Bruyne')
                    ManUClubMoney=ManUClubMoney-74000000
            if value9.get()==1:
                if ('Silva' in ManUP) != 1:
                    ManUP.append('Silva')
                    ManUClubMoney=ManUClubMoney-50000000
            if value10.get()==1:
                if ('Isco' in ManUP) != 1:
                    ManUP.append('Isco')
                    ManUClubMoney=ManUClubMoney-40000000
            if value11.get()==1:
                if ('Vidal' in ManUP) != 1:
                    ManUP.append('Vidal')
                    ManUClubMoney=ManUClubMoney-35000000
            if value12.get()==1:
                if ('Casemiro' in ManUP) != 1:
                    ManUP.append('Casemiro')
                    ManUClubMoney=ManUClubMoney-6000000
            if value13.get()==1:
                if ('Coutinho' in ManUP) != 1:
                    ManUP.append('Coutinho')
                    ManUClubMoney=ManUClubMoney-163000000
            if value14.get()==1:
                if ('Mane' in ManUP) != 1:
                    ManUP.append('Mane')
                    ManUClubMoney=ManUClubMoney-34000000
            if value15.get()==1:
                if ('J.Rodriguez' in ManUP) != 1:
                    ManUP.append('J.Rodriguez')
                    ManUClubMoney=ManUClubMoney-80000000
            
            
            messagebox.showinfo('','영입이 완료되었습니다.')    
            
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='영입',command=ManUPlayerMFrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUDEFrecruit(): # 맨유 수비수 영입
    global ManUClubMoney
    global ManUM
    global ManUP
    

    def ManUPlayerDEFrecruit():
        global ManUClubMoney
        global ManUM
        global ManUP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Marcelo' in ManUP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value2.get()==1:
            if ('Pique' in ManUP) != 1:
                usedMoney+=7000000
            else:
                messagebox.showinfo('','Pique 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value3.get()==1:
            if ('Sergio Ramos' in ManUP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 이미 해당 구단에 있습니다.')
                 
                    
        if value4.get()==1:
            if ('Jordi Alba' in ManUP) != 1:
                usedMoney+=14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 이미 해당 구단에 있습니다.')
                   
        if value5.get()==1:
            if ('Hummels' in ManUP) != 1:
                usedMoney+=41000000
            else:
                messagebox.showinfo('','Hummels 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value6.get()==1:
            if ('Otamendi' in ManCP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 이미 해당 구단에 있습니다.')
        
                    
        if usedMoney>ManUClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
            
        elif usedMoney<=ManUClubMoney:
        
            if value1.get()==1:
                if ('Marcelo' in ManUP) != 1:
                    ManUP.append('Marcelo')
                    ManUClubMoney=ManUClubMoney-6000000
            if value2.get()==1:
                if ('Pique' in ManUP) != 1:
                    ManUP.append('Pique')
                    ManUClubMoney=ManUClubMoney-7000000
            if value3.get()==1:
                if ('Sergio Ramos' in ManUP) != 1:
                    ManUP.append('Serigio Ramos')
                    ManUClubMoney=ManUClubMoney-90000000
            if value4.get()==1:
                if ('Jordi Alba' in ManUP) != 1:
                    ManUP.append('Jordi Alba')
                    ManUClubMoney=ManUClubMoney-14000000
            if value5.get()==1:
                if ('Hummels' in ManUP) != 1:
                    ManUP.append('Hummels')
                    ManUClubMoney=ManUClubMoney-41000000
            if value6.get()==1:
                if ('Otamendi' in ManUP) != 1:
                    ManUP.append('Otamendi')
                    ManUClubMoney=ManUClubMoney-45000000
            
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='영입',command=ManUPlayerDEFrecruit).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUGKrecruit(): # 맨유 골키퍼 영입
    global ManUClubMoney
    global ManUM
    global ManUP
    

    def ManUPlayerGKrecruit():
        global ManUClubMoney
        global ManUM
        global ManUP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Casillas' in ManUP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casillas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('De Gea' in ManUP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','De Gea 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Neuer' in ManUP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Neuer 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Buffon' in ManUP) != 1:
                usedMoney+=53500000
            else:
                messagebox.showinfo('','Buffon 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Navas' in ManUP) != 1:
                usedMoney+=10000000
            else:
                messagebox.showinfo('','Navas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Van der Sar' in ManUP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Oblak' in ManUP) != 1:
                usedMoney+=16000000
            else:
                messagebox.showinfo('','Oblak 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Ederson' in ManUP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Ederson 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Lloris' in ManUP) != 1:
                usedMoney+=19000000
            else:
                messagebox.showinfo('','Lloris 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Ter Stegen' in ManUP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>ManUClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=ManUClubMoney:
        
            if value1.get()==1:
                if ('Casillas' in ManUP) != 1:
                    ManUP.append('Casillas')
                    ManUClubMoney=ManUClubMoney-6000000
            if value2.get()==1:
                if ('De Gea' in ManUP) != 1:
                    ManUP.append('De Gea')
                    ManUClubMoney=ManUClubMoney-40000000
            if value3.get()==1:
                if ('Neuer' in ManUP) != 1:
                    ManUP.append('Neuer')
                    ManUClubMoney=ManUClubMoney-30000000
            if value4.get()==1:
                if ('Buffon' in ManUP) != 1:
                    ManUP.append('Navas')
                    ManUClubMoney=ManUClubMoney-53500000
            if value5.get()==1:
                if ('Navas' in ManUP) != 1:
                    ManUP.append('Navas')
                    ManUClubMoney=ManUClubMoney-10000000
            if value6.get()==1:
                if ('Van der Sar' in ManUP) != 1:
                    ManUP.append('Van der Sar')
                    ManUClubMoney=ManUClubMoney-23000000
            if value7.get()==1:
                if ('Oblak' in ManUP) != 1:
                    ManUP.append('Oblak')
                    ManUClubMoney=ManUClubMoney-16000000
            if value8.get()==1:
                if ('Ederson' in ManUP) != 1:
                    ManUP.append('Ederson')
                    ManUClubMoney=ManUClubMoney-40000000
            if value9.get()==1:
                if ('Lloris' in ManUP) != 1:
                    ManUP.append('Lloris')
                    ManUClubMoney=ManUClubMoney-19000000
            if value10.get()==1:
                if ('Ter Stegen' in ManUP) != 1:
                    ManUP.append('Ter Stegen')
                    ManUClubMoney=ManUClubMoney-23000000
           
            
                
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='영입',command=ManUPlayerGKrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUFWrelease(): # 맨유 공격수 방출
    global ManUClubMoney
    global ManUM
    global ManUP
    

    def ManUPlayerFWrelease():
        global ManUClubMoney
        global ManUM
        global ManUP
      
        
        if value1.get()==1:
            if ('Messi' in ManUP) == 1:
                ManUP.remove('Messi')
                ManUClubMoney=ManUClubMoney+300000000
            else:
                messagebox.showinfo('','Messi 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('L.Suarez' in ManUP) == 1:
                ManUP.remove('L.Suarez')
                ManUClubMoney=ManUClubMoney+86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Ronaldo' in ManUP) == 1:
                ManUP.remove('Ronaldo')
                ManUClubMoney=ManUClubMoney+45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Bale' in ManUP) == 1:
                ManUP.remove('Bale')
                ManUClubMoney=ManUClubMoney+100000000
            else:
                messagebox.showinfo('','Bale 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Benzema' in ManUP) == 1:
                ManUP.remove('Benzema')
                ManUClubMoney=ManUClubMoney+46000000
            else:
                messagebox.showinfo('','Benzema 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Neymar' in ManUP) == 1:
                ManUP.remove('Neymar')
                ManUClubMoney=ManUClubMoney+222000000
            else:
                messagebox.showinfo('','Neymar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Lewandowski' in ManUP) == 1:
                ManUP.remove('Lewandowski')
                ManUClubMoney=ManUClubMoney+86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Muller' in ManUP) == 1:
                ManUP.remove('Muller')
                ManUClubMoney=ManUClubMoney+97500000
            else:
                messagebox.showinfo('','Muller 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Ronaldinho' in ManUP) == 1:
                ManUP.remove('Ronaldinho')
                ManUClubMoney=ManUClubMoney+25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('C.Ronaldo' in ManUP) == 1:
                ManUP.remove('C.Ronaldo')
                ManUClubMoney=ManUClubMoney+100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('SON' in ManUP) == 1:
                ManUP.remove('SON')
                ManUClubMoney=ManUClubMoney+90000000
            else:
                messagebox.showinfo('','SON 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('R.Carlos' in ManUP) == 1:
                ManUP.remove('R.Carlos')
                ManUClubMoney=ManUClubMoney+6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Mbappe' in ManUP) == 1:
                ManUP.remove('Mbappe')
                ManUClubMoney=ManUClubMoney+180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Rooney' in ManUP) == 1:
                ManUP.remove('Rooney')
                ManUClubMoney=ManUClubMoney+30000000
            else:
                messagebox.showinfo('','Rooney 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('M.Salah' in ManUP) == 1:
                ManUP.remove('M.Salah')
                ManUClubMoney=ManUClubMoney+39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 해당 구단에 속해 있지 않습니다.')
        if value16.get()==1:
            if ('Kane' in ManUP) == 1:
                ManUP.remove('Kane')
                ManUClubMoney=ManUClubMoney+198000000
            else:
                messagebox.showinfo('','Kane 선수는 해당 구단에 속해 있지 않습니다.')
        if value17.get()==1:
            if ('Griezmann' in ManUP) == 1:
                ManUP.remove('Griezmann')
                ManUClubMoney=ManUClubMoney+30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 해당 구단에 속해 있지 않습니다.')
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='방출',command=ManUPlayerFWrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUMFrelease(): # 맨유 미드필더 방출
    global ManUClubMoney
    global ManUM
    global ManUP
    

    def ManUPlayerMFrelease():
        global ManUClubMoney
        global ManUM
        global ManUP
      
        
        if value1.get()==1:
            if ('J.S.Park' in ManUP) == 1:
                ManUP.remove('J.S.Park')
                ManUClubMoney=ManUClubMoney+7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pogba' in ManUP) == 1:
                ManUP.remove('Pogba')
                ManUClubMoney=ManUClubMoney+102000000
            else:
                messagebox.showinfo('','Pogba 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('A.Iniesta' in ManUP) == 1:
                ManUP.remove('A.Iniesta')
                ManUClubMoney=ManUClubMoney+35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Modric' in ManUP) == 1:
                ManUP.remove('Modric')
                ManUClubMoney=ManUClubMoney+35000000
            else:
                messagebox.showinfo('','Modric 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Sergio Busquets' in ManUP) == 1:
                ManUP.remove('Sergio Busquets')
                ManUClubMoney=ManUClubMoney+100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Eriksen' in ManUP) == 1:
                ManUP.remove('Eriksen')
                ManUClubMoney=ManUClubMoney+62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Kroos' in ManUP) == 1:
                ManUP.remove('Kroos')
                ManUClubMoney=ManUClubMoney+25000000
            else:
                messagebox.showinfo('','Kroos 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('De Bruyne' in ManUP) == 1:
                ManUP.remove('De Bruyne')
                ManUClubMoney=ManUClubMoney+74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Silva' in ManUP) == 1:
                ManUP.remove('Silva')
                ManUClubMoney=ManUClubMoney+50000000
            else:
                messagebox.showinfo('','Silva 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Isco' in ManUP) == 1:
                ManUP.remove('Isco')
                ManUClubMoney=ManUClubMoney+40000000
            else:
                messagebox.showinfo('','Isco 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('Vidal' in ManUP) == 1:
                ManUP.remove('Vidal')
                ManUClubMoney=ManUClubMoney+35000000
            else:
                messagebox.showinfo('','Vidal 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('Casemiro' in ManUP) == 1:
                ManUP.remove('Casemiro')
                ManUClubMoney=ManUClubMoney+6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Coutinho' in ManUP) == 1:
                ManUP.remove('Coutinho')
                ManUClubMoney=ManUClubMoney+163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Mane' in ManUP) == 1:
                ManUP.remove('Mane')
                ManUClubMoney=ManUClubMoney+34000000
            else:
                messagebox.showinfo('','Mane 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('J.Rodriguez' in ManUP) == 1:
                ManUP.remove('J.Rodriguez')
                ManUClubMoney=ManUClubMoney+80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='방출',command=ManUPlayerMFrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUDEFrelease(): # 맨유 수비수 방출
    global ManUClubMoney
    global ManUM
    global ManUP
    

    def ManUPlayerDEFrelease():
        global ManUClubMoney
        global ManUM
        global ManUP
      
        
        if value1.get()==1:
            if ('Marcelo' in ManUP) == 1:
                ManUP.remove('Marcelo')
                ManUClubMoney=ManUClubMoney+6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pique' in ManUP) == 1:
                ManUP.remove('Pique')
                ManUClubMoney=ManUClubMoney+7000000
            else:
                messagebox.showinfo('','Pique 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Sergio Ramos' in ManUP) == 1:
                ManUP.remove('Sergio Ramos')
                ManUClubMoney=ManUClubMoney+90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Jordi Alba' in ManUP) == 1:
                ManUP.remove('Jordi Alba')
                ManUClubMoney=ManUClubMoney+14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Hummels' in ManUP) == 1:
                ManUP.remove('Hummels')
                ManUClubMoney=ManUClubMoney+41000000
            else:
                messagebox.showinfo('','Hummels 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Otamendi' in ManUP) == 1:
                ManUP.remove('Otamendi')
                ManUClubMoney=ManUClubMoney+45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='방출',command=ManUPlayerDEFrelease).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def ManUGKrelease(): # 맨유 골키퍼 방출
    global ManUClubMoney
    global ManUM
    global ManUP
    

    def ManUPlayerGKrelease():
        global ManUClubMoney
        global ManUM
        global ManUP
      
        
        if value1.get()==1:
            if ('Casillas' in ManUP) == 1:
                ManUP.remove('Casillas')
                ManUClubMoney=ManUClubMoney+6000000
            else:
                messagebox.showinfo('','Casillas 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('De Gea' in ManUP) == 1:
                ManUP.remove('De Gea')
                ManUClubMoney=ManUClubMoney+40000000
            else:
                messagebox.showinfo('','De Gea 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Neuer' in ManUP) == 1:
                ManUP.remove('Neuer')
                ManUClubMoney=ManUClubMoney+30000000
            else:
                messagebox.showinfo('','Neuer 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Buffon' in ManUP) == 1:
                ManUP.remove('Buffon')
                ManUClubMoney=ManUClubMoney+53500000
            else:
                messagebox.showinfo('','Buffon 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Navas' in ManUP) == 1:
                ManUP.remove('Navas')
                ManUClubMoney=ManUClubMoney+10000000
            else:
                messagebox.showinfo('','Navas 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Van der Sar' in ManUP) == 1:
                ManUP.remove('Van der Sar')
                ManUClubMoney=ManUClubMoney+23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Oblak' in ManUP) == 1:
                ManUP.remove('Oblak')
                ManUClubMoney=ManUClubMoney+16000000
            else:
                messagebox.showinfo('','Oblak 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Ederson' in ManUP) == 1:
                ManUP.remove('Ederson')
                ManUClubMoney=ManUClubMoney+40000000
            else:
                messagebox.showinfo('','Ederson 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Lloris' in ManUP) == 1:
                ManUP.remove('Lloris')
                ManUClubMoney=ManUClubMoney+19000000
            else:
                messagebox.showinfo('','Lloris 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Ter Stegen' in ManUP) == 1:
                ManUP.remove('Ter Stegen')
                ManUClubMoney=ManUClubMoney+23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="ManU2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='방출',command=ManUPlayerGKrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def Livrecruit(): # 리버풀 영입
    global LivClubMoney
    global LivM
    global LivP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=LivFWrecruit).place(x=120,y=60)
    Button(win, text='미드필더', command=LivMFrecruit).place(x=120,y=100)
    Button(win, text='수비수', command=LivDEFrecruit).place(x=120,y=140)
    Button(win, text='골키퍼', command=LivGKrecruit).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
    
def Livrelease(): # 리버풀 방출
    global LivClubMoney
    global LivM
    global LivP
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Button(win, text='공격수', command=LivFWrelease).place(x=120,y=60)
    Button(win, text='미드필더', command=LivMFrelease).place(x=120,y=100)
    Button(win, text='수비수', command=LivDEFrelease).place(x=120,y=140)
    Button(win, text='골키퍼', command=LivGKrelease).place(x=120,y=180)
    Button(win, text='완료', command=win.destroy).place(x=120, y=220)
    win.mainloop()
    
def LivFWrecruit(): # 리버풀 공격수 영입
    global LivClubMoney
    global LivM
    global LivP
                            
    def LivPlayerFWrecruit():
        global LivClubMoney
        global LivM
        global LivP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Messi' in LivP) != 1:
                usedMoney+=300000000
            else:
                messagebox.showinfo('','Messi 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('L.Suarez' in LivP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('Ronaldo' in LivP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Bale' in LivP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Bale 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Benzema' in LivP) != 1:
                usedMoney+=46000000
            else:
                messagebox.showinfo('','Benzema 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Neymar' in LivP) != 1:
                usedMoney+=222000000
            else:
                messagebox.showinfo('','Neymar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Lewandowski' in LivP) != 1:
                usedMoney+=86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Muller' in LivP) != 1:
                usedMoney+=97500000
            else:
                messagebox.showinfo('','Muller 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Ronaldinho' in LivP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('C.Ronaldo' in LivP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('SON' in LivP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','SON 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('R.Carlos' in LivP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Mbappe' in LivP) != 1:
                usedMoney+=180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Rooney' in LivP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Rooney 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('M.Salah' in LivP) != 1:
                usedMoney+=39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value16.get()==1:
            if ('Kane' in LivP) != 1:
                usedMoney+=198000000
            else:
                messagebox.showinfo('','Kane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value17.get()==1:
            if ('Griezmann' in LivP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>LivClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=LivClubMoney:
        
            if value1.get()==1:
                if ('Messi' in LivP) != 1:
                    LivP.append('Messi')
                    LivClubMoney=LivClubMoney-300000000
            if value2.get()==1:
                if ('L.Suarez' in LivP) != 1:
                    LivP.append('L.Suarez')
                    LivClubMoney=LivClubMoney-86000000
            if value3.get()==1:
                if ('Ronaldo' in LivP) != 1:
                    LivP.append('Ronaldo')
                    LivClubMoney=LivClubMoney-45000000
            if value4.get()==1:
                if ('Bale' in LivP) != 1:
                    LivP.append('Bale')
                    LivClubMoney=LivClubMoney-100000000
            if value5.get()==1:
                if ('Benzema' in LivP) != 1:
                    LivP.append('Benzema')
                    LivClubMoney=LivClubMoney-46000000
            if value6.get()==1:
                if ('Neymar' in LivP) != 1:
                    LivP.append('Neymar')
                    LivClubMoney=LivClubMoney-222000000
            if value7.get()==1:
                if ('Lewandowski' in LivP) != 1:
                    LivP.append('Lewandowski')
                    LivClubMoney=LivClubMoney-86000000
            if value8.get()==1:
                if ('Muller' in LivP) != 1:
                    LivP.append('Muller')
                    LivClubMoney=LivClubMoney-97500000
            if value9.get()==1:
                if ('Ronaldinho' in LivP) != 1:
                    LivP.append('Ronaldinho')
                    LivClubMoney=LivClubMoney-25000000
            if value10.get()==1:
                if ('C.Ronaldo' in LivP) != 1:
                    LivP.append('C.Ronaldo')
                    LivClubMoney=LivClubMoney-100000000
            if value11.get()==1:
                if ('SON' in LivP) != 1:
                    LivP.append('SON')
                    LivClubMoney=LivClubMoney-90000000
            if value12.get()==1:
                if ('R.Carlos' in LivP) != 1:
                    LivP.append('R.Carlos')
                    LivClubMoney=LivClubMoney-6000000
            if value13.get()==1:
                if ('Mbappe' in LivP) != 1:
                    LivP.append('Mbappe')
                    LivClubMoney=LivClubMoney-180000000
            if value14.get()==1:
                if ('Rooney' in LivP) != 1:
                    LivP.append('Rooney')
                    LivClubMoney=LivClubMoney-30000000
            if value15.get()==1:
                if ('M.Salah' in LivP) != 1:
                    LivP.append('M.Salah')
                    LivClubMoney=LivClubMoney-39000000
            if value16.get()==1:
                if ('Kane' in LivP) != 1:
                    LivP.append('Kane')
                    LivClubMoney=LivClubMoney-198000000
            if value17.get()==1:
                if ('Griezmann' in LivP) != 1:
                    LivP.append('Griezmann')
                    LivClubMoney=LivClubMoney-30000000
            
            
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='영입',command=LivPlayerFWrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def LivMFrecruit(): # 리버풀 미드필더 영입
    global LivClubMoney
    global LivM
    global LivP
    
    def LivPlayerMFrecruit():
        global LivClubMoney
        global LivM
        global LivP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('J.S.Park' in LivP) != 1:
                usedMoney+=7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value2.get()==1:
            if ('Pogba' in LivP) != 1:
                usedMoney+=102000000
            else:
                messagebox.showinfo('','Pogba 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value3.get()==1:
            if ('A.Iniesta' in LivP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 이미 해당 구단에 있습니다.')
                     
                        
        if value4.get()==1:
            if ('Modric' in LivP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Modric 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Sergio Busquets' in LivP) != 1:
                usedMoney+=100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Eriksen' in LivP) != 1:
                usedMoney+=62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Kroos' in LivP) != 1:
                usedMoney+=25000000
            else:
                messagebox.showinfo('','Kroos 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('De Bruyne' in LivP) != 1:
                usedMoney+=74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Silva' in LivP) != 1:
                usedMoney+=50000000
            else:
                messagebox.showinfo('','Silva 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Isco' in LivP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Isco 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value11.get()==1:
            if ('Vidal' in LivP) != 1:
                usedMoney+=35000000
            else:
                messagebox.showinfo('','Vidal 선수는 이미 해당 구단에 있습니다.')
                        
                       
                    
        if value12.get()==1:
            if ('Casemiro' in LivP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value13.get()==1:
            if ('Coutinho' in LivP) != 1:
                usedMoney+=163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value14.get()==1:
            if ('Mane' in LivP) != 1:
                usedMoney+=34000000
            else:
                messagebox.showinfo('','Mane 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value15.get()==1:
            if ('J.Rodriguez' in LivP) != 1:
                usedMoney+=80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 이미 해당 구단에 있습니다.')
        
                        
        if usedMoney>LivClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=LivClubMoney:
            if value1.get()==1:
                if ('J.S.Park' in LivP) != 1:
                    LivP.append('J.S.Park')
                    LivClubMoney=LivClubMoney-7300000
            if value2.get()==1:
                if ('Pogba' in LivP) != 1:
                    LivP.append('Pogba')
                    LivClubMoney=LivClubMoney-102000000
            if value3.get()==1:
                if ('A.Iniesta' in LivP) != 1:
                    LivP.append('A.Iniesta')
                    LivClubMoney=LivClubMoney-35000000
            if value4.get()==1:
                if ('Modric' in LivP) != 1:
                    LivP.append('Modric')
                    LivClubMoney=LivClubMoney-35000000
            if value5.get()==1:
                if ('Sergio Busquets' in LivP) != 1:
                    LivP.append('Sergio Busquets')
                    LivClubMoney=LivClubMoney-100000000
            if value6.get()==1:
                if ('Eriksen' in LivP) != 1:
                    LivP.append('Eriksen')
                    LivClubMoney=LivClubMoney-62000000
            if value7.get()==1:
                if ('Kroos' in LivP) != 1:
                    LivP.append('Kroos')
                    LivClubMoney=LivClubMoney-25000000
            if value8.get()==1:
                if ('De Bruyne' in LivP) != 1:
                    LivP.append('De Bruyne')
                    LivClubMoney=LivClubMoney-74000000
            if value9.get()==1:
                if ('Silva' in LivP) != 1:
                    LivP.append('Silva')
                    LivClubMoney=LivClubMoney-50000000
            if value10.get()==1:
                if ('Isco' in LivP) != 1:
                    LivP.append('Isco')
                    LivClubMoney=LivClubMoney-40000000
            if value11.get()==1:
                if ('Vidal' in LivP) != 1:
                    LivP.append('Vidal')
                    LivClubMoney=LivClubMoney-35000000
            if value12.get()==1:
                if ('Casemiro' in LivP) != 1:
                    LivP.append('Casemiro')
                    LivClubMoney=LivClubMoney-6000000
            if value13.get()==1:
                if ('Coutinho' in LivP) != 1:
                    LivP.append('Coutinho')
                    LivClubMoney=LivClubMoney-163000000
            if value14.get()==1:
                if ('Mane' in LivP) != 1:
                    LivP.append('Mane')
                    LivClubMoney=LivClubMoney-34000000
            if value15.get()==1:
                if ('J.Rodriguez' in LivP) != 1:
                    LivP.append('J.Rodriguez')
                    LivClubMoney=LivClubMoney-80000000
            
                
            messagebox.showinfo('','영입이 완료되었습니다.')
        
            
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='영입',command=LivPlayerMFrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def LivDEFrecruit(): # 리버풀 수비수 영입
    global LivClubMoney
    global LivM
    global LivP
    

    def LivPlayerDEFrecruit():
        global LivClubMoney
        global LivM
        global LivP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Marcelo' in LivP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value2.get()==1:
            if ('Pique' in LivP) != 1:
                usedMoney+=7000000
            else:
                messagebox.showinfo('','Pique 선수는 이미 해당 구단에 있습니다.')        
                    
        if value3.get()==1:
            if ('Sergio Ramos' in LivP) != 1:
                usedMoney+=90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 이미 해당 구단에 있습니다.')     
                    
        if value4.get()==1:
            if ('Jordi Alba' in LivP) != 1:
                usedMoney+=14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 이미 해당 구단에 있습니다.')
                   
        if value5.get()==1:
            if ('Hummels' in LivP) != 1:
                usedMoney+=41000000
            else:
                messagebox.showinfo('','Hummels 선수는 이미 해당 구단에 있습니다.')
                    
                    
        if value6.get()==1:
            if ('Otamendi' in LivP) != 1:
                usedMoney+=45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 이미 해당 구단에 있습니다.')
        
                    
        if usedMoney>LivClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
            
        elif usedMoney<=LivClubMoney:
            
                
                
            if value1.get()==1:
                if ('Marcelo' in LivP) != 1:
                    LivP.append('Marcelo')
                    LivClubMoney=LivClubMoney-6000000
                    
            if value2.get()==1:
                if ('Pique' in LivP) != 1:
                    LivP.append('Pique')
                    LivClubMoney=LivClubMoney-7000000
            if value3.get()==1:
                if ('Sergio Ramos' in LivP) != 1:
                    LivP.append('Serigio Ramos')
                    LivClubMoney=LivClubMoney-90000000
            if value4.get()==1:
                if ('Jordi Alba' in LivP) != 1:
                    LivP.append('Jordi Alba')
                    LivClubMoney=LivClubMoney-14000000
            if value5.get()==1:
                if ('Hummels' in LivP) != 1:
                    LivP.append('Hummels')
                    LivClubMoney=LivClubMoney-41000000
            if value6.get()==1:
                if ('Otamendi' in LivP) != 1:
                    LivP.append('Otamendi')
                    LivClubMoney=LivClubMoney-45000000
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='영입',command=LivPlayerDEFrecruit).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def LivGKrecruit(): # 리버풀 골키퍼 영입
    global LivClubMoney
    global LivM
    global LivP
    

    def LivPlayerGKrecruit():
        global LivClubMoney
        global LivM
        global LivP
        global usedMoney
        usedMoney=0
        if value1.get()==1:
            if ('Casillas' in LivP) != 1:
                usedMoney+=6000000
            else:
                messagebox.showinfo('','Casillas 선수는 이미 해당 구단에 있습니다.')            
                        
        if value2.get()==1:
            if ('De Gea' in LivP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','De Gea 선수는 이미 해당 구단에 있습니다.')            
                        
        if value3.get()==1:
            if ('Neuer' in LivP) != 1:
                usedMoney+=30000000
            else:
                messagebox.showinfo('','Neuer 선수는 이미 해당 구단에 있습니다.')         
                        
        if value4.get()==1:
            if ('Buffon' in LivP) != 1:
                usedMoney+=53500000
            else:
                messagebox.showinfo('','Buffon 선수는 이미 해당 구단에 있습니다.')
                       
        if value5.get()==1:
            if ('Navas' in LivP) != 1:
                usedMoney+=10000000
            else:
                messagebox.showinfo('','Navas 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value6.get()==1:
            if ('Van der Sar' in LivP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value7.get()==1:
            if ('Oblak' in LivP) != 1:
                usedMoney+=16000000
            else:
                messagebox.showinfo('','Oblak 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value8.get()==1:
            if ('Ederson' in LivP) != 1:
                usedMoney+=40000000
            else:
                messagebox.showinfo('','Ederson 선수는 이미 해당 구단에 있습니다.')
                       
                        
        if value9.get()==1:
            if ('Lloris' in LivP) != 1:
                usedMoney+=19000000
            else:
                messagebox.showinfo('','Lloris 선수는 이미 해당 구단에 있습니다.')
                        
                        
        if value10.get()==1:
            if ('Ter Stegen' in LivP) != 1:
                usedMoney+=23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 이미 해당 구단에 있습니다.')
                        
        if usedMoney>LivClubMoney:
            messagebox.showinfo('','남아 있는 자본이 충분하지 않습니다.')
        elif usedMoney<=LivClubMoney:
        
            if value1.get()==1:
                if ('Casillas' in LivP) != 1:
                    LivP.append('Casillas')
                    LivClubMoney=LivClubMoney-6000000
            if value2.get()==1:
                if ('De Gea' in LivP) != 1:
                    LivP.append('De Gea')
                    LivClubMoney=LivClubMoney-40000000
            if value3.get()==1:
                if ('Neuer' in LivP) != 1:
                    LivP.append('Neuer')
                    LivClubMoney=LivClubMoney-30000000
            if value4.get()==1:
                if ('Buffon' in LivP) != 1:
                    LivP.append('Navas')
                    LivClubMoney=LivClubMoney-53500000
            if value5.get()==1:
                if ('Navas' in LivP) != 1:
                    LivP.append('Navas')
                    LivClubMoney=LivClubMoney-10000000
            if value6.get()==1:
                if ('Van der Sar' in LivP) != 1:
                    LivP.append('Van der Sar')
                    LivClubMoney=LivClubMoney-23000000
            if value7.get()==1:
                if ('Oblak' in LivP) != 1:
                    LivP.append('Oblak')
                    LivClubMoney=LivClubMoney-16000000
            if value8.get()==1:
                if ('Ederson' in LivP) != 1:
                    LivP.append('Ederson')
                    LivClubMoney=LivClubMoney-40000000
            if value9.get()==1:
                if ('Lloris' in LivP) != 1:
                    LivP.append('Lloris')
                    LivClubMoney=LivClubMoney-19000000
            if value10.get()==1:
                if ('Ter Stegen' in LivP) != 1:
                    LivP.append('Ter Stegen')
                    LivClubMoney=LivClubMoney-23000000
           
            
                
            messagebox.showinfo('','영입이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="영입할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='영입',command=LivPlayerGKrecruit).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def LivFWrelease(): # 리버풀 공격수 방출
    global LivClubMoney
    global LivM
    global LivP
    

    def LivPlayerFWrelease():
        global LivClubMoney
        global LivM
        global LivP
      
        
        if value1.get()==1:
            if ('Messi' in LivP) == 1:
                LivP.remove('Messi')
                LivClubMoney=LivClubMoney+300000000
            else:
                messagebox.showinfo('','Messi 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('L.Suarez' in LivP) == 1:
                LivP.remove('L.Suarez')
                LivClubMoney=LivClubMoney+86000000
            else:
                messagebox.showinfo('','L.Suarez 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Ronaldo' in LivP) == 1:
                LivP.remove('Ronaldo')
                LivClubMoney=LivClubMoney+45000000
            else:
                messagebox.showinfo('','Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Bale' in LivP) == 1:
                LivP.remove('Bale')
                LivClubMoney=LivClubMoney+100000000
            else:
                messagebox.showinfo('','Bale 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Benzema' in LivP) == 1:
                LivP.remove('Benzema')
                LivClubMoney=LivClubMoney+46000000
            else:
                messagebox.showinfo('','Benzema 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Neymar' in LivP) == 1:
                LivP.remove('Neymar')
                LivClubMoney=LivClubMoney+222000000
            else:
                messagebox.showinfo('','Neymar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Lewandowski' in LivP) == 1:
                LivP.remove('Lewandowski')
                LivClubMoney=LivClubMoney+86000000
            else:
                messagebox.showinfo('','Lewandowski 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Muller' in LivP) == 1:
                LivP.remove('Muller')
                LivClubMoney=LivClubMoney+97500000
            else:
                messagebox.showinfo('','Muller 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Ronaldinho' in LivP) == 1:
                LivP.remove('Ronaldinho')
                LivClubMoney=LivClubMoney+25000000
            else:
                messagebox.showinfo('','Ronaldinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('C.Ronaldo' in LivP) == 1:
                LivP.remove('C.Ronaldo')
                LivClubMoney=LivClubMoney+100000000
            else:
                messagebox.showinfo('','C.Ronaldo 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('SON' in LivP) == 1:
                LivP.remove('SON')
                LivClubMoney=LivClubMoney+90000000
            else:
                messagebox.showinfo('','SON 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('R.Carlos' in LivP) == 1:
                LivP.remove('R.Carlos')
                LivClubMoney=LivClubMoney+6000000
            else:
                messagebox.showinfo('','R.Carlos 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Mbappe' in LivP) == 1:
                LivP.remove('Mbappe')
                LivClubMoney=LivClubMoney+180000000
            else:
                messagebox.showinfo('','Mbappe 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Rooney' in LivP) == 1:
                LivP.remove('Rooney')
                LivClubMoney=LivClubMoney+30000000
            else:
                messagebox.showinfo('','Rooney 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('M.Salah' in LivP) == 1:
                LivP.remove('M.Salah')
                LivClubMoney=LivClubMoney+39000000
            else:
                messagebox.showinfo('','M.Salah 선수는 해당 구단에 속해 있지 않습니다.')
        if value16.get()==1:
            if ('Kane' in LivP) == 1:
                LivP.remove('Kane')
                LivClubMoney=LivClubMoney+198000000
            else:
                messagebox.showinfo('','Kane 선수는 해당 구단에 속해 있지 않습니다.')
        if value17.get()==1:
            if ('Griezmann' in LivP) == 1:
                LivP.remove('Griezmann')
                LivClubMoney=LivClubMoney+30000000
            else:
                messagebox.showinfo('','Griezmann 선수는 해당 구단에 속해 있지 않습니다.')
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하세요 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Messi", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.L.Suarez", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Ronaldo", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Bale", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Benzema", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Neymar", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Lewandowski", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.Muller", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Ronaldinho", variable=value9,onvalue=1,offvalue=0).place(x=120,y=380)
    value10 = IntVar()
    Checkbutton(win, text="10.C.Ronaldo", variable=value10,onvalue=1,offvalue=0).place(x=280,y=60)
    value11 = IntVar()
    Checkbutton(win, text="11.SON", variable=value11,onvalue=1,offvalue=0).place(x=280,y=100)
    value12 = IntVar()
    Checkbutton(win, text="12.R.Carlos", variable=value12,onvalue=1,offvalue=0).place(x=280,y=140)
    value13 = IntVar()
    Checkbutton(win, text="13.Mbappe", variable=value13,onvalue=1,offvalue=0).place(x=280,y=180)
    value14 = IntVar()
    Checkbutton(win, text="14.Rooney", variable=value14,onvalue=1,offvalue=0).place(x=280,y=220)
    value15 = IntVar()
    Checkbutton(win, text="15.M.Salah", variable=value15,onvalue=1,offvalue=0).place(x=280,y=260)
    value16 = IntVar()
    Checkbutton(win, text="16.Kane", variable=value16,onvalue=1,offvalue=0).place(x=280,y=300)
    value17 = IntVar()
    Checkbutton(win, text="17.Griezmann", variable=value17,onvalue=1,offvalue=0).place(x=280,y=340)
    Button(win, text='방출',command=LivPlayerFWrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def LivMFrelease(): # 리버풀 미드필더 방출
    global LivClubMoney
    global LivM
    global LivP
    

    def LivPlayerMFrelease():
        global LivClubMoney
        global LivM
        global LivP
      
        
        if value1.get()==1:
            if ('J.S.Park' in LivP) == 1:
                LivP.remove('J.S.Park')
                LivClubMoney=LivClubMoney+7300000
            else:
                messagebox.showinfo('','J.S.Park 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pogba' in LivP) == 1:
                LivP.remove('Pogba')
                LivClubMoney=LivClubMoney+102000000
            else:
                messagebox.showinfo('','Pogba 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('A.Iniesta' in LivP) == 1:
                LivP.remove('A.Iniesta')
                LivClubMoney=LivClubMoney+35000000
            else:
                messagebox.showinfo('','A.Iniesta 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Modric' in LivP) == 1:
                LivP.remove('Modric')
                LivClubMoney=LivClubMoney+35000000
            else:
                messagebox.showinfo('','Modric 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Sergio Busquets' in LivP) == 1:
                LivP.remove('Sergio Busquets')
                LivClubMoney=LivClubMoney+100000000
            else:
                messagebox.showinfo('','Sergio Busquets 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Eriksen' in LivP) == 1:
                LivP.remove('Eriksen')
                LivClubMoney=LivClubMoney+62000000
            else:
                messagebox.showinfo('','Eriksen 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Kroos' in LivP) == 1:
                LivP.remove('Kroos')
                LivClubMoney=LivClubMoney+25000000
            else:
                messagebox.showinfo('','Kroos 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('De Bruyne' in LivP) == 1:
                LivP.remove('De Bruyne')
                LivClubMoney=LivClubMoney+74000000
            else:
                messagebox.showinfo('','De Bruyne 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Silva' in LivP) == 1:
                LivP.remove('Silva')
                LivClubMoney=LivClubMoney+50000000
            else:
                messagebox.showinfo('','Silva 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Isco' in LivP) == 1:
                LivP.remove('Isco')
                LivClubMoney=LivClubMoney+40000000
            else:
                messagebox.showinfo('','Isco 선수는 해당 구단에 속해 있지 않습니다.')
        if value11.get()==1:
            if ('Vidal' in LivP) == 1:
                LivP.remove('Vidal')
                LivClubMoney=LivClubMoney+35000000
            else:
                messagebox.showinfo('','Vidal 선수는 해당 구단에 속해 있지 않습니다.')
        if value12.get()==1:
            if ('Casemiro' in LivP) == 1:
                LivP.remove('Casemiro')
                LivClubMoney=LivClubMoney+6000000
            else:
                messagebox.showinfo('','Casemiro 선수는 해당 구단에 속해 있지 않습니다.')
        if value13.get()==1:
            if ('Coutinho' in LivP) == 1:
                LivP.remove('Coutinho')
                LivClubMoney=LivClubMoney+163000000
            else:
                messagebox.showinfo('','Coutinho 선수는 해당 구단에 속해 있지 않습니다.')
        if value14.get()==1:
            if ('Mane' in LivP) == 1:
                LivP.remove('Mane')
                LivClubMoney=LivClubMoney+34000000
            else:
                messagebox.showinfo('','Mane 선수는 해당 구단에 속해 있지 않습니다.')
        if value15.get()==1:
            if ('J.Rodriguez' in LivP) == 1:
                LivP.remove('J.Rodriguez')
                LivClubMoney=LivClubMoney+80000000
            else:
                messagebox.showinfo('','J.Rodriguez 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.J.S.Park", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pogba", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.A.Iniesta", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Modric", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Sergio Busquets", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Eriksen", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    value7 = IntVar()
    Checkbutton(win, text="7.Kroos", variable=value7,onvalue=1,offvalue=0).place(x=120,y=300)
    value8 = IntVar()
    Checkbutton(win, text="8.De Bruyne", variable=value8,onvalue=1,offvalue=0).place(x=120,y=340)
    value9 = IntVar()
    Checkbutton(win, text="9.Silva", variable=value9,onvalue=1,offvalue=0).place(x=280,y=60)
    value10 = IntVar()
    Checkbutton(win, text="10.Isco", variable=value10,onvalue=1,offvalue=0).place(x=280,y=100)
    value11 = IntVar()
    Checkbutton(win, text="11.Vidal", variable=value11,onvalue=1,offvalue=0).place(x=280,y=140)
    value12 = IntVar()
    Checkbutton(win, text="12.Casemiro", variable=value12,onvalue=1,offvalue=0).place(x=280,y=180)
    value13 = IntVar()
    Checkbutton(win, text="13.Coutinho", variable=value13,onvalue=1,offvalue=0).place(x=280,y=220)
    value14 = IntVar()
    Checkbutton(win, text="14.Mane", variable=value14,onvalue=1,offvalue=0).place(x=280,y=260)
    value15 = IntVar()
    Checkbutton(win, text="15.J.Rodriguez", variable=value15,onvalue=1,offvalue=0).place(x=280,y=300)
    value16 = IntVar()
    Button(win, text='방출',command=LivPlayerMFrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def LivDEFrelease(): # 리버풀 수비수 방출
    global LivClubMoney
    global LivM
    global LivP
    

    def LivPlayerDEFrelease():
        global LivClubMoney
        global LivM
        global LivP
      
        
        if value1.get()==1:
            if ('Marcelo' in LivP) == 1:
                LivP.remove('Marcelo')
                LivClubMoney=LivClubMoney+6000000
            else:
                messagebox.showinfo('','Marcelo 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('Pique' in LivP) == 1:
                LivP.remove('Pique')
                LivClubMoney=LivClubMoney+7000000
            else:
                messagebox.showinfo('','Pique 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Sergio Ramos' in LivP) == 1:
                LivP.remove('Sergio Ramos')
                LivClubMoney=LivClubMoney+90000000
            else:
                messagebox.showinfo('','Sergio Ramos 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Jordi Alba' in LivP) == 1:
                LivP.remove('Jordi Alba')
                LivClubMoney=LivClubMoney+14000000
            else:
                messagebox.showinfo('','Jordi Alba 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Hummels' in LivP) == 1:
                LivP.remove('Hummels')
                LivClubMoney=LivClubMoney+41000000
            else:
                messagebox.showinfo('','Hummels 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Otamendi' in LivP) == 1:
                LivP.remove('Otamendi')
                LivClubMoney=LivClubMoney+45000000
            else:
                messagebox.showinfo('','Otamendi 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    Checkbutton(win, text="1.Marcelo", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.Pique", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Sergio Ramos", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Jordi Alba", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Hummels", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Otamendi", variable=value6,onvalue=1,offvalue=0).place(x=120,y=260)
    Button(win, text='방출',command=LivPlayerDEFrelease).place(x=500,y=60)    
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()
    
def LivGKrelease(): # 리버풀 골키퍼 방출
    global LivClubMoney
    global LivM
    global LivP
    

    def LivPlayerGKrelease():
        global LivClubMoney
        global LivM
        global LivP
      
        
        if value1.get()==1:
            if ('Casillas' in LivP) == 1:
                LivP.remove('Casillas')
                LivClubMoney=LivClubMoney+6000000
            else:
                messagebox.showinfo('','Casillas 선수는 해당 구단에 속해 있지 않습니다.')
        if value2.get()==1:
            if ('De Gea' in LivP) == 1:
                LivP.remove('De Gea')
                LivClubMoney=LivClubMoney+40000000
            else:
                messagebox.showinfo('','De Gea 선수는 해당 구단에 속해 있지 않습니다.')
        if value3.get()==1:
            if ('Neuer' in LivP) == 1:
                LivP.remove('Neuer')
                LivClubMoney=LivClubMoney+30000000
            else:
                messagebox.showinfo('','Neuer 선수는 해당 구단에 속해 있지 않습니다.')
        if value4.get()==1:
            if ('Buffon' in LivP) == 1:
                LivP.remove('Buffon')
                LivClubMoney=LivClubMoney+53500000
            else:
                messagebox.showinfo('','Buffon 선수는 해당 구단에 속해 있지 않습니다.')
        if value5.get()==1:
            if ('Navas' in LivP) == 1:
                LivP.remove('Navas')
                LivClubMoney=LivClubMoney+10000000
            else:
                messagebox.showinfo('','Navas 선수는 해당 구단에 속해 있지 않습니다.')
        if value6.get()==1:
            if ('Van der Sar' in LivP) == 1:
                LivP.remove('Van der Sar')
                LivClubMoney=LivClubMoney+23000000
            else:
                messagebox.showinfo('','Van der Sar 선수는 해당 구단에 속해 있지 않습니다.')
        if value7.get()==1:
            if ('Oblak' in LivP) == 1:
                LivP.remove('Oblak')
                LivClubMoney=LivClubMoney+16000000
            else:
                messagebox.showinfo('','Oblak 선수는 해당 구단에 속해 있지 않습니다.')
        if value8.get()==1:
            if ('Ederson' in LivP) == 1:
                LivP.remove('Ederson')
                LivClubMoney=LivClubMoney+40000000
            else:
                messagebox.showinfo('','Ederson 선수는 해당 구단에 속해 있지 않습니다.')
        if value9.get()==1:
            if ('Lloris' in LivP) == 1:
                LivP.remove('Lloris')
                LivClubMoney=LivClubMoney+19000000
            else:
                messagebox.showinfo('','Lloris 선수는 해당 구단에 속해 있지 않습니다.')
        if value10.get()==1:
            if ('Ter Stegen' in LivP) == 1:
                LivP.remove('Ter Stegen')
                LivClubMoney=LivClubMoney+23000000
            else:
                messagebox.showinfo('','Ter Stegen 선수는 해당 구단에 속해 있지 않습니다.')
        
            
        messagebox.showinfo('','방출이 완료되었습니다.')
    win = Toplevel()
    win.geometry('900x430')

    backgnd1=PhotoImage(file="Liv2.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="방출할 선수를 선택하시오 : ").place(x=40,y=20)
    value1 = IntVar()
    v1=Checkbutton(win, text="1.Casillas", variable=value1,onvalue=1,offvalue=0).place(x=120,y=60)
    value2 = IntVar()
    Checkbutton(win, text="2.De Gea", variable=value2,onvalue=1,offvalue=0).place(x=120,y=100)
    value3 = IntVar()
    Checkbutton(win, text="3.Neuer", variable=value3,onvalue=1,offvalue=0).place(x=120,y=140)
    value4 = IntVar()
    Checkbutton(win, text="4.Buffon", variable=value4,onvalue=1,offvalue=0).place(x=120,y=180)
    value5 = IntVar()
    Checkbutton(win, text="5.Navas", variable=value5,onvalue=1,offvalue=0).place(x=120,y=220)
    value6 = IntVar()
    Checkbutton(win, text="6.Van der Sar", variable=value6,onvalue=1,offvalue=0).place(x=280,y=60)
    value7 = IntVar()
    Checkbutton(win, text="7.Oblak", variable=value7,onvalue=1,offvalue=0).place(x=280,y=100)
    value8 = IntVar()
    Checkbutton(win, text="8.Ederson", variable=value8,onvalue=1,offvalue=0).place(x=280,y=140)
    value9 = IntVar()
    Checkbutton(win, text="9.Lloris", variable=value9,onvalue=1,offvalue=0).place(x=280,y=180)
    value10 = IntVar()
    Checkbutton(win, text="10.Ter Stegen", variable=value10,onvalue=1,offvalue=0).place(x=280,y=220)
    Button(win, text='방출',command=LivPlayerGKrelease).place(x=500,y=60)
    Button(win, text='완료', command=win.destroy).place(x=500, y=100)
    win.mainloop()

def resetClub():
    global BarClubMoney
    global BarM
    global BarP
    global RealClubMoney
    global RealM
    global RealP
    global ManCClubMoney
    global ManCM
    global ManCP
    global ManUMoney
    global ManUM
    global ManUP
    global LivClubMoney
    global LivM
    global LivP
   
    win = Toplevel()
    win.geometry('900x430')

    Button(win, text='완료', command=win.destroy).place(x=100, y=260)
    backgnd1=PhotoImage(file="reset.gif")
    w=Label(win,image=backgnd1)
    w.pack()
    Label(win, text="초기화하고 싶은 구단을 선택하시오 : ").place(x=40,y=20)
    Button(win, text='1.Barcelona',command=resetBar).place(x=100,y=50)
    Button(win, text='2.Real Madrid',command=resetReal).place(x=100,y=90)
    Button(win, text='3.Manchester City',command=resetManC).place(x=100,y=130)
    Button(win, text='4.Manchester United',command=resetManU).place(x=100,y=170)
    Button(win, text='5.Liverpool',command=resetLiv).place(x=100,y=210)
     # 버튼을 누르면 자식 윈도우를 닫고 부모 윈도우로 돌아감 
    Button(win, text='완료', command=win.destroy).place(x=100, y=260)
    win.mainloop()

# 구단 초기화 메뉴
def resetBar():
    global BarClubMoney
    global BarM
    global BarP
    BarClubMoney=BarM
    BarP=[]
    messagebox.showinfo('','초기화가 완료되었습니다.')
def resetReal():
    global RealClubMoney
    global RealM
    global RealP
    RealClubMoney=RealM
    RealP=[]
    messagebox.showinfo('','초기화가 완료되었습니다.')
def resetManC():
    global ManCClubMoney
    global ManCM
    global ManCP
    ManCClubMoney=ManCM
    ManCP=[]
    messagebox.showinfo('','초기화가 완료되었습니다.')
def resetManU():
    global ManUClubMoney
    global ManUM
    global ManUP
    ManUClubMoney=ManUM
    ManUP=[]
    
    messagebox.showinfo('','초기화가 완료되었습니다.')
def resetLiv():
    global LivClubMoney
    global LivM
    global LivP
    LivClubMoney=LivM
    LivP=[]
    messagebox.showinfo('','초기화가 완료되었습니다.')

def StartGame(): # 에어 하키 게임
    global x_R,y_R,x_R_change, y_R_change,x_F_change,y_F_change,x_F,y_F,point1P,point2P

    def moving(): # asdw 키 입력시 Ryan 이동 , 화살표 키 입력시 Frodo 이동
        global x_R_change, y_R_change, x_R, y_R, x_F_change, y_F_change, x_F, y_F
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                y_R_change = y_R_change + 30
            if event.key == pygame.K_w:
                y_R_change = y_R_change - 30
            if event.key == pygame.K_a:
                x_R_change = x_R_change - 30
            if event.key == pygame.K_d:
                x_R_change = x_R_change + 30
            if event.key == pygame.K_DOWN:
                y_F_change = y_F_change + 30
            if event.key == pygame.K_UP:
                y_F_change = y_F_change - 30
            if event.key == pygame.K_LEFT:
                x_F_change = x_F_change - 30
            if event.key == pygame.K_RIGHT:
                x_F_change = x_F_change + 30
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or \
            event.key == pygame.K_a or event.key == pygame.K_d or pygame.K_UP or event.key == pygame.K_DOWN or \
            event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_R_change = 0
                y_R_change = 0
                x_F_change = 0
                y_F_change = 0
        x_F += x_F_change
        y_F += y_F_change
        x_R += x_R_change
        y_R += y_R_change

   
        
    def can_t_out1p(): # player1 화면 안에 가두기 하프라인 까지
        global x_R,y_R
        if x_R<45:
            x_R=45 
        if x_R>480:
            x_R=480
        elif y_R<20:
            y_R=20
        elif y_R>465:
            y_R=465
    def can_t_out2p(): # player2 화면 안에 가두기 하프라인 까지
        global x_F,y_F
        if x_F<515:
            x_F=515 
        if x_F>947:
            x_F=947
        elif y_F<20:
            y_F=20
        elif y_F>465:
            y_F=465
            
    def moveBall():
        bLoc[0]+=bDir[0] # x축 이동
        bLoc[1]+=bDir[1] # y축 이동

        if bLoc[0]<45 or bLoc[0]+bSize[0] >= wid-45: # 공이 좌우 라인에 부딪히면 방향전환
            bDir[0] = -bDir[0]
            
        if bLoc[1]<20 or bLoc[1]>hei-47: # 공이 위, 아래에 부딪히면 방향 전환
            bDir[1] = -bDir[1]
        # 라이언 이미지와 공 충돌 처리 (x 축 방향 변경)
        if bLoc[0]+bSize[0]>=x_R and bLoc[1]+bSize[1]>=y_R and \
           bLoc[0]<=x_R+30 and bLoc[1]+bSize[1]<=y_R+30 and bLoc[1]<=y_R+30:
            bDir[1]=-(bDir[1])
            bDir[0]=-(bDir[0])
        # 프로도 이미지와 공 충돌 처리 (x 축 방향 변경  
        if bLoc[0]+bSize[0]>=x_F and bLoc[1]+bSize[1]>=y_F and \
           bLoc[0]<=x_F+30 and bLoc[1]+bSize[1]<=y_F+30 and bLoc[1]<=y_F+30:
            bDir[1]=-(bDir[1])
            bDir[0]=-(bDir[0])

        

    def getpointMessage():
        global point1P, point2P
        
        if bLoc[0]<= 45 and bLoc[1]+bSize[1] < hei*0.475 + 40 and bLoc[1] > hei*0.475 - 40:
            point1P+=1
            
        

        if bLoc[0]+bSize[0]>=947 and bLoc[1]+bSize[1]<hei*0.475+40 and bLoc[1]>hei*0.475 -40:
            point2P+=1

    
                                 
    def show_start_screen():
        screen.fill((255,255,255))
        #draw_text('Press SPACE key to play',22,(255,255,255),wid/2,hei*3/4)
        pygame.display.update()
        wait_for_key()
    def draw_text(text,size,color,x,y):
        font=pygame.font.Font(font_name,size)
        text_surface = font.render(text,True,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        screen.blit(text_surface,text_rect)
        
    # 게임 시작 버튼 누른 후 SPACE 키를 누르면 게임 시작
    def wait_for_key():
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting =False
                        
    def gameOverMessage():        # 게임 종료 메시지 출력
        font1 = pygame.font.Font (None, 70)
        text1 = "Game Over"
        text1_img = font1.render(text1, True, [255,0,0])
        screen.blit(text1_img, [100,150])
             


    # 메인 프로그램

    pygame.init()


    # 게임 환경 설정    
    speed =1
    play = True             
    point1P = 0
    point2P = 0
    sfont=pygame.font.SysFont("monospace",16)
    

    clock = pygame.time.Clock() # pygame에서 제공하는 시간관련 클래스

    wid=1024 # 너비
    hei=512 # 높이

    screen = pygame.display.set_mode((wid,hei)) # 화면 크기 설정
    pygame.display.set_caption("game") # 게임 창 제목

    background = pygame.image.load('field.jpg') # 배경 축구 경기장
    background = pygame.transform.scale(background,(1024,512)) # 축구 경기장 크기 설정

    # 1player 생성 및 설정
    x_R_change = 0
    y_R_change = 0
    Ryan = pygame.image.load('Ryan.jpg') # Ryan 이미지 불러오기
    Ryan = pygame.transform.scale(Ryan,(30,30)) # Ryan 이미지 크기 설정
    x_R= wid * 0.05 # 이미지 위치 설정
    y_R= hei * 0.475 # x, y 의 곱해지는 비율 만큼의 위치
    RSize=[30,30]
    RLoc=[x_R,y_R]

    # 2player 생성 및 설정
    x_F_change = 0
    y_F_change = 0
    Frodo = pygame.image.load('Frodo.jpg') # Ryan 이미지 불러오기
    Frodo = pygame.transform.scale(Frodo,(30,30)) # Ryan 이미지 크기 설정
    x_F= wid * 0.95 # 이미지 위치 설정
    y_F= hei * 0.475 # x, y 의 곱해지는 비율 만큼의 위치
    FSize=[30,30]
    FLoc=[x_F,y_F]

    # 볼 생성 및 설정

    ball = pygame.image.load('ball.jpg') # 축구공 이미지
    ball = pygame.transform.scale(ball,(20,20)) # 축구공 크기 설정
    
    bSize = ball.get_size()
    bLoc=[wid/2-10,hei/2-10]
    bDir=[5,-7] # 값에 따라 속도, 방향  조절 가능
    
    show_start_screen() # 스페이스 키 누르면 게임 시작
    
    while play:
        for event in pygame.event.get(): # 입력 이벤트가 있을 경우
            if event.type == pygame.KEYDOWN: # 이벤트 타입이 게임 종료일 때
                if event.key == pygame.K_ESCAPE:
                    gameOverMessage()
                    play=False # esc키 입력 시 프로그램 종료
                    
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:  # 게임오버시 스페이스바를 누르면 다시 게임시작
                                             # 공을 초기 상태로 다시 되돌려놔야 다시 게임이 시작된다.
                                             
                    # 볼 위치 재설정
                    bDir = [5, -7]          #방향: 맨 처음에는 오른쪽 위로 올라간다 (처음부터 밑으로 내려오면 어려우므로)
                    bLoc = [wid/2-10, hei/2-10]       #위치
     
                    # 패들 위치 재설정
                    pLoc = [W/2, H-30]
     
                    # 게임 환경
                    speed = 1
            if play == True:
                moving()
                can_t_out1p()
                can_t_out2p()
            
        
        #point1Ptext=sfont.render("Score {0}".format(point1P),1,(0,0,0))
        #point2Ptext=sfont.render("Score {0}".format(point2P),1,(0,0,0))
        #getpointMessage()
        pygame.time.delay(speed)
        moveBall()
           
        clock.tick(60) # 초당 60프레임
            
        
        
        screen.blit(background,(0,0))
        screen.blit(Ryan,(x_R,y_R)) # Ryan 이미지 위치
        screen.blit(Frodo,(x_F,y_F)) # Frodo 이미지 위치
        screen.blit(ball,(bLoc[0],bLoc[1]))
        #screen.blit(point1Ptext,(50,500))
        #screen.blit(point2Ptext,(50,550))
        pygame.display.update() # 화면 갱신
        
        
    pygame.quit() 

# 메인 프로그램      

root = Tk() # 부모 윈도우 창
root.title('Football Club Simulater') # 부모 윈도우 창 제목
root.geometry('800x800')


# 구단 가치(최근 7시즌 지출 이적료 기준)

BarM=725000000 
RealM=497000000
ManCM=878000000
ManUM=747000000
LivM=461000000
JuvM=448000000
EverM=365000000
ArsM=403000000
ChelM=592000000
PSGM=805000000

BarClubMoney=BarM
RealClubMoney=RealM
ManCClubMoney=ManCM
ManUClubMoney=ManUM
LivClubMoney=LivM

# 영입된 선수들을 리스트에 저장
BarP=[]
RealP=[]
ManCP=[]
ManUP=[]
LivP=[]
JuvP=[]
EverP=[]
ArsP=[]
ChelP=[]
PSGP=[]

# 프로그램 이름
main_label=Label(root,text='FCS',font=('맑은고딕',30),fg='#1F50B5')
main2_label=Label(root,text='Football Club Simulater',font=('맑은고딕',20),fg='#1F50B5')


# 메인 메뉴
button1 = Button(root,text='게임 시작',command=StartGame) 
button2 = Button(root,text='구단 만들기',command=pickClub)
button3 = Button(root,text='구단 초기화하기',command=resetClub)
button4 = Button(root,text='종료',command=quit)

# 위치 설정
main_label.pack()
main2_label.pack()


button1.pack()
button2.pack()
button3.pack()
button4.pack()

backgnd1=PhotoImage(file="laliga.gif")
w1=Label(root,image=backgnd1)
w1.pack()

root.mainloop()

