
var = 0
def TotalVariable():

    #func = 0

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

    comment = list()

    def parse(str):
        global var
        #global func
        token = list()
        left = 0
        right = 0
        strlen = len(str) - 1

        while (right <= strlen and left <= right):
            # print(str[right],end=" ")
            if (isDelimeter(str[right]) == False):
                # print(str[right])
                right += 1
                continue

            if (isDelimeter(str[right]) == True and left == right):
                if str[right] == '(' or str[right] == ')':
                    token.append(str[right])
                    right += 1
                    left = right
                else:
                    right += 1
                    left = right

            elif (isDelimeter(str[right]) == True and left != right or (right == strlen and left != right)):

                subStr = str[left:right]
                token.append(subStr)
                left = right
        # print(token)
        if len(token) != 0:
            if token[0] == "int" or token[0] == 'char' or token[0] == "float" or token[0] == "double":
                for i in range(1, len(token)):
                    if not isDelimeter(token[i][0]):
                        var += 1
                    if token[i] == "(":
                        var -= 1
                        #func += 1

    for x in f:
        parse(x)
    print("Number of Variable: ",var)
    f.close()
    #print(func)


def TotalComment():
    comm = 0
    multi = False
    f = open("input.txt", "r")

    for x in f:
        for i in range(len(x)):
            if x[i] != ' ':
                if (x[i] == '/' and x[i + 1] == '/'):
                    comm += 1
                    # print(comm)
                    # print(comm,x)
                    break
                elif (x[i] == '/' and x[i + 1] == '*'):
                    multi = True
                    # print(comm,multi,x)
                    break
        l = len(x)
        if multi == True and x[l - 3] == '*' and x[l - 2] == '/':
            comm += 1
            # print(comm)
            # print(comm,multi,x)
            multi = False
    f.close()
    print("Number of comment: ",comm)



print("1.Number of Comment.")
print("2.Number of Variable.")
print("3.Exit.")
print("Enter Choice: ",end="")
ch=input()

if ch=='1':
    TotalComment()
elif ch=='2':
    TotalVariable()
elif ch=='3':
    exit()