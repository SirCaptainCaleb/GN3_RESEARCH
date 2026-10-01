# Uncrossed splice gives four-edge spacing

## Statement

Let e_1,e_2,e_4 be ascending nonspecial edges of a linear 3-graph sharing a common last vertex v, with q_i=φ(e_i) and q_1<=q_2<=q_4. Let x_i be the unique entrance of e_i. Let P_4 be a q_4-edge path ending in e_4 with last vertex v, and suppose x_2 lies on P_4. Let Q_1 be a (q_1-1)-edge path ending at x_1 such that Q_1,e_1 is a longest path ending in e_1. If Q_1,e_1,e_4 followed by the reverse tail of P_4 from the edge preceding e_4 down to x_2 is a linear path, then 2q_2>=q_1+q_4+2. If x_2 is private to a single edge of P_4, the stronger bound 2q_2>=q_1+q_4+3 holds.

## Body

Proof. Because e_2 is ascending, φ(x_2)=q_2-1. Split P_4 at x_2. Let α be the length of a prefix of P_4 ending at x_2, and let β be the number of precursor edges of P_4 that can be traversed backwards from the edge preceding e_4 to a final edge ending at x_2. If x_2 is private to one edge of P_4 then α+β=q_4; if x_2 is the intersection of two consecutive edges then α+β=q_4-1. Thus in all cases α+β>=q_4-1. Since the prefix ending at x_2 is a linear path, α<=φ(x_2)=q_2-1.

By hypothesis the concatenation Q_1,e_1,e_4 followed by that reverse tail is a linear path ending at x_2. Its length is (q_1-1)+2+β=q_1+β+1. Hence q_1+β+1<=φ(x_2)=q_2-1, so β<=q_2-q_1-2. Combining with α<=q_2-1 and α+β>=q_4-1 gives

q_4-1 <= 2q_2-q_1-3,

and therefore 2q_2>=q_1+q_4+2. In the private-vertex case α+β=q_4, yielding 2q_2>=q_1+q_4+3.

Thus a violation of the conjectural four-edge spacing inequality cannot occur in this uncrossed configuration. Any counterexample must force an additional intersection between Q_1 or e_1 and the reverse P_4 tail (or otherwise prevent the stated splice).
