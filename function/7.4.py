# 지역 변수(Local Variable) : 정의된 함수 내에서 사용되는 변수
# 전역 변수(Global Variable) : 메인 루틴의 제일 앞에 정의된 변수


# 지역 변수 사용 예
def func():
    x = 100  # 지역 변수 : x
    print(x)


func()

## 메인 루틴에서 지역 변수 사용 시 오류
## def func():
##   x=100
##   print(x)
##
## func()
## print(x) # x가 정의되지 않음


# 전역 변수 사용 예
def func():
    print(x)  # x -> 전역 변수


x = 100  # 전역 변수 : x
func()
print(x)  # x -> 전역 변수


# 동일한 이름의 전역/지역 변수 사용 예
def func():
    x = 200  # 지역 변수 : x
    print(x)  # x -> 지역 변수


x = 100  # 전역 변수 : x
func()
print(x)  # x -> 전역 변수


# 키워드 global 개념 익히기
def func():
    global x  # 여기서 x는 메인 루틴의 전역 변수
    x = 200  # x-> 전역 변수
    print(x)  # x -> 전역 변수


x = 100  # 전역 변수 : x
print(x)  # x -> 전역 변수
func()
print(x)  # x -> 전역 변수

# 키워드 global을 이용한 원의 면적과 둘레 구하기
import math  # 원주율(pi)을 사용하기 위해 수학 모듈을 가져오기


def cir_area():  # 원의 면적 구하기
    global r
    result = r * r * math.pi
    return result


def cir_length():  # 원주의 길이 구하기
    global r
    result = 2 * r * math.pi
    return result


r = float(input("반지름을 입력하세요 :"))
area = cir_area()
length = cir_length()
print("원의 면적 : %.1f, 원주의 길이: %.1f" % (area, length))

# 매개변수를 이용한 원의 면적과 둘레 구하기
import math  # 원주율(pi)을 사용하기 위해 수학 모듈을 가져오기


def cir_area(r):  # 매개변수 : r
    result = r * r * math.pi
    return result


def cir_length(r):  # 매개변수 : r
    result = 2 * r * math.pi
    return result


r = float(input("반지름을 입력하세요 :"))
area = cir_area(r)  # 인수 : r
length = cir_length(r)  # 인수 : r
print("원의 면적 : %.1f, 원주의 길이: %.1f" % (area, length))
