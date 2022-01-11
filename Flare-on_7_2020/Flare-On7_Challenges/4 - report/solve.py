def rigmarole(s_):
    furphy = ''
    for i in range(0,len(s_),4):
        c = int(s_[i:i+2],16)
        s = int(s_[i+2:i+4],16)
        furphy += chr(c-s)
    return furphy


FL = '9655B040B64667238524D15D6201.B95D4E01C55CC562C7557405A532D768C55FA12DD074DC697A06E172992CAF3F8A5C7306B7476B38.C555AC40A7469C234424.853FA85C470699477D3851249A4B9C4E.A855AF40B84695239D24895D2101D05CCA62BE5578055232D568C05F902DDC74D2697406D7724C2CA83FCF5C2606B547A73898246B4BC14E941F9121D464D263B947EB77D36E7F1B8254.853FA85C470699477D3851249A4B9C4E.9A55B240B84692239624.CC55A940B44690238B24CA5D7501CF5C9C62B15561056032C468D15F9C2DE374DD696206B572752C8C3FB25C3806.A8558540924668236724B15D2101AA5CC362C2556A055232AE68B15F7C2DC17489695D06DB729A2C723F8E5C65069747AA389324AE4BB34E921F9421.CB55A240B5469B23.AC559340A94695238D24CD5D75018A5CB062BA557905A932D768D15F982D.D074B6696F06D5729E2CAE3FCF5C7506AD47AC388024C14B7C4E8F1F8F21CB64'

i = 0
for f in FL.split('.'):
    print(i,' - ',rigmarole(f))
    i +=1

'''
0  -  AppData1  -  \Microsoft\stomp.mp3
2  -  play 
3  -  FLARE-ON
4  -  Sorry, this machine is not supported.
5  -  FLARE-ON
6  -  Error
7  -  winmgmts:\\.\root\CIMV2
8  -  SELECT Name FROM Win32_Process
9  -  vbox
10  -  WScript.Network
11  -  \Microsoft\v.png
'''


def canoodle(panjandrum,ardylo,s,bibble):
    quean = 0
    kerfufle = bytearray()
    for cattywampus in range(0,len(panjandrum),4):
        a = int(panjandrum[cattywampus+ardylo:cattywampus+ardylo+2],16)
        b = bibble[quean%len(bibble)]
        kerfufle.append(a^b)
        quean+=1
        if quean == s:
            break
    return kerfufle


xertz = [0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xaa,0xbb,0xcc,0xdd,0xee]
FLTEXT = open('FLTEXT.txt','r').read()

buff = "FLARE-ON"[::-1]
buff = [ord(c) for c in buff]

mp3 = canoodle(FLTEXT, 0, 168667,xertz)
# img = canoodle(FLTEXT,2,285729,buff)


with open('stomp.mp3','wb') as f:
    f.write(mp3)


# with open('v.png','wb') as f:
#     f.write(img)
