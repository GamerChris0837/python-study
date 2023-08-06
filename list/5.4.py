# 리스트 병합
person1=["kim",24,"kim@naver.com"]
person2=["lee",35,"lee@hanmail.net"]

person=person1+person2   # 두 리스트 합치기

print(person)

# 리스트 요소의 합계와 평균
scores=[80,90,85,95,100]

sm=sum(scores)
avg=sm/len(scores)   # len() 함수 : 리스트의 길이

print("합계 :",sm)
print("평균 :",avg)

# reverse() 메소드로 리스트 순서 반대로 하기
data=[10,20,30,40,50]
print(data)

data.reverse()
print(data)

# copy() 메소드로 리스트 복사하기
fruits=["apple","banana","orange"]
print(fruits)

# fruits의 요소들을 복붙해 요소들이 서로같은 값을 가지고 있음
x=fruits.copy()
print(x)

# sort() 메소드로 리스트 정렬하기
data=[12,8,15,32,-3,-20,15,34,6]
print(data)

data.sort()   # data 내의 요소을 오름차순으로 정렬함.
print(data)

data.sort(reverse=True)   # data 내의 요소를 내림차순으로 정렬함.
print(data)
# append() : 리스트 제일 뒤에 새로운 요소를 추가함.
# insert() : 리스트에서 특정 인덱스 앞에 새로운 요소를 삽임함.
# index() : 리스트에서 특정 요소의 위치인 인덱스 번호를 구함.
# remove() : 리스트에서 특정 값을 가진 요소를 삭제함.
# pop() : 리스트에서 특정 인덱스 번호를 가진 요소를 추출하고,
# 그 요소를 리스트에서 삭제함.
# clear() : 리스트의 전체 요소를 삭제함.
# reverse() : 리스트 요소들의 순서를 거꾸로 함.
# copy() : 리스트를 복사하여 새로운 리스트를 생성함.
# sort() : 리스트 요소들을 오른차순 또는 내림차순으로 정렬함.

# list() : 새로운 리스트를 생성함.
# len() : 리스트의 길이를 구함.
# sum() : 리스트 요소들의 합계를 구함.