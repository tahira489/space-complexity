def sum(n):
    return n*(n+1)/2
print(sum(4))
#space cpmplexity = 1
#time complexity = 1

def arraysum(a):
    sum=0
    for i in a:
        sum=sum + i
    return sum
a=[1,2,3,4]
print(arraysum(a))
#space complexity = n
#time compleity = a