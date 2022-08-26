# Read from a CSV
with open('input.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)


dummy_data = 'name,age,city\nsara,33,portland\nbob,99,tampa'

# Write to different csv
with open('output.csv', 'w') as file:
        file.write(dummy_data)