# 파이썬의 내장 함수
# print() : 데이터나 변수를 화면에 출력함
# input() : 키보드로 데이터를 입력 받음
# type() : 변수의 데이터 형을 구함
# int() : 실수나 문자열을 정수로 변환함
# float() : 정수나 문자열을 실수로 변환함
# str() : 정수나 실수를 문자열로 변환함
# sum() : 리스트나 튜플 요소들의 합을 구함
# len() : 문자열, 리스트, 튜플, 딕셔너리의 길이를 구함
# range() : 10진 정수를 2진수로 변환함
# list() : 새로운 리스트를 생성함
# tuple() : 새로운 튜플을 생성함
# dict() : 새로운 딕셔너리를 생성함
## ord() : 문자의 아스키(ASCII) 코드 값을 구함
## bin() : 10진 정수를 2진수로 변환함
## hex() : 10진 정수를 2진수로 변환함
## round() : 반올림 값을 구함
## max() : 리스트나 튜플의 최댓값을 구함
## min() : 리스트나 튜플의 최솟값을 구함

# 아스키 코드(ASCII) 구하기 - ord()
x = "1"  # x : 문자열
print("아스키 코드 :", ord(x))  # ord() : x의 아스키 코드 값

# 'a'의 아스키 코드(16진수/2진수) 구하기
x = "a"
code = ord(x)

print("아스키 코드(10진수) : %d" % code)
print("아스키 코드(16진수) : %s" % hex(code))
print("아스키 코드(2진수) : %s" % bin(code))

# 반올림 값 구하기
x = round(7.65676)  # 소수점 첫째 자리 반올림
print(x)

y = round(7.65676, 2)  # 소수점 셋째 자리 반올림
print(y)

# 최댓값 구하기
x = max(3, 5, 2)  # 3,5,2 중 최댓값
print(x)

data = [3, 7, 2, 12, 6]
y = max(data)  # 리스트 요소 중 최댓값
print(y)
