import time
num = 0
round = 1

while True:
    if round <= 20:
        if num == 0:
            print(round, num, "OFF")
            num = 1
        elif num == 1:
            print(round, num, "ON")
            num = 0
        time.sleep(1)  # sleep for 1 second
    else:
        break
    round = round + 1
