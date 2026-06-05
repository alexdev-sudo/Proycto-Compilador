; ModuleID = '/tmp/tmpzmwicx9j/input.ll'
source_filename = "/tmp/tmpzmwicx9j/input.ll"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-w64-windows-gnu"

@str_0 = internal constant [6 x i8] c"lejos\00"
@str_1 = internal constant [6 x i8] c"cerca\00"
@str_2 = internal constant [4 x i8] c"%s\0A\00"
@str_3 = internal constant [11 x i8] c"opcion uno\00"
@str_4 = internal constant [4 x i8] c"%s\0A\00"
@str_5 = internal constant [11 x i8] c"opcion dos\00"
@str_6 = internal constant [4 x i8] c"%s\0A\00"
@str_7 = internal constant [12 x i8] c"otra opcion\00"
@str_8 = internal constant [4 x i8] c"%s\0A\00"
@str_9 = internal constant [4 x i8] c"%d\0A\00"
@str_10 = internal constant [4 x i8] c"%d\0A\00"

declare i32 @printf(ptr, ...)

declare ptr @strcat(ptr, ptr)

declare ptr @malloc(i64)

define i32 @main() {
entry:
  %p = alloca { i32, i32 }, align 8
  %.2 = getelementptr inbounds { i32, i32 }, ptr %p, i32 0, i32 0
  store i32 3, ptr %.2, align 4
  %.4 = getelementptr inbounds { i32, i32 }, ptr %p, i32 0, i32 1
  store i32 4, ptr %.4, align 4
  %.6 = getelementptr inbounds { i32, i32 }, ptr %p, i32 0, i32 0
  %.7 = load i32, ptr %.6, align 4
  %.8 = getelementptr inbounds { i32, i32 }, ptr %p, i32 0, i32 0
  %.9 = load i32, ptr %.8, align 4
  %.10 = mul i32 %.7, %.9
  %.11 = getelementptr inbounds { i32, i32 }, ptr %p, i32 0, i32 1
  %.12 = load i32, ptr %.11, align 4
  %.13 = getelementptr inbounds { i32, i32 }, ptr %p, i32 0, i32 1
  %.14 = load i32, ptr %.13, align 4
  %.15 = mul i32 %.12, %.14
  %.16 = add i32 %.10, %.15
  %.17 = sitofp i32 %.16 to double
  %.20 = fcmp ogt double %.17, 2.000000e+01
  %.21 = getelementptr inbounds [6 x i8], ptr @str_0, i32 0, i32 0
  %.22 = getelementptr inbounds [6 x i8], ptr @str_1, i32 0, i32 0
  %.23 = select i1 %.20, ptr %.21, ptr %.22
  %.26 = getelementptr inbounds [4 x i8], ptr @str_2, i32 0, i32 0
  %.27 = call i32 (ptr, ...) @printf(ptr %.26, ptr %.23)
  switch i32 2, label %switch_default [
    i32 1, label %switch_case
    i32 2, label %switch_case.1
  ]

switch_end:                                       ; preds = %switch_case.1, %switch_case, %switch_default
  %nums = alloca [5 x i32], align 4
  %.43 = getelementptr inbounds [5 x i32], ptr %nums, i32 0, i32 0
  store i32 5, ptr %.43, align 4
  %.45 = getelementptr inbounds [5 x i32], ptr %nums, i32 0, i32 1
  store i32 8, ptr %.45, align 4
  %.47 = getelementptr inbounds [5 x i32], ptr %nums, i32 0, i32 2
  store i32 13, ptr %.47, align 4
  %.49 = getelementptr inbounds [5 x i32], ptr %nums, i32 0, i32 3
  store i32 21, ptr %.49, align 4
  %.51 = getelementptr inbounds [5 x i32], ptr %nums, i32 0, i32 4
  store i32 34, ptr %.51, align 4
  %i = alloca i32, align 4
  store i32 0, ptr %i, align 4
  %total = alloca i32, align 4
  store i32 0, ptr %total, align 4
  br label %while_cond

switch_default:                                   ; preds = %entry
  %.39 = getelementptr inbounds [12 x i8], ptr @str_7, i32 0, i32 0
  %.40 = getelementptr inbounds [4 x i8], ptr @str_8, i32 0, i32 0
  %.41 = call i32 (ptr, ...) @printf(ptr %.40, ptr %.39)
  br label %switch_end

switch_case:                                      ; preds = %entry
  %.31 = getelementptr inbounds [11 x i8], ptr @str_3, i32 0, i32 0
  %.32 = getelementptr inbounds [4 x i8], ptr @str_4, i32 0, i32 0
  %.33 = call i32 (ptr, ...) @printf(ptr %.32, ptr %.31)
  br label %switch_end

switch_case.1:                                    ; preds = %entry
  %.35 = getelementptr inbounds [11 x i8], ptr @str_5, i32 0, i32 0
  %.36 = getelementptr inbounds [4 x i8], ptr @str_6, i32 0, i32 0
  %.37 = call i32 (ptr, ...) @printf(ptr %.36, ptr %.35)
  br label %switch_end

while_cond:                                       ; preds = %endif.1, %switch_end
  %.56 = load i32, ptr %i, align 4
  %.57 = icmp slt i32 %.56, 5
  br i1 %.57, label %while_body, label %while_end

while_body:                                       ; preds = %while_cond
  %r = alloca i32, align 4
  %.59 = load i32, ptr %i, align 4
  %.60 = getelementptr inbounds [5 x i32], ptr %nums, i32 0, i32 %.59
  %.61 = load i32, ptr %.60, align 4
  %.62 = srem i32 %.61, 2
  store i32 %.62, ptr %r, align 4
  %.64 = load i32, ptr %r, align 4
  %.65 = icmp eq i32 %.64, 0
  br i1 %.65, label %then, label %else

while_end:                                        ; preds = %then.1, %while_cond
  %.84 = call i32 @fibonacci(i32 10)
  %.85 = getelementptr inbounds [4 x i8], ptr @str_9, i32 0, i32 0
  %.86 = call i32 (ptr, ...) @printf(ptr %.85, i32 %.84)
  %.87 = load i32, ptr %total, align 4
  %.88 = getelementptr inbounds [4 x i8], ptr @str_10, i32 0, i32 0
  %.89 = call i32 (ptr, ...) @printf(ptr %.88, i32 %.87)
  ret i32 0

then:                                             ; preds = %while_body
  %.67 = load i32, ptr %total, align 4
  %.68 = load i32, ptr %i, align 4
  %.69 = getelementptr inbounds [5 x i32], ptr %nums, i32 0, i32 %.68
  %.70 = load i32, ptr %.69, align 4
  %.71 = add i32 %.67, %.70
  store i32 %.71, ptr %total, align 4
  br label %endif

else:                                             ; preds = %while_body
  br label %endif

endif:                                            ; preds = %else, %then
  %.75 = load i32, ptr %i, align 4
  %.76 = add i32 %.75, 1
  store i32 %.76, ptr %i, align 4
  %.78 = load i32, ptr %total, align 4
  %.79 = icmp sgt i32 %.78, 50
  br i1 %.79, label %then.1, label %else.1

then.1:                                           ; preds = %endif
  br label %while_end

else.1:                                           ; preds = %endif
  br label %endif.1

endif.1:                                          ; preds = %else.1
  br label %while_cond
}

define i32 @fibonacci(i32 %.1) {
entry:
  %.5 = icmp sle i32 %.1, 1
  br i1 %.5, label %then, label %else

then:                                             ; preds = %entry
  ret i32 %.1

else:                                             ; preds = %entry
  br label %endif

endif:                                            ; preds = %else
  %.11 = sub i32 %.1, 1
  %.12 = call i32 @fibonacci(i32 %.11)
  %.14 = sub i32 %.1, 2
  %.15 = call i32 @fibonacci(i32 %.14)
  %.16 = add i32 %.12, %.15
  ret i32 %.16
}
