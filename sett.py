import re

s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}

s1 = s1 & s2

# & -> 교집합
# | -> 합집합
# - -> 차집합

print(s1)

# 지역-국번-가입자개별번호 -> 국번 출력 프로그램
# regex을 통해서 체크
# aa-123-abcd -> 전화번호가 올바르지 않습니다.
# 00-1234-0000 -> 1234
# 00-789-0000 -> 789
# 02, 041, 031 - 지역번호 2~3자리
# 국번 - 3~4자리
# 개별번호 - 4자리

# number = input("전화번호를 입력하세요 : ")

# r = re.compile('^\d{2,3}-\d{3,4}-\d{4}$')

# if r.match(number):
#    print(number.split('-')[1])
# else:
#    print('전화번호가 아닙니다.')

# 숫자3자리-숫자2자리-숫자5자리 형식의 사업자등록번호를 입력받아서 혁시이 맞는지 점검하는 프로그램 구현
# - 전체 글자수 점검 ( x )
# - 모든 하이픈의 위치가 올바른지 ( x )
# - 하이픈을 제외하면 모든 글자가 숫자여야합니다( x )

number = input("사업자등록번호를 입력하세요")

r = re.compile('^\d{3}-\d{2}-\d{5}$')

if r.match(number):
    print("올바른 형식입니다.")
else:
    print('잘못된 형식입니다.')

# 학교 성적 관리 프로그램을 구현하세요.
# 다음과 같이 (,)로 구분된 데이터가 넘어옵니다.
# name 변수에는 이름
# socre 변수에는 점수를 저장

# "김철수",85

# replace -> 문자열 안의 특정 문자열 다른 문자열로 변경
# split -> 문자열 가르기
# strip -> 문자열의 양 끝에 있는 불필요한 문자 제거
# lstrip -> 문자열의 왼쪽 끝에 있는 불필요한 문자 제거
# rstrip -> 문자열의 오른쪽 끝에있는 불필요한 문자 제거

data = '"김철수",85'

args = data.split(',')

name = data.split(',')[0].strip('"')
score = args[1]

print(name, score)


# def 이름(매개변수):

#매개변수가 몇개인지 ( 넘어오는 인자가 몇개인지 ) 모르는 경우
#가변인자 (variable arguments)
# - args

#키워드 가변인자 (keyword variable arguments) **
# - kwargs
# - key:value
# - 가변인자와 함께 쓸 때 무조건 뒤에 와야한다.

def add(*args ,**kwargs:int) -> int:
    return kwargs

print(add(a=5, c=10, d=15, k=20))
