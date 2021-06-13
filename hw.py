import time
def print_sleep():
    count = 0
    while(1):
        print("Hello:", count)
        count += 1
        time.sleep(1)
print_sleep()
