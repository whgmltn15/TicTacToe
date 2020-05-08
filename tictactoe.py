import random

#판 만들기
a = []
for i in range(9):
    a.append("-")
def print_board(a):
    for i in range(0, 9, 3):
        print(a[i], a[i + 1], a[i + 2])
print_board(a)

#o, x 정하기
player1 = ""
player2 = ""
while player1 == "":
    n = input()
    if n == "o":
        player1 = "o"
        player2 = "x"
    elif n == "x":
        player1 = "x"
        player2 = "o"
    else:
        print("choose again")
    print(player1, player2)

#순서정하기(랜덤)
b = random.randrange(2)
turn = ""
if b == 0:
    turn = "o"
else:
    turn = "x"

#이길조건
def win():
    c = 0
    if a[0] == a[1] == a[2]:
        if a[0] != "-":
            c = 1
    elif a[3] == a[4] == a[5]:
        if a[3] != "-":
            c = 1
    elif a[6] == a[7] == a[8]:
        if a[6] != "-":
            c = 1
    elif a[0] == a[3] == a[6]:
        if a[3] != "-":
            c = 1
    elif a[1] == a[4] == a[7]:
        if a[1] != "-":
            c = 1
    elif a[0] == a[4] == a[8]:
        if a[4] != "-":
            c = 1
    elif a[2] == a[4] == a[6]:
        if a[6] != "-":
            c = 1
    return c

#플레이어1이 어느부분에 ,o나 x를 칠지 결정
def player1_turn(player1):
    while True:
        d = int(input())
        if 1 <= d <= 9:
            if a[d - 1] == "-":
                a[d - 1] = player1
                break
            else:
                print("choose again")
        else:
            print("choose again")

#플레이어2가 어느부분에 o나x 를 칠지 결정
def player2_turn(player2):
    while True:
        d = int(input())
        if 1 <= d <= 9:
            if a[d - 1] == "-":
                a[d - 1] = player2
                break
            else:
                print("choose again")
        else:
            print("choose again")

print_board(a)

#턴 바꾸기 & 누가 이겼는지 출력
z = 0
while True:
    if player1 == "o":
        if turn == "o":
            player1_turn(player1)
            print_board(a)
            k = win()
            if k == 1:
                print("o win")
                break
            turn = "x"
        else:
            player2_turn(player2)
            print_board(a)
            k = win()
            if k == 1:
                print("x win")
                break
            turn = "o"
    else:
        if turn == "o":
            player2_turn(player2)
            print_board(a)
            k = win()
            if k == 1:
                print("o win")
                break
            turn = "x"
        else:
            player1_turn(player1)
            print_board(a)
            k = win()
            if k == 1:
                print("x win")
                break
            turn = "o"

#비겼을때
    z += 1
    if z == 9 and win() == 0:
        print("draw")
        break