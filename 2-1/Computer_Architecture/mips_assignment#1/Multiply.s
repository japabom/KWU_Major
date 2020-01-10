# $t0 = mul , $t2 = n , $t4 = n+1 , $t3 = input[0] , $a0 = txt storage
        .data

        txt1:    .asciiz "result mul = "
        txt3:    .asciiz "\n"

        input:    .word    8, 2, 6, 4, 10, 7, 3, 1, 5, 0
        mulre:    .word    1

        .text
main:
        li    $t0,1        # set mul=1
        la    $t3,input         # $t3<- addr of input


for:
        lw     $t2,0($t3)# load 8,2,..... (n)
        lw     $t4,4($t3) # n+1
        blez    $t4,Exit    # end with data(n+1) = 0
        mul    $t0,$t2,$t4# mul n*(n+1)
        addiu    $t3,$t3,4#inc by word size
        bgtz    $t2,print # data > 0

# print result
print:
        li       $v0,4
        la       $a0,txt1        # "result mul : "
        syscall

        sw       $t0,mulre

        li       $v0,1
        lw       $a0,mulre    # print mulre

        syscall

        li       $v0,4
        la       $a0,txt3        # "\n"
        syscall
        j    for


Exit:   li       $v0,10
        syscall

