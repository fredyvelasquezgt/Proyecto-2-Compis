	T0 <- 17 * 8
	T1 <- 11 + T0
L0 := T2 <- T1 @ variable1
	T3 <- 11 + 3
	T4 <- T3 + 8
	T5 <- T4 @ variable2
	T6 <- 7 * 8
	T7 <- 5 + T6
	T8 <- T7 + 2
	T9 <- T8 @ variable3
	T10 <- goto (main) L0
