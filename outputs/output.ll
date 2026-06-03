; ModuleID = "programa"
target triple = "x86_64-w64-windows-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i8* @"strcat"(i8* %".1", i8* %".2")

declare i8* @"malloc"(i64 %".1")

define i32 @"main"()
{
entry:
  %"p" = alloca {i32, i32}
  %".2" = getelementptr inbounds {i32, i32}, {i32, i32}* %"p", i32 0, i32 0
  store i32 3, i32* %".2"
  %".4" = getelementptr inbounds {i32, i32}, {i32, i32}* %"p", i32 0, i32 1
  store i32 4, i32* %".4"
  %"dist" = alloca double
  %".6" = getelementptr inbounds {i32, i32}, {i32, i32}* %"p", i32 0, i32 0
  %".7" = load i32, i32* %".6"
  %".8" = getelementptr inbounds {i32, i32}, {i32, i32}* %"p", i32 0, i32 0
  %".9" = load i32, i32* %".8"
  %".10" = mul i32 %".7", %".9"
  %".11" = getelementptr inbounds {i32, i32}, {i32, i32}* %"p", i32 0, i32 1
  %".12" = load i32, i32* %".11"
  %".13" = getelementptr inbounds {i32, i32}, {i32, i32}* %"p", i32 0, i32 1
  %".14" = load i32, i32* %".13"
  %".15" = mul i32 %".12", %".14"
  %".16" = add i32 %".10", %".15"
  %".17" = sitofp i32 %".16" to double
  store double %".17", double* %"dist"
  %"etiqueta" = alloca i8*
  %".19" = load double, double* %"dist"
  %".20" = fcmp ogt double %".19", 0x4034000000000000
  %".21" = getelementptr inbounds [6 x i8], [6 x i8]* @"str_0", i32 0, i32 0
  %".22" = getelementptr inbounds [6 x i8], [6 x i8]* @"str_1", i32 0, i32 0
  %".23" = select  i1 %".20", i8* %".21", i8* %".22"
  store i8* %".23", i8** %"etiqueta"
  %".25" = load i8*, i8** %"etiqueta"
  %".26" = getelementptr inbounds [4 x i8], [4 x i8]* @"str_2", i32 0, i32 0
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26", i8* %".25")
  %"opcion" = alloca i32
  store i32 2, i32* %"opcion"
  %".29" = load i32, i32* %"opcion"
  switch i32 %".29", label %"switch_default" [i32 1, label %"switch_case" i32 2, label %"switch_case.1"]
switch_end:
  %"nums" = alloca [5 x i32]
  %".43" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  store i32 5, i32* %".43"
  %".45" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  store i32 8, i32* %".45"
  %".47" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 2
  store i32 13, i32* %".47"
  %".49" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 3
  store i32 21, i32* %".49"
  %".51" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 4
  store i32 34, i32* %".51"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"total" = alloca i32
  store i32 0, i32* %"total"
  br label %"while_cond"
switch_default:
  %".39" = getelementptr inbounds [12 x i8], [12 x i8]* @"str_7", i32 0, i32 0
  %".40" = getelementptr inbounds [4 x i8], [4 x i8]* @"str_8", i32 0, i32 0
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i8* %".39")
  br label %"switch_end"
switch_case:
  %".31" = getelementptr inbounds [11 x i8], [11 x i8]* @"str_3", i32 0, i32 0
  %".32" = getelementptr inbounds [4 x i8], [4 x i8]* @"str_4", i32 0, i32 0
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32", i8* %".31")
  br label %"switch_end"
switch_case.1:
  %".35" = getelementptr inbounds [11 x i8], [11 x i8]* @"str_5", i32 0, i32 0
  %".36" = getelementptr inbounds [4 x i8], [4 x i8]* @"str_6", i32 0, i32 0
  %".37" = call i32 (i8*, ...) @"printf"(i8* %".36", i8* %".35")
  br label %"switch_end"
