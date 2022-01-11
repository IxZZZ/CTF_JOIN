def xor(filename, i):
    file = open(filename, 'rb')
    content = file.read()

    file_new = open('.\\final_decrypt'+f'\decrypt_{i}.txt', 'wb')
    m = 'meoow'
    for i in range(len(content)):
        file_new.write(bytes([content[i] ^ ord(m[i % 5])]))

    file_new.close()
    file.close()
from revenge import Process

# We need to interact with a process. It doesn't really matter which one. Let's just use calc
p = Process(r"C:\Windows\System32\calc.exe") 

# Since calc doesn't have the required patch library loaded, we need to load it first
p.memory['LoadLibraryA'](r"C:\Windows\System32\msdelta.dll")

# We can now grab the patch API. We'll use the ApplyDeltaA call. See the documentation linked above for more details
ApplyDeltaA = p.memory["ApplyDeltaA"]

# We will assume here that we already stripped off the first 4 bytes of that file, so that the file now starts with the PA30 header

# Now all we have to do is run the api. The format is:
# ApplyDeltaA(flags, source_file, patch_file, output_file)
# We'll use the value 1 for flags to enable PatchAPI compatability, though that's not necessary here.


# print(ApplyDeltaA(1, r"win32k.patched.sys",
#       r"patch-tuesday", r"out"))

print(ApplyDeltaA(1, r'source_pre_xor/patch_file_48',
      r"source_pre_xor/patch_file_50", r"output.txt"))

xor('output.txt',99999)


# You should see 1 returned from this, indicating success
