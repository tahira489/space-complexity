def recursion(n):
    if (n<=0):
        return n
    print("codingal")
    recursion(n/2)
    recursion(n/2)
recursion(3)
#time complexity = O(nlogn)with base 2
#recurrance relation = Tn/2+Tn/2
#extra work done = n 

