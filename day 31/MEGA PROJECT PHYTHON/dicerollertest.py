name =input ("Enter your name:")
user_score =0 
computer_score =0 
def rolldice ():
    global user_score 
    global computer_score 
    import random 
    user =random .randint (1 ,6 )
    computer =random .randint (1 ,6 )
    print ("Computer rolled",user )
    print (name +" rolled",computer )
    if user >computer :
        computer_score +=1 
        print ("Computer wins this round!")
    elif user <computer :
        user_score +=1 
        print (name +" wins this round!")
    else :
        print ("It's a tie!")#line:20
    print (f"Score - {name}: {user_score}, Computer: {computer_score}")
for _ in range (6 ):
    rolldice ()
 





