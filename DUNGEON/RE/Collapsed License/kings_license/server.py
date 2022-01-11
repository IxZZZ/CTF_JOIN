import os
import base64
import tempfile
import subprocess

if __name__ == '__main__':
    os.system("stty -icanon")
    # try:
    b64lic = input("License Key: ")
    print(input("> "))
    lic = base64.b64decode(b64lic)
    with tempfile.NamedTemporaryFile('w+b') as f:
        f.write(lic)
        f.flush()
        print('name: ', f.name)
        subprocess.run(["./yoshikingsoft", f.name])
    # except Exception as e:
    #     print(e)
    #     print("[-] Error")
