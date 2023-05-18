# Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001):
    if x%5== 0:
        print(x)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for v in range(1,101):
    if v%10==0:
        v="Coding Dojo"
    elif v%5==0:
        v="Coding"
    print(v)
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for t in range(0,500001):
    if t%2!=0:
        sum+=t
print(sum)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for h in range(2018,0,-4):
    print(h)
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if i%mult==0:
        print(i)