def timeConversion(s):
    if s[-2:] == "PM":
        li=s.split(':')
        li[0]=str(int(li[0])+12)
        s=":".join(li)
        print(s[:-2])
    else:
        print(s[:-2])
timeConversion("07:05:45AM")