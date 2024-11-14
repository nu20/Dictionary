student = {
    "name" : "Ishaan" , 
    "grade" : 6 , 
    "school" : "BJEM" ,
    "Roll no." : 18 ,
    }
print("name : " , student["name"])
print("grade : " , student["grade"])
print("school : " , student["school"])
print("Roll no. : " , student["Roll no."])


print(len(student))
print(student)
student.popitem()
print(student)

print(student.get("abc" , "key does not exist"))

student["name"] = "Ishaan Mahapatra"
print(student)

student["Row no."] = 89
print(student)
