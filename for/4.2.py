# 1~10 정수 합계 구하기
sum = 0

for i in range(1, 11):
    sum = sum + i
    print("i의 값 : %d => 합계 : %d" % (i, sum))


# range() 함수
for i in range(10):  # 0 ~ 9
    print(i, end=" ")
print()  # 줄 바꿈

for i in range(1, 11):  # 1 ~ 10
    print(i, end=" ")
print()  # 줄 바꿈

for i in range(1, 10, 2):  # 1,3,5,7,9
    print(i, end=" ")
print()  # 줄 바꿈

for i in range(20, 0, -2):  # 20,18,16, ... ,2
    print(i, end=" ")


print()

# 5의 배수 합계 구하기
sum = 0

for i in range(100, 201, 5):  # i가 100 ~ 200(5씩 증가)의 값을 가짐
    sum = sum + i

print("100부터 200까지의 5의 배수의 합계 : %d" % sum)

# if문을 사용하여 5의 배수 합계 구하기
sum = 0

for i in range(100, 201):
    if i % 5 == 0:
        sum = sum + i

print("100에서 200까지의 5의 배수의 합계 : %d" % sum)

# 영어 문장을 세로로 한 자씩 출력하기
word = input("영어 문장을 입력하세요 :")

for x in word:
    print(x)

# 전화번호에서 하이픈(-) 삭제하기
phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요 :")

for x in phone:
    if x != "-":
        print("%s" % x, end="")

# 섭씨를 화씨로 환산하기
# 화씨 온도 = 섭씨 온도 * 9/5 + 32
print("-" * 30)
print("  섭씨  화씨")
print("-" * 30)

for c in range(-20, 31, 5):
    f = c * 9.0 / 5.0 + 32.0
    print("%5d %6.1f" % (c, f))
# %5d : 정수 5자리 / %6.1f : 실수 6자리, 소수점 첫째 자리까지
print("-" * 30)
