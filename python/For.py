list=[1,2,3,4,5,6,7,8,9,10]

# for i in list:
#     print(i)

# for i  in range(len(list)):
#     print(i)    

# for i in enumerate(list):
#     print(i)   

# create a list of subjects
data = ["java", "python", "HTML", "PHP"]

print("Indices in list:")

# get the indices using list comprehension method
print([i for i in range(len(data))])

# indices=[i for i in range(len(data))]
item=[data[i] for i in range(len(data))]
print("values in list:")

# get the values from indices using list
# comprehension method
print([data[i] for i in range(len(data))])
     
    