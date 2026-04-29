i = 0
while i <= 10:
    print(i)
    i += 1


def password():
    maxcount = 5
    count = 0
    while True:
        inp = int(input("Enter a password: "))
        if inp == 101:
            print("Yes")
            break
        else:
            count += 1
            if count == maxcount:
                print("Max attentions")
                break
            print("No")


#while True:
#    print("34")