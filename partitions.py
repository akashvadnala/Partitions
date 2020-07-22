def p(n, r):
    if r==0:
        return 'invalid'
    elif r==1 or n==r or n==r+1:
        return 1
    elif n>2*r:
        k=0
        for i in range(1,r+1):
            k+=p(n-r,i)
        return k
    else:
        k=0
        for i in range(1,n-r+1):
            k+=p(n-r,i)
        return k

def partition(a):
    return p(2*a,a)

num = int(input('enter the number..'))

print(partition(num))

# 100 : 190569292

'''
for num in range(1,31):
    print('{}\t: {}'.format(num,partition(num)))'''

input()