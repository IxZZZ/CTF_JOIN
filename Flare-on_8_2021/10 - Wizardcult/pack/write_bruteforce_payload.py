f = open('/mages_tower/cool_wizard_meme.png','wb')

for i in range(256):
    str = bytes([i])*24
    f.write(str)

f.close()
