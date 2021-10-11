import sys
import random

def RightTriangle(a, b):
    
    #print('the a is', a)
    #print('the b is', b)
    temp=(int(a)**2)+(int(b)**2)
    c=pow(temp,0.5)
    print(int(c))
    return int(c)


    
    
if __name__ == '__main__':
    try:
        a, b= sys.argv[1:3]
        RightTriangle(a, b)
    except Exception as e:
        print(sys.argv)
        print(e)