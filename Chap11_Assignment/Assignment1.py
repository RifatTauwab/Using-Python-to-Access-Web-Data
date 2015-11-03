import re 
sum = 0
f = open('data.txt', 'r')
file = f.read()
All_number = re.findall('[0-9]+',file)


for num in All_number:
    sum = sum + int(num)

print sum
