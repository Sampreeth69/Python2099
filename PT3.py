#This Is Just A Basic Program So It Has Some Problems
m = float(input("Enter Your Maths Marks: "))
e = float(input("Enter Your English Marks: "))
s = float(input("Enter Your Science Marks: "))
ss = float(input("Enter Your Social Marks: "))
t = float(input("Enter Your Tamil Marks: "))
h = float(input("Enter Your Hindi Marks: "))
a = float(input("Enter Your AI Marks: "))

total = m+e+s+ss+t+h+a
percent = total/240*100
print("You Got",total,"Out Of 240.0 Which Is",percent,"%")