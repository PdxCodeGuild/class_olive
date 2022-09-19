from distutils.util import change_root


# LAB 6 MAKE CHANGE 
# Muki

# making some stuff to support

inp = input('enter an amount to make change for or "q to quit":\t')
coins = {
    'half-dollar': .50,
    'quarter': .25,
    'dime': .10,
    'nickle': .05,
    'penny': .01,
    
}
# inp = float(inp)
# # input = 100 * inp
# output_q = inp // coins['quarter']
# output_d = (inp - (output_q * 0.25)) // coins['dime']    
# q_d = (output_q * 0.25) + (output_d * 0.10)
# output_n = (inp - q_d) // coins['nickle']
# q_d_n = q_d + output_n
# output_p = (inp - q_d_n) // coins['penny']

# print(inp)
# print(output_q)
# print(output_d)
# print(output_n)
# print(output_p)


def make_change(input_value, coins):
    input_value = float(input_value)
    # print(input_value)
    output_h = input_value // coins['half-dollar']
    # print(f' output_h {output_h}')
    output_q = (input_value - (output_h * 0.50)) // coins['quarter']
    # print(f' output_q {output_q}')
    h_q = (output_h * 0.50) + (output_q * 0.25)
    # print(f' h_q {h_q}')
    output_d = (input_value - (h_q)) // coins['dime']
    # print(f' output_d {output_d}')    
    h_q_d = (output_q * 0.25) + (output_d * 0.10) + (output_h * 0.50)
    # print(f' hqd {h_q_d}')
    output_n = (input_value - h_q_d) // coins['nickle']
    # print(input_value - h_q_d)
    h_q_d_n = h_q_d + (output_n * 0.05)
    # print(f' hqdn {h_q_d_n}')
    output_p = int((input_value - h_q_d_n) / coins['penny'])
    # print(output_n)
    result = f'Your change is:\n{output_h} half-dollars\n{output_q} quarters,\n{output_d} dimes,\n{output_n} nickles,\n{output_p} pennies.\nTotalling ${input_value}'
    return result



while True:
    if inp == "q":
        break
    elif inp !="q":
        print(make_change(inp, coins))
        break
