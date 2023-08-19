# 함수 값의 반환
def func(n):
    x = n + 5
    return x  # x를 함수 값으로 반환


a = func(10)  # func(10)은 함수 정의에서 반환된 x 값을 가짐.
print(a)
b = func(20)  # func(20)은 함수 정의에서 반환된 x 값을 가짐.
print(b)

# def 함수(매개변수1,매개변수2,...):
#    문장1
#    문장2
#    ...
#    return 변수1
# ...
# 변수2=함수(입력값1,입력값2,...)
# ...


# 함수 값의 반환을 이용한 인치/센티미터 환산
def inch_to_cm(inch):
    cm = inch * 2.54
    return cm  # cm를 함수 값으로 반환


num = int(input("길이(인치)를 입력하세요 :"))
result = inch_to_cm(num)
print("%d inch => %.2f cm" % (num, result))
