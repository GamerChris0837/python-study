# # 쓸데 없는 거
# id=input("아이디 : ")
# password=input("비번 : ")

# print("아이디 :",id)
# print("비밀번호 :",password)
# a=int(input("아무 번호 : "))

# if a==1:
#     print("1")
# elif a==2:
#     print("22")
# else:
#     print(":)")

# # 알바 급여 계산기
# print("아르바이트 급여 계산 프로그램")
# print("🎉 시급")
# print("- 주간 근무 : 10,000원")
# print("- 야간 근무 : 주간 시급 * 15")
# print()

# hour_pay=10000

# a=int(input("1(주간 근무) 또는 2(야간 근무)를 입력 해주세요 : "))
# work=int(input("근무 시간을 입력 해주세요 : "))

# if a==1:
#     day_night="주간"
#     pay=hour_pay*work
# else:
#     day_night="야간"
#     pay=hour_pay*work*1.5

# print("%d시간 동안 일한 %s 급여는 %d원 입니다."% (work,day_night,pay))

# # 다이어트 필요성을 판정하기
# height=int(input("키? : "))
# weight=int(input("몸무게? : "))

# s=(height-100)*0.9

# print("="*50)
# print("키 :",height)
# print("weight :",weight)

# if weight>s:
#     print("다이어트")
# else:
#     print("X")

# # * 나무 만들기
# for i in range(1,11):
#     print("*"*i,end="")
#     print()

# # 트리 반전
# for i in range(10):
#     print("*"*(10-i),end="")
#     print()

# # 홀수의 개수 카운트하기
# number=input("수를 입력하세요 : ")

# total=0

# for a in number:
#     a=int(a)
#     if a%2!=0:
#         total=total+1

# # print("홀수의 개수 : %d개"% total)

# for i in range(0,5):
#     for j in range(0,10):
#         print("*",end=" ")
#     print()

# # 역삼각형 형태의 숫자 피라미드 만들기
# for i in range(10):
#     for j in range(10-i):
#         print(10-i,end=" ")
#     print()

# # 홀수의 누적 합계 구하기
# n=1
# sum=0
# count=0

# while n<=100:
#     if n%2==1:
#         sum=sum+n
#         print("%6d"% sum,end="")
#         count=count+1
        
#         if count%10==0:
#             print()

#     n=n+1

# # 영어 문장을 연숙으로 출력하기
# sentence=input("문장을 입력해 주세요 : ")

# i=len(sentence)-1

# while i>=0:
#     if sentence[i]==" ":
#         print("-",end="")
#     else:
#         print("%s"% sentence[i],end="")

#     i=i-1

# # 1~20의 양의 정수 리스트 생성하기
# data=list(range(1,21))

# for i in range(1,21):
#     print("%d"% i,end=" ")

# # 위 코드에서 짝수 요소 출력하기
# data=list(range(1,21))

# for i in range(1,21):
#     if i%2==0:
#         print("%d"% i,end=" ")