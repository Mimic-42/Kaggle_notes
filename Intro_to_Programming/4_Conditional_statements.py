# Conditional statements

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature"
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = 'Fever'
    return message

print(evaluate_temp(38.5))

# -------------------------------------------------

def evalutae_temp_2(temp):
    if(temp>38):
        message='Fever'
    else:
        message="Normal"
    return message

print(evalutae_temp_2(39))

# -------------------------------------------------

def evalutae_temp_3(temp):
    if(temp>38):
        message='Fever'
    elif(temp>35):
        message="Normal"
    else:
        message="Lower"
    return message

print(evalutae_temp_3(35))