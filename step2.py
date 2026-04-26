import time
end_time = time.time() + 5  # set timer for 5 seconds

while True:
    # calculate remaining time and print it
    remain = int(end_time - time.time() + 1)
    print(remain)
    # if remaining time is less than or equal to 1 second, break the loop
    if remain <= 1:
        break
    # wait for 1 second before the next update
    time.sleep(1)
print("Timer over!!!")