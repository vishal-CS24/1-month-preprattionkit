def pangrams(s):
    alphabets='abcdefghijklmnopqrstubwxyz '
    ans= False
    s=s.lower()
    for i in alphabets:
        if i in s:
            ans=True
        else:
            return "not pangram"
    if ans==True:
        return 'pangram'
    else:
        return 'not pangram'
print(pangrams('We promptly judged antique ivory buckles for the prize'))

