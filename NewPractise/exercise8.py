# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:33:12 2021

@author: lenovo
"""
def games():
    print('let us play the Rock-Paper-Scissors game!')
    player_1_name=input('please input the name of first player:')
    player_2_name=input('please input the name of the other player:')
    player_1=input('please the first player input Rock,Scissors or Paper. ')
    player_2=input('please the other player input Rock,Scissors or Paper. ')
    if player_1 in ['Rock','Scissors','Paper'] and player_2 in ['Rock','Scissors','Paper']:
        if player_1==player_2:
            print('Draw')
        elif player_1=='Rock':
            if player_2=='Scissors':
                print(str(player_1_name) +' win.')
            elif player_2=='Paper':
                print(str(player_2_name) +' win.')
        elif player_1=='Scissors':
            if player_2=='Rock':
                print(str(player_2_name) +' win.')
            elif player_2=='Paper':
                print(str(player_1_name) +' win.')
        elif player_1=='Paper':
            if player_2=='Rock':
                print(str(player_1_name) +' win.')
            elif player_2=='Scissors':
                print(str(player_2_name) +' win.')
    else:
        print('this is not the valid input,please try again.')
        return games()
    
games()
while True:
    restart=input('Do you want to restart the geme?enter Y or N:')
    if restart=='Y':
        games()
    else:
       print('game over')
       break