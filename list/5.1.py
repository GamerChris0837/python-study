# 리스트 생성
list1 = [3,15,-12.5,"사과","딸기"]
print(list1)

list2=list(range(1,21,2))
print(list2)

# 리스트에서 요소 추출하기
color=["빨강","주황","노랑","초록","파랑","남색","보라"]

print(color[0])   # 인덱스는 0부터 : 빨강
print(color[5])   # 인덱스 5의 요소 : 남색
print(color[2:6])   # 인덱스 2부터 5까지 : 노랑 ~ 남색
print(color[-3])    #뒤에서 3번째 요소 : 파랑
print(color[-4:-1])
# 뒤에서 4번째부터 뒤에서 2번째 까지의 요소 : 초록 ~ 남색