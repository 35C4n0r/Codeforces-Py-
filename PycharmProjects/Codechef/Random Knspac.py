
def sumSubsets(sets, n, target):
    x = [0] * len(sets)
    arr5 = []
    j = len(sets) - 1
    while n > 0:
        x[j] = n % 2
        n = n // 2
        j -= 1
    sum = 0
    for i in range(len(sets)):
        if x[i] == 1:
            sum += sets[i]
    if sum == target:
        for i in range(len(sets)):
            print(sets)
            if x[i] == 1:
                print(sets[i])
                arr5.append(sets[i])
            if len(arr) > 0:
                dream = False
        return arr5


def findSubsets(arr, K):
    xxx = pow(2, len(arr))

    for i in range(1, xxx):
        aa = sumSubsets(arr, i, K)
        return aa
        #if not dream:
         #   break


dream = True
nn = int(input())
arr = list(map(int, input().split()))
x = list(map(int, input().split()))
for K in x:
    aaa = findSubsets(arr, K)
    print(aaa)