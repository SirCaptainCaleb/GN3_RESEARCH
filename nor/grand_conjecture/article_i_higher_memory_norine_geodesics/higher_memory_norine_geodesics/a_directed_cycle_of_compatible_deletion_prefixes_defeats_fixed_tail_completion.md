# A directed cycle of compatible deletion prefixes defeats fixed-tail completion

For every m>=4, a reversal-antisymmetric ternary coloring can have a tail T=(t_1,...,t_m) with word 0 1^{m-3} and residual vertices a,b,c whose feasible predecessor graph is a directed cycle. The deletion orders (a,b,T), (b,c,T), (c,a,T) all have word 0^3 1^{m-3}, but all six full prefixes fail.

Prescribe h(z,t_1,t_2)=0; h(s,t,t_1)=0 precisely on a->b,b->c,c->a; and h(a,b,c)=h(b,c,a)=h(c,a,b)=1. Reverse tuples receive complementary colors. Tail windows receive the stated tail word. Cyclic full prefixes have word 1,0,0,0,1^{m-3}; reversed prefixes have 0,1,0,0,1^{m-3}.

The coloring is globally soluble: setting h(b,c,t_2)=h(c,t_2,t_3)=1 gives (t_1,a,b,c,t_2,...,t_m) word 0 1^m. The prescriptions occupy consistent reversal-orbits.

Thus even synchronized residual deletion existence need not produce the paired-prefix construction of section 38. An exchange must resolve the directed cycle while allowing the tail to change. This is an arbitrarily long symbolic obstruction to the attempted fixed-tail argument, not a counterexample to NOR.
