print('Enter the sides of triangle')
a=int(input('First Side :\n'))
b=int(input('Second Side :\n'))
c=int(input('Third Side :\n'))

if(a+b>=c and b+c>=a and c+a>=b):
    print('Valid Triangle')
    if(a==b and b==c):
        print('Equilateral triangle')
    elif(a==b or b==c or c==a):
        print('Isosceles triangle')
    else :
        print('Triangle is scalane')
else :
    print('Not a valid triangle')