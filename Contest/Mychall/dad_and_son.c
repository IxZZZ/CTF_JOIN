#include <seccomp.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <unistd.h>
#include <sys/ptrace.h>
#include <stdint.h>

// gcc dad_and_son.c -o res -lseccomp

unsigned char code[] = "\x4C\x8D\x2F\x48\x8D\x26\x4D\x31\xE4\x4D\x31\xFF\x45\x8B\x7D\x00\x41\x80\xFF\x00\x74\x29\x41\xFE\xC4\x49\x83\xC5\x04\x48\x31\xC0\x48\x31\xFF\x48\xF7\xF9\x48\xC7\xC0\x3E\x00\x00\x00\x48\xC7\xC7\x00\x00\x00\x00\x48\xC7\xC6\x12\x00\x00\x00\x0F\x05\xEB\xCD\xCC\x4D\x31\xC9\x4D\x31\xFF\x45\x38\xE1\x74\x0F\x45\x8B\x7D\x00\x0F\x0B\x41\xFE\xC1\x49\x83\xC5\x04\xEB\xEC\xCC\x4D\x31\xC9\x4D\x31\xFF\x4D\x31\xD2\x49\xC1\xFC\x02\x45\x38\xE1\x0F\x84\x80\x00\x00\x00\x4D\x8B\x7D\x00\x4D\x8B\x75\x08\x48\xC7\xC0\x3E\x00\x00\x00\x48\xC7\xC7\x00\x00\x00\x00\x48\xC7\xC6\x1C\x00\x00\x00\x0F\x05\x48\xC7\xC0\x2C\x01\x00\x00\x0F\x05\x48\x31\xC9\x44\x8B\x3C\x24\x45\x8B\x5D\x04\x45\x39\xDF\x75\x4F\x48\x83\xC4\x04\x44\x8B\x3C\x24\x45\x8B\x5D\x08\x45\x39\xDF\x75\x3E\x48\x83\xC4\x04\x44\x8B\x3C\x24\x45\x39\xD7\x75\x31\x48\x83\xC4\x04\x44\x8B\x3C\x24\x41\x39\xEF\x75\x24\x48\x83\xC4\x04\x44\x8B\x3C\x24\x45\x39\xC7\x75\x17\x48\x83\xC4\x04\x41\xFE\xC1\x49\x83\xC5\x10\xE9\x77\xFF\xFF\xFF\x48\x31\xDB\xB3\x01\xEB\x03\x48\x31\xDB\x48\x8B\x04\x25\x00\x00\x00\x00\x48\x31\xFF\x48\xC7\xC0\x3C\x00\x00\x00\x0F\x05";
int size = 272;

int cal_const[][10] = {{3, 9, 4, 8, 6, 7}, {3, 2, 4, 6, 7, 6}, {2, 1, 3, 9, 5, 6}, {8, 4, 9, 8, 3, 3}};

int final_const[][5] = {{4168099905, 3460811466, 3166149980, 1926604705, 829546058}, {3888838837, 3549494509, 834302606, 4187959490, 522221212}, {2783117493, 3710170029, 3759869023, 340280210, 1711963366}, {4025500862, 969913447, 2943343419, 2060407396, 1464290225}};
int index_v5 = 0;
int v5[20];

int v[4];

void check_input(int correct)
{
    if (correct)
    {
        puts("Congratulations!!!");
    }
    else
    {
        puts("Wrong, Let's try again!");
    }
    exit(0);
}

int SIGTRAP_f(char *key)
{
    return ((((((key[3] << 8) + key[2]) << 8) + key[1]) << 8) + key[0]);
}

int SIGWINCH_f(int v4[4], int cal_const[6])
{
    return (v4[2] >> cal_const[0]) + v4[0];
}

int SIGSYS_f(int v4[4], int cal_const[4])
{
    return (cal_const[1] * v4[3] + cal_const[2] * v4[0]);
}

int SIGFPE_f(int v6)
{
    int v24 = ((((v6 >> 3) & 0x20000000) + 32 * v6) ^ v6);
    return v24 ^ (v24 << 7);
}

int SIGCONT_f(int v23)
{
    int v22 = ((0xff & (v23 >> 1)) + v23);
    return v22 ^ (((v22 >> 3) & 0x20000000) + 32 * v22);
}

int SIGILL_f(int v5_)
{
    int v8 = (v5_ ^ (v5_ << 7));
    return ((0xff & (v8 >> 1)) + v8);
}

