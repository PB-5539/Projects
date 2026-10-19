#Parker Behagg
#10-19-2026
#simple minesweeper clone

import tkinter as tk
import random
import copy
def random_grid(grid_template, bombs): #Randomizes the rid
    randomized_grid = copy.deepcopy(grid_template)
    for i in range(bombs):
        selected_row = random.randint(0,len(randomized_grid)-1 )
        selected_column = random.randint(0,9)
        while randomized_grid[selected_row][selected_column] == "B":
            print(f"({selected_row},{selected_column}) already 'B' Trying again")
            selected_row = random.randint(0,len(randomized_grid)-1 )
            selected_column = random.randint(0,9)
        print(f"({selected_row},{selected_column})")
        randomized_grid[selected_row][selected_column] = "B"
    for i in range(len(randomized_grid)):
        print(randomized_grid[i])
    return randomized_grid

def poll_grid(grid,x,y): #gets the value of an x,y pair
    value = grid[x][y]
    return value

def set_grid_vale(grid,x,y,value): #sets the value of an x,y pair
    grid[x][y] = value
    return grid
    
    
def main():
    GRID_TEMPLATE = [ #a 10x10 grid template to work with
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"},
                {0:"E",1:"E",2:"E",3:"E",4:"E",5:"E",6:"E",7:"E",8:"E",9:"E"}
                ]
    minefield = random_grid(GRID_TEMPLATE, 10)
    counter = 0
    print()
    for i in range(len(minefield)):
        tlist = []
        for k in range(len(minefield[i])):
            value = poll_grid(minefield,i,k)
            if value == "B":
                counter += 1
            tlist.append(f"({i},{k}): {value}   ")
        for i in range(len(tlist)):
            print(tlist[i], end="")
        print("\n")
    print("bombs:", counter)
    print()
    for i in range(len(GRID_TEMPLATE)):
        print(GRID_TEMPLATE[i])
    
main()