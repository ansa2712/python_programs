# students={"student1":{"rollno":101,"name":"Annie","age":24,"course":"Python","mark":85},
#           "student2":{"rollno":102,"name":"Jeena","age":23,"course":"Java","mark":88},
#           "student3":{"rollno":103,"name":"Manu","age":24,"course":"HTML","mark":86}}
# print(students)
# print(students["student1"])
# print(students["student2"])
# print(students["student3"])
# students["student4"]={"rollno":104,"name":"Kiran","age":22,"course":"Java","mark":86}
# print(students)
# print(students["student4"])
# students["student1"]["mark"]=90
# print(students["student1"])
# rollno=int(input("Enter the roll number: "))
# found=False
# for key,values in students.items():
#     if values["rollno"]==rollno:
#         print("Student Found! ")
#         print("Roll no : ",values["rollno"])
#         print("Name : ",values["name"])
#         print("Age : ",values["age"])
#         print("Course : ",values["course"])
#         print("Mark : ",values["mark"])
#         found=True
#         break
# if found==False:
#     print("Student Not Found ! ")
    
# students.pop("student3")
# print(students)
# students.popitem()
# print(students)