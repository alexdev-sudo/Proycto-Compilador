struct Punto
p = new Punto
p.x = 3
p.y = 4
t1 = p.x
t2 = p.x
t3 = t1 * t2
t4 = p.y
t5 = p.y
t6 = t4 * t5
t7 = t3 + t6
t8 = cast(float) t7
dist = t8
t9 = dist > 20.0
if t9 goto L1
t10 = "cerca"
goto L2
L1:
t10 = "lejos"
L2:
etiqueta = t10
print etiqueta
opcion = 2
t11 = opcion == 1
ifFalse t11 goto L4
print "opcion uno"
break
goto L3
L4:
t12 = opcion == 2
ifFalse t12 goto L5
print "opcion dos"
break
goto L3
L5:
print "otra opcion"
L3:
begin_func fibonacci
param n
t13 = n <= 1
if t13 goto L6
goto L7
L6:
return n
L7:
t14 = n - 1
arg t14
t15 = call fibonacci, 1
t16 = n - 2
arg t16
t17 = call fibonacci, 1
t18 = t15 + t17
return t18
end_func fibonacci
nums = [5, 8, 13, 21, 34]
i = 0
total = 0
L8:
t19 = i < 5
ifFalse t19 goto L9
t20 = nums[i]
t21 = t20 % 2
r = t21
t22 = r == 0
if t22 goto L10
goto L11
L10:
t23 = nums[i]
t24 = total + t23
total = t24
L11:
t25 = i + 1
i = t25
t26 = total > 50
if t26 goto L12
goto L13
L12:
break
L13:
goto L8
L9:
arg 10
t27 = call fibonacci, 1
print t27
print total