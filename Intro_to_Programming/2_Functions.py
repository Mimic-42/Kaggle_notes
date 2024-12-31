# Intro to functions: a simple example

def add_three(input_var):
    output_var = input_var + 3
    return output_var

new_output = add_three(10)

print(new_output)

print(add_three(11))

# ----------------------------------------------------------------------------
# A more complex example

def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1-0.12)
    return pay_aftertax

pay_fulltime = get_pay(60)
print(pay_fulltime)

# ------------------------------------------------------------------------------
# Functions with multiple arguments

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After_tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

higher_pay_aftertax = get_pay_with_more_inputs(20, 100, 0.4)
print(higher_pay_aftertax)

