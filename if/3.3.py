age=int(input("나이?"))
ticket=50000

if age>=65:
    ticket=0

print("나이 : %d세"% age)
print("입장료 : %d원"% ticket)

num=int(input("양의 정수를 입력하세요 :"))
result="3의 배수도 4의 배수도 아님!"

if num%3==0:
    result="3의 배수!"
if num%4==0:
    result="4의 배수!"
if num%3==0 and num%4==0:
    result="3의 배수이면서 4의 배수!"
print("%d은(는) %s"% (num,result))

ans1=input("'사자'의 영어 단어는 뭐여? :")
result="틀렸으니 뒤져라"
if ans1=="lion":
    result="맞았으니 뒤져라"
print(result)