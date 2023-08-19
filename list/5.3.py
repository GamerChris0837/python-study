# 리스트 요소 수정
flowers = ["목련", "벚꽃", "장미", "백일홍"]
print(flowers)

flowers[1] = "무궁화"
print(flowers)

# 리스트에 새로운 요소 추가
arr = [5, 3, 12, 9, 2]
print(arr)

arr.append(10)  # 제일 뒤에 10 추가
print(arr)

# 빈 리스트에 요소 추가
scores = []  # 빈 리스트, 요소가 없음

while True:  # 무한 반복
    score = int(input("성적을 입력하세요(종료 : -1) :"))

    if score == -1:
        break  # score가 -1이면 while 루프 탈출
    else:
        scores.append(score)  # 리스트 추가

print(scores)

# insert() 메소드로 요소 삽입하기
fruits = ["apple", "orange", "banana", "cherry"]
print(fruits)

fruits.insert(1, "melon")  # 1번 인덱스에 "melon" 삽입
print(fruits)

fruits.insert(2, "strawberry")  # 2번 인덱스에 "strawberry" 삽입
print(fruits)

# index() 메소드로 요소의 인덱스 구하기
number = [5, 20, 13, 7, 8, 22, 7, 17]
print(number)

idx = number.index(7)  # 7이 가장 먼저 나오는 인덱스 번호 : 3
print(idx)

# remove() 메소드로 리스트의 요소 삭제
member = ["이지안", 16, "서울시 서울시", "       @gmail.com", "010-    -    "]
print(member)

member.remove(16)
print(member)

# pop() 메소드로 리스트의 요소 삭제
data = [10, 20, 30, 40, 50, 60, 70, 80]
print(data)

x = data.pop(2)  # 인덱스 2에 있는 30을 추출하고 data에서 삭제
print(x)
print(data)

x = data.pop(3)  # 인덱스 3에 있는 50을 추출하고 data에서 삭제
print(x)
print(data)

# 리스트의 모든 요소 삭제
data = [3, 12, 7, -3, -9]
print(data)

data.clear()  # data 내에 있는 모든 요소 삭제
print(data)
