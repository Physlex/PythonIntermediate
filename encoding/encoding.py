
def PrintType(string) -> None :
    print(string, type(string))
    return

def Encode(string:str) -> bytes :
    byte = string.encode('utf-8')
    return byte

def Decode(byte:bytes) -> str :
    string = byte.decode('utf-8') 
    return string

diff = 4

def IndexWindow(index: int, s: str) :
    global diff
    n = index % len(s)
    window = s[n: (diff + n)]
    return window

windowTowords = {}

def AddToWTW(window: str) :
    global windowTowords
    if Iwindow not in windowTowords :
        windowTowords[Iwindow] = 0
    else :
        windowTowords[Iwindow] += 1    

s = "This is unicode"
i = 0
while(i < 10000) :
    i += 1
    Iwindow = IndexWindow(i, s)
    print(Iwindow)

    if (Iwindow[0] == " ") :
        AddToWTW(Iwindow)

    if (Iwindow[len(Iwindow) - 1] == " ") : 
        AddToWTW(Iwindow)

validElements = []
for i, iVal in enumerate(windowTowords) :
    validElements.append( "i: %d, exl: %s " % (i, Encode(iVal)) )
PrintType(validElements)