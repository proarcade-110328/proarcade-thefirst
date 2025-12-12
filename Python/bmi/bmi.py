print("BMI 계산기입니다.")
while True:
    height = input("당신의 키는 얼마인가요? cm 단위로 입력해주세요.")
    try:
        height = float(height)
        weight = input("당신의 몸무게는 얼마인가요? kg 단위로 입력해주세요.")
        try:
            weight = float(weight)
        except ValueError:
            print("숫자가 아닙니다!")
        bmi = weight / ((height / 100) * (height / 100))
        print(f"당신의 BMI: {bmi}")
        if bmi <= 18.5:
            print("저체중입니다.")
        elif 18.5 < bmi <= 25:
            print("정상체중입니다.")
        elif 25 < bmi <= 30:
            print("과체중입니다.")
        else:
            print("비만입니다.")
    except ValueError:
        print("숫자가 아닙니다!")