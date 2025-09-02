

N = int (input()) # 단어갯수
words = []

for _ in range(N):
    word = input()
    words.append(word)
    
# set은 중복을 제거해줌 
words = list(set(words))
    
    
# 파이썬의 sorted() 함수는 정렬 기준을 직접 정해서 쓸수 있음 이걸 정렬 기준 함수 즉 key 를 이용해서 지정해줌
# 람다의 첫번째 인자 : 처음엔 len (길이 비교 ), 두번짼 사전 순서 비교(=단어 자체의 순서 비교로 한다임.)
sorted_words = sorted(words, key=lambda x:(len(x),x))

# 한줄씩 출력!
for w in sorted_words:
    print(w)