int main()
{
    char input[70];
    int64_t rip;
    int64_t regs[28];
    int64_t val;
    int v23;
    puts("Enter the secret key: ");
    scanf("%64s", input);
    if (strlen(input) != 64)
    {
        puts("We need more than that!");
        exit(0);
    }
    int stat_loc;
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_ALLOW);
    seccomp_rule_add(ctx, SCMP_ACT_TRAP, SCMP_SYS(fanotify_init), 0);
    seccomp_load(ctx);
    unsigned int pid = fork();
    if (!pid)
    {
        char *addr = mmap(0, 0x6b5, PROT_EXEC | PROT_READ | PROT_WRITE, 34, -1, 0);
        memcpy(addr, code, size);
        ptrace(PTRACE_TRACEME, 0, 0, 0);
        int (*foo)() = (int (*)())addr;
        foo(input, final_const);
        exit(0);
    }
    while (waitpid(pid, &stat_loc, 0) != -1)
    {
        switch (stat_loc >> 8)
        {
        case 5:
            // SIGTRAP
            // printf("Raise SIGTRAP\n");
            ptrace(PTRACE_GETREGS, pid, 0, regs);
            regs[2] = 0;
            regs[2] = regs[2] | (int64_t)(v5);

            ptrace(PTRACE_SETREGS, pid, 0, regs);
            index_v5 = 0;
            break;
        case 4:
            // SIGILL
            // printf("Raise SIGILL\n");

            ptrace(PTRACE_GETREGS, pid, 0, regs);
            regs[16] += 2;
            ptrace(PTRACE_SETREGS, pid, 0, regs);
            v5[index_v5++] = SIGILL_f(regs[0]);
            val = ptrace(PTRACE_PEEKTEXT, pid, &v5[index_v5 - 1], 0) & 0xffffffff00000000;
            ptrace(PTRACE_POKETEXT, pid, &v5[index_v5 - 1], val | (v5[index_v5 - 1] & 0xffffffff));

            break;
        case 8:
            // SIGFPE
            // printf("Raise SIGFPE\n");
            ptrace(PTRACE_GETREGS, pid, 0, regs);
            regs[16] += 3;
            ptrace(PTRACE_SETREGS, pid, 0, regs);

            regs[0] = SIGFPE_f(regs[0]);
            ptrace(PTRACE_SETREGS, pid, 0, regs);
            break;
        case 11:
            // SIGEGV
            // printf("Raise SIGEGV\n");
            ptrace(PTRACE_GETREGS, pid, 0, regs);
            regs[16] += 8;
            ptrace(PTRACE_SETREGS, pid, 0, regs);
            check_input(regs[5]);
            break;
        case 18:
            // SIGCONT
            // printf("Raise SIGCONT\n");
            ptrace(PTRACE_GETREGS, pid, 0, regs);

            v5[index_v5++] = SIGCONT_f(regs[0]);
            val = ptrace(PTRACE_PEEKTEXT, pid, &v5[index_v5 - 1], 0) & 0xffffffff00000000;
            ptrace(PTRACE_POKETEXT, pid, &v5[index_v5 - 1], val | (v5[index_v5 - 1] & 0xffffffff));
            break;
        case 28:
            // SIGWINCH
            // printf("Raise SIGWINCH\n");
            ptrace(PTRACE_GETREGS, pid, 0, regs);
            v[0] = regs[0] & 0xffffffff;
            v[1] = (regs[0] >> 32) & 0xffffffff;
            v[2] = regs[1] & 0xffffffff;
            v[3] = (regs[1] >> 32) & 0xffffffff;
            regs[7] = SIGWINCH_f(v, cal_const[regs[8]]);
            regs[9] = SIGSYS_f(v, cal_const[regs[8]]);
            ptrace(PTRACE_SETREGS, pid, 0, regs);
            break;
        case 31:
            // SIGSYS
            // printf("Raise SIGSYS\n");
            ptrace(PTRACE_GETREGS, pid, 0, regs);
            regs[7] = (cal_const[regs[8]][3] * regs[7] + cal_const[regs[8]][4] * regs[9]) & 0xffffffff;
            regs[4] = (cal_const[regs[8]][5] * regs[9] + regs[0] & 0xffffffff) & 0xffffffff;
            ptrace(PTRACE_SETREGS, pid, 0, regs);
            // printf("res: %llx,%llx,%llx,%llx,%llx\n", (regs[0] >> 32) & 0xffffffff, regs[1] & 0xffffffff, regs[7], regs[4], regs[9] & 0xffffffff);
            val = ptrace(PTRACE_PEEKTEXT, pid, regs[19], 0);
            // printf("const: %llx\n", val);
            break;
        default:
            if ((stat_loc & 0x7f) == 0 || stat_loc >> 8 == 17)
            {
                puts("Something went wrong!");
            }
            break;
        }
        ptrace(PTRACE_CONT, pid, 0, 0);
    }
    return 0;
}