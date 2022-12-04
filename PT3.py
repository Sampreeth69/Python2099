#Maths
while True:
    try:
        m = float(input("Enter Your Maths Marks: "))
    except ValueError:
        print("Enter Number Dude")
        continue
    if m>40:
        print("No Extra Marks For Good Handwriting")
        continue
    else:
        break
#English
while True:
    try:
        e = float(input("Enter Your English Marks: "))
    except ValueError:
        print("Enter Number Dude")
        continue
    if e>40:
        print("No Extra Marks For Good Handwriting")
        continue
    else:
        break
#Science
while True:
    try:
        s = float(input("Enter Your Science Marks: "))
    except ValueError:
        print("Enter Number Dude")
        continue
    if s>40:
        print("No Extra Marks For Good Handwriting")
        continue
    else:
        break
#Social
while True:
    try:
        ss = float(input("Enter Your Social Marks: "))
    except ValueError:
        print("Enter Number Dude")
        continue
    if ss>40:
        print("No Extra Marks For Good Handwriting")
        continue
    else:
        break
#Tamil
while True:
    try:
        t = float(input("Enter Your Tamil Marks: "))
    except ValueError:
        print("Enter Number Dude")
        continue
    if t>40:
        print("No Extra Marks For Good Handwriting")
        continue
    else:
        break
#Hindi
while True:
    try:
        h = float(input("Enter Your Hindi Marks: "))
    except ValueError:
        print("Enter Number Dude")
        continue
    if h>20:
        print("No Extra Marks For Good Handwriting")
        continue
    else:
        break
#AI
while True:
    try:
        a = float(input("Enter Your AI Marks: "))
    except ValueError:
        print("Enter Number Dude")
        continue
    if a>20:
        print("No Extra Marks For Good Handwriting")
        continue
    else:
        break

total = m+e+s+ss+t+h+a
average = total/7

print("-----------------------------------------------------------------")
print("You Got",total,"out of 240 and the average mark is",average,"%")
print("-----------------------------------------------------------------")
