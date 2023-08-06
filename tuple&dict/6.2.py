# 딕셔너리 : 자료를 찾는 인덱스를 의미하는 키(Key)와 자료의 내용인 값(Value)을
# 이용하여 데이터를 관리한다. 딕셔너리에서는 요소들을 중괄호{}로 감싼다.

# 딕셔너리 생성
member={"name":"이지안","age":22,"email":"jjangga4227@gmail.com"}
print(member)

score=dict([("국어",100),("영어",100),("수학",100)])
print(score)

# 딕셔너리 요소 추출
user={"id":"GChr1s","name":"이지안","level":-1, "point":-1}

print(user)   # 딕셔너리 전체 출력
print(user["id"])   # "id" 키의 값 출력
print(user["name"])   # "name" 키의 값 출력
print(user["point"])   # "point" 키의 값 출력