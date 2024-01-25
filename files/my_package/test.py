def sum_file(a, b, filename='sum.txt'):
    result = a + b
    with open(filename, 'w') as file:
        file.write(str(result)+ '\n')



    