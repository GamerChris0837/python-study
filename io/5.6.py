# 2차원 리스트의 구조
numbers=[[10,20,30],[40,50,60,70,80]]

print(numbers[0][0])
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])

# 2차원 리스트와 이중 for문
data=[[10,20],[30,40],[50,60],[70,80]]
for i in range(4):   # i는 리스트의 행
    for j in range(2):   # j는 리스트의 열
        print("data[%d][%d] = %d"% (i,j,data[i][j]))

# 2차원 리스트로 성적 합계와 평균 구하기
scores=[[75,83,90],[86,86,73],[76,95,83],[89,96,69],[89,76,93]]

for i in range(len(scores)):   # i : 인덱스의 행, j : 인덱스의 열
    sum=0
    for j in range(len(scores[i])):   # len(scores[i]) : 인덱스 i 행의 길이
        sum=sum+scores[i][j]   # scores[i][j] : 인덱스의 각 요소
    avg=sum/len(scores[i])

    print("%d번째 학생의 성적 합계 : %d, 평균 : %.2f"% (i+1,sum,avg))

strings=[["원두커피","라떼","콜라"],["우동","국수","피자","파스타"]]

for i in range(len(strings)):   # len(strings) : 2(리스트 행의 개수)
    for j in range(len(strings[i])):   # len(strings[i]) : 3,4(리스트 각 행의 길이)
        print(strings[i][j])