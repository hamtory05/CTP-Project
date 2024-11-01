# [ 계산기 프로그램 ]

# 덧셈
def puls():
    pass

# 뺼셈
def minus():
    pass

# 곱하기
def time():
    pass

# 나누기
def div():
    pass

# 나머지
def rest():
    pass

# [ MAIN CODE ]

print("[ H A N N A M   C A L C U L A T O R ]")
print("한남대 계산기 프로그램에 오신 것을 환영합니다.")
print()

print("[ 계산기 설명 ]")
print("1. 연산자는 '+, -, *, /, %' 만 존재합니다.")
print("2. 잘못된 연산자 입력시 다시 연산자를 입력할 수 있습니다.")
print("3. 연산자 입력칸에 '=' 입력시 값이 출력됩니다.")
print("4. 연산자 입력칸에 'AC' 입력시 값이 초기화 됩니다.")

answer = 0

while True:
    n1 = int(input("숫자를 입력해주세요 : "))
    shape = input("연산자를 입력해주세요 : ")

    # 무한루프 종료 조건
    if shape == "=":
        print("[", answer, "]")
        break
    
    if shape == "+":
        pass
    elif shape == "-":
        pass
    elif shape == "*":
        pass
    elif shape == "/":
        pass
    elif shape == "%":
        pass
    elif shape == "AC":
        pass


