from Linkedlist_Utility.Linkedlist_Utility import Singlelinkedlist

sl=Singlelinkedlist()

class Calender:
    #see if the year is leapyear or not
    def leapyear(self,year):
        if len(year)==4:
            if int(year)%400==0:
                if int(year)%100==0:
                    if int(year)%4==0:
                        return True
                    else:
                        return  False
                else:
                    return True
            else:
                return False
        else:
            print("invalid year")

    #see the number of days in the given month
    def month_days(self,month,year):
        if month=="January" or "March" or " May" or "July" or "August" or "Octomber" or  "December":
            Number_of_days=31
        elif month=="April" or "June" or " September" or "November":
            Number_of_days=30
        elif month=="February":
            if obj.leapyear(year):
                Number_of_days=29
            else:
                Number_of_days=28
        return  Number_of_days

    #Find the which in the 1st of tha month
    def Week_day(self,month,year):
        year1=year-((14-month)//12)
        x=year1+(year1//400)+(year1//4)-(year1//100)
        month1=month+12*((14-month)//12)-2
        day1=(1+x+(31*month1)//12)%7
        return day1

    #convert the month into corresponding interger value
    def month_int(self,month):
        if month=="January":
            return 1
        elif month=="February":
            return 2
        elif month=="March":
            return 3
        elif month=="April":
            return 4
        elif month=="May":
            return 5
        elif month=="June":
            return 6
        elif month=="July":
            return 7
        elif month=="August":
            return 8
        elif month=="September":
            return 9
        elif month=="Octomber":
            return 10
        elif month=="November":
            return 11
        elif month=="December":
            return 12

obj=Calender()
week=["mon","tue","wed","thurs","fri","sat","sun"]
try:
    month=input("enter the month : ")
    year=int(input("enter the year : "))
except:
    print("enter the valid month and year")
    print("ex: 2019 April")

number_of_days=obj.month_days(month,year)
print("number of days ",str(number_of_days),"in the month of ",month,"bcoz the year is ",str(year))
month_i=obj.month_int(month)
day=obj.Week_day(month_i,year)
print("day is",week[day])

Calender_row=[]

print("mon","tue","wed","thurs","fri","sat","sun")

for month_day in range(1,number_of_days):
    for i in range(day):
        Calender_row.append(" ")

    if month_day%7==0:
        sl.add(month_day)
    else:
        sl.add(month_day)


sl.display()




