class Windchill:
    def eff_temp(self):
        t=int(input("enter the temperature in (Fahrenheit:"))
        v=int(input("enter the wind speed in (in miles per hour):"))
        if abs(t)<=50 and (t<=120 or t>=3):
            return 35.74+(0.6125*t)+((0.4275*t-35.75)*(v**0.16))
        else:
            return "enter the value are not correct,plz enter the value correctly"