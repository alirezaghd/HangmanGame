import random
import turtle

score = 7
true_chars =[]
words = ["tree ","watch" , "apple", "cherry","android","book","happy","ali","moon","mobile","kids"]

word = random.choice(words)

t = turtle.Turtle()
t.pu() 
t.setx(-250)
t.sety(80)
t.pd() 
t.speed(1)
t.fd(100)
t.rt(180)
t.fd(50)
t.rt(90)
t.fd(170)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(50)
t.ht()



while True:
    for i in range(len(word)):
        if word[i] in true_chars:
            print(word[i],end='')
        else:
            print('_ ' ,end='')
    char = input('\n please enter character : ')
    char = char.lower()

    if char in word:
        true_chars.append(char)
        
    else:
        score -= 1

    if score == 6:
    
        t.pu()
        t.setx(-120)
        t.sety(180)
        t.pd()
        t.circle(20)
        t.ht() 
    elif score == 5:
        t.pu()
        t.setx(-100)
        t.sety(160)
        t.pd()
        t.fd(50)
        t.ht() 
    elif score == 4:
        t.rt(45)
        t.fd(30)
        t.ht() 
    elif score == 3:
        t.pu()
        t.rt(-90)
        t.setx(-100)
        t.sety(110)
        t.pd()
        t.fd(30)
        t.ht() 
    elif score == 2:
        t.pu()
        t.rt(-45)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.ht() 
    elif score == 1:
        t.pu()
        t.rt(180)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.pu()
        t.ht() 
        


    if score == 0:
        print('game over')
        break
    if all(char in true_chars for char in word) and score > 0:
        print("you win")
        break

    


    print(score)





