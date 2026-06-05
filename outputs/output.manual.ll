; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-pc-linux-gnu"

@str_0 = internal constant [6 x i8] c"lejos\00"
@str_5 = internal constant [11 x i8] c"opcion dos\00"
@str_9 = internal constant [4 x i8] c"%d\0A\00"
@str_10 = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %puts = tail call i32 @puts(ptr nonnull dereferenceable(1) @str_0)
  %puts3 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str_5)
  %nums = alloca [5 x i32], align 16
  store <4 x i32> <i32 5, i32 8, i32 13, i32 21>, ptr %nums, align 16
  %.51 = getelementptr inbounds nuw i8, ptr %nums, i64 16
  store i32 34, ptr %.51, align 16
  br label %while_body

while_body:                                       ; preds = %while_body, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %.76, %while_body ]
  %total.0 = phi i32 [ 0, %entry ], [ %spec.select, %while_body ]
  %0 = zext nneg i32 %i.0 to i64
  %.60 = getelementptr inbounds nuw [5 x i32], ptr %nums, i64 0, i64 %0
  %.61 = load i32, ptr %.60, align 4
  %1 = and i32 %.61, 1
  %.65 = icmp eq i32 %1, 0
  %.71 = select i1 %.65, i32 %.61, i32 0
  %spec.select = add i32 %.71, %total.0
  %.76 = add nuw nsw i32 %i.0, 1
  %.79 = icmp slt i32 %spec.select, 51
  %.57 = icmp samesign ult i32 %i.0, 4
  %or.cond = and i1 %.57, %.79
  br i1 %or.cond, label %while_body, label %while_end

while_end:                                        ; preds = %while_body
  %.84 = tail call i32 @fibonacci(i32 10)
  %.86 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @str_9, i32 %.84)
  %.89 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @str_10, i32 %spec.select)
  ret i32 0
}

; Function Attrs: nofree nosync nounwind memory(none)
define i32 @fibonacci(i32 %.1) local_unnamed_addr #1 {
entry:
  %.54 = icmp slt i32 %.1, 2
  br i1 %.54, label %common.ret, label %endif

common.ret:                                       ; preds = %endif, %entry
  %accumulator.tr.lcssa = phi i32 [ 0, %entry ], [ %.16, %endif ]
  %.1.tr.lcssa = phi i32 [ %.1, %entry ], [ %.14, %endif ]
  %accumulator.ret.tr = add i32 %.1.tr.lcssa, %accumulator.tr.lcssa
  ret i32 %accumulator.ret.tr

endif:                                            ; preds = %endif, %entry
  %.1.tr6 = phi i32 [ %.14, %endif ], [ %.1, %entry ]
  %accumulator.tr5 = phi i32 [ %.16, %endif ], [ 0, %entry ]
  %.11 = add nsw i32 %.1.tr6, -1
  %.12 = tail call i32 @fibonacci(i32 %.11)
  %.14 = add nsw i32 %.1.tr6, -2
  %.16 = add i32 %.12, %accumulator.tr5
  %.5 = icmp samesign ult i32 %.1.tr6, 4
  br i1 %.5, label %common.ret, label %endif
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
attributes #1 = { nofree nosync nounwind memory(none) }
