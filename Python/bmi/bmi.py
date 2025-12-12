print("BMI 계산기입니다.")
while True:
    try:
        height = input("당신의 키는 얼마인가요? cm 단위로 입력해주세요. ")
        height = float(height)
        if height <= 0:
            print("키가 0보다 작습니다.")
            continue
    except ValueError:
        print("숫자가 아닙니다!")
        continue

    try:
        weight = input("당신의 몸무게는 얼마인가요? kg 단위로 입력해주세요. ")
        weight = float(weight)
        if weight <= 0:
            print("몸무게가 0보다 작습니다.")
            continue
    except ValueError:
        print("숫자가 아닙니다!")
        continue

    bmi = weight / ((height / 100) ** 2)
    print(f"당신의 BMI: {bmi}")

    if bmi <= 18.5:
        print("저체중입니다.")
    elif 18.5 < bmi <= 25:
        print("정상체중입니다.")
    elif 25 < bmi <= 30:
        print("과체중입니다.")
    else:
        print("비만입니다.")