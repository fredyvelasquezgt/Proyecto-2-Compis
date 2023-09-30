	_r0 <- n = 1
	_r1 <- not _r0
l_0 := _r2 <- 1 @ f
	_r3 <- n = 2
	_r4 <- not _r3
l_1 := _r5 <- 1 @ f
	_r6 <- n - 1
	_r7 <- goto fibonacci (_r6)
	_r8 <- n - 2
	_r9 <- goto fibonacci (_r8)
	_r10 <- _r7 + _r9
l_2 := _r11 <- _r10 @ f
l_3 := goto l_1 if _r3
	goto l_2 if _r4
l_4 := goto l_0 if _r0
	goto l_3 if _r1
	_r16 <- let l_4
	_r17 <- f
l_5 := _r18 <- _r16
	_r19 <- goto (fibonacci) l_5
	_r20 <- 5 + 6
l_6 := _r21 <- _r20 @ n
	_r22 <- goto (fibonacci) l_6
	_r23 <- goto (copy) self
	_r24 <- 5 + 6
l_7 := _r25 <- _r24 @ n
	_r26 <- true
	_r27 <- _r26 @ s
	_r28 <- not s
	_r29 <- _r28 @ t
	_r30 <- new Fibonacci
	_r31 <- _r30 @ myfibonacci
	_r32 <- goto myfibonacci.fibonacci (n)
	_r33 <- goto out_int (_r32)
	_r34 <- goto (main) l_7
