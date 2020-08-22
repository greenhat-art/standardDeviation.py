import csv
import math

with open('datacopy.csv',newline='') as f:
    reader = csv.reader(f)
    fileDta=list(reader)

data=fileDta[0]


#find mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean

# square and get the values
sum =0
sq_list=[]
for num in data:
    a = int(num) - mean(data)
    a=a**2
    sq_list.append(a)

for i in sq_list:
    sum = sum+i

result = sum/(len(data)-1)

std_Dev = math.sqrt(result)
print(std_Dev)
    