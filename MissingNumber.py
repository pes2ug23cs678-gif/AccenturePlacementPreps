#Finding the missing number
def CheckMissing(string, n):
    for i in range(1, n):
        if str(i) not in string:
            return i #This is the case of success over here
    return -1 #This is the case of failure in this case
def giveMeProgram(g, Output):
    for i in g:
        Output.append(int(i))
    return Output
def giveMeMax(Output, Max):
    for i in range(1, len(Output), 1):
        if Max < Output[i]:
            Max = Output[i]
    return Max
def main():
    string = "1 2 3 4 5 7 8 9"
    g = string.strip().split()
    Output = giveMeProgram(g, [])
    n = giveMeMax(Output, Output[0])
    print(f"The missing number over here is = {CheckMissing(g, int(n))}")
if __name__ == "__main__":
    main()
