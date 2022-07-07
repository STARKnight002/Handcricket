print('HANDCRICKET')
print('''
NOTE:
Type - "quit" to end innings\n
If you quit an innings, you can proceed to the next innings but the match will not have a result
It will simple be counted as a practice innings''')
name=input('Enter you name - ')
import random
import time

c=0   
def choice():
    global ch
    ch = input('BAT OR BOWL - ')
    while True:
        if ((ch.lower()) == 'bat') or ((ch.lower()) == 'bowl'):
            break
        else:
            print("Invalid")
            ch = input('BAT OR BOWL - ')
    return ch

def end():
    global ex
    time.sleep(0.5)
    print("Done")
    pl = input("Type 'play' if you want to restart innings. Hit ENTER otherwise - ")
    if pl.lower()=='play':
        run()
    else:
        ex=0
    
def numinp():
    global ex,c
    while True:    
        try:
            y1=input('Enter your number - ')
            if y1=='quit':
                ex=0
                c+=1
                break
            y = int(y1)
            while (y>6)|(y<=0):
                print('ENTER NUMBER FROM 1-6 ONLY')
                y=int(input('Enter your number - '))
            break
        except:
            print("Enter Integer only")
    try:
        return y
    except:
        end()

def TOSS():
    global toss,ch,r1,ex
    print('\nTOSS')
    ex=1
    c=input('ODD or EVEN - ')
    while (c.lower()!='odd')&(c.lower()!='even'):
        print("ENTER 'odd' OR 'even' ONLY")
        c=input('ODD or EVEN - ')
    c1=c.lower()
    while True:    
        try:
            y1=input('Enter your number - ')
            if y1=='quit':
                end()
                break
            t = int(y1)
            while (t>6)|(t<=0):
                print('ENTER NUMBER FROM 1-6 ONLY')
                t=int(input('Enter your number for toss - '))
            break
        except:
            print("Enter Integer only")
    if ex!=0:
        r=random.randint(1,6)
        time.sleep(0.5)
        print('Computer plays-',r)
    try:
        if (t>0)&(t<7):
            if (c1=='odd'):
                if (t+r)%2!=0:
                    time.sleep(1)
                    print("\nThe sum is 'ODD'")
                    print('YOU WIN TOSS')
                    toss='plyr'
                    ch = choice()
                    print(name,' chooses to ',ch)
                else:
                    time.sleep(1)
                    print("\nThe sum is 'EVEN'")
                    print('Computer WINS TOSS')
                    toss='cmpr'
                    r1=random.choice(['BAT','BOWL'])
                    time.sleep(1)
                    print('Computer chooses to ',r1)
            elif (c1=='even'):
                if (t+r)%2==0:
                    time.sleep(1)
                    print("\nThe sum is 'EVEN'")
                    print('YOU WIN TOSS')
                    toss='plyr'
                    ch = choice()
                    print(name,' chooses to ',ch)
                else:
                    time.sleep(1)
                    print("\nThe sum is 'ODD'")
                    print('Computer WINS TOSS')
                    toss='cmpr'
                    r1=random.choice(['BAT','BOWL'])
                    time.sleep(1)
                    print('Computer chooses to ',r1)
    except:
        ex=0
        if ex!=0:
            end()
                
sp=0
sc=0

def ply():
    print(name,' Bats')
    global sp
    while 3:
        x=numinp()
        if ex==0:
            break
        r3=random.randint(1,6)
        time.sleep(0.5)
        print('Computer plays - ',r3)
        if (x!=r3):
            sp+=x
            time.sleep(1)
            print('Your score-',sp)
        elif(x==r3):
            time.sleep(1)
            print('\nYou are out')
            break
    time.sleep(1)
    print('\n',name,'Final score - ',sp)
    if ex!=0:
        print('Computer needs',sp+1,'to win')

def ply1():
    print(name,' Bats')
    global sp,ex
    while (sc>=sp):
        ex=1
        x=numinp()
        if ex==0:
            break
        r3=random.randint(1,6)
        time.sleep(0.5)
        print('Computer plays - ',r3)
        if (x!=r3):
            sp+=x
            time.sleep(1)
            print('Your score - ',sp)
        elif(x==r3):
            time.sleep(1)
            print('\nYou are out')
            break
    time.sleep(1)
    print('\n',name,'Final score - ',sp)
    print('Game over')

def cmp():
    print('Computer Bats')
    global sc
    while 3:
        x=numinp()
        if ex==0:
            break
        r3=random.randint(1,6)
        time.sleep(0.5)
        print('Computer plays - ',r3)
        if (x!=r3):
            sc+=r3
            time.sleep(1)
            print('Computer score - ',sc)
        elif(x==r3):
            time.sleep(1)
            print('\nComputer is out')
            break
    time.sleep(1)
    print('\nComputer final score - ',sc)
    if ex!=0:
        print(name,'needs',sc+1,'to win')

def cmp1():
    print('Computer Bats')
    global sc,ex
    while (sp>=sc):
        ex=1
        x=numinp()
        if ex==0:
            break
        r3=random.randint(1,6)
        time.sleep(0.5)
        print('Computer plays - ',r3)
        if (x!=r3):
            sc+=r3
            time.sleep(1)
            print('Computer score - ',sc)
        elif(x==r3):
            time.sleep(1)
            print('\nComputer is out')
            break
    time.sleep(1)
    print('\nComputer final score - ',sc)
    print('Game over')

def innings():
    if (toss=='plyr'):
        if (ch.lower()=='bat'):
            time.sleep(1)
            print('\nFIRST INNINGS')
            ply()
            time.sleep(1)
            print('\nSECOND INNINGS')
            cmp1()
        else:
            time.sleep(1)
            print('\nFIRST INNINGS')
            cmp()
            time.sleep(1)
            print('\nSECOND INNINGS')
            ply1()
    if (toss=='cmpr'):
        if (r1.lower()=='bat'):
            time.sleep(1)
            print('\nFIRST INNINGS')
            cmp()
            time.sleep(1)
            print('\nSECOND INNINGS')
            ply1()
        else:
            time.sleep(1)
            print('\nFIRST INNINGS')
            ply()
            time.sleep(1)
            print('\nSECOND INNINGS')
            cmp1()

def result():
    if (sp>sc):
        print('\n',name,'WINS')
        print('CONGRATULATIONS',name)
    elif (sc>sp):
        print('Computer wins')
        print('Better luck next time')
    else:
        print("IT'S A DRAW..")
        print("WELL PLAYED")

def run():
    TOSS()
    if ex!=0:
        innings()
    else:
        pass
    if (ex!=0)&(c==0):
        result()
    
if __name__=="__main__":
    run()
