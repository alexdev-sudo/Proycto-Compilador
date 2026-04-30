; ModuleID = "programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %"nums" = alloca [5 x i32]
  %".2" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  store i32 3, i32* %".2"
  %".4" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  store i32 1, i32* %".4"
  %".6" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 2
  store i32 4, i32* %".6"
  %".8" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 3
  store i32 1, i32* %".8"
  %".10" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 4
  store i32 5, i32* %".10"
  %"total" = alloca i32
  store i32 0, i32* %"total"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"r" = alloca i32
  %"msg" = alloca i8*
  br label %"while_cond"
while_cond:
  %".15" = load i32, i32* %"i"
  %".16" = icmp slt i32 %".15", 5
  br i1 %".16", label %"while_body", label %"while_end"
while_body:
  %".18" = load i32, i32* %"i"
  %".19" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".18"
  %".20" = load i32, i32* %".19"
  %".21" = srem i32 %".20", 2
  store i32 %".21", i32* %"r"
  %".23" = load i32, i32* %"r"
  %".24" = icmp ne i32 0, 0
  br i1 %".24", label %"if_then", label %"if_else"
while_end:
  %".43" = getelementptr [12 x i8], [12 x i8]* @"str_2", i32 0, i32 0
  %".44" = getelementptr [10 x i8], [10 x i8]* @"str_3", i32 0, i32 0
  %".45" = getelementptr [21 x i8], [21 x i8]* @"str_4", i32 0, i32 0
  store i8* %".45", i8** %"msg"
  %".47" = load i8*, i8** %"msg"
  %".48" = getelementptr [4 x i8], [4 x i8]* @"str_5", i32 0, i32 0
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i8* %".47")
  %".50" = load i32, i32* %"total"
  %".51" = getelementptr [4 x i8], [4 x i8]* @"str_6", i32 0, i32 0
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %".50")
  ret void
if_then:
  %".26" = load i32, i32* %"total"
  %".27" = load i32, i32* %"i"
  %".28" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 %".27"
  %".29" = load i32, i32* %".28"
  %".30" = add i32 %".26", %".29"
  store i32 %".30", i32* %"total"
  br label %"if_end"
if_else:
  br label %"if_end"
if_end:
  %".34" = load i32, i32* %"i"
  %".35" = add i32 %".34", 1
  store i32 %".35", i32* %"i"
  %".37" = load i32, i32* %"total"
  %".38" = icmp sgt i32 %".37", 10
  br i1 %".38", label %"if_then.1", label %"if_else.1"
if_then.1:
  br label %"while_end"
if_else.1:
  br label %"if_end.1"
if_end.1:
  br label %"while_cond"
}

declare i32 @"printf"(i8* %".1", ...)

@"str_2" = constant [12 x i8] c"Resultado: \00"
@"str_3" = constant [10 x i8] c"calculado\00"
@"str_4" = constant [21 x i8] c"Resultado: calculado\00"
@"str_5" = constant [4 x i8] c"%s\0a\00"
@"str_6" = constant [4 x i8] c"%d\0a\00"