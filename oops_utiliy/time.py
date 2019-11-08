from _datetime import datetime
class Timenow:
    def time(self):
        now = datetime.now()
        return now.strftime("%x %X %p")

a = Timenow()
if __name__=="__main__":
    print(a.time())