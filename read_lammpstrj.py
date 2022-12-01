import numpy as np
import matplotlib.pyplot as plt

input_file=input("please the name of file:")
lines=[]
with open(input_file,'r') as f1:
    num_atom=f1.readline()
    f1.seek(0,0)
    for i in range(17500):
        line=f1.readline()
        lines.append(line)
print(lines)
