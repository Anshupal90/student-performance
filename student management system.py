#=========Student Management System=======
student = [
    {
        "id" : (101,"raj"),
        "marks" : [50,60,80],
        "subjects" : {"python","c++","c"}
    },
    {
        "id" : (102,"riya"),
        "marks" : [50,80,80],
        "subjects" : {"python","c++","c"}

    }
]

print(student)
#sorted
print(sorted(student[0]["marks"]))

print("Add new student")
new_id = int(input("enter id:"))
new_name = input("enter name:")
m1 = int(input("enter gk marks:"))
m2 = int(input("enter java marks:"))
m3 = int(input("enter html marks:"))

new_student = [
    {
        "id" : (new_id,new_name),
        "marks" : [m1,m2,m3],
        "subject" : {"gk","java","html"}
    }
]
#add new data

student.append(new_student)
print(new_student)
#search student
search_name = input("enter the search name:")
found = False
for s in student:
    if s["id"][1].lower() == search_name.lower():
        print("student found")
        print(s["marks"])
        found = True
        break

if found == False:
    print("student not found")

      # Update Marks
sid = int(input("enter id:"))    
for s in student:
    if s["id"][0] == sid:
        print("old marks:",s["marks"])
        s["marks"][0] = int(input("enter new python marks:"))
        s["marks"][1] = int(input("enter c++ marks:"))
        s["marks"][2] = int(input("enter new c marks:"))
        print("update marks:",s["marks"])
        break
    else:
        print("student not found") 

#find topper
hightest = 0
topper = " "
for s in student:
    name = s["id"][1]
    total = sum(s["marks"])
    if total > hightest:
        hightest = total
        topper = name
print("hightest:",hightest)
print("topper:",topper)

#delet data

sid = int(input("enter the id:"))
found = False
for s in student:
    if s["id"][0] == sid:
        student.remove(s)
        print("student deleted successfully")
        found = True
        break
    else:
        print("student do not deleted")


