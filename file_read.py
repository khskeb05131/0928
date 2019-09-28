import sys

filereader = open("sample.txt",'r')

for row in filereader:
    print(row.strip())

filereader.close()
