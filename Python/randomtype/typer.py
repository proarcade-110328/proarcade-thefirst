import random
import time
with open("ransentence.txt", "r", encoding = "UTF-8") as f:
    sentences = f.read().splitlines()
while True:
    ransen = random.choice(sentences)
    print (ransen)
    start_perf = time.perf_counter()
    answer = input("아까 뜬 문장을 입력해주세요.")
    if answer.strip() == ransen.strip():
        end_perf = time.perf_counter()
        total_time = end_perf - start_perf
        print(f"타자 시간: {total_time}초.")
        break
    else:
        print("잘못된 입력입니다.")
        continue