#if Fibonachi starts from 0: 0 1 1 2 3 5 8 13 21 34 55 89

f=int(input('Input position of number of Fibonnachi: '))
n=f-1
result=0
first=0
second=1


def fibonacci(n,first,second):
    
    global result
    if f==2:
        result=1
    if n>1:
        result=first+second
        first=second
        second=result
        return fibonacci(n-1,first,second)

    return result



if __name__ == '__main__':
    fibonacci(n,first,second)
    print(result)