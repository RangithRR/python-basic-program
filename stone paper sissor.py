player1=input("player 1 :")
player2=input("player 2 :")
if( player1=="r" and player2=="p"):
   print("player2 win")
elif(player1=="r" and player2=="s"):
    print("player1 win")
elif(player1=="s" and player2=="p"):
    print("player1 win")
elif(player1=="p" and player2=="s"):
    print("player2 win")
elif(player1=="s" and player2=="r"):
    print("player2 win")
elif(player1=="s" and player2=="s"):
    print("equal point")
elif(player1=="r" and player2=="r"):
    print("equal point")
elif(player1=="p" and player2=="p"):
    print("equal point")
else:
    print("invalid")
