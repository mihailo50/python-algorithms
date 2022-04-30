# problem 1

# def calPoints(ops) -> int:

#     result = None

#     result = []
#     for i in ops:
#         if i == "+":
#             result.append(result[-1]+result[-2])
#         elif i == "D":
#             result.append(2 * result[-1])
#         elif i == "C":
#             result.pop()
#         else:
#             result.append(int(i))

#     return sum(result)

# if __name__ == '__main__':
#     line = input()
#     ops = line.strip().split()

#     print(calPoints(ops))

# problem 2

def isValid(s: str) -> bool:
    result = None
    if len(s) %2!=0:
        return False

    dict = {'(' : ')', '[' : ']', '{' : '}'}
    result = []
    for i in s:
        if i in dict.keys():
            result.append(i)
        else:
            if result == []:
                return False

    return result

if __name__ == '__main__':
    line = input()
    if isValid(line):
        print('valid')
    else:
        print('Invalid')
