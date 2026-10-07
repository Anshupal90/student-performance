name=(input("enter the student name:"))

maths=int(input("enter the math marks:"))
english=int(input("enter the enlish marks:"))
python=int(input("enter the python marks:"))

total=maths + english + python
percentage = total / 3

print("student performance\n")
print("name:",name)
print("total:",total)
print("percentage:",percentage)

if percentage >= 80 and percentage <= 100:
    print("grade A")
elif percentage >= 60 and percentage <= 80:
     print("grade B")  
elif percentage >= 40 and percentage <= 60:
    print("grade C")
else:
    print("grade F")

if percentage >= 40:
    result = "pass"
else:
    result = "fail"

print("result:",result)      
