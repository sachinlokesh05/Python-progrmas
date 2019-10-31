# 3. Simple Balanced Parentheses

class BalancedParenthesis:

    def balanced_method(self,f_expression):
        parentheses_stack = []
        if len(f_expression) > 0:
            for iterating_element in range(0, len(f_expression)):
                # If you find "(" push it onto the stack
                if f_expression[iterating_element] == '(':
                    parentheses_stack.append(f_expression[iterating_element])

                elif f_expression[iterating_element] == '{':
                    parentheses_stack.append(f_expression[iterating_element])

                elif f_expression[iterating_element] == '[':
                    parentheses_stack.append(f_expression[iterating_element])

                # if you find ")" then pop "(" from stack
                elif f_expression[iterating_element] == ")" :
                    try:
                        parentheses_stack.remove("(")
                    except:
                        print("( is missing")

                elif  f_expression[iterating_element] == "}":
                    try:
                        parentheses_stack.remove("{")
                    except:
                        print("{ is missing")

                elif f_expression[iterating_element] == "]":
                    try:
                        parentheses_stack.remove("[")
                    except:
                        print("[ is missing")

            if parentheses_stack == []:  # if stack is empty
                print("Expression is balanced")
            else:
                print("Expression is unbalanced")
            return
        else:
            print("Invalid input")


