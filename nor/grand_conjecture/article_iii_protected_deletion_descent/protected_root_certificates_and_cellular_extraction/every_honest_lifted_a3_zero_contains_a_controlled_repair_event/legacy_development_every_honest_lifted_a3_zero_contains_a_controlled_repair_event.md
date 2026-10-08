# Every honest lifted A3 zero contains a controlled repair event — preserved pre-item development

Work in the coboundary-flat alternating ternary sector and one exact A3 Coxeter block B of four coordinates. Consider a positive zero of honest switch-prism labels (rho,s) supported in this block. Its physical root component is a positive circulation on the four block coordinates.

Normalize the pre-switch target color to 0. Thus a violating window has actual color y=1 on the pre-switch side and y=0 on the post-switch side.

For an oriented physical edge u->v inside B there are exactly two possible middle coordinates in B. If the selected middle is violating but the alternative middle is satisfied at the same internal window rank, connect those chamber states inside the product cell. Along a 1-skeleton path the tracked violation must first disappear; the arbitrary-cell extraction theorem yields a controlled repair. We therefore analyze a simple physical cycle under the contrary assumption that BOTH possible middle triples violate for every edge.

Write B={0,1,2,3} and
A=alpha(0,1,2), Bf=alpha(0,1,3), C=alpha(0,2,3), D=alpha(1,2,3).

### Directed triangle
For 0->1->2->0, let y_i be the violation color on edge i.

No alternate-middle repair gives
A=Bf=1-y_0,
A=D=1-y_1,
1-A=C=y_2.
Hence y_0=y_1=y_2=:y and the face pattern is
A=Bf=D=1-y, C=y.
Its tetrahedral xor is 1, contradicting coboundary flatness. Therefore every directed triangle contains an edge with a satisfying alternate middle.

### Directed four-cycle
For 0->1->2->3->0, absence of alternate-middle repairs gives
A=Bf=1-y_0,
A=D=1-y_1,
C=D=1-y_2,
Bf=C=1-y_3.
Thus all y_i are equal and all four face bits A,Bf,C,D are equal to 1-y.

So a repair-free directed four-cycle is possible only when ALL four selected violations lie on the same switch side. It is maximally side-imbalanced.

### Directed two-cycle
For 0->1 and 1->0, no alternate-middle repair gives
A=Bf=1-y_0
and
A=Bf=y_1.
Thus y_1=1-y_0: the two violations lie on opposite sides. This is a two-term honest lifted reversal pair, already handled by the two-term A3 extraction theorem, which gives a controlled repair whether the selected middles coincide or differ.

### From simple cycles to an arbitrary lifted zero
Decompose the positive physical circulation into directed simple cycles. If any constituent is a two-cycle or triangle, it contains a controlled repair. If a four-cycle uses both switch sides, it also contains a controlled repair by the four-cycle calculation.

Therefore, if NO controlled repair occurs anywhere in the support, every constituent physical cycle must be a four-cycle whose labels all lie on one common side.

But the lifted scalar equation requires total positive weight on the two switch sides to balance. Hence there must be at least one all-pre four-cycle and at least one all-post four-cycle in the decomposition.

An all-pre repair-free four-cycle has y=1 and therefore forces
A=Bf=C=D=0
on the unique four-set B.
An all-post repair-free four-cycle has y=0 and forces
A=Bf=C=D=1
on the same four-set.
These cannot coexist.

Therefore every positive honest side-lifted switch-prism zero supported in one ternary A3 Coxeter block contains a controlled local repair event.

Combined with the complete A2 extraction theorem, a genuinely unextracted lifted topological obstruction cannot be supported in a Coxeter block of size three or four. Its block size is at least five (A4).
