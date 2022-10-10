#!/usr/bin/env python
# coding: utf-8

# Crerate a game of snake water gun using python

# In[1]:


import random

    
player2 = input('''Enter your choice \n  
                  (s) for Snake,
                  (w) for Water,
                   (g) for Gun'''
               )

def winning_game(player1, player2):
    
    if player1 == player2:
        return None
    
    elif player1 == 's':
        if player2 == 'w':
            return 'Player2 fails and Player1 wins'
        elif player2 == 'g':
            return 'Player2 wins and Player1 fails'
        
    
    elif player1 == 'w':
        if player2 == 's':
            return 'Player2 wins and Player1 fails'
        elif player2 == 'g':
            return 'Player2 fails and PLayer1 wins'
        
    elif player1 == 'g':
        if player2 == 's':
            return 'Player2 fails and Player1 wins'
        elif player2 == 'w':
            return 'Player2 wins and Player1 fails'
        

print(" Snake(s) , Water(w) or Gun(g)....")

rand_num = random.randint(1,3)
if rand_num == 1:
    player1 = 's'
elif rand_num == 2:
    player1 = 'w'
elif rand_num == 3:
    player1 = 'g'
else:
    print('invalid option')        
        
game_status = winning_game(player1, player2)

print(f"\nPlayer1 Choice {player1} and Player2 Choice {player2}")

if(game_status == None):
    print("\nGame Tie")
elif(game_status):
    print("\nCongratulations, You've Won the Game...!")
else:
    print("\nYou've Lost the Game, Better Luck Next Time...")
    
    


# In[ ]:




