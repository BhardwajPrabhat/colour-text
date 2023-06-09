import turtle as t
a=int(input("Enter The Size Of Heading Of Pen: <30     "))
j=str(input("Enter The  Color  Of  Pen        (only lowercase):         "))
n=str(input("Enter Your Name:   "))
t.penup()
t.setpos(-675,350)
t.pensize(a)
t.pencolor(j)

for i in range (len(n)):
    if n[i]=='a'or n[i]=='A':
        s=t.pos()
        t.penup()

        t.setx(s[0]+60)
        g=t.pos()
        t.pendown()
        t.goto(s[0],s[1]-176)
        t.goto(g)
        t.goto(s[0]+120,s[1]-176)
        t.penup()
        t.goto(s[0]+30,s[1]-88)
        t.pendown()
        t.fd(60)
        t.penup()
        t.setpos(s[0]+150,s[1])



    elif n[i]=='b' or n[i]=='B':
        s=t.pos()
        t.pendown()
        t.fd(40)
        t.circle(-44,180)
        t.fd(40)
        t.left(180)
        t.fd(40)
        t.circle(-44,180)
        t.fd(40)
        t.right(90)
        t.fd(176)
        t.right(90)
        t.penup()
        t.goto(s[0]+120,s[1])


        

    elif n[i]=='c' or n[i]=='C':

        s=t.pos()
        t.fd(120)
        t.left(180)
        t.pendown()
        t.fd(30)
        t.circle(88,180)
        t.fd(30)
        t.penup()
        t.setpos(s[0]+150,s[1])

        

    elif n[i]=='d' or n[i]=='D':
        
        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.left(90)
        t.fd(30)
        t.circle(88,180)
        t.fd(30)
        t.right(180)
        t.penup()
        t.setpos(s[0]+150,s[1])

        

    elif n[i]=='e' or n[i]=='E':

        s=t.pos()
        t.pendown()
        t.fd(120)
        t.bk(120)
        t.right(90)
        t.fd(88)
        t.left(90)
        t.fd(110)
        t.bk(110)
        t.right(90)
        t.fd(88)
        t.left(90)
        t.fd(120)
        t.penup()
        t.setpos(s[0]+150,s[1])


    elif n[i]=='f' or n[i]=='F':
        s=t.pos()
        t.pendown()
        t.fd(120)
        t.bk(120)
        t.right(90)
        t.fd(88)
        t.left(90)
        t.fd(110)
        t.bk(110)
        t.right(90)
        t.fd(88)
        t.left(90)
        t.penup()
        t.setpos(s[0]+150,s[1])


        

    elif n[i]=='g' or n[i]=='G':

        s=t.pos()
        t.fd(120)
        t.right(180)
        t.pendown()
        t.fd(30)
        t.circle(88,180)
        t.fd(30)
        t.left(90)
        t.fd(80)
        t.left(90)
        t.fd(55)
        t.left(90)
        t.fd(20)
        t.left(90)
        t.penup()
        t.goto(s[0]+150,s[1])


    elif n[i]=='h' or n[i]=='H':
        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.bk(88)
        t.left(90)
        t.fd(120)
        t.right(90)
        t.fd(88)
        t.bk(176)
        t.left(90)
        t.penup()
        t.goto(s[0]+150,s[1])

        

    elif n[i]=='i' or n[i]=='I':
        s=t.pos()
        t.pendown()
        t.fd(120)
        t.bk(60)
        t.right(90)
        t.fd(176)
        t.left(90)
        t.fd(60)
        t.bk(120)
        t.penup()
        t.setpos(s[0]+150,s[1])

        

    elif n[i]=='j' or n[i]=='J':

        s=t.pos()
        t.pendown()
        t.fd(120)
        t.bk(60)
        t.right(90)
        t.fd(146)
        t.circle(-30,180)
        t.right(90)
        t.penup()
        t.setpos(s[0]+150,s[1])


    elif n[i]=='k' or n[i]=='K':

        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.bk(88)
        j=t.pos()
        t.goto(s[0]+100,s[1])
        t.goto(j)
        t.goto(s[0]+100,s[1]-176)
        t.left(90)
        t.penup()
        t.setpos(s[0]+130,s[1])


    elif n[i]=='l' or n[i]=='L':

        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.left(90)
        t.fd(120)
        t.penup()
        t.setpos(s[0]+150,s[1])


    elif n[i]=='m' or n[i]=='M':
        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.bk(176)
        t.goto(s[0]+60,s[1]-88)
        t.goto(s[0]+120,s[1])
        t.fd(176)
        t.left(90)
        t.penup()
        t.setpos(s[0]+150,s[1])
        

    elif n[i]=='n' or n[i]=='N':

        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.bk(176)
        t.goto(s[0]+120,s[1]-176)
        t.bk(176)
        t.left(90)
        t.penup()
        t.setpos(s[0]+150,s[1])


    elif n[i]=='o' or n[i]=='O':
        s=t.pos()
        t.right(90)
        t.fd(60)
        t.pendown()
        t.fd(56)
        t.circle(60,180)
        t.fd(56)
        t.circle(60,180)
        t.left(90)
        t.penup()
        t.goto(s[0]+150,s[1])

        
        

        

    elif n[i]=='p' or n[i]=='P':

        s=t.pos()
        t.pendown()
        t.fd(76)
        t.circle(-44,180)
        t.fd(76)
        t.left(90)
        t.fd(88)
        t.bk(176)
        t.left(90)
        t.penup()
        t.setpos(s[0]+150,s[1])
        
        
        

    elif n[i]=='q' or n[i]=='Q':

        s=t.pos()
        t.right(90)
        t.fd(60)
        t.pendown()
        t.fd(56)
        t.circle(60,180)
        t.fd(56)
        t.circle(60,180)
        t.left(90)
        t.penup()
        t.goto(s[0]+80,s[1]-132)
        t.pendown()
        t.goto(s[0]+140,s[1]-150)
        t.penup()
        t.setpos(s[0]+150,s[1])

        


    elif n[i]=='r' or n[i]=='R':
        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.bk(176)
        t.left(90)
        t.fd(76)
        t.circle(-44,180)
        t.fd(76)
        t.right(90)
        t.goto(s[0]+120,s[1]-176)
        t.right(90)
        t.penup()
        t.setpos(s[0]+150,s[1])


    elif n[i]=='s' or n[i]=='S':
        s=t.pos()
        t.fd(120)
        t.left(90)
        t.pendown()
        t.bk(10)
        t.fd(10)
        t.left(90)
        t.fd(76)
        t.circle(44,180)
        t.fd(32)
        t.circle(-44,180)
        t.fd(76)
        t.right(90)
        t.fd(10)
        t.right(90)
        t.penup()
        t.setpos(s[0]+150,s[1])
    


    elif n[i]=='t' or n[i]=='T':
        s=t.pos()
        t.pendown()
        t.fd(120)
        t.bk(60)
        t.right(90)
        t.fd(176)
        t.left(90)
        t.penup()
        t.setpos(s[0]+150,s[1])


    elif n[i]=='u' or n[i]=='U':
        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(116)
        t.circle(60,180)
        t.fd(116)
        t.right(90)
        t.penup()
        t.setpos(s[0]+150,s[1])

    elif n[i]=='v' or n[i]=='V':
        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(40)
        t.goto(s[0]+60,s[1]-176)
        t.goto(s[0]+120,s[1]-40)
        t.bk(40)
        t.left(90)
        t.penup()
        t.setpos(s[0]+150,s[1])

    elif n[i]=='w' or n[i]=='W':
        s=t.pos()
        t.right(90)
        t.pendown()
        t.fd(176)
        t.goto(s[0]+60,s[1]-88)
        t.goto(s[0]+120,s[1]-176)
        t.bk(176)
        t.left(90)
        t.penup()
        t.setpos(s[0]+150,s[1])


    elif n[i]=='x' or n[i]=='X':
        s=t.pos()
        t.pendown()
        t.goto(s[0]+120,s[1]-176)
        t.penup()
        t.goto(s[0],s[1]-176)
        t.pendown()
        t.goto(s[0]+120,s[1])
        t.penup()
        t.setpos(s[0]+150,s[1])

    elif n[i]=='y' or n[i]=='Y':
        s=t.pos()
        t.right(90)
        t.pendown()
        t.goto(s[0]+60,s[1]-88)
        t.goto(s[0]+120,s[1])
        t.goto(s[0]+60,s[1]-88)
        t.fd(88)
        t.left(90)
        t.penup()
        t.goto(s[0]+150,s[1])

    elif n[i]=='z' or n[i]=='Z':
        s=t.pos()
        t.pendown()
        t.left(90)
        t.bk(10)
        t.fd(10)
        t.right(90)
        t.fd(120)
        t.goto(s[0],s[1]-176)
        t.fd(120)   
        t.left(90)
        t.fd(10)
        t.right(90)
        t.penup()
        t.goto(s[0]+150,s[1])

    elif n[i]=='_':
        s=t.pos()
        t.goto(s[0],s[1]-176)
        t.pendown()
        t.goto(s[0]+120,s[1]-176)
        t.penup()
        t.goto(s[0]+150,s[1])


    elif n[i]==' ':
        t.penup()
        t.setpos(-675,144)

    else :
        print("WRONG INPUT!!!")
