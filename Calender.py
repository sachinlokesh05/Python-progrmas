# class Calendar:
#
#  #See if given year is a leap year or not
#     def leapYear(self, year):
#         if len(year) == 4:
#             if int(year) % 400 == 0:
#                 if int(year) % 100 == 0:
#                     if int(year) % 4 == 0:
#                         return True
#                     else:
#                         return False
#                 else:
#                      return True
#             else:
#                   return False
#         else:
#             return True
#
#  # Find thw number of days in given month
#     def month_day(self,month,year):
#         if month == 'January' or 'March' or 'May' or 'July' or 'August' \
#                 or 'October' or 'December':
#             number_of_days = 31
# #         elif month == "April" or 'June' or 'September' or 'November' :
#             number_of_days = 30
#         elif month == 'February':
#             if obj.leapYear(year) == True:
#                 number_of_days = 29
#             else:
#                 number_of_days = 28
#         return  number_of_days
#
#
# # # Find wich day it is on 1sst of that month
#     def week_day(self, month, year):
#
#         year1 = year - ((14 - month) / 12)
#         x = year1 + (year1/4) - (year1/100) + (year1/400)
#         month1 = month + 12 * ((14 - month) / 12) - 2
#         day1 = (1 + x + (31*month1) / 12) % 7
#         return int(day1)
#
#
# #  # Convert month into coreesponding integer value for calculation
#     def month_int(self,month):
#         if month == 'January':
#             return 1
#         if month == 'February':
#             return 2
#         if month == 'March':
#             return 3
#         if month == 'April':
#             return 4
#         if month == 'May':
#             return 5
#         if month == 'June':
#             return 6
#         if month == 'July':
#             return 7
#         if month == 'August':
#             return 8
#         if month == 'September':
#             return 9
#         if month == 'October':
#             return 10
#         if month == 'November':
#             return 11
#         if month == 'December':
#             return 12
#
#
# week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# obj = Calendar()
# year = int(input("Enter year:"))
# month = input("Enter month : ")
# number_of_days = obj.month_day(month, year)
# print(str(month) + " has " + str(number_of_days) + " number of days" + "coz year is "
#       + str(year))
# month_i = obj.month_int(month)
# day = obj.week_day(month_i, year)
# print("Day is : ", week[day])
#
# calender_row = []
# print('Mon', 'Tue', 'Wed','Thur', 'Fri','Sat','Sun')
#
# for month_day in range(1, number_of_days):
#     # for i in range(day):
#         # calender_row.append(' ')
#         if month_day % 7 == 0:
#             calender_row.append(month_day)
#         else:
#             calender_row.append(month_day)
#
#  # def print(calender_row):
#         if len(calender_row) == 7:
#             print(calender_row)
#             calender_row.clear()
#         else:
#             print(calender_row)
#             calender_row.clear()
#
#
#
# for month_day in range(1, number_of_days):
#     for i in range(day):
#         calender_row.append(' ')
#     if month_day % 7 == 0:
#         calender_row.append(month_day)
#     else:
#         calender_row.append(month_day)
# if len(calender_row) == 7:
#     print(calender_row)
#     calender_row.clear()
# from calendar import Calendar
#
# from DataStructure.Linkedlist_Utility.Linkedlist_Utility import Singlelinkedlist
#
# ll = Singlelinkedlist()
# calender = Calendar()
# year = int(input("Enter year:"))
# month = input("Enter month : ")
# # number_of_days = calender.month_day(month, year)
# print("Days in month are : ")
# for iterating_value in range(1, calender.month_day(month,year)+1):
#     ll.append(iterating_value)
# ll.print()

input_list = [99, 11, 22, 3, 4, 5, 6, 7, 44, 66, 77, 88, 110, 8888]
list1 = [1]
hash_table = {}
for i in range(len(input_list)):
    list1.clear()
    key_v = input_list[i] % 11
    # Divide the number by total number of slots + 1
    # Get the key
    # if input_list[i] not in hash_table.values():

    # print(key_v)
    for j in range(len(input_list)):
            if key_v == input_list[j]%11:
                # See if any other value matches with the key
                if input_list[i] not in list1:
                    # Add it to corresponding slot
                    list1.append(input_list[j])
            else:
                break

    hash_table[key_v] = list1
    # print(hash_table)
    # print(list)
print(hash_table)