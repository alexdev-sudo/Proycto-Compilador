total = 0
i = 0
l1:
t1 = i < 5
ifFalse t1 goto l2
t2 = nums[i]
t3 = t2 % 2
r = t3
t4 = r == 0
ifFalse t4 goto l3
t5 = nums[i]
t6 = total + t5
total = t6
goto l4
l3:
l4:
t7 = i + 1
i = t7
t8 = total > 10
ifFalse t8 goto l5
goto l6
l5:
l6:
goto l1
l2:
t9 = "Resultado: " + "calculado"
msg = t9