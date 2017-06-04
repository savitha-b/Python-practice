import time
import webbrowser

breaks = 3
breakcount = 0

print("This Program started on" +time.ctime())
while(breakcount<breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=qno1qzek-hw")
    breakcount = breakcount+1
