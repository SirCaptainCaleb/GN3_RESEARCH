# A five-side with no neutral endpoint exchange forces reversed displayed edges on both long components

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover that is Phi-minimal in a trapped pairwise-repartition component, with |X|=5 and |P|,|Q|>=7. Suppose none of the equal-Phi endpoint support exchanges supplied by astra003fiveswapobstruct is legal at any of the four displayed endpoints of P and Q. Then there exist vertices x_P,x_Q in V(X), not necessarily distinct, such that x_P is noninsertable into every position of the displayed order of P and x_Q is noninsertable into every position of the displayed order of Q. Consequently some tight triple reverses a displayed edge of P and some tight triple reverses a displayed edge of Q.

## Body

Apply astra003fivecommoncore to the pair X|P. With P=(p_1,...,p_m), define I_L={x in X:(X-{x}) union {p_1} is Hamiltonian} and I_R={x in X:(X-{x}) union {p_m} is Hamiltonian}. Both sets have order at least three, so they intersect. Because by hypothesis neither endpoint support exchange is legal, 45229a54c95a shows that every x in I_L intersect I_R is noninsertable into the full displayed path P. Choose one such vertex and call it x_P. Apply the same argument independently to the pair X|Q to obtain x_Q in X noninsertable into every position of Q. Finally apply acdec36ae3ca to P with x_P and to Q with x_Q. It yields a tight triple reversing one displayed edge of P and, independently, a tight triple reversing one displayed edge of Q. The labels x_P,x_Q may coincide; no distinction is required. No path reversal or cyclic permutation is used.
