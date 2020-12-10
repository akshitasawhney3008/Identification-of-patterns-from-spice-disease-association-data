def gcd(j,k):
    if j == 0:
        return j
    if k == 0:
        return k
    if j == 1 or k == 1:
        return 1
    return gcd(k, j % k)

def check_if_coprime(j,k):
    return gcd(j,k)


t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    flag = 2
    l.sort()
    for j in range(len(l)-1):
        if (int(l[j]) == 1):
            break
        else:
            flag = check_if_coprime(l[j],l[j+1])
            if (flag == 1):   #coprime found
                print("0")
                break
    if(flag == 0):
        print("-1")
    elif(flag == 2):
        print("0")
