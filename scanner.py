from hashTable import HashTable
import re
import sys

reservedWords = ["if","while","for","and","or","not","char","int","float","string","else","read","real",
                 "length","getInput","end","break","main","const","do","sum","div","return"]
operands = [":=","+", "-", "*", "/", "=","%","!=",">",">=","<","<=","\\\\","[","]","(",")","{","}",
            ",",".","!",":","!!"]

'''def checkConstantOrIdentifier(token):
    try:
        int(token)
    except: #first condition: beginning of token, second conditon: strings with double quotes
        return re.match("^[A-Z0-9\"_']", token) is None or re.match('^"[a-zA-Z0-9]+"$', token) is not None
    return True'''

def checkIntOrReal(token):
    if token[0] == '0' and len(token) > 1:
        return False
    try:
        int(token)
        return True
    except ValueError:
        try:
            float(token)
            return True
        except ValueError:
            return False


def checkCharOrString(token):
    return re.match("^'[a-zA-Z0-9*()!@_-{}]?'$",token) is not None \
           or re.match("^\"[a-zA-Z0-9*()!@_-{}]+\"$",token) is not None

def checkBool(token):
    if token in ['True','False']:
        return True
    return False

def checkTypeOfConstant(token):
    return checkIntOrReal(token) or checkCharOrString(token) or checkBool(token)

def checkIdentifier(token):
    return re.match("^[0-9A-Z\"']", token) is None

def splitInTokens(line):
    delm = '|'.join(map(re.escape, operands))

    return re.split('(' + delm + '|^"[a-zA-Z0-9*()!@_\-{}]*"$' + "|^'[a-zA-Z0-9*()!@_\-{}]*'$" +
                    '|[^"\'a-zA-Z0-9.]' + ')', line)

symboltable = HashTable()
pif={}

if len(sys.argv) != 2:
    raise Exception("Wrong parameter count")

filename = sys.argv[1]

with open(filename) as file:
    lineCount = 1
    line = file.readline()
    while line:
        splitLine = splitInTokens(line)
        splitLine = list(filter(lambda x: x is not None and x != '', map(lambda x: x.strip(), splitLine)))
        print(splitLine)

        for token in splitLine:
            if token in reservedWords or token in operands:
                pif[token] = -1
            elif checkTypeOfConstant(token) or checkIdentifier(token):
                i = symboltable.add(token)
                pif[token] = i
            else:
                raise Exception("Lexical error on line {}; Invalid token '{}'".format(lineCount, token))

        line = file.readline()
        lineCount += 1

    print("\n" + str(symboltable))
    print(str(pif) + "\n")
    print("Valid")




