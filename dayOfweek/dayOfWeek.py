class DayOfWeek:

    def Day(self,dd,mm,yy):
        day = ["sunday","monday","tuesday","wednesday","thursday","friday","satay"]
        month = ["","jan","feb","march","april","may","june","july","aug","sep","oct","nov","dec"]
        y = yy-(14-mm)//12
        x = y+y//4-y//100+y//400
        m = mm+12*((14-mm)//12)-2
        d = (dd+x+31*m//12) % 7
        print(day[d],"\n", dd,"/", month[mm],"/", yy)
