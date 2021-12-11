
token =list()
comment=list()




def isDelimeter(a):
    if (a == ' ' or a == '+' or a == '-' or a == '*' or a == '/' or a == '%' or a == ',' or a == ';' or a == '=' or a == '<' or a == '>' or a == '(' or a == ')' or a == '{' or a == '}' or a == '[' or a == ']'):
        return True
    return False


def isOperator(a):
    if (a == '+' or a == '-' or a == '*' or a == '/' or a == '%' or a == '=' or a == '<' or a == '>'):
        return True
    return False


def validIdentifier(str):
    if (str[0] == '0' or str[0] == '1' or str[0] == '2' or str[0] == '3' or str[0] == '4' or str[0] == '5' or str[
        0] == '6' or str[0] == '7' or str[0] == '8' or str[0] == '9' or isDelimeter(str[0]) == True):
        return False
    return True


def isKeyword(str):
    keyword = ["auto", "double", "int", "struct", "break", "else", "long", "switch",
               "case", "enum", "register", "typedef", "char", "extern", "return", "union",
               "const", "float", "short", "unsigned", "continue", "for", "signed", "void",
               "default", "goto", "sizeof", "volatile", "do", "if", "static", "while"]

    if str in keyword:
        return True
    return False


def isInteger(str):
    if len(str) == 0:
        return False
    hasDecimal = False
    for i in range(len(str)):
        if (str[i] != '.' and str[i] != '0' and str[i] != '1' and str[i] != '2' and str[i] != '3' and str[i] != '4' and
                str[i] != '5' and str[i] != '6' and str[i] != '7' and str[i] != '8' and str[i] != '9' or (
                        str[i] != '-' and i > 0)):
            return False
        if str[i] == '.':
            hasDecimal = True
    return hasDecimal  # confusioning


# ck=False

def isComment(i, ck):
    t = False
    if ck == False:
        for j in range(len(i)):
            if i[j] != ' ':
                if i[j] == '/':
                    if i[j + 1] == '/':
                        #print(i, "is a comment!")
                        comment.append(i)
                        return True
                    elif i[j + 1] == "*":
                        ck = True
                        l = len(i)
                        if l > 3:
                            if i[l - 3] == '*' and i[l - 2] == '/':
                                print(i[l-2],i[l-1])
                                comment.append(i)
                                #print(i, "is a comment")
                                ck = False
                                t = True
                                break

    if ck == True and len(i) > 1:
        for j in range(len(i)):
            if i[j] == '*' and i[j + 1] == '/':
                print("a multiline comment found!")
                ck = False
                return True
    if t == True:
        return True
    return False


def parse(str):
    left = 0
    right = 0
    strlen = len(str) - 1

    while (right <= strlen and left <= right):
        # print(str[right],end=" ")
        if (isDelimeter(str[right]) == False):
            right += 1
            continue

        if (isDelimeter(str[right]) == True and left == right):
            if (isOperator(str[right]) == True):

                print(str[right], "is an operator")
                token.append(str[right])
                right += 1
                left = right
            else:
                right += 1
                left = right

        elif (isDelimeter(str[right]) == True and left != right or (right == strlen and left != right)):

            subStr = str[left:right]
            token.append(subStr)
            right += 1
            if (isKeyword(subStr) == True): print(subStr, "is a keyword")
            if (isInteger(subStr) == True): print(subStr, "is a integer")
            # elif(isRealNumber(subStr)==True):print(subStr, "is a real number")

            if (validIdentifier(subStr) == True and isDelimeter(str[right - 1]) == False):
                print(subStr, "is a valid identifier")
            if (validIdentifier(subStr) == False and isDelimeter(str[right - 1]) == False):
                print(subStr, "is a not valid identifier")
            left = right


f = open("input.txt", "r")
ckcomment = False
ckheader=False

for x in f:
    if x[0] == '#':
        #pass
        print(x, 'is header file')

    elif isComment(x, ckcomment):
        print(ckcomment)
        #pass
    #if ckcomment != True:
    else:
        #pass
        parse(x)

    # parse(x)
print(token)
print(comment)
















