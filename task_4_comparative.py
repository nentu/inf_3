import subprocess
import time

for i in range(1, 4):

    start_time = time.time()
    for _ in range(100):
        subprocess.Popen(["python", f"task_{i}.py"], stdout=None).wait()

    end_time = time.time()
    print(f"100 кратное выполнения программы для {i} задания: {(end_time-start_time)} секунд")
