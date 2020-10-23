def repeatedString(s, n):
    a =  set(s)
    le = len(a)
    if le == 1 and 'a' in a:
        return n
    repeated_num = n // len(s)
    rem_letters = n % len(s)

    return ((s.count('a' )* repeated_num)+ s[:rem_letters].count('a'))