def line_max(line):
    length = len(line)
    value_max = 0
    for i in range(length):
        s = ''.join(line)
        value = int(s, 2)
        if i == 0:
            value_max = value
        else:
            if value_max < value:
                value_max = value
    tmp = line.pop()
    line.insert(0 ,tmp)
    return value_max

if __name__ == '__main__':
    N = int(input())
    array = []
    for i in range(N):
        s = input()
        array.append(s)

    ans = 0
    for line in array:
        line = line.split(',')
        ans += line_max(line)
    print(ans)
