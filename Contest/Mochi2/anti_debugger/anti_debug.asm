.text:000056196000B567 ; int __cdecl main(int argc, const char **argv, const char **envp)
.text:000056196000B567 public main
.text:000056196000B567 main proc near                          ; DATA XREF: _start+21↑o
.text:000056196000B567
.text:000056196000B567 var_2CEC= dword ptr -2CECh
.text:000056196000B567 var_2CE8= dword ptr -2CE8h
.text:000056196000B567 var_2CE4= dword ptr -2CE4h
.text:000056196000B567 stream= qword ptr -2CE0h
.text:000056196000B567 ptr= qword ptr -2CD8h
.text:000056196000B567 key= byte ptr -2CD0h
.text:000056196000B567 var_2000= qword ptr -2000h
.text:000056196000B567 store= byte ptr -1670h
.text:000056196000B567 var_1000= qword ptr -1000h
.text:000056196000B567 var_8= qword ptr -8
.text:000056196000B567
.text:000056196000B567 endbr64
.text:000056196000B56B push    rbp
.text:000056196000B56C mov     rbp, rsp
.text:000056196000B56F sub     rsp, 1000h
.text:000056196000B576 or      [rsp+1000h+var_1000], 0
.text:000056196000B57B sub     rsp, 1000h
.text:000056196000B582 or      [rsp+2000h+var_2000], 0
.text:000056196000B587 sub     rsp, 0CF0h
.text:000056196000B58E mov     rax, fs:28h
.text:000056196000B597 mov     [rbp+var_8], rax
.text:000056196000B59B xor     eax, eax
.text:000056196000B59D lea     rsi, modes                      ; "r"
.text:000056196000B5A4 lea     rdi, aSomethingsecre            ; "./somethingSecret.txt"
.text:000056196000B5AB call    _fopen
.text:000056196000B5B0 mov     [rbp+stream], rax
.text:000056196000B5B7 mov     edi, 165Dh                      ; size
.text:000056196000B5BC call    _malloc
.text:000056196000B5C1 mov     [rbp+ptr], rax
.text:000056196000B5C8 mov     rdx, [rbp+stream]
.text:000056196000B5CF mov     rax, [rbp+ptr]
.text:000056196000B5D6 mov     rcx, rdx                        ; stream
.text:000056196000B5D9 mov     edx, 1                          ; n
.text:000056196000B5DE mov     esi, 165Ch                      ; size
.text:000056196000B5E3 mov     rdi, rax                        ; ptr
.text:000056196000B5E6 call    _fread
.text:000056196000B5EB mov     rax, [rbp+stream]
.text:000056196000B5F2 mov     rdi, rax                        ; stream
.text:000056196000B5F5 call    _fclose
.text:000056196000B5FA lea     rdi, s                          ; "Oh no, the stupid author leaked somethi"...
.text:000056196000B601 call    _puts
.text:000056196000B606 lea     rax, [rbp+key]
.text:000056196000B60D mov     edx, 165Dh                      ; n
.text:000056196000B612 mov     esi, 0                          ; c
.text:000056196000B617 mov     rdi, rax                        ; s
.text:000056196000B61A call    _memset
.text:000056196000B61F lea     rax, [rbp+store]
.text:000056196000B626 mov     edx, 165Dh                      ; n
.text:000056196000B62B mov     esi, 0                          ; c
.text:000056196000B630 mov     rdi, rax                        ; s
.text:000056196000B633 call    _memset
.text:000056196000B638 mov     edi, 0                          ; timer
.text:000056196000B63D call    _time
.text:000056196000B642 mov     rsi, rax
.text:000056196000B645 lea     rdi, format                     ; "%ld\n"
.text:000056196000B64C mov     eax, 0
.text:000056196000B651 call    _printf
.text:000056196000B656 mov     edi, 0                          ; timer
.text:000056196000B65B call    _time
.text:000056196000B660 mov     edi, eax                        ; seed
.text:000056196000B662 call    _srand
.text:000056196000B667 mov     [rbp+var_2CEC], 0
.text:000056196000B671 jmp     short loc_56196000B690
.text:000056196000B673 ; ---------------------------------------------------------------------------
.text:000056196000B673
.text:000056196000B673 loc_56196000B673:                       ; CODE XREF: main+133↓j
.text:000056196000B673 call    _rand
.text:000056196000B678 mov     edx, eax
.text:000056196000B67A mov     eax, [rbp+var_2CEC]
.text:000056196000B680 cdqe
.text:000056196000B682 mov     [rbp+rax+key], dl
.text:000056196000B689 add     [rbp+var_2CEC], 1
.text:000056196000B690
.text:000056196000B690 loc_56196000B690:                       ; CODE XREF: main+10A↑j
.text:000056196000B690 cmp     [rbp+var_2CEC], 165Bh
.text:000056196000B69A jle     short loc_56196000B673
.text:000056196000B69C mov     [rbp+var_2CE8], 0
.text:000056196000B6A6 jmp     short loc_56196000B6FC
.text:000056196000B6A8 ; ---------------------------------------------------------------------------
.text:000056196000B6A8
.text:000056196000B6A8 loc_56196000B6A8:                       ; CODE XREF: main+19F↓j
.text:000056196000B6A8 mov     eax, [rbp+var_2CE8]
.text:000056196000B6AE movsxd  rdx, eax
.text:000056196000B6B1 mov     rax, [rbp+ptr]
.text:000056196000B6B8 add     rax, rdx
.text:000056196000B6BB movzx   edx, byte ptr [rax]
.text:000056196000B6BE mov     eax, [rbp+var_2CE8]
.text:000056196000B6C4 cdqe
.text:000056196000B6C6 movzx   eax, [rbp+rax+key]
.text:000056196000B6CE xor     eax, edx
.text:000056196000B6D0 mov     edx, eax
.text:000056196000B6D2 mov     eax, [rbp+var_2CE8]
.text:000056196000B6D8 cdqe
.text:000056196000B6DA movzx   eax, [rbp+rax+key]
.text:000056196000B6E2 add     eax, edx
.text:000056196000B6E4 mov     edx, eax
.text:000056196000B6E6 mov     eax, [rbp+var_2CE8]
.text:000056196000B6EC cdqe
.text:000056196000B6EE mov     [rbp+rax+store], dl
.text:000056196000B6F5 add     [rbp+var_2CE8], 1
.text:000056196000B6FC
.text:000056196000B6FC loc_56196000B6FC:                       ; CODE XREF: main+13F↑j
.text:000056196000B6FC cmp     [rbp+var_2CE8], 165Bh
.text:000056196000B706 jle     short loc_56196000B6A8
.text:000056196000B708 mov     [rbp+var_2CE4], 0
.text:000056196000B712 jmp     short loc_56196000B744
.text:000056196000B714 ; ---------------------------------------------------------------------------
.text:000056196000B714
.text:000056196000B714 loc_56196000B714:                       ; CODE XREF: main+1E4↓j
.text:000056196000B714 mov     eax, [rbp+var_2CE4]
.text:000056196000B71A cdqe
.text:000056196000B71C movzx   eax, [rbp+rax+store]
.text:000056196000B724 movsx   eax, al
.text:000056196000B727 movzx   eax, al
.text:000056196000B72A mov     esi, eax
.text:000056196000B72C lea     rdi, a02x                       ; "%02X "
.text:000056196000B733 mov     eax, 0
.text:000056196000B738 call    _printf
.text:000056196000B73D add     [rbp+var_2CE4], 1
.text:000056196000B744
.text:000056196000B744 loc_56196000B744:                       ; CODE XREF: main+1AB↑j
.text:000056196000B744 cmp     [rbp+var_2CE4], 9
.text:000056196000B74B jle     short loc_56196000B714
.text:000056196000B74D mov     edi, 0Ah                        ; c
.text:000056196000B752 call    _putchar
.text:000056196000B757 mov     eax, 0
.text:000056196000B75C call    dump_something
.text:000056196000B761 mov     eax, 0
.text:000056196000B766 mov     rcx, [rbp+var_8]
.text:000056196000B76A sub     rcx, fs:28h
.text:000056196000B773 jz      short locret_56196000B77A
.text:000056196000B775 call    ___stack_chk_fail
.text:000056196000B77A ; ---------------------------------------------------------------------------
.text:000056196000B77A
.text:000056196000B77A locret_56196000B77A:                    ; CODE XREF: main+20C↑j
.text:000056196000B77A leave
.text:000056196000B77B retn



