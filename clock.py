import time
from win10toast import ToastNotifier
import pipreqs

timer = int(input("How many hours from now do you want a notification: "))
start = time.time
toaster = ToastNotifier()

timer2 = timer * 60
while timer2 != 0:
    timer2 -= 1
    print(timer2)
    time.sleep(2)
else:
    toaster.show_toast("Timer Notification", "Its over!!!")
