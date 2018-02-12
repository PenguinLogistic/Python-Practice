import math

#Given a list of 0 and 1s it will sort it, put 0s on the left and 1s on the right.
def sorter(A = []):
    B = A[:]
    C = []
    for x in range(0,len(A)-1):
        if A[x] == 1:
            B.remove(1)
            C.append(1)

    return B+C

#fizzbuzz question, given an int on mults of 3 print fizz, 5 buzz, 3&5 fizzbuzz, o.w. print number
def fizzbuzz(n):
    fizbuz = ""
    for i in range (1,n+1):
        if (i%3==0 and i%5==0):
            fizbuz+= "fizzbuzz\n"
        elif (i%3==0):
            fizbuz+="fizz\n"
        elif (i%5==0):
            fizbuz+="buzz\n"
        else:
            fizbuz+=str(i)
            fizbuz+="\n"
    return print(fizbuz)


#using a hashtable
def hshRepeat(phrase):
    htabl = []
    for z in range(0,27):
        htabl.append([])
    workingstr=phrase.lower().strip().replace(" ","")
    #could be like value item / total # of item in terms of ints
    #can turn strings into int values through unicode
    for x in workingstr:
        i=ord(x)-96
        htabl[i].append(x)

    for y in htabl:
        if len(y) > 1:
            print("The letter "+y[0]+" has: "+ str(len(y)) +"duplicates.")
    return            
#tictactoe
def tictactoe():
    game = True;
    player = "X";
    B1 = [[[],[],[]], [[],[],[]], [[],[],[]]]
    print("This is a game of tictactoe, first to make a line of 3 X's or O's wins\n")
    print("When the turn player is prompted, they will need to enter two numbers, both between the numbers 0 and 2 (inclusive)\n")
    print("The game board will look like this:\n")
    print("[[0,0],[0,1],[0,2]]\n")
    print("[[1,0],[1,1],[1,2]]\n")
    print("[[2,0],[2,1],[2,2]]\n") 
    while (game != False):
        print("player " + player +" is up!\n")
        xcoord = int(input("Choose the x coordinates of your placement [x,y]: "))
        ycoord = int(input("Choose the y coordinates of your placement [x,y]: "))
        if(xcoord < 0 or xcoord > 2 or ycoord < 0 or ycoord > 2):
            break
        else:
            if(len(B1[xcoord][ycoord]) == 1):
                print("That space is already filled!")
            else:
                B1[xcoord][ycoord].append(player)
                if(player == "X"):
                    player = "O"
                else:
                    player = "X"
        if(checkWin(B1, player) != "on"):
            game = True
            print(player+" has won the game!")
            break
    return
            
def checkWin(B, letter):
    if ((B[0][0] and B[0][1] and B[0][2] == [letter]) or
        (B[1][0] and B[1][1] and B[1][2] == [letter]) or
        (B[2][0] and B[2][1] and B[2][2] == [letter]) or
        (B[0][0] and B[1][0] and B[2][0] == [letter]) or
        (B[0][1] and B[1][1] and B[2][1] == [letter]) or
        (B[0][2] and B[1][2] and B[2][2] == [letter]) or
        (B[0][0] and B[1][1] and B[2][2] == [letter]) or
        (B[0][2] and B[1][1] and B[2][0])
    ):
        return letter
    else:
        return "on"      

def subSeq(str1, str2):
    x = len(str1)
    y = len(str2)
    a = 0
    b = 0
    while a<x and b<y:
        if str1[a] == str2[b]:
            a+=1
        b+=1
    return a==b

def perm(str1, n, m):
    if m == 0:
        print(str1)
    else:
        if n > 0:
            perm(str1 + '{', n-1, m)
        if m > n:
            perm(str1 + '}', n, m-1)
    return

def towerh(height, source, helper, targ):
    if height > 0:
        # move source tower to helper, -1 from height
        towerh(height-1, source, targ, helper)
        # move a disk from source to target
        if source != []:
            targ.append(source.pop())
        # move tower of size n-1 from help to targ
        towerh(height-1, helper, source, targ)

def palindrome(str1):
    if(len(str1)%2 == 0):
        return False
    else:
        a = math.floor(len(str1)/2)
        x = len(str1)-1
        for i in range(0,a):
            if str1[i] != str1[x]:
                return False
            else:
                i+=1
                x-=1
    return True

def searchList(drugList):
    #search immediately uses the last element in the list as that is the keyterm
    search = drugList[-1]
    count = 0
    topThree = []
    
    #base case in case druglist is empty
    if (drugList == []):
        print("the list is empty!")

    for x in drugList:
        # startswith() is a built-in python function that compares one string to
        # the start of the other string.
        if (search.startswith(x)):
            count += 1
            topThree.append(x)
        #if we've found 3 drugs then we break out of the loop
        if (count == 3):
            break
    # check if topthree is empty after the loop is done
    topThree.pop()
    if(topThree == []):
        return ["<NONE>"]
    # if it's not empty just return as is
    return topThree
