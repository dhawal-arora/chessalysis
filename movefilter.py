def pawn(chessmove):
    if len(chessmove)==2:
        if chessmove[0] in ["a","b","c","d","e","f","g","h"]:
            if chessmove[1] in ["2","3","4","5","6","7"]:
                moves.append(chessmove)
    elif len(chessmove)==3:
        if chessmove[0] in ["a","b","c","d","e","f","g","h"]: 
            if chessmove[1]==8 or chessmove[1]==1:
                if chessmove[2] in ["R","N","B","Q"]:
                    moves.append(chessmove)                   
    elif len(chessmove)==4:
        if chessmove[0]!=chessmove[2]:
            if chessmove[0] in ["a","b","c","d","e","f","g","h"]:
                if chessmove[1]=="x":
                    if chessmove[2] in ["a","b","c","d","e","f","g","h"]:
                        if chessmove[3] in ["2","3","4","5","6","7"]:
                            moves.append(chessmove)
    elif len(chessmove)==5:
        if chessmove[0]!=chessmove[2]:
            if chessmove[0] in ["a","b","c","d","e","f","g","h"]:
                if chessmove[1]=="x":
                    if chessmove[2] in ["a","b","c","d","e","f","g","h"]:
                        if chessmove[3]==8 or chessmove[3]==1:
                            if chessmove[4] in ["R","N","B","Q"]:
                                moves.append(chessmove)

def piece(chessmove):
    if len(chessmove)==3:
        if chessmove[0] in ["R","N","B","Q","K"]:
            if chessmove[1] in ["a","b","c","d","e","f","g","h"]:
                if chessmove[2] in ["1","2","3","4","5","6","7","8"]:
                    moves.append(chessmove)

    elif len(chessmove)==4:
        if chessmove[0] in ["R","N","B","Q"]:
            if chessmove[1] in ["a","b","c","d","e","f","g","h","x"]:
                if chessmove[2] in ["a","b","c","d","e","f","g","h"]:
                    if chessmove[3] in ["1","2","3","4","5","6","7","8"]:
                        moves.append(chessmove)
        elif chessmove[0]=="K":
            if chessmove[1]=="x":
                if chessmove[2] in ["a","b","c","d","e","f","g","h"]:
                    if chessmove[3] in ["1","2","3","4","5","6","7","8"]:
                        moves.append(chessmove)
    elif len(chessmove)==5:
        if chessmove[0] in ["R","N","B","Q"]:
            if chessmove[1] in ["a","b","c","d","e","f","g","h"]:
                if chessmove[2]=="x":
                    if chessmove[3] in ["a","b","c","d","e","f","g","h"]:
                        if chessmove[4] in ["1","2","3","4","5","6","7","8"]:
                            moves.append(chessmove)
    elif len(chessmove)==6:
        if chessmove[1]+chessmove[2]!=chessmove[4]+chessmove[5]:
            if chessmove[0] in ["R","N","B","Q"]:
                if chessmove[1] in ["a","b","c","d","e","f","g","h"]:
                    if chessmove[2] in ["1","2","3","4","5","6","7","8"]:
                        if chessmove[3]=="x":
                            if chessmove[4] in ["a","b","c","d","e","f","g","h"]:
                                if chessmove[5] in ["1","2","3","4","5","6","7","8"]:
                                    moves.append(chessmove)

chessmove=input("Enter chessmove: ")
moves=[]

if chessmove[0] in ["a","b","c","d","e","f","g","h"] and 1<len(chessmove)<6:
    pawn(chessmove)
elif chessmove[0] in ["R","N","B","Q","K"] and 2<len(chessmove)<7:
    piece(chessmove)
else:
    print("MOVE ERROR")

print(moves)