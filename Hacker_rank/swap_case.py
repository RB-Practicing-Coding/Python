# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    result = ''
    for c in s:
        if c.islower():
            c = c.upper()
        else:
            c = c.lower()
        result += c
    return result

if __name__ == '__main__':
    s = 'Www.HackerRank.com'
    result = swap_case(s)
    print(result)