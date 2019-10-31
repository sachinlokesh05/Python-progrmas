from DataStructure.BalancedParathesis.balanced_Parathensise import BalancedParenthesis

g_expression = list(input("Enter string : "))  # Convert the expression into a
# list of characters
b=BalancedParenthesis()
b.balanced_method(g_expression)