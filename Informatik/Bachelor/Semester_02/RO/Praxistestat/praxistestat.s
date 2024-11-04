.data
mystring: .asciz "%d \n"     	//Output string
a: .word 1337                	//variable a
b: .word 69                  	//variable b
c: .word 420                 	//variable c
d: .word 42                  	//variable d
e: .word 11                  	//variable e
f: .word 41                  	//variable f
.text
.global main
main:
	push {lr}                	//save return adress
	ldr r0, =a            		//load a into r0
	ldr r0, [r0]
	ldr r1, =b              	//load b into r1
	ldr r1, [r1]
	and r0, r0, r1           	//use AND with r1 and r2 and save into r1: a & b
	ldr r1, =c             		//load c into r1
	ldr r1, [r1]
	mvn r1, r1               	//negate r1 and save into r1: ~ c
	ldr r2, =d              	//load d into r2
	ldr r2, [r2]
	mul r1, r2, r1           	//multiply r1 and r2 and save into r1: ~ c * d
	eor r0, r0, r1           	//use exclusive or with r0 and r1 and save into r0: ~ c * d ^ (a & b)
	ldr r1, =e              	//load e into r1
	ldr r1, [r1]
	ldr r2, =f              	//load f into r2
	ldr r2, [r2]
	orr r1, r1, r2           	//use or with r1 and r2 and save into r1: e | f
	sub r1, r0, r1           	//subtract r1 from r0 and save into r1 (~c * d ^ (a & b)) - (e | f)
	ldr r0, =mystring			
	bl printf                	//calls printf
	pop {lr}                 	//get return adress back
	bx lr                    	//return or exit
