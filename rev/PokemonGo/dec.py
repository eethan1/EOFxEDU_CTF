minus = [185,212,172,145,185,212,172,177,217,212,204,177,185,212,204,209,161,124,172,177]
s = [0]*20
goto = 0
for i in range(len(s)):
    arr[i] -= minus[i]
    last += arr[i]
    if i == 19:
        if last == 0:
            print("correct!!!")
            break
        else:
            print("Cheater= =")
            break