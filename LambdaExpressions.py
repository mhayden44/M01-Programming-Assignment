#1. Square
my_list=[5,4,3]
print(list(map(lambda i:i**2,my_list)))

#2. List Sorting
a = [(0,2),(4,3),(9,9),(10,-1)]
print(sorted(a,key=lambda i:i[1]))