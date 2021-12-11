




var=0
func=0

def isDelimeter(a):
    if (a == ' ' or a == '+' or a == '-' or a == '*' or a == '/' or a == '%' or a == ',' or a == ';' or a == '=' or a == '<' or a == '>' or a == '(' or a == ')' or a == '{' or a == '}' or a == '[' or a == ']'):
        return True
    return False

def validIdentifier(str):
    if (str[0] == '0' or str[0] == '1' or str[0] == '2' or str[0] == '3' or str[0] == '4' or str[0] == '5' or str[
        0] == '6' or str[0] == '7' or str[0] == '8' or str[0] == '9' or isDelimeter(str[0]) == True):
        return False
    return True


f = open("input.txt", "r")



comment=list()


def parse(str):
    global var
    global func
    token = list()
    left = 0
    right = 0
    strlen = len(str) - 1

    while (right <= strlen and left <= right):
        # print(str[right],end=" ")
        if (isDelimeter(str[right]) == False):
            #print(str[right])
            right += 1
            continue

        if (isDelimeter(str[right]) == True and left == right):
            if str[right]=='(' or str[right]==')':
                token.append(str[right])
                right+=1
                left=right
            else:
                right += 1
                left = right

        elif (isDelimeter(str[right]) == True and left != right or (right == strlen and left != right)):

            subStr = str[left:right]
            token.append(subStr)
            left = right
    #print(token)
    if len(token)!=0:
        if token[0]=="int" or token[0]=='char' or token[0]=="float" or token[0]=="double":
            for i in range(1,len(token)):
                if not isDelimeter(token[i][0]):
                    var+=1
                if token [i]=="(":
                    var-=1
                    func+=1

for x in f:
    parse(x)
print(var)
print(func)












"""
/*This code was
written using python*/
//sample program
#include<iostrem>
using namespace std;

int main(){
	//single line 2
	//single line 3

/*Multiline example 2*/
/*Multiline example 3 and
last comment in this sample program*/
}



comm=0
multi=False
f = open("input.txt", "r")

for x in f:
    for i in range(len(x)):
        if x[i]!=' ':
            if(x[i]=='/' and x[i+1]=='/'):
                comm+=1
                #print(comm)
                #print(comm,x)
                break
            elif (x[i]=='/' and x[i+1]=='*'):
                multi=True
                #print(comm,multi,x)
                break
    l=len(x)
    if multi==True and x[l-3]=='*' and x[l-2]=='/':
        comm+=1
        #print(comm)
        #print(comm,multi,x)
        multi=False

print(comm)

"""













print("ph")
import re


inp=list()
#def tokenize(file):
f = open("input.txt", 'r')


operators = {'+': 'Additon Operator', '-': 'Substraction Operator', '/': 'Division Operator', '*':
    'Multiplication Operator', '++': 'increment Operator', '--': 'Decrement Operator'}
