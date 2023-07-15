# Snake water gun game 
import random

def gamewin(comp,you):
    # If two values are equal, declare a tie! 
    if comp=='you':
        return None
    
    # Check for all possibilities when computer chose s 
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        
    # Check for all possibilities when computer chose w  
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
        
    # Check for all possibilities when computer chose g 
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


print("Comp Turn Turn: Snake(s) Water(w) or Gun(g)?")
randno=random.randint(1,3)
# ab ye 1,2 aur 3 mei se no. choose krta rahega 
print(randno)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
you=input("Your's Turn: Snake(s) Water(w) or Gun(g)?")
a=gamewin(comp,you)

print("Computer chose",comp)
print("You chose",you)

if a==None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")
