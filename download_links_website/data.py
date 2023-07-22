'''data.py'''

import os

def read_file(filename:str) -> list[str]:
    
    data = []
    if not os.path.exists(filename):
        return data

    with open(filename, 'r') as reader:
        for line in reader.readlines():
            line = line.replace('\r\n','\n')
            line = line.replace('\n','')
            data.append(line)
            #print(line,end='\n')

    return data
