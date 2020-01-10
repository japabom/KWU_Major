# $t0 = for loop count, $t6 = sum, $a0 = function return variable
main:   li          $t0,10        # set count=10
        li    $t6,0        # set sum=0

for:    bgt    $t0,200,print    # end with t0 > 200
        addu    $t6,$t6,$t0    # sum each data
        addi    $t0,$t0,10        # inc 10

        j    for

# print result
print:
        li       $v0,1
        move       $a0,$t6   # print sum

        syscall

Exit:   li       $v0,10
        syscall

