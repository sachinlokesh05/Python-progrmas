import re
from datetime import date


class Regex:
    def __init__(self):
        pass

    def regex(self, data,first_name,full_name,phone_number):
        # Replace name at every position by user_name
        replace_name = re.sub('<<name>>',first_name, data)
        replace_f_name = re.sub('<<.*name>>', full_name, replace_name)

        # Replace xxxxxxxxx with contact number
        replace_num = re.sub("\w*x",phone_number, replace_f_name)

        # Get current date
        today = date.today().strftime("%d/%m/%Y")
        replace_date = re.sub("\w+(\/)\w+(\/)\w+", today, replace_num)
        return replace_date


obj = Regex()
f=open("File.txt","r+")
data=f.read()
try:
    user_name = input("enter the first name :")
    Full_name = input("enter the full name : ")
except:
    print("pls enter the correct name")
    print("ex:user_name=sachin \n Full_name=sachin lokesh")
try:
    phone_number = int(input("enter the phone number"))
except:
    print("pls enter the correct phone number")
    print("ex: phone_number=89869xxxxx")

else:
    print("ORIGINAL DATA :\n", data)

    result = obj.regex(data,user_name,Full_name,str(phone_number))

g=open("File.txt","w+")
g.write(result)
print("RESULT : \n", result)
