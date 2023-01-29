#다음 조건을 만족하는 구구단을 출력
# - 짝수인 단 (2,4,6,8)은 출력하지 않고 빈 라인 출력
# - 각 단 까지만 (3-> 3*3, 5-> 5*5)

for i in range (1, 10, 2):
    for j in range (1, i+1):
        print(f"{i} * {j} = {i*j}", end = "\t")
    print("")



print("\n" + ("=" * 50) + "\n")

#메소드 (method) ~ gkatn ( funtion)
#객체가 들고 있는 (함수) -> 메소드
#함수지향 [c언어]

#def -> define
#def 이름(매개변수):
#   코드

# 함수 호출
# 이름(인자)

#전역변수 - 프로그램이 종료되면 사라짐
a = 15

# TypeHint(3.x)
# 변수명: 타입 -> 해당 타입이 와야한다라는 힌트

#매개변수 - 함수가 종료되면 사라짐
def add(x:int,y:int):
    #지역변수 - 함수가 종료되면 사라짐
    global a #전역변수 a를 사용할 것임을 선언
    a = 10
    print(x+y)


add(10,45)
print(a)
