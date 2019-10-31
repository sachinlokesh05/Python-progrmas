# 5 This program checks if the given string is palindrom or not
class Palindrome:
    def check_Palindrome(self,user_string):
        original_queue = list(user_string)
        check_queue = []
        for iterating_number in range(len(user_string)):
            # Pop the elements from the list into another list
            value = user_string.pop()
            check_queue.append(value)

        print("1--", original_queue)
        print("2--", check_queue)
        # Check if poped list and original list are same or not
        if check_queue == original_queue:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")