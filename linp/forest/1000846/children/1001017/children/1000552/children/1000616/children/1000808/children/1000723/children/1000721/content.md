# Every charged four-edge spacing violation is tail-terminal or splice-blocked

## Statement

Let e_i={x_i,v,u_i}, i=1,2,3,4, be potential-charged ascending nonspecial edges through a common terminal v, with q_1<=q_2<=q_3<=q_4. Suppose 2q_2<q_1+q_4+1. Fix a q_4-edge path P_4 ending in e_4 with last vertex v, and a (q_1-1)-edge path Q_1 ending at x_1 such that Q_1,e_1 is a longest path ending in e_1. Then either (A) x_2 is absent from P_4 and u_2 occurs in one of the final q_2-2 precursor edges of P_4, or (B) x_2 lies on P_4 and the splice Q_1,e_1,e_4 followed by the reverse P_4-tail down to x_2 is not a linear path. Thus every spacing counterexample is forced into a terminal-tail state or an explicit cross-intersection obstruction.

## Body

Apply the terminal-tail blocker lemma to e_2 and P_4, which has length q_4>=q_2 and ends at the common terminal v. Since e_2 is distinct from the last edge e_4, e_2 is not used by P_4. Hence one of x_2,u_2 occurs in the final q_2-2 precursor edges of P_4. If x_2 is absent from P_4, this forces u_2 into that tail, giving (A). Now suppose x_2 lies on P_4. If the displayed splice were a linear path, the certified uncrossed-splice lemma would give 2q_2>=q_1+q_4+2, contradicting the assumed violation 2q_2<q_1+q_4+1. Therefore the splice is obstructed by an additional intersection, giving (B). The argument applies to every chosen P_4 and Q_1 of the stated types.
