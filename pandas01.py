# import pandas
# mydata = {
#     "car": ["a", "b", "c", "d"],
#     "number":[1, 2 ,3, 4]
# }
# myvar = pandas.DataFrame(mydata)
# print(myvar)
# import pandas
# mydata = {
#     "name": ["jone", "deo", "alis", "neo"],
#     "number":[2, 3, 4, 5]
# }
# myvar = pandas.DataFrame(mydata)
# print(myvar)













# import pandas
# mydic = {
#     "students": ["jone", "deo", "alice"],
#     "roll.no": [23445, 234555, 567688]
# }
# myvar = pandas.DataFrame(mydic)
# print(myvar)
# import pandas as pd
# a = [1, 2, 3]
# myvarai = pd.Series(a)
# print(myvarai)








# import pandas as pd
# calories = {
#     "day1": 200, "day2": 210, "day3": 220, "day4": 230, "day5": 240
# }
# myvar = pd.Series(calories)
# print(myvar)

# import pandas
# a = {"name": "alise", "age": 27, "class": "findal year"}
# print(a)
# myvar = pandas.Series(a)
# print(myvar)



# import pandas as pd
# a = 1, 2, 4, 5
# myvar =  pd.Series(a, index=["x", "y", "z", "a"])               # Series using for one D array
# print(myvar)
# print(myvar["z"])




# import pandas
# data1 = {"alish": 234, "jone": 345, "deo": 789}
# var = pandas.Series(data1, index=["alish", "deo"])
# print(var)


# import pandas
# a = {
#      "name": ["rohit", "mohit", "susohit"],
#      "number": [123, 456, 789]

# }
# myvar = pandas.DataFrame(a, index= ["person1", "person2", "person3"])
# print(myvar.loc["person3"])


# import pandas as pd
# file = pd.read_excel('/home/harish/Downloads/timesheet_august_2025.xlsx')
# print(file.head())


# import pandas as pd
# #pd.options.display .max_rows = 1
# myfile = pd.read_csv('/home/harish/Downloads/sample_data.csv')
# #print(myfile.head(2))
# #print(myfile.tail(2))
# print(myfile.to_string())
# print(myfile.info())


# import pandas as pd
# a = [1, 2, 3, 4, 5]
# myvar = pd.Series(a, index= ['first', 'second', 'third', 'fourth', 'fith'])
# print(myvar.loc["second"])
# print(myvar)





# import pandas as pd
# student = {
#     'name': ['raju', 'kaju', 'kunju', 'anil bhaiya'],
#     'roll.no': [1234, 5678, 8900, 2468]
# }
# myvar = pd.DataFrame(student, index= ['001', '002', '003', '004'])
# print(myvar.loc['003'])



# import pandas as pd
# file = pd.read_excel('/home/harish/Downloads/timesheet_august_2025.xlsx')
# print(file.head())