.text:000056196000B369 public dump_something
.text:000056196000B369 dump_something proc near                ; CODE XREF: main+1F5↓p
.text:000056196000B369
.text:000056196000B369 haystack= qword ptr -60h
.text:000056196000B369 stream= qword ptr -58h
.text:000056196000B369 off= qword ptr -50h
.text:000056196000B369 var_48= qword ptr -48h
.text:000056196000B369 var_40= qword ptr -40h
.text:000056196000B369 ptr= qword ptr -38h
.text:000056196000B369 var_30= qword ptr -30h
.text:000056196000B369 s= qword ptr -22h
.text:000056196000B369 dest= qword ptr -15h
.text:000056196000B369 var_8= qword ptr -8
.text:000056196000B369
.text:000056196000B369 endbr64
.text:000056196000B36D push    rbp
.text:000056196000B36E mov     rbp, rsp
.text:000056196000B371 sub     rsp, 60h
.text:000056196000B375 mov     rax, fs:28h
.text:000056196000B37E mov     [rbp+var_8], rax
.text:000056196000B382 xor     eax, eax
.text:000056196000B384 mov     edi, 12Ch                       ; size
.text:000056196000B389 call    _malloc
.text:000056196000B38E mov     [rbp+haystack], rax
.text:000056196000B392 lea     rax, [rbp+s]
.text:000056196000B396 mov     edx, 0Dh                        ; n
.text:000056196000B39B mov     esi, 0                          ; c
.text:000056196000B3A0 mov     rdi, rax                        ; s
.text:000056196000B3A3 call    _memset
.text:000056196000B3A8 lea     rax, [rbp+dest]
.text:000056196000B3AC mov     edx, 0Dh                        ; n
.text:000056196000B3B1 mov     esi, 0                          ; c
.text:000056196000B3B6 mov     rdi, rax                        ; s
.text:000056196000B3B9 call    _memset
.text:000056196000B3BE lea     rsi, modes                      ; "r"
.text:000056196000B3C5 lea     rdi, filename                   ; "/proc/self/maps"
.text:000056196000B3CC call    _fopen
.text:000056196000B3D1 mov     [rbp+stream], rax
.text:000056196000B3D5 jmp     short loc_56196000B402
.text:000056196000B3D7 ; ---------------------------------------------------------------------------
.text:000056196000B3D7
.text:000056196000B3D7 loc_56196000B3D7:                       ; CODE XREF: dump_something+AF↓j
.text:000056196000B3D7 mov     rax, [rbp+haystack]
.text:000056196000B3DB mov     edx, 8                          ; n
.text:000056196000B3E0 mov     esi, 0                          ; c
.text:000056196000B3E5 mov     rdi, rax                        ; s
.text:000056196000B3E8 call    _memset
.text:000056196000B3ED mov     rdx, [rbp+stream]               ; stream
.text:000056196000B3F1 mov     rax, [rbp+haystack]
.text:000056196000B3F5 mov     esi, 96h                        ; n
.text:000056196000B3FA mov     rdi, rax                        ; s
.text:000056196000B3FD call    _fgets
.text:000056196000B402
.text:000056196000B402 loc_56196000B402:                       ; CODE XREF: dump_something+6C↑j
.text:000056196000B402 mov     rax, [rbp+haystack]
.text:000056196000B406 lea     rsi, needle                     ; "[st"
.text:000056196000B40D mov     rdi, rax                        ; haystack
.text:000056196000B410 call    _strstr
.text:000056196000B415 test    rax, rax
.text:000056196000B418 jz      short loc_56196000B3D7
.text:000056196000B41A mov     rax, [rbp+stream]
.text:000056196000B41E mov     rdi, rax                        ; stream
.text:000056196000B421 call    _fclose
.text:000056196000B426 mov     rcx, [rbp+haystack]
.text:000056196000B42A lea     rax, [rbp+s]
.text:000056196000B42E mov     edx, 0Ch                        ; n
.text:000056196000B433 mov     rsi, rcx                        ; src
.text:000056196000B436 mov     rdi, rax                        ; dest
.text:000056196000B439 call    _strncpy
.text:000056196000B43E mov     rax, [rbp+haystack]
.text:000056196000B442 lea     rcx, [rax+0Dh]
.text:000056196000B446 lea     rax, [rbp+dest]
.text:000056196000B44A mov     edx, 0Ch                        ; n
.text:000056196000B44F mov     rsi, rcx                        ; src
.text:000056196000B452 mov     rdi, rax                        ; dest
.text:000056196000B455 call    _strncpy
.text:000056196000B45A lea     rcx, [rbp+s]
.text:000056196000B45E lea     rax, [rbp+s]
.text:000056196000B462 mov     edx, 10h                        ; base
.text:000056196000B467 mov     rsi, rcx                        ; endptr
.text:000056196000B46A mov     rdi, rax                        ; nptr
.text:000056196000B46D call    _strtoll
.text:000056196000B472 mov     [rbp+off], rax
.text:000056196000B476 lea     rcx, [rbp+dest]
.text:000056196000B47A lea     rax, [rbp+dest]
.text:000056196000B47E mov     edx, 10h                        ; base
.text:000056196000B483 mov     rsi, rcx                        ; endptr
.text:000056196000B486 mov     rdi, rax                        ; nptr
.text:000056196000B489 call    _strtoll
.text:000056196000B48E mov     [rbp+var_48], rax
.text:000056196000B492 lea     rsi, modes                      ; "r"
.text:000056196000B499 lea     rdi, aProcSelfMem               ; "/proc/self/mem"
.text:000056196000B4A0 call    _fopen
.text:000056196000B4A5 mov     [rbp+var_40], rax
.text:000056196000B4A9 mov     rcx, [rbp+off]
.text:000056196000B4AD mov     rax, [rbp+var_40]
.text:000056196000B4B1 mov     edx, 0                          ; whence
.text:000056196000B4B6 mov     rsi, rcx                        ; off
.text:000056196000B4B9 mov     rdi, rax                        ; stream
.text:000056196000B4BC call    _fseek
.text:000056196000B4C1 mov     rax, [rbp+var_48]
.text:000056196000B4C5 sub     rax, [rbp+off]
.text:000056196000B4C9 add     rax, 1
.text:000056196000B4CD mov     rdi, rax                        ; size
.text:000056196000B4D0 call    _malloc
.text:000056196000B4D5 mov     [rbp+ptr], rax
.text:000056196000B4D9 mov     rax, [rbp+var_48]
.text:000056196000B4DD sub     rax, [rbp+off]
.text:000056196000B4E1 lea     rsi, [rax+1]                    ; size
.text:000056196000B4E5 mov     rdx, [rbp+var_40]
.text:000056196000B4E9 mov     rax, [rbp+ptr]
.text:000056196000B4ED mov     rcx, rdx                        ; stream
.text:000056196000B4F0 mov     edx, 1                          ; n
.text:000056196000B4F5 mov     rdi, rax                        ; ptr
.text:000056196000B4F8 call    _fread
.text:000056196000B4FD mov     rax, [rbp+var_40]
.text:000056196000B501 mov     rdi, rax                        ; stream
.text:000056196000B504 call    _fclose
.text:000056196000B509 lea     rsi, aW                         ; "w"
.text:000056196000B510 lea     rdi, aDump                      ; "./dump"
.text:000056196000B517 call    _fopen
.text:000056196000B51C mov     [rbp+var_30], rax
.text:000056196000B520 mov     rax, [rbp+var_48]
.text:000056196000B524 sub     rax, [rbp+off]
.text:000056196000B528 lea     rsi, [rax+1]                    ; size
.text:000056196000B52C mov     rdx, [rbp+var_30]
.text:000056196000B530 mov     rax, [rbp+ptr]
.text:000056196000B534 mov     rcx, rdx                        ; s
.text:000056196000B537 mov     edx, 1                          ; n
.text:000056196000B53C mov     rdi, rax                        ; ptr
.text:000056196000B53F call    _fwrite
.text:000056196000B544 mov     rax, [rbp+var_30]
.text:000056196000B548 mov     rdi, rax                        ; stream
.text:000056196000B54B call    _fclose
.text:000056196000B550 nop
.text:000056196000B551 mov     rax, [rbp+var_8]
.text:000056196000B555 sub     rax, fs:28h
.text:000056196000B55E jz      short locret_56196000B565
.text:000056196000B560 call    ___stack_chk_fail
.text:000056196000B565 ; ---------------------------------------------------------------------------
.text:000056196000B565
.text:000056196000B565 locret_56196000B565:                    ; CODE XREF: dump_something+1F5↑j
.text:000056196000B565 leave
.text:000056196000B566 retn