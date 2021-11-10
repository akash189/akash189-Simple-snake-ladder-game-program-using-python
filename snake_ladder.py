# Snake-Ladder Game
# import random module to genrate random value
import random as rd
win = ""
d = {}
la = [1, 4, 8, 21, 28, 50, 80, 71]  # Starting position of ladder.
la2 = [38, 14, 30, 42, 76, 67, 99, 92]  # Ending position of ladder.
sn = [32, 36, 48, 62, 88, 95, 97]  # Starting position snake.
sn2 = [10, 6, 26, 18, 24, 56, 78]  # Ending position of snake.
print("Enter no. of players")
nm = int(input())

print("Enter", nm, "name")
i = 0
while i < nm:
    pl_name = input()
    d[pl_name] = 0
    i = i+1

print(d)
print()
ls1 = list(d.keys())  # Getting list of keys from dictionary
j = 0
while True:
    r = j+1
    print("======= Round", r, "=======")
    k = 0
    c = []
    while k < nm:
        print()
        print("Your turn : ", ls1[k])
        input("press enter to roll dice")
        a = rd.randint(1, 6)
        c.append(a)
        print("You got = ", a)
        ls = list(d.values())  # Getting list of values from dictionary
        # print(ls)
        cv = ls[k]
        b = cv+a
        if b <= 100:
            d[ls1[k]] = b
        print("Your score is", d[ls1[k]])
        if b in la:
            if b <= 100:
                d[ls1[k]] = b
            if d[ls1[k]] == 100:
                break
            print("You got ladder at", d[ls1[k]], "move up")
            ind1 = la.index(d[ls1[k]])
            d[ls1[k]] = la2[ind1]
            print("Now your score is", d[ls1[k]])
        elif d[ls1[k]] in sn:
            print("You ate by snake", b, "move down")
            ind1 = sn.index(d[ls1[k]])
            d[ls1[k]] = sn2[ind1]
            print("Now your score is", d[ls1[k]])
        if b == 100:
            print(ls1[k], "You won")
            d.pop(ls1[k])  # Pop the first winner to find second winner
            nm = nm-1
            if nm < 2:
                win = "win"
                break
        # print(d)
        k = k+1

    if win == "win":
        break
    j = j+1
