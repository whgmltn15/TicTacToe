import random

#판 만들기
a = []
for i in range(9):
    a.append("-")
def print_board(a):
    for i in range(0, 9, 3):
        print(a[i], a[i + 1], a[i + 2])
print_board(a)

#o, x정하기
user = ""
computer = ""
while user == "":
    n = input()
    if n == "o":
        user = "o"
        computer = "x"
    elif n == "x":
        user = "x"
        computer = "o"
    else:
        print("choose again")
    print(user, computer)

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

#유저가 어느부분에 ,o나 x를 칠지 결정
def user_turn(user):
    while True:
        d = int(input())
        if 1 <= d <= 9:
            if a[d - 1] == "-":
                a[d - 1] = user
                break
            else:
                print("choose again")
        else:
            print("choose again")

print_board(a)

#컴퓨터가 어느부분에 o나x 를 칠지 결정
def computer_turn(computer):
    while True:
        num = random.randrange(9)
        if a[num] == "-":
            a[num] = computer
            break

#턴 바꾸기 & 누가 이겼는지 출력
z = 0
while True:
    if user == "o":
        if turn == "o":
            user_turn(user)
            print_board(a)
            k = win()
            if k == 1:
                print("o win")
                break
            turn = "x"
        else:
            computer_turn(computer)
            print_board(a)
            k = win()
            if k == 1:
                print("x win")
                break
            turn = "o"
    else:
        if turn == "o":
            computer_turn(computer)
            print_board(a)
            k = win()
            if k == 1:
                print("o win")
                break
            turn = "x"
        else:
            user_turn(user)
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