'''
This program calculates voltage, current, and resistance for a circuit.
'''
import json

class Circuit:
    def __init__(self, voltage={'?':'?'}, resistance={'?':'?'}, current={'?':'?'}):
        self.voltage = {'Voltage':voltage}
        self.resistance = {'Resistance':resistance}
        self.current = {'Current':current}

    def print_circuit(self):
        for key, value in self.items():
            print('--', key, '--')
            # Again iterate over the nested dictionary
            for subject, score in value.items():
                print(subject, ' : ', score)

    def add_to_resistance(self):
        self.resistance['Resistance'] = {'Rt':resistance_total}
        rs = 1
        rp = 1
        for value in resistance_series:
            self.resistance['Resistance']['Rs'+str(rs)] = value
            rs += 1
        for value in resistance_parallel:
            self.resistance['Resistance']['Rp'+str(rp)] = value
            rp += 1


def print_circuit(input_dict):
    for key, value in input_dict.items():
        print('--', key, '--')
        # Again iterate over the nested dictionary
        for subject, score in value.items():
            print(subject, ' : ', score)


circuit_1 = Circuit()
print(f'''
    Circuit 1
    Voltage = {circuit_1.voltage}
    Total resistance = {circuit_1.resistance}
    Current = {circuit_1.current}''')


voltage = int(input('Enter Voltage.\n>: '))

resistance_series_str = input('Enter ohms of each resistor IN SERIES separated by a ","\n>: ')
resistance_series = resistance_series_str.split(',')
resistance_series = [int(i) for i in resistance_series]

resistance_parallel_str = input('Enter ohms of each resistor IN PARALLEL separated by a ","\n>: ')
resistance_parallel = resistance_parallel_str.split(',')
resistance_parallel = [int(i) for i in resistance_parallel]

# print(resistance_series, resistance_parallel)


resistance_parallel_total = 0
if 0 not in resistance_parallel:
    for ohms in resistance_parallel:
        resistance_parallel_total += 1/ohms
    resistance_parallel_total = 1/resistance_parallel_total


resistance_total = round(sum(resistance_series) + resistance_parallel_total, 7)

circuit_1.add_to_resistance()


print_circuit(circuit_1.voltage)
print_circuit(circuit_1.resistance)
print_circuit(circuit_1.current)