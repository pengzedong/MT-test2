import sys


def check(a, b, c):
    
    #print('the a is', a)
    #print('the b is', b)
    if (int(c)<int(a)+int(b)):
      # if (int(c)<abs(int(a))-abs(int(b))):
      #     t=int(c)<abs(int(a))-abs(int(b))
      #print(t)
      t=abs(int(a))-abs(int(b))
      if (abs(t)<int(c)):
        #print(abs(t))
        print("pass")
        return True
      else:
        print("invalid")
        sys.stderr.write('It failed!\n')
        raise SystemExit(1)
        return False
    else:
        print("invalid")
        sys.stderr.write('It failed!\n')
        raise SystemExit(1)
        return False


    
    
if __name__ == '__main__':
    try:
        a, b, c= sys.argv[1:5]
        check(a, b, c)
    except Exception as e:
        print(sys.argv)
        print(e)