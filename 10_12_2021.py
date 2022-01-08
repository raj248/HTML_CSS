'''input
7
6
7
3
6
2
'''
import random

# Q1 Take a no from user between 1 to 10 and generate that much no.
# of rnadom nos. between 1 to 100

n = int(input('Enter a Number between 1 and 10 : '))
if n>=1 and n <=10:
	for i in range(n):
		print(random.randint(1,100))

 
# Q2 Take nos. From user in a loop and prints the total and avg of those 5 nos

total = 0

for i in range(5):
	total += int(input('Enter a Number : '))
avg = total/5
print('Total : ',total,'Average : ',avg)