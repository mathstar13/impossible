def encode(txt,key=False,ek=""):
    ssc = "01234567890abcdefghijklmnopqrstuvwxyz,"
    from random import sample,choice
    nt = ""
    lc = 'l'
    for char in txt:
        nt += hex(ord(char))+","
    txt = nt[::-1].replace(",","",1)[::-1]
    sp = ','
    if ek == "":
        s = ""
        sc = ''.join(sample(ssc,len(ssc)))
        c = ''.join(sample(sc,len(sc)))
    else:
        sp = ek[::-1][0]
        s = ""
        spl = ek.split(sp)
        sc = spl[1]
        c = spl[0]
    for char in txt:
        try:
            s += c[sc.index(char)]
        except ValueError:
            s += char
    if key:
        return [s,c+sp+sc+sp]
    else:
        return s+sp+c+sp+sc+lc+sp
def encodeShort(txt,key=False,ek="",ssc=' !"#$%&\'()*,-./0123456+789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ',uus=True):
    from random import sample,choice
    nt = ""
    lc = "s"
    if ek == "":
        if "␟" in txt or "␟" in ssc or not uus:
            while True:
                sp = choice(ssc)
                if not sp in txt:
                    ssc = list(ssc)
                    del ssc[ssc.index(sp)]
                    ssc = ''.join(ssc)
                    break
        else:
            sp = "␟"
        s = ""
        sc = ''.join(sample(ssc,len(ssc)))
        c = ''.join(sample(sc,len(sc)))
    else:
        sp = ek[::-1][0]
        s = ""
        spl = ek.split(sp)
        sc = spl[1]
        c = spl[0]
    for char in txt:
        try:
            s += c[sc.index(char)]
        except ValueError:
            s += char
    if key:
        return [s,c+sp+sc+sp]
    else:
        return s+sp+c+sp+sc+lc+sp
sssc=' !"#$%&\'()*,-./0123456+789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ'
def decode(txt,key=''):
    long = False
    if txt[::-1][1] == "l":
        long = True
        txt = txt[::-1].replace('l','',1)[::-1]
    else:
        txt = txt[::-1].replace('s','',1)[::-1]
    if key == '':
        sp = txt[::-1][0]
        spt = txt.split(sp)
        s = spt[0]
        c = list(spt[1])
        sc = list(spt[2])
    else:
        s = txt
        sp = key[::-1][0]
        spt = key.split(sp)
        c = list(spt[0])
        sc = list(spt[1])
    txt = ""
    for char in s:
        try:
            txt += sc[c.index(char)]
        except ValueError:
            txt += char
    if long:
        r = ""
        for item in txt.split(","):
            r += chr(int(item,16))
        return r
    else:
        return txt
def generate_key():
    from random import sample
    sp = "."
    ssc = "0123456789abcdefghijklmnopqrstuvwxyz,"
    sc = ''.join(sample(ssc,len(ssc)))
    c = ''.join(sample(sc,len(sc)))
    return c+sp+sc+sp
def generate_key_short(sp="␟",ssc=' !"#$%&\'()*,-./0123456+789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ'):
    from random import sample
    sc = ''.join(sample(ssc,len(ssc)))
    c = ''.join(sample(sc,len(sc)))
    if sp in c:
        raise SyntaxError("Value of SP cannot be in SSC.")
    return c+sp+sc+sp
k = "1cfyljmbd6trpsi4aog378huqve2z9,0nx5kw.32ad,67piwn0toqs8xvb915ulhrcjg4yefzmk."
print(k)
print(encode("ASDF",ek=k,key=True))
print(decode(encode("ASDF",ek=k)))
'''s = ""
for char in "ASDF":
    s += hex(ord(char))+","
s = s[::-1].replace(",","",1)[::-1]
e = encode(s)
v = decode(e)
o = ""
for item in v.split(","):
    o += chr(int(item,16))
print(o)
#print(decode(d,key=k))'''
