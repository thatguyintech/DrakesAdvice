from drake import *

song = input()

text_file = open("drake/" + song, "r")
lines = text_file.read().split("\n")

for line in lines:
    if line == '':
        del lines[lines.index(line)]
        
def empty_line(x):
    return x == ''

span = 2
lines2 = ["\n".join(lines[i:i+span]) for i in range(0, len(lines), span)]