optr_keys = operators.keys()
comments = {r'//': 'Single Line Comment', r'/*': 'Multiline Comment Start', r'*/': 'Multiline Comment End', ' / ** / ' : 'Empty Multiline comment'}
comment_keys = comments.keys()
header = {'.h': 'header file'}
header_keys = header.keys()
sp_header_files = {'stdio.h': 'Standard Input Output Header', 'stdlib.h': 'Standard Library Header'}
datatype = {'int': 'Integer', 'float': 'Floating Point', 'char': 'Character', 'void': 'Void'}
datatype_keys = datatype.keys()
keyword = {'return': 'Return', 'case': 'Case', 'break': 'Break', 'switch': 'Switch', 'begin': 'Begin keyword', 'end' : 'End keyword'}
keyword_keys = keyword.keys()
delimiter = {';': 'Semicolon'}
delimiter_keys = delimiter.keys()
blocks = {'{': 'Curly Brace Open', '}': 'Curly Brace Closed', '(': 'Open Parenthesis', ')': 'Close Paranthesis'}
block_keys = blocks.keys()
builtin_functions = {'printf': 'printf', 'main': 'Main function', 'scanf': 'scanf'}
non_identifiers = ['_', '`', '~', '!', '@', '#', '$', '%', '^', '&', '|', '"', '{' , '}', '[', ']', '<', '>', '?', '/', ',', '=', '\'', ':']
relational_operators = {'==': 'Relational Equals to', '<=': 'Less than or equal to', '>=': 'Greater than or equal to', '!=': 'Not Equal to'}
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
insert_space = re.compile(r"([(<,+\-*=/%;:>)])")
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
    line = insert_space.sub(" \\1 ", line)
    line = re.sub(r'\t', '', line)
    tokens = line.split(' ')
    tokens = [x for x in tokens if x]
    print(tokens)
    for token in tokens:
        token = token.strip('')
        if token == '':
            continue
        if token in builtin_functions.keys():
            if (token == 'printf'):
                inp.append('t')
            elif (token == 'main'):
                inp.append('e')
            print(token, ":", builtin_functions[token])
        elif token in block_keys:
            if (token == '('):
                inp.append('f')
            elif (token == ')'):
                inp.append('g')

            print(token, ":", blocks[token])
        elif token in optr_keys:
            print(tokens.index(token))
            print(token, ":", operators[token])
            inp.append('m')

        # elif token in comment_keys:
        # print("Comment Type: ", comments[token])

        elif '.h' in token:
            print(token, ":", sp_header_files[token])
        elif token in non_identifiers:

            if (token == '=' and tokens[tokens.index(token) + 1] == '='):
                print((token + "="), ":", relational_operators[token + "="])
                tokens.pop(tokens.index(token) + 1)
                token += "="
                inp.append('o')
            elif (token == '='):
                inp.append('k')
                print(token, ":", "Assignment operator")
            elif (token == ','):
                inp.append('i')
                print(token, ":", "comma operator")

            elif (token == '<' and tokens[tokens.index(token) + 1] == '='):
                print((token + "="), ":", relational_operators[token + "="])
                tokens.pop(tokens.index(token) + 1)
                token += "="
                inp.append('o')
            elif (token == '<'):
                inp.append('o')
                print(token, ":", "less than")

            elif (token == '>' and tokens[tokens.index(token) + 1] == '='):
                print((token + "="), ":", relational_operators[token + "="])
                tokens.pop(tokens.index(token) + 1)
                token += "="
                inp.append('o')
            elif (token == '>'):
                inp.append('o')
                print(token, ":", "greater than")
            elif (token == '\''):
                inp.append('u')

                print(token, ":", "single Quote")
            elif (token == ':'):
                inp.append('v')
                print(token, ":", "colon")
            elif (token == '!' and tokens[tokens.index(token) + 1] == '='):
                print((token + "="), ":", relational_operators[token + "="])
                tokens.pop(tokens.index(token) + 1)
                token += "="
                inp.append('o')

            elif (token == '!'):
                inp.append('m')
                print(token, ":", "not operator")

            else:
                inp.append('m')
                print(token, ":", "special symbol")
        elif token in delimiter:
            inp.append('h')
            print(token, ":", delimiter[token])
        elif token in datatype_keys:
            inp.append('a')
            print(token, ":", datatype[token])
            token = "datatype"
        elif token in keyword_keys:
            if (token == 'return'):
                inp.append('p')
            elif (token == 'switch'):
                inp.append('n')
            elif (token == 'begin'):
                inp.append('b')
            elif (token == 'end'):
                inp.append('d')
            elif (token == 'case'):
                inp.append('q')
            elif (token == 'break'):
                inp.append('s')
            elif (token == 'printf'):
                inp.append('t')
                print(keyword[token])
                token = "keyword"
        elif token in numerals:
            inp.append('l')
            print(token, ": Numeric Value")
            token = "num"

        elif (token not in non_identifiers) and ('()' not in token):
            inp.append('j')
            print(token, ": Identifier")
            token = "id"

        token_list.append(token)
    dataFlag = False
    inp.append('c')
    print()
print(token_list)
print("Done with LEXICAL ANALYSIS")
print(inp)
print()
f.close()