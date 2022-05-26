def winner(player1choice,player2choice):
    if(player1choice==player2choice):
        return None
    elif(player1choice=="stone"):
        if(player2choice=="sissor"):
            return True
        else :return False  
    elif(player1choice=="sissor"):
        if(player2choice=="paper"):
            return True
        else :return False      
    elif(player1choice=="paper"):
        if(player2choice=="stone"):
            return True       
        else :return False  
player1choice=input("player1choice: ")
player2choice=input("player2choice: ")

winner(player1choice,player2choice)

if winner(player1choice,player2choice) == None:
    print("game tied")
elif winner(player1choice,player2choice) == True:
    print("player1 is winner") 
elif winner(player1choice,player2choice) == False:
    print("player2 is winner")        
