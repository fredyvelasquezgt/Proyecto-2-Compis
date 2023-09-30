
from yaplWalker import yaplWalker

error = 0
def checkInferenceRule(operator, a, aType, b, bType):
    if aType == "INT" and bType == "INT":
        pass
    elif (aType == "INT" and bType == "STRING") or (aType == "STRING" and bType == "INT"):
        if operator == "+" or operator == "-" or operator == "/":
            error += 1
    elif aType == "STRING" and bType == "STRING":
        if operator == "-" or operator == "*" or operator == "/":
            error += 1
    elif (aType == "INT" and bType == "TRUE") or (aType == "INT" and bType == "FALSE") or (aType == "STRING" and bType == "TRUE") or (aType == "STRING" and bType == "FALSE"):
        error += 1
    elif (aType == "TRUE" and bType == "TRUE") or (aType == "TRUE" and bType == "FALSE") or (aType == "FALSE" and bType == "TRUE") or (aType == "FALSE" and bType == "FALSE"):
        error += 1

