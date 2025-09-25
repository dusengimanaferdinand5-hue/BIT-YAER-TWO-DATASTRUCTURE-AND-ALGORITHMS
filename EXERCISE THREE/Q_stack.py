# In Irembo, push ["Fill Name", "Fill Address", "Confirm"]. 
irembo_stack = []
print("Irembo Steps Tracker Initialized")
def irembo_steps(items):
    irembo_stack.append(items)
    return f"irembo_steps: {irembo_stack}"
irembo_steps("Fill Name")
irembo_steps("Fill Address")
irembo_steps("Confirm")
print(f"irembo_steps in stack: {irembo_stack} \n")

# Pop last. 
def irembo_stack_pop():
    if irembo_stack:
        removed = irembo_stack.pop()
        print(f" the undone item is: {removed}")
        return f"Removed from irembo_steps the last item: {removed}"
    else:
        return "irembo_steps stack is empty, nothing to pop."

print(irembo_stack_pop())
print(f"irembo_steps after removing the last item: {irembo_stack} \n")

# UR student pushes ["Math", "English", "ICT"]. 
ur_stack = []
print("UR Steps Tracker Initialized")
def ur_steps(items):
    ur_stack.append(items)
    return f"UR_steps: {ur_stack}"
ur_steps("Math")
ur_steps("English")
ur_steps("ICT")
print(f"UR_steps in stack: {ur_stack} \n")

#  Which is top now?
def ur_stack_top():
    if ur_stack:
        top_item = ur_stack[-1]
        print("The top item in UR steps")
        return f"The top item in UR_steps stack is: {top_item}"
    else:
        return "UR_steps stack is empty."

print(ur_stack_top())


# Challenge: Reverse "QUEUE" using stack.
print('\n Challenge: Reverse "QUEUE" using stack. \n')
def reverse_string_using_stack(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
reversed_result = reverse_string_using_stack("QUEUE")
print(f'Reversed "QUEUE": {reversed_result} \n')

