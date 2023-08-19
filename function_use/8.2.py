# 소수 여부 판별하기
def is_prime(n):
    prime = True  # prime의 초깃값은 True
    if n > 1:  # n이 2부터 시작
        for i in range(2, n):  # n:2~n-1
            if n % i == 0:  # i로 나눈 나머지가 0이면
                prime = False  # prime을 False로 설정

    return prime


number = int(input("수를 입력하세요 :"))

if is_prime(number):
    print("소수!")
else:
    print("소수X!")


# 1~N 세제곱 합계 구하기
def square_sum(n):
    sm = 0
    for i in range(1, n + 1):  # i:1~n
        sm = sm + (i * i * i)  # 누적합계 sm 구함

    return sm


N = int(input("N의 값을 입력하세요 :"))
print(square_sum(N))

# 회문(Palindrome) : 똑바로 읽어도 거꾸로 읽어도 똑같은 단어나 문장


# 회문인지 판별하기
def is_palindrome(s):
    for i in range(0, int(len(s) / 2)):  # 문자열의 좌측 절반 읽음
        if s[i] != s[len(s) - i - 1]:  # 좌측과 우측 인덱스가 다른지 비교
            return False

    return True


string = input("문장 or 단어? : ")

if is_palindrome(string):
    print("%s은(는) 회문!" % string)
else:
    print("%s은(는) 회문X!" % string)


# 문장 단어 반대로 하기
def reverse_sentence(s):
    words = s.split(" ")  # 문자열 s를 쪼개서 리스트로 저장
    result = ""  # result에 빈 문자열 저장
    for word in words:
        result = word + " " + result  # result 앞 부분에 word 삽입

    return result


sentence = "Nice to meet you"
print(reverse_sentence(sentence))


# 문자열 존재 여부 판별
def check_word(s, keyword):
    if s.find(keyword) == -1:  # 검색 후 반환된 인덱스가 -1인가?
        print("'%s'은(는) 존재하지 않음!" % keyword)
    else:
        print("'%s'은(는) 존재함!" % keyword)


string = "A good book is a great friend."
word = "friend"

print("문장 :", string)
print("찾는 단어 :", word)

check_word(string, word)


# 다수의 문자열 치환하기
def replace_word(string, word_list, word):
    arr = string.split(" ")  # 문자열 쪼개서 리스트 arr에 저장
    new_arr = []  # new_arr에 빈 리스트 저장
    for x in arr:
        if x in word_list:
            new_arr.append(word)  # new_arr에 word 추가
        else:
            new_arr.append(x)  # new_arr에 x 추가

    result = " ".join(new_arr)  # new_arr을 붙여서 문자열로 만듦
    return result


string = "python java php apple orange banana"
word_list = ["apple", "orange", "banana"]  # 치환할 단어 목록
word = "fruits"  # 치환 단어
print("문자열 :", string)
print("단어 리스트 :", word_list)
print("치환할 단어 :", word)

new_str = replace_word(string, word_list, word)
print("치환된 문자열 :", new_str)


# 문자열 위치 이동시키기
def string_shift(string, d, direction):
    if direction == "left":  # 왼쪽으로 이동
        left_part = string[d:]  # left_part : 이동 후 문자열 왼쪽 부분
        right_part = string[0:d]  # right_part : 이동 후 문자열 오른쪽 부분
    else:  # 오른쪽 이동
        left_part = string[len(string) - d :]
        right_part = string[0 : len(string) - d]

    result = left_part + right_part  # 왼쪽과 오른쪽 부분 서로 연결
    return result


string = "pythonprogramming"

str_left = string_shift(string, 2, "left")
str_right = string_shift(string, 3, "right")

print("원래 문자열 :", string)
print("좌측으로 2칸 이동 :", str_left)
print("우측으로 3칸 이동 :", str_right)
