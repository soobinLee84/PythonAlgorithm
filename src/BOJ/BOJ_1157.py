# - 문자열 처리  
# - 리스트 사용  
# - 반복문  
# - `.count()`  
# - `max()`  
# - `index()`  
# - `chr()`  
# - 조건문


W = input()
unify = W.upper()
print(unify)

a = list(unify)

print(a.count('N'))

maxCount = []

for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    maxCount.append(a.count(ch))
    print(ch,":" ,a.count(ch))


maxOne = max(maxCount)

print('print : ' , maxOne)

duplicateOne = maxCount.count(maxOne)

if duplicateOne == 1:
    index = maxCount.index(maxOne)
    result = chr(65+index).upper()
    print(result)
else:
    print("?")