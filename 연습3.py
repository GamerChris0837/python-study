# # 주민번호로 성별 찾기
# x=int(input("주민번호 뒷자리 첫 번째 숫자를 입력하세요 : "))

# if x%2==1:
#     print("남자!")
# elif x%2==0:
#     print("여자!")
# else:
#     print("중성!")

# # 함수에서 리스트를 활용하는 프로그램 만들기
# def multiply(num,x):
#     i=0
#     while i<len(num):
#         num[i]=num[i]*x

#         i=i+1

# numbers=[10,20,30,40,50]

# multiply(numbers,10)
# print(numbers)

# multiply(numbers,10)
# print(numbers)

# # 배수의 합계 구하기
# def sum_besu(n):
#     sum=0
#     for i in range(1,101):
#         if i%n==0:
#             sum=sum+i

#     return sum

# besu=int(input("구하고자 하는 배수를 입력하세요 : "))

# total=sum_besu(besu)

# print("1~100 사이 %d의 배수의 합계 : %d"% (besu,total))

# # 문장에 포함된 공백 카운트하기
# def count_space(a):
#     count=0

#     for x in a:
#         if x==" ":
#             count=count+1

#     return count

# sentence="Python is easy and powerful."

# print(sentence)
# num_space=count_space(sentence)
# print("- 공백의 개수 :",num_space)