import time 
#import time module to use sleep function
sec = 5
#can use any loop to implement the timer
while sec > 0:
    #prints the remaining seconds
    print(sec)
    #waits for 1 second
    time.sleep(1) 
    #decrements the seconds by 1
    sec -= 1
#prints the message when the timer is over after completely exiting the loop
print("Timer over!!!")