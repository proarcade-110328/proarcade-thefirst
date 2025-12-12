# 메인 함수 코딩
def calc():
    try:
        height = float(height_enter.get())
        weight = float(weight_enter.get())
        bmi = weight / ((height / 100) ** 2)
        bmi_label.config(text = f"BMI: {bmi}")

        if bmi <= 18.5:
            bmi_result.config(text = "저체중")
        elif 18.5 < bmi <= 25:
            bmi_result.config(text = "정상 체중")
        elif 25 < bmi <= 30:
            bmi_result.config(text = "과체중")
        else:
            bmi_result.config(text = "비만")
    except ValueError:
        bmi_result.config(text = "숫자만 입력하세요.")


# GUI 코딩
import tkinter as tk
bmiwindow = tk.Tk()
bmiwindow.title("GUI BMI 계산기")
bmiwindow.geometry("450x250")

height_label = tk.Label(bmiwindow, text = "키 (cm 단위)", font = ("Arial, 15"))
height_label.grid(row=0, column=0, padx=10, pady=5)
height_enter = tk.Entry(bmiwindow)
height_enter.grid(row=0, column=1, padx=10, pady=5)

weight_label = tk.Label(bmiwindow, text = "몸무게 (kg 단위)", font = ("Arial, 15"))
weight_label.grid(row=1, column=0, padx=10, pady=5)
weight_enter = tk.Entry(bmiwindow)
weight_enter.grid(row=1, column=1, padx=10, pady=5)

bmi_label = tk.Label(bmiwindow, text = "BMI: ", font = ("Arial, 15"))
bmi_label.grid(row=2, column=0, padx=10, pady=5)
bmi_btn = tk.Button(bmiwindow, text = "계산", command = calc)
bmi_btn.grid(row=2, column=1, padx=10, pady=5)
bmi_result = tk.Label(bmiwindow, text = "", font = ("Arial, 15"))
bmi_result.grid(row=3, column=0, padx=10, pady=5)

bmiwindow.mainloop()