my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
max_index = len(my_numbers)
output_file = "number.csv"
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("Output appened to file\n")
