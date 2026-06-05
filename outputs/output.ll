; ModuleID = "programa"
target triple = "x86_64-w64-windows-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"nums" = alloca [5 x i32]
  %".2" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  store i32 3, i32* %".2"
  %".4" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  store i32 1, i32* %".4"
  %".6" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 2
  store i32 4, i32* %".6"
  %".8" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 3
  store i32 1, i32* %".8"
  %".10" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 4
  store i32 5, i32* %".10"
  %"total" = alloca i32
  store i32 0, i32* %"total"
  %"i" = alloca i32
  store i32 0, i32* %"i"
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
  %".18" = load i32, i32* %"i"
  %".19" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".18"
  %".20" = load i32, i32* %".19"
  %".21" = srem i32 %".20", 2
  store i32 %".21", i32* %"r"
  %".23" = load i32, i32* %"r"
  %".24" = icmp eq i32 %".23", 0
  br i1 %".24", label %"then", label %"else"
while_end:
  %"msg" = alloca i32
  %".43" = add i32 0, 0
  store i32 %".43", i32* %"msg"
  %".45" = load i32, i32* %"msg"
  %".46" = bitcast [4 x i8]* @"fmt_2" to i8*
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46", i32 %".45")
  %".48" = load i32, i32* %"total"
  %".49" = bitcast [4 x i8]* @"fmt_3" to i8*
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49", i32 %".48")
  ret i32 0
then:
  %".26" = load i32, i32* %"total"
  %".27" = load i32, i32* %"i"
  %".28" = getelementptr inbounds [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".27"
  %".29" = load i32, i32* %".28"
  %".30" = add i32 %".26", %".29"
  store i32 %".30", i32* %"total"
  br label %"endif"
else:
  br label %"endif"
endif:
  %".34" = load i32, i32* %"i"
  %".35" = add i32 %".34", 1
  store i32 %".35", i32* %"i"
  %".37" = load i32, i32* %"total"
  %".38" = icmp sgt i32 %".37", 10
  br i1 %".38", label %"then.1", label %"else.1"
then.1:
  br label %"while_end"
else.1:
  br label %"endif.1"
endif.1:
  br label %"while_cond"
}

@"fmt_2" = constant [4 x i8] c"%d\0a\00"
@"fmt_3" = constant [4 x i8] c"%d\0a\00"
