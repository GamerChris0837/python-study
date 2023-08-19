s = "안녕하살법!"

# s[0]에서 0을 문자열의 인덱스(Index)라고 부르는데,
# 인덱스는 문자열에서 해당 문자의 위치를 나타냄.
print(s[0])
print(s[1])

# s[2:5]는 인덱스 2부터 5 미만의 값,
# 즉 2부터 4까지의 문자열을 추출하는데 사용됨.
print(s[2:5])

name = "이지안"
hello = "안녕하살법"
print(name + "님 " + hello)

score = 100
print("성적:" + str(score))
# str(?)는 ?가 가진 정수 값을 문자열로 변경함.

x = "CAT" * 10
print(x)

# len(x) 함수는 문자열의 길이를 구하는 데 사용됨.
x = "가는 말이 고와야 오는 말이 곱다."
n = len(x)
print("문자열의 길이:" + str(n))
# 함수 int()는 실수나 문자열을 정수로 변환함.
# 함수 float()는 정수나 문자열을 실수로 변환함.
# 함수 str()은 정수나 실수를 문자열로 변환함.

# %s는 'String'의 첫 글자로서 문자열을 의미함.
# %d는 'Digit'의 첫 글자로 정수형 숫자를 의미함.
# %f는 'Floating Point'의 첫 글자로서 실수형 숫자를 의미함.
animal = "CAT"
x = "I love %ss" % animal
print(x)

age = 16
print("나는 %d세!" % age)

kor = 100
eng = 50
math = 0
sum = kor + eng + math
avg = sum / 3
print("합계: %d, 평균: %.2f" % (sum, avg))
