# # 인치 cm 계산기
# x=int(input("inch to cm(1)\ncm to inch(2) :"))

# if x==1:
#     a=float(input("몇인치?"))
#     cm=float(a)*2.54
#     print("%.2f인치 = %.4fcm"% (a,cm))
# elif x==2:
#     b=float(input("몇cm?"))
#     inch=float(b)/2.54
#     print("%.2fcm = %.4f인치"% (b,inch))
# else:
#     print(">:(")

# # 위위 코드에서 홀수 요소 출력하기
# data=list(range(1,21))

# for i in range(1,21):
#     if i%2==1:
#         print("%d"% i,end=" ")

# # 빈 리스트에 요소 추가하기
# data=list()

# for x in range(10,21):
#     data.append(x)

# print(data)

# # 성적 합계와 평균 구하기
# scores=[]

# while True:
#     x=int(input("성적을 입력하세요(종료 시 -1 입력) : "))

#     if x==-1:
#         break
#     else:
#         scores.append(x)

# sum=0
# for score in scores:
#     sum=sum+score

# avg=sum/len(scores)
# print("합계 : %d, 평균 %.2f"% (sum,avg))

# # 수/우/미/양/가 개수 카운트하기
# s=[64,89,100,85,75,58,79,67,96,87,87,36,82,98,84,76,63,69,53,22]

# soo=0
# woo=0
# mi=0
# yang=0
# ga=0

# i=0
# while i<len(s):
#     if s[i]>=90 and s[i]<=100:
#         soo=soo+1

#     if s[i]>=80 and s[i]<=89:
#         woo=woo+1

#     if s[i]>=70 and s[i]<=79:
#         mi=mi+1

#     if s[i]>=60 and s[i]<=69:
#         yang=yang+1

#     if s[i]>=0 and s[i]<=59:
#         ga=ga+1

#     i=i+1

# print("수 : %d명"% soo)
# print("우 : %d명"% woo)
# print("미 : %d명"% mi)
# print("양 : %d명"% yang)
# print("가 : %d명"% ga)

# # 구구단표 만들기
# dans=(2,3,4,5,6,7,8,9)

# print("구구단표")
# print("="*30)

# for dan in dans:
#     print(str(dan)+"단")
#     for i in range(1,10):
#         print("%d * %d = %d"% (dan,i,dan*i))
#     print("-"*30)

# # 성적 합계 평균 구하기
# scores={"김채린":85,"박수정":98,"함소희":94,"안예린":90,"연수진":93}

# sum=0

# for key in scores:
#     sum=sum+scores[key]

#     print("%s : %d"% (key,scores[key]))

# avg=sum/len(scores)

# print("합계 : %d, 평균 : %.2f"% (sum,avg))

# # 두 수의 합 구하기
# def add(a,b):
#     c=a+b
#     print("%d + %d = %d"% (a,b,c))

# add(12,15)
# add(245,300)
# add(-38,-12)

# # 매개변수 *args를 활용하는 프로그램 작성하기
# def member_join(*args):
#     result=""
#     for arg in args:
#         result=result+arg+" "

#     print("가입 회원 :",result)

# member_join("김정연","안서영")
# member_join("황선형","김철영","이창연")
# member_join("정수진","김보람","종수연","함소영")
