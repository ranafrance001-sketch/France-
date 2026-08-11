import random
import time

s = "0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ@#$%^&*"

try:
    while True:
        line = "".join(random.choice(s) if random.random() > 0.7 else " " for _ in range(30))
        print(f"\033[32m{line}\033[0m")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nMatrix Stopped!")
