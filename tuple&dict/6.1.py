# 튜플(Tuple) : 리스트(list)와 많은 부분이 유사하고 사용법도 거의 같지만 차이점이 두 가지가 있다.
# 1. 튜플에선 리스트의 대괄호[] 대신 소괄호()를 사용한다.
# 2. 튜플에선 리스트와 달리 요소의 수정과 추가가 불가능하다.

# 튜플 생성
animals = ("토끼", "거북이", "사자", "여우")
print(animals)

numbers = tuple(range(10))
print(numbers)

# 튜플 요소 수정 시 오류 발생
# animals=("토끼","거북이","사자","여우")
# animals[2]="호랑이"   # 튜플은 요소 수정 불가

# 튜플의 요소 추출
n = tuple(range(10, 21))  # 10 ~ 20
print(n)

print("n[0] =", n[0])  # 10(인덱스 0)
print("n[2:5] =", n[2:5])  # 12 ~ 14(인덱스 2~4)
print("n[2:] =", n[2:])  # 12 ~ 20(인덱스 2부터 끝까지)
print("n[:5] =", n[:5])  # 10 ~ 14(인덱스 처음부터 4까지)
print("n[-2] =", n[-2])  # 19(뒤에서 두 번째)
print("n[::-1] =", n[::-1])  # 20 ~ 10(반전)
# n[::-1]을 이용하면 튜플 n의 순서가 반대로 된 튜플을 얻을 수 있다.

# 튜플의 길이
tup1 = (10, 20, 30, 40, 50)

for i in range(len(tup1)):  # len(tup1) : tup1의 길이
    print(tup1[i])

# 튜플의 병합
tup1 = (10, 20, 30)
tup2 = (40, 50, 60)
tup3 = tup1 + tup2
print(tup3)

# 튜플에 관리자 정보 저장
admin_info = ("GChr1s", "0837", "jjangga4227@gmail.com")

print("관리자 정보")
print("아이디 :" + admin_info[0])  # 인덱스 0 : 관리자 아이디
print("비밀번호 :" + admin_info[1])  # 인덱스 1 : 비밀번호
print("이메일 :" + admin_info[2])  # 인덱스 2 : 이메일 주소
