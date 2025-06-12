#dictionary
Student = {
    "name": "John Doe",
    "age": 20,
    "email": "john@gmail.com ",
    "tall": True,
    "salary": 2500.50,
}
Student["name"] = "Jane Doe"
#print(Student)
#print(type(Student))
#print(Student.keys())
#print(Student.values())
#print(Student.items())
for key, value in Student.items():
    print(key,value)
for key in Student.keys():
    print(key)
for value in Student.values():
    print(value)