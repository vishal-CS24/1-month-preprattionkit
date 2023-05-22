def timeConversion(s):
    li=s.split(':')
    if s[-2:] == "PM":
        if li[0]=='12':
            li[0]='12'
        else:
            li[0]=str(int(li[0])+12)
        s=":".join(li)
        return s[:-2]
    else:
        if li[0]=='12':
            li[0]='00'
            s=":".join(li)
            return s[:-2]
        else:
            return s[:-2]
timeConversion("07:05:45AM")
