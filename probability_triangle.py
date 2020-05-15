from random import random


def is_triangle(a, b, c):
#simply checks if the triplet is a triangle
    if a < (b+c) and a > abs(b-c):
        return True
    elif b < (a+c) and b > abs(a-c):
        return True
    elif c < (b+c) and c > abs(b-c):
        return True
    else:
        return False

def get_tri():
#all the values are in the range [0, 1] for simplicity reason
#this does not affect the validity of the resault because of the
#similarity rules concerning triangles
    a = random()
    diff = 1-a
    b = diff*random()
    c = 1-a-b
    return a, b, c

n = int(input('number of iterations = '))
#this two counter variables will be used in the for loops to take account of the
#number of occureance of a triangle in order to determine a statistics
is_tri = 0
is_not = 0

for i in range(n):
    a, b, c = get_tri()
    flag = is_triangle(a, b, c)
    if flag:
        is_tri += 1
    elif flag == False:
        is_not += 1
    else :
        #this prevents the loop from going on in case there is an ecception thus producing non valid data
        print('FATAL ERROR')
        break

print(f'the probability of having a triangle is {is_tri/n}')
