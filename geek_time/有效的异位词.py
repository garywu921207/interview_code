def is_anagram(s, t):
    d1, d2 = {}, {}
    for item in s:
        d1[item] = d1.get(item, 0) + 1
    for item in t:
        d2[item] = d2.get(item, 0) + 1
    return d1 == d2

if __name__ == '__main__':
    s = 'var'
    t = 'ragv'
    print(is_anagram(s, t))
