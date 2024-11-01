# [ 계산기 프로그램 ]

# 덧셈
def plus(x, answer):
    answer += x
    return answer

# 뺼셈
def minus(x, answer):
    answer -= x
    return answer

# 곱하기
def time(x, answer):
    answer *= x
    return answer

# 나누기
def div(x, answer):
    answer /= x
    return answer

# 나머지
def rest(x, answer):
    answer %= x
    return answer

# [ MAIN CODE ]

print("[ H A N N A M   C A L C U L A T O R ]")
print("한남대 계산기 프로그램에 오신 것을 환영합니다.")
print()

print("[ 계산기 설명 ]")
print("1. 연산자는 '+, -, *, /, %' 만 존재합니다.")
print("2. 잘못된 연산자 입력시 다시 연산자를 입력할 수 있습니다.")
print("3. 연산자 입력칸에 '=' 입력시 값이 출력됩니다.")
print("4. 연산자 입력칸에 'AC' 입력시 값이 초기화 됩니다.")
print()

print("[ 계산기 실행 ]")
answer = int(input("숫자를 입력해주세요 : "))

while True:
    shape = input("연산자를 입력해주세요 : ")

    # 무한루프 종료 조건
    if shape == "=":
        print("[", answer, "]")
        break

    n1 = int(input("숫자를 입력해주세요 : "))

    # 예외처리
    if shape != "=" and shape != "+" and shape != "-" and shape != "*" and shape != "/" and shape != "%" and shape != "AC":
        print("연산자가 아닙니다.")
        shape = input("연산자를 입력해주세요 : ")
 
    if shape == "+":
        answer = plus(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "-":
        answer = minus(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "*":
        answer = time(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "/":
        answer = div(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "%":
        answer = rest(n1, answer)
        print("현재 값 :",  answer)
    
    elif shape == "AC":
        answer = 0


