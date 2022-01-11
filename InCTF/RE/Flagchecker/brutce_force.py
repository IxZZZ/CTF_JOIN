import idaapi
import time
rip = 0x55E7EB43B60D
offset_input = 0x000055E7EC6D7AC0
str_number = '012346789'
c0 = '8'
arr_res = ['234231224221234231224221233423', '442444424444324434424444524454', '305878012345623010341238012344', '778782745678012157676002345670',
           '124342431242424212433424331243', '312242212342312242212334233123', '241412414132413412414152415142', '344244445244541241412414132413']


for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            for c4 in range(10):
                str_arr = [c0, c1, c2, c3, c4]
                str_arr = list('85481')
                str_arr.append(chr(0))
                for i in range(len(str_arr)):
                    ida_bytes.patch_byte(offset_input+i, ord(str_arr[i]))
                idaapi.set_reg_val('rip', rip)
                idaapi.continue_process()
                break
            break
        break
    break
