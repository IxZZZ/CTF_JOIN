Võ Văn Minh, [16.10.21 13:46]
[ Photo ]

IxZ, [16.10.21 13:46]
tầm 10 hàm

Võ Văn Minh, [16.10.21 13:58]
void __usercall sub_157F(int a1@<ebx>, int a2@<ebp>, int a3@<esi>)
{
  int v3; // esi
  int v4; // [esp-70h] [ebp-70h]
  __pid_t pid; // [esp-6Ch] [ebp-6Ch]
  int (*v6)(); // [esp-68h] [ebp-68h]
  __pid_t v7; // [esp-64h] [ebp-64h]
  int input_key_len; // [esp-60h] [ebp-60h]
  int v9; // [esp-5Ch] [ebp-5Ch]
  void *v10; // [esp-58h] [ebp-58h]
  user_regs_struct regs; // [esp-54h] [ebp-54h]
  unsigned int v12; // [esp-10h] [ebp-10h]
  int v13; // [esp-Ch] [ebp-Ch]
  int v14; // [esp-8h] [ebp-8h]
  int v15; // [esp-4h] [ebp-4h]

  __asm { endbr32 }
  v15 = a2;
  v14 = a3;
  v13 = a1;
  v12 = __readgsdword(0x14u);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  malloc(0xFFu);
  pid = 4660;
  v6 = sub_1ADC;
  ptrace(PTRACE_ATTACH, 4660, 0, 0);
  while ( 1 )
  {
    v7 = waitpid(pid, &v4, 0);
    if ( v7 == -1 )
      break;
    if ( BYTE1(v4) == 19 )
      ptrace(PTRACE_POKEDATA, pid, sub_1B23, 0xB0F);
    if ( BYTE1(v4) == 4 )
    {
      input_key_len = strlen((const char *)input_key);
      sub_19F7((int)&v15, pid, input_key, (int *)input_key, input_key_len);
      ptrace(PTRACE_GETREGS, pid, 0, &regs);
      v9 = regs.esp;
      if ( ptrace(PTRACE_POKEDATA, pid, regs.esp + 8, input_key) == -1 )
      {
        perror((const char *)&unk_300C);
        exit(0);
      }
      ptrace(PTRACE_POKEDATA, pid, regs.esp + 4, input_key_len);
      regs.eip = (int)sub_1B7E;
      ptrace(PTRACE_SETREGS, pid, 0, &regs);
    }
    if ( BYTE1(v4) == 5 )
    {
      ptrace(PTRACE_GETREGS, pid, 0, &regs);
      switch ( 28344 * (regs.orig_eax ^ 0xCAFE) )
      {
        case 0x57CA9BD8:
          fgets((char *)input_key, 255, stdin);
          v3 = input_key;
          *(_BYTE *)(v3 + strlen((const char *)input_key) - 1) = 0;
          sub_142D(input_key);
          break;
        case 0x57C94FB0:
          v10 = malloc(regs.edx);
          sub_18DD(pid, regs.ecx, v10, regs.edx);
          write(1, v10, regs.edx);
          sub_11D0(v10);
          break;
        case 0x57A18590:
          sub_14C6(pid, regs.ebx, regs.ecx);
          break;
        case 0x57CB7948:
          ptrace(PTRACE_DETACH, pid, 0, 0);
          break;
      }
    }
    ptrace(PTRACE_SYSCALL|PTRACE_CONT, pid, 0, 0);
  }
  ptrace(PTRACE_DETACH, pid, 0, 0);
  exit(0);
}