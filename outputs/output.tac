import math
nums = [3, 1, 4, 1, 5]
total = 0
i = 0
L1:
t1 = i < 5
ifFalse t1 goto L2
t2 = nums[i]
t3 = t2 % 2
r = t3
t4 = r == 0
if t4 goto L3
goto L4
L3:
t5 = nums[i]
t6 = total + t5
total = t6
L4:
t7 = i + 1
i = t7
t8 = total > 10
if t8 goto L5
goto L6
L5:
break
L6:
goto L1
L2:
t9 = "Resultado: " + "calculado"
msg = t9
print msg
print total