# [ 중간 과제 & 계산기 프로그램 ]

# < 예제 활용한 것 >
# 1. 137p 5번 : 연산자를 확인하고 그의 맞는 계산하기
# 2. 168p 15번 : 교수님이 알려주신 while True를 사용하여 메인 코드를 작성
# 3. 
# 4. 196p 8, 9, 10번 : 함수 매개변수 사용법, return 사용법을 활용하여 작성
# 5. 201p 8번 : 연산자 예외처리를 활용하여 코드를 작성
# 6. 전에 배운 누적합 활용해서 answer에 계속 값을 누적시킴

# ==========[ MAIN CODE ]==========

# < 덧셈 >
def plus(x, total):
    total += x
    return total

# < 뺼셈 >
def minus(x, total):
    total -= x
    return total

# < 곱하기 >
def time(x, total):
    total *= x
    return total

# < 나누기 >
def div(x, total):
    # 나누기 예외처리 
    if x == 0: 
        print("0으로 나눌 수 없습니다.")
        return total
    total /= x
    return total

# < 나머지 >
def rest(x, total):
    total %= x
    return total

# < 제곱 >
def square(x, total):
    # 누적값을 따로 저장
    tmp = total
    for i in range(int(x) - 1): # x를 float로 입력받고 있어서 int로 바꿔서 for문을 작성함.
        total *= tmp # 누적값을 제곱하는 과정
    return total


# < 계산기 프로그램 설명 >
print("[ H A N N A M   C A L C U L A T O R ]")
print("한남대 계산기 프로그램에 오신 것을 환영합니다.")
print()

print("[ 계산기 설명 ]")
print("1. 연산자는 '+, -, *, /, %, **' 만 존재합니다.")
print("2. 잘못된 연산자 입력시 다시 연산자를 입력할 수 있습니다.")
print("3. 연산자 입력칸에 '=' 입력시 값이 출력됩니다.")
print("4. 연산자 입력칸에 'AC' 입력시 값이 초기화 됩니다.")
print("5. 연산을 할 때마다 현재 값을 계속 출력합니다.")
print("6. 잘못된 숫자 입력시 프로그램이 종료됩니다.")
print()

# < 계산기 프로그램 실행 코드 >
print("[ 계산기 실행 ]")

# 출력 값을 알려주는 answer에 처음 숫자를 저장.
answer = float(input("숫자를 입력해주세요 : "))

# 무한 루프 ('=' 을 입력할 때까지 반복)
while True:
    # 연산자 입력 (+, -, *, /, %, =, **, AC)
    shape = input("연산자를 입력해주세요 : ")

    # 무한루프 종료 조건
    if shape == "=":
        print("[", answer, "]")
        break 
  
    # 연산자 예외처리
    if shape != "=" and shape != "+" and shape != "-" and shape != "*" and shape != "/" and shape != "%" and shape != "**" and shape != "AC":
        # 무한 루프 
        while True:
            # 정확한 연산자 입력시 무한루프 탈출
            if shape == "=" or shape == "+" or shape == "-" or shape == "*" or shape == "/" or shape == "%" or shape == "**" or shape == "AC":
                break
            print("연산자가 아닙니다.")
            shape = input("연산자를 입력해주세요 : ")
        
    # AC를 입력했을 때
    if shape == "AC": 
        answer = 0 # answer을 0으로 초기화
        print("현재 값 :",  answer)
        # answer를 초기화 했으므로 answer에 처음 숫자를 다시 저장
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

    elif shape == "**": # 제곱
        answer = square(n1, answer)
        print("현재 값 :", answer)  