#myNumber.py

import random

#숫자 선택
computer_number = random.randint(1,100)

def is_same(target, number):
    if target == number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"
    return result

#게임시작
print("Hi\n I choose a number between 1 and 100.")

#유저의 숫자를 받음
guess = int(input("숫자를 쓰고 엔터 키를 누르세요."))

#함수 is_same()를 사용
higher_or_lower = is_same(computer_number, guess)

#답이 맞을 때 까지 계속 유지
while higher_or_lower !="Win":
    if higher_or_lower == "Low":
        guess = int(input("Higher than that. Think again."))
    else:
        guess = int(input("Lower than that. Think again."))

    higher_or_lower = is_same(computer_number, guess)
    
#게임 
input("Correct!\nGood job\n\n\nPress enter to finsh.")


