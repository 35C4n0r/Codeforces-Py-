fuck = input()
arr = list(map(str, list(fuck)))
'''arr1000 = set(lis)'''
arr3 = list("AEIOU")
'''arr5 = set(arr3)
vowel = set(arr3)
arr4 = arr1000.intersection(arr5)'''
fuck = fuck.replace('lis', '')
fuck = fuck.replace('E', '')
fuck = fuck.replace('I', '')
fuck = fuck.replace('O', '')
fuck = fuck.replace('U', '')
if len(fuck) >= 5:
    for k in range(len(arr) - 2):
        if (arr[k] in arr3) and (arr[k+1] in arr3) and (arr[k+2] in arr3):
            print("GOOD")
            exit()
print(-1)