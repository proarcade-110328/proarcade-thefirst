jamsand = 0
hamsand = 0
fruit = 0
juice = 0
price = 0

def jamadd():
    global jamsand
    jamsand += 1
    jam_label.config(text = f"딸기잼 샌드위치: {jamsand}개.")

def hamadd():
    global hamsand
    hamsand += 1
    ham_label.config(text = f"햄 치즈 샌드위치: {hamsand}개.")

def fruitadd():
    global fruit
    fruit += 1
    fruit_label.config(text = f"생과일: {fruit}개.")

def juiceadd():
    global juice
    juice += 1
    juice_label.config(text = f"생과일 주스: {juice}개.")

def pricecalc():
    global price
    price = 1000 * jamsand + 1500 * hamsand + 1500 * fruit + 2000 * juice
    price_label.config(text = f"지불할 돈: {price}원.")

def reset():
    global jamsand, hamsand, fruit, juice, price
    jamsand = 0
    hamsand = 0
    fruit = 0
    juice = 0
    price = 0
    jam_label.config(text = f"딸기잼 샌드위치: {jamsand}개.")
    ham_label.config(text = f"햄 치즈 샌드위치: {hamsand}개.")
    fruit_label.config(text = f"생과일: {fruit}개.")
    juice_label.config(text = f"생과일 주스: {juice}개.")
    price_label.config(text = f"지불할 돈: {price}원.")


import tkinter as tk
window = tk.Tk()
window.title("주문 프로그램")
window.geometry("800x450")

jam_label = tk.Label(window, text = f"딸기잼 샌드위치: {jamsand}개.", font = "Arial, 15")
jam_label.grid(row=0, column=0, padx=10, pady=5)

jambtn = tk.Button(window, text = "딸기잼", command = jamadd)
jambtn.grid(row=0, column=1, padx=10, pady=5)

ham_label = tk.Label(window, text = f"햄 치즈 샌드위치: {hamsand}개.", font = "Arial, 15")
ham_label.grid(row=1, column=0, padx=10, pady=5)

hambtn = tk.Button(window, text = "햄치즈", command = hamadd)
hambtn.grid(row=1, column=1, padx=10, pady=5)

fruit_label = tk.Label(window, text = f"생과일: {fruit}개.", font = "Arial, 15")
fruit_label.grid(row=2, column=0, padx=10, pady=5)

fruitbtn = tk.Button(window, text = "생과일", command = fruitadd)
fruitbtn.grid(row=2, column=1, padx=10, pady=5)

juice_label = tk.Label(window, text = f"생과일 주스: {juice}개.", font = "Arial, 15")
juice_label.grid(row=3, column=0, padx=10, pady=5)

juicebtn = tk.Button(window, text = "주스", command = juiceadd)
juicebtn.grid(row=3, column=1, padx=10, pady=5)

price_label = tk.Label(window, text = "지불할 돈: 0원.", font = "Arial, 15")
price_label.grid(row=4, column=0, padx=10, pady=5)

pricebtn = tk.Button(window, text = "가격", command = pricecalc)
pricebtn.grid(row=4, column=1, padx=10, pady=5)

resetbtn = tk.Button(window, text = "리셋", command = reset)
resetbtn.grid(row=5, column=1, padx=10, pady=5)

window.mainloop()