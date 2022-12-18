while True:
    num = int(input("Enter The Number: "))
    r = num%2

    if r == 0:
        print(num,"Is Even")
    else:
        print(num,"Is Odd")

    try_again = input("Do You Want To Try Again With Another Number (y/n): ").lower()
    if not try_again == "y":
        break