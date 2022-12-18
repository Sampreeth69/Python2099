while True:
    num = int(input("Enter Which Table Do You Want To Display (1-100): "))

    t1 = num*1
    t2 = num*2
    t3 = num*3
    t4 = num*4
    t5 = num*5
    t6 = num*6
    t7 = num*7
    t8 = num*8
    t9 = num*9
    t10 = num*10

    if num > 100:
        print("I Can Only Do Till 100")
        continue

    print(num,"x 1 =",t1)
    print(num,"x 2 =",t2)
    print(num,"x 3 =",t3)
    print(num,"x 4 =",t4)
    print(num,"x 5 =",t5)
    print(num,"x 6 =",t6)
    print(num,"x 7 =",t7)
    print(num,"x 8 =",t8)
    print(num,"x 9 =",t9)
    print(num,"x 10 =",t10)

    again = input("You Wanna See Any Other Table (y/n): ").lower()
    if not again == "y":
        break