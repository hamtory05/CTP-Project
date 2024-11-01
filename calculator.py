# [ 계산기 프로그램 ]

# 덧셈
def plus(x, total):
    total += x
    return total

# 뺼셈
def minus(x, total):
    total -= x
    return total

# 곱하기
def time(x, total):
    total *= x
    return total

# 나누기
def div(x, total):
    if x == 0:
        print("0으로 나눌 수 없습니다.")
        return total
    total /= x
    return total

# 나머지
def rest(x, total):
    total %= x
    return total

# [ MAIN CODE ]

# < 설명 >
print("[ H A N N A M   C A L C U L A T O R ]")
print("한남대 계산기 프로그램에 오신 것을 환영합니다.")
print()

print("[ 계산기 설명 ]")
print("1. 연산자는 '+, -, *, /, %' 만 존재합니다.")
print("2. 잘못된 연산자 입력시 다시 연산자를 입력할 수 있습니다.")
print("3. 연산자 입력칸에 '=' 입력시 값이 출력됩니다.")
print("4. 연산자 입력칸에 'AC' 입력시 값이 초기화 됩니다.")
print()

# < 실행 >
print("[ 계산기 실행 ]")

# 출력 값을 알려주는 answer에 처음 숫자를 저장.
answer = float(input("숫자를 입력해주세요 : "))

# 무한 루프 ('=' 을 입력할 때 까지)
while True:
    # 연산자 입력
    shape = input("연산자를 입력해주세요 : ")

    # 무한루프 종료 조건
    if shape == "=":
        print("[", answer, "]")
        break

    # 연산자 예외처리
    if shape != "=" and shape != "+" and shape != "-" and shape != "*" and shape != "/" and shape != "%" and shape != "AC":
        print("연산자가 아닙니다.")
        shape = input("연산자를 입력해주세요 : ")
    
    # AC를 입력했을 때
    if shape == "AC": 
        answer = 0 # answer을 0으로 초기화
        print("현재 값 :",  answer)
        answer = float(input("숫자를 입력해주세요 : "))
        continue

    # 연산할 숫자 입력
    n1 = float(input("숫자를 입력해주세요 : "))

    # 계산 
    if shape == "+": # 덧셈
        answer = plus(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "-": # 뺄셈
        answer = minus(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "*": # 곱셈
        answer = time(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "/": # 나눗셈
        answer = div(n1, answer)
        print("현재 값 :",  answer)

    elif shape == "%": # 나머지
        answer = rest(n1, answer)
        print("현재 값 :",  answer)
    