while_cond:
  %".56" = load i32, i32* %"i"
  %".57" = icmp slt i32 %".56", 5
  br i1 %".57", label %"while_body", label %"while_end"
while_body:
  %"r" = alloca i32
  %".59" = load i32, i32* %"i"
  %".60" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".59"
  %".61" = load i32, i32* %".60"
  %".62" = srem i32 %".61", 2
  store i32 %".62", i32* %"r"
  %".64" = load i32, i32* %"r"
  %".65" = icmp eq i32 %".64", 0
  br i1 %".65", label %"then", label %"else"
while_end:
  %".84" = call i32 @"fibonacci"(i32 10)
  %".85" = getelementptr inbounds [4 x i8], [4 x i8]* @"str_9", i32 0, i32 0
  %".86" = call i32 (i8*, ...) @"printf"(i8* %".85", i32 %".84")
  %".87" = load i32, i32* %"total"
  %".88" = getelementptr inbounds [4 x i8], [4 x i8]* @"str_10", i32 0, i32 0
  %".89" = call i32 (i8*, ...) @"printf"(i8* %".88", i32 %".87")
  ret i32 0
then:
  %".67" = load i32, i32* %"total"
  %".68" = load i32, i32* %"i"
  %".69" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".68"
  %".70" = load i32, i32* %".69"
  %".71" = add i32 %".67", %".70"
  store i32 %".71", i32* %"total"
  br label %"endif"
else:
  br label %"endif"
endif:
  %".75" = load i32, i32* %"i"
  %".76" = add i32 %".75", 1
  store i32 %".76", i32* %"i"
  %".78" = load i32, i32* %"total"
  %".79" = icmp sgt i32 %".78", 50
  br i1 %".79", label %"then.1", label %"else.1"
then.1:
  br label %"while_end"
else.1:
  br label %"endif.1"
endif.1:
  br label %"while_cond"
}

@"str_0" = internal constant [6 x i8] [i8 108, i8 101, i8 106, i8 111, i8 115, i8 0]
@"str_1" = internal constant [6 x i8] [i8 99, i8 101, i8 114, i8 99, i8 97, i8 0]
@"str_2" = internal constant [4 x i8] [i8 37, i8 115, i8 10, i8 0]
@"str_3" = internal constant [11 x i8] [i8 111, i8 112, i8 99, i8 105, i8 111, i8 110, i8 32, i8 117, i8 110, i8 111, i8 0]
@"str_4" = internal constant [4 x i8] [i8 37, i8 115, i8 10, i8 0]
@"str_5" = internal constant [11 x i8] [i8 111, i8 112, i8 99, i8 105, i8 111, i8 110, i8 32, i8 100, i8 111, i8 115, i8 0]
@"str_6" = internal constant [4 x i8] [i8 37, i8 115, i8 10, i8 0]
@"str_7" = internal constant [12 x i8] [i8 111, i8 116, i8 114, i8 97, i8 32, i8 111, i8 112, i8 99, i8 105, i8 111, i8 110, i8 0]
@"str_8" = internal constant [4 x i8] [i8 37, i8 115, i8 10, i8 0]
define i32 @"fibonacci"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %".4" = load i32, i32* %"n"
  %".5" = icmp sle i32 %".4", 1
  br i1 %".5", label %"then", label %"else"
then:
  %".7" = load i32, i32* %"n"
  ret i32 %".7"
else:
  br label %"endif"
endif:
  %".10" = load i32, i32* %"n"
  %".11" = sub i32 %".10", 1
  %".12" = call i32 @"fibonacci"(i32 %".11")
  %".13" = load i32, i32* %"n"
  %".14" = sub i32 %".13", 2
  %".15" = call i32 @"fibonacci"(i32 %".14")
  %".16" = add i32 %".12", %".15"
  ret i32 %".16"
}

@"str_9" = internal constant [4 x i8] [i8 37, i8 100, i8 10, i8 0]
@"str_10" = internal constant [4 x i8] [i8 37, i8 100, i8 10, i8 0]