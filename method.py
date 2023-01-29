import re

# 메소드 (method) ~ 함수 (function)
#함수 -> 코드 집합
#객체가 들고 있는 (함수) -> 매소드

#str class (객체)
#문자열 메소드? str이 들고있는 함수

#< : 왼쪽 정렬
#> : 오른쪽 정렬
#^ : 가운데 정렬
#decimal - 정수

#print("10자리 왼쪽 정렬{:!>100d}".format(10))

#s = "hello wolrd"

#print(s.count("l"))
#print(s[int(s.find("r"))])

s = '홍길동:17:01012345678'

# [] -> list
#split
print(s.split(':'))
#replace
print(s.replace(':',"-"))


#주민번호를 입력받는 프로그램 구현
#6자리-7자리 검사
#하이픈이 정확한 위치에 없다면
#하이픈의 위치가 잘못되었습니다.
#잘 입력했다면
#생년월일은 000000입니다.

Personal_card = input("주민번호를 입력해주세요 >>> ")

if (Personal_card.find('-') == 6):
    print(f'생년월일은 {Personal_card.split("-")[0]}입니다.')
else:
    print("하이픈의 위치가 잘못되었습니다.")
#정규 표현식?

#regex (정규표현식)
#''

p = input("이메일을 입력해주세요 >>> ")

email = '^[a-zA-Z0-9]+@^[a-zA-Z0-9]+\.[a-z]+$'

r = re.compile('^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]+$')

# False - None, 0, [] ~~
# true - False 이외의 모든 값

if r.match(p):
    print('이메일입니다.')
else:
    print("이메일이 아닙니다.")
