# import random

# randno=random.randint(1,100)
# print(randno)

# for i in range(1,)--->isse loop sirf ek baar chl rha 
# for i in range( )--->gives error
# for i in range(1,11):
#     guess=int(input("Guess the no. please: "))
#     if guess>randno:
#         print("Lower no. please")
#     elif guess<randno:
#         print("Higher no. please")
#     elif guess==randno:
#         print("Perfect guess")
#         break
# if i==10:
#     print("You reach your max limit. Try next time")
# else:
#     print("You are taken",i,"chance to guess the no.")


# Because question mei specify nhi tha ki user ko max kitne chance milenge guess krne ke that's why we use while loop here kyuki vaha condition lgti hai range deni nhi pdti ki max kitni lagegi 

import random

randno=random.randint(1,100)
print(randno)

i=0
guess=0 #baad mei overwite kr dega na 
# guess=None #ye bhi ke skte hai 
while(guess!=randno):
    guess=int(input("Guess the no. please: "))
    if guess>randno:
        print("Lower no. please")
    elif guess<randno:
        print("Higher no. please")
    i=i+1
if(guess==randno):
    print("Perfect guess!")
    print("You are taken",i,"chance to guess the no.")    
with open("highscore.txt","r") as f:
    # beacuse by default f.read ek string hogi 
    highscore=int(f.read())
if(i<highscore):
    print("You have just broken the high score, Congrats!")
    with open("highscore.txt","w") as f:
        f.write(str(i))
        # write() argument must be str, not int
