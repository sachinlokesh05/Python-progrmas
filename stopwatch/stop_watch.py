import time as t
class stopwatch:
    x=int(input("enter 1 to start"))
    start=t.time()
    y=int(input("enter 0 to stop"))
    stop=t.time()

    eclapsed_time=stop-start
    print("starting time is:",start)
    print("ending time is :",stop)
    print("total time taken is:",eclapsed_time)

t=stopwatch()

