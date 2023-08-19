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


# # 함수로 딕셔너리에서 게임 아이템 가져오기
# def get_item(userid):
#     game_items = {
#         "Sledge": "오함마",
#         "Mute": "전파 방해기",
#         "Fuze": "초코파이 클러스터",
#         "Blitz": "섬광 방패",
#     }

#     for key in game_items:
#         if userid == key:
#             item = game_items[key]

#     return item


# user1 = "Sledge"
# user2 = "Fuze"

# print("%s님의 게임 아이템 : %s" % (user1, get_item(user1)))
# print("%s님의 게임 아이템 : %s" % (user2, get_item(user2)))


# # 예제 8-6의 출력 포맷 바꾸기
# def square_sum(n):
#     sm = 0
#     for i in range(1, n + 1):
#         sm = sm + (i * i * i)
#         print("%d*%d*%d" % (i, i, i),end=(""))

#         if i == n:
#             print("=", end="")
#         else:
#             print("+", end="")
#     print(sm)


# N = int(input("N의 값을 입력하세요 : "))
# square_sum(N)


# # 1~N 홀수의 세제곱 합 구하기
# def square_sum(n):
#     sm = 0
#     for i in range(1, n + 1):
#         if i % 2 == 1:
#             sm = sm + (i * i * i)
#             print("%d*%d*%d" % (i, i, i), end="")

#             if i == n or i == (n - 1):
#                 print("=", end="")
#             else:
#                 print("+", end="")
#     print(sm)


# N = int(input("N의 값을 입력하세요 : "))
# square_sum(N)


# # 키보드로 받은 단어가 회문인지 판별하기
# def is_palindrome(s):
#     for i in range(0, int(len(s) / 2)):
#         if s[i] != s[len(s) - i - 1]:
#             return False

#     return True


# string = input("단어를 입력하세요 : ")

# if is_palindrome(string):
#     print("'%s'는 회문!" % string)
# else:
#     print("'%s'는 회문X!" % string)
