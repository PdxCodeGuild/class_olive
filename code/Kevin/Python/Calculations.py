'''
This program calculates voltage, current, and resistance for a circuit.
'''

class Circuit:
    def __init__(self, voltage={'?':'?'}, resistance={'?':'?'}, current={'?':'?'}):
        self.voltage = {'Voltage':voltage}
        self.resistance = {'Resistance':resistance}
        self.current = {'Current':current}

    def add_to_resistance(self, resistance_total, resistance_series, resistance_parallel):
        self.resistance['Resistance'] = {'Rt':resistance_total}
        rs = 1
        rp = 1
        for value in resistance_series:
            self.resistance['Resistance']['Rs'+str(rs)] = value
            rs += 1
        for value in resistance_parallel:
            self.resistance['Resistance']['Rp'+str(rp)] = value
            rp += 1

    def add_to_voltage(self, voltage, current, resistance_series, resistance_parallel):
        self.voltage['Voltage'] = {'Vt': voltage}
        vp_value = 0
        vs = 1
        vp = 1
        for ohms in resistance_series:
            self.voltage['Voltage']['Vs'+str(vs)] = (ohms * current)
            vp_value += ohms * current
            vs += 1
        vp_value = round(voltage - vp_value, 8)
        for ohms in resistance_parallel:
            self.voltage['Voltage']['Vp'+str(vp)] = vp_value
            vp += 1
        return vp_value

    def add_to_current(self, current, resistance_series, resistance_parallel, voltage_parallel):
        self.current['Current'] = {'S1':(1000 * current)}
        cs = 1
        cp = 1
        for ohms in resistance_parallel:
            if ohms == 0:
                break
            self.current['Current']['Cp'+str(cp)] = 1000 * round(voltage_parallel / ohms, 8)
            cp += 1



def print_circuit(input_dict):
    for key, value in input_dict.items():
        print('--', key, '--')
        for nested_key, nested_value in value.items():
            print(nested_key, ' : ', nested_value)


circuit_1 = Circuit()
# print(f'''
#     Circuit 1
#     Voltage = {circuit_1.voltage}
#     Total resistance = {circuit_1.resistance}
#     Current = {circuit_1.current}''')

def circuit_builder(voltage_int, resistance_series_str, resistance_parallel_str):

    voltage = voltage_int
    resistance_series = resistance_series_str.split(',')
    resistance_series = [int(i) for i in resistance_series]

    
    resistance_parallel = resistance_parallel_str.split(',')
    resistance_parallel = [int(i) for i in resistance_parallel]



    resistance_parallel_total = 0
    if 0 not in resistance_parallel:
        for ohms in resistance_parallel:
            resistance_parallel_total += 1/ohms
        resistance_parallel_total = 1/resistance_parallel_total

    resistance_total = round(sum(resistance_series) + resistance_parallel_total, 8)

    current = round(voltage / resistance_total, 8)

    circuit_1.add_to_resistance(resistance_total, resistance_series, resistance_parallel)
    voltage_parallel = circuit_1.add_to_voltage(voltage, current, resistance_series, resistance_parallel)
    circuit_1.add_to_current(current, resistance_series, resistance_parallel, voltage_parallel)
    # print(voltage_parallel)

    return circuit_1




# circuit_builder(10,'300,850','600,450')
# print_circuit(circuit_1.voltage)
# print_circuit(circuit_1.resistance)
# print_circuit(circuit_1.current)