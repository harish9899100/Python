# student = {
#     "name":"rohan",
#     "edu":"bca",                    # in the dictionary we are using key and valu pair, duplicasis are not allow and ordered
#     "location":"noida",
#     "name":"hothii"
# }
# print(student)
# print(student["edu"])


# car = {
#     "brand": "mercedese",
#     "model": "mayback",
#     "lounch": 2022,
#     "luxery": True
# }
# print(car)

# a = {"name": "rohan", "edu": "LLM", "age": 23}
# for x in a.values():
#     print(x)


# students = {                        #nested dectionary in python
#     "student1": {
#         "name": "jone",
#         "class": "5th",
#         "age": 10

#     },
#     "student2": {
#         "name": "deo",
#         "class": "8th",
#         "age": 13
#     },
#     "student3": {
#         "name": "AI",
#         "class": "2nd",
#         "age": 3
#     }
# }
# print(students)
# print(students["student3"])


student1 = {
    "name": "jone",
    "class": "10th",
    "age": 15
}
student2 = {
    "name": "deo",
    "class": "11th",
    "age": 16
}
student3 = {
    "name": "harry",
    "class": "5th",
    "age": 10
}
students = {
    "student1": student1,
    "student2": student2,
    "student3": student3
}
print(student1)
print(students)