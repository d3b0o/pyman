from readchar import readkey, key
import os
import time
import random

width = 15
height = 15
lives = 2

points = 0 
position = [0,0]
hability = False
times = 0
character = ">"

obstaculos = []
bonus = []

# Generar pomes a les cantonades

pomes = [[0, height - 1],[width - 1,height - 1], [width - 1, 0]]
print(pomes)


print("pomes {}".format(pomes))

# Generar obstacles

for i in range(1,10): # dos nivells / minim sempre tres

    while True:
    
        temp = []
        x = random.randint(3, width - 1)
        y = random.randint(3, height - 1)
        temp.append(x)
        temp.append(y)
            
        if temp in obstaculos or temp in pomes:
            pass
        else:
            obstaculos.append(temp)
            break

# Generar bonus

for i in range(1,10): # dos nivells / minim sempre tres

    while True:
    
        temp = []
        x = random.randint(3, width - 1)
        y = random.randint(3, height - 1)
        temp.append(x)
        temp.append(y)
            
        if temp in obstaculos or temp in bonus or temp in pomes:
            pass
        else:
            bonus.append(temp)
            break



def colors(color):
    if color == "green":
        return '\033[92m'
    elif color == "red":
        return '\033[91m'
    elif color == "yellow":
        return '\033[93m'
    elif color == "reset":
        return '\033[0m'
    elif color == "superyellow":
        return "\033[43m"
    elif color == "blue":
        return "\033[96;1m"



character = ">"
def map(character):
    os.system("clear")
    print("+" + "-" * width * 3 + "+" )

    for y in range(height):
        print("|",end="")
        for x in range(width):
            celda = [x, y]
            if position == celda:
                print(" {}{}{} ".format(colors("yellow"),character, colors("reset")), end="")
            elif celda in obstaculos:
                if hability:
                    print(" {}#{} ".format(colors("blue"), colors("reset")), end="")
                else:
                    print(" {}#{} ".format(colors("red"), colors("reset")), end="")
            elif celda in bonus:
                print(" {}${} ".format(colors("green"), colors("reset")), end="")
            elif celda in pomes:
                print("{} + {}".format(colors("superyellow"), colors("reset")), end="")
            else:
                print("   ", end="")
        print("|")
        

    print("+" + "-" * width * 3 + "+" )
    
    #print("\nLEVEL: 1\nPOINTS: {}\nLIVES: {}\n>: {}".format(points,lives * "<3 ", position))
    #print("#:", end=" ")
    
    #print(obstaculos)
    #print(bonus)
    




for i in range(0, lives):
    #print("start")
    # Movimiento de los fantasmas
    while True:
        times -= 1
        if times < 0:
            hability = False

        if hability:
            for i in range(len(obstaculos)):
                if obstaculos[i][0]:
                    pass
                diferencia_x = position[0] - obstaculos[i][0]
                diferencia_y = position[1] - obstaculos[i][1]
                
                if abs(diferencia_y) > abs(diferencia_x):
                    if diferencia_y < 0:
                        if obstaculos[i][1] + 1 != height and  obstaculos[i][1] + 1 not in obstaculos:
                            obstaculos[i][1] += 1
                    else:
                        if obstaculos[i][1] -1 != -1 and obstaculos[i][1] - 1 not in obstaculos:   
                            obstaculos[i][1] -= 1
                elif obstaculos[i] == position:
                    break
                else:
                    if diferencia_x < 0:
                        if obstaculos[i][0] + 2 != width and obstaculos[i][0] + 1 not in obstaculos:
                            obstaculos[i][0] += 1
                    else:
                        if obstaculos[i][0] -1 != -1 and obstaculos[i][0] - 1 not in obstaculos: 
                            obstaculos[i][0] -= 1

        else:            
            for i in range(len(obstaculos)):
                if obstaculos[i][0]:
                    pass
                diferencia_x = position[0] - obstaculos[i][0]
                diferencia_y = position[1] - obstaculos[i][1]
                
                if abs(diferencia_y) > abs(diferencia_x):
                    if diferencia_y < 0 and obstaculos[i][1] - 1 not in obstaculos:
                        obstaculos[i][1] -= 1
                    elif obstaculos[i][1] + 1 not in obstaculos: 
                        obstaculos[i][1] += 1
                elif obstaculos[i] == position:
                    break
                else:
                    if diferencia_x < 0 and obstaculos[i][0] - 1 not in obstaculos:
                        obstaculos[i][0] -= 1
                    elif obstaculos[i][0] + 1 not in obstaculos: 
                        obstaculos[i][0] += 1

        # Borrar los puntos pillados

        for i in bonus:
            #print(i)
            if i == position:
                #pass
                bonus.remove(i)
                points += 10

        # Borrar pomes
        for i in pomes:
            #print(i)
            if i == position:
                #pass
                pomes.remove(i)
                hability = True
                times = 7

        # Comprobar si se come un fantasma con habilidad
        
        for i in obstaculos:
            if i == position:
                if hability:
                    obstaculos.remove(i)
                    obstaculos.append([0,0])
                else:
                    position = [0,0]
                    lives -= 1
                    break

        

        map(character)

        if len(bonus) == 0:
            print("Good Job!")
            break
        
        # Movimiento personaje
        k = readkey()
        if k == "w" or k == key.UP:
            if position[1] - 1 == -1:
                position[1] = height - 1
            else:
                position[1] -= 1
            character = "^"
        if k == "s" or k == key.DOWN:
            if position[1] + 1 == height:
                position[1] = 0
            else:
                position[1] += 1
            character = "v"
        if k == "a" or k == key.LEFT:
            if position[0] - 1 == -1:
                position[0] = width - 1
            else:
                position[0] -= 1
            character = "<"
        if k == "d" or k == key.RIGHT:
            if position[0] + 1 == height:
                position[0] = 0
            else:
                position[0] += 1
            character = ">"
        if k == key.BACKSPACE:
            print("[!] Saliendo...")
            exit(0)
        

        
        
