print("ph")
import re

operators=['+','-','*','/','++','--']
comments=[r'//',r'/*',r'*/','/**/']
headers=['#']
dataType=['int','float','double','char','void']
keyword=['return','case','for','while','do','if','else']
delimiter=[';']
blocks=['(',')','{','}']
buildFunction=['scanf','printf','main']
non_identifiers = ['_', '`', '~', '!', '@', '#', '$', '%', '^', '&', '|', '"', '{' , '}', '[', ']', '<', '>', '?', '/', ',', '=', '\'', ':']
relationalOp=['==','<=','>=''!=']
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
insert_space = re.compile(r"([(<,+\-*=/%;:>)])")

f=open("input.txt")
i = f.read()
dataFlag = False
token_list = []
count = 0
flag1 = flag2 = flag3 = 0
program = i.split('\n')
print("LEXICAL ANALYSIS:")
print()

for line in program:
    if line == '':
        continue
    count += 1
    print("Line #" + str(count))
    print("Line :", line)





