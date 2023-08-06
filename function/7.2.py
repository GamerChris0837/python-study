# 매개변수 : 호출 함수에서 전달하고자 하는 값이나
# 변수를 전달받기 위해 함수 정의에서 사용되는 변수

# 함수의 매개변수
def say_hello(name):   # 매개변수 : name
    print("%s님 안녕하세요!"% name)

say_hello("홍지수")   # 인수 : "홍지수"
say_hello("안지영")   # 인수 : "안지영"
say_hello("황예린")   # 인수 : "황예린" 

# 매개변수와 인수의 개수 일치
# 매개변수 : first_name, last_name
def print_name(first_name,last_name):
    name=first_name+last_name
    print("이름 :"+name)

print_name("홍","정원")   # 인수 : "홍","정원"

# 매개변수에서의 오류 발생
# def print_name(first_name,last_name):   # 매개변수는 2개
#   name=first_name+last_name
#   print("이름 :",name)
# print_name("최")   # 인수는 1개