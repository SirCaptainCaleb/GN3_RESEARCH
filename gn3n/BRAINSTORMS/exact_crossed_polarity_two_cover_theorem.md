# Exact crossed-polarity two-cover theorem

Close the ideal two-camp polarity branch of the mediator-swap dichotomy by aligning the color camps on each side with the mediator camps on the other side.

Let |A|=|B|=r and suppose there are partitions

  A=U disjoint union W,
  B=C disjoint union D,

with |U|=|C| and |W|=|D|, together with tournaments R on A and S on B such that

  T_b[A]=R for every b in C,
  T_b[A]=reverse(R) for every b in D,

and symmetrically

  T_a[B]=S for every a in U,
  T_a[B]=reverse(S) for every a in W.

Choose directed Hamilton paths

  P_U=(u_1,...,u_c) in R[U],
  P_W=(w_1,...,w_d) in R[W],
  P_C=(c_1,...,c_c) in S[C],
  P_D=(d_1,...,d_d) in S[D],

where c=|C|=|U| and d=|D|=|W|.

Form the alternating spanning order

  pi=(u_1,c_1,u_2,c_2,...,u_c,c_c,w_1,d_1,w_2,d_2,...,w_d,d_d).

Consider the odd status stream. Inside U, every A-edge u_i u_{i+1} is forward in R and its mediator c_i belongs to C, so the status is tight. The U-W junction edge u_c w_1 is mediated by c_c in C and is unconstrained. Inside W, every edge w_i w_{i+1} is forward in R while its mediator d_i belongs to D and uses reverse(R), so the status is non-tight. Thus the odd stream is

  1^(c-1), star, 0^(d-1).

For the even stream, every edge c_i c_{i+1} is forward in S and is mediated by u_{i+1} in U, so it is tight. The C-D junction c_c d_1 is mediated by w_1 in W and is unconstrained. Every edge d_i d_{i+1} is forward in S but mediated by w_{i+1} in W, whose local tournament is reverse(S), so it is non-tight. Thus the even stream is

  1^(c-1), star, 0^(d-1)

with its junction interlaced immediately after the odd junction.

Consequently the full status word is all 1s before two consecutive junction positions and all 0s afterward. Equivalently q<=p+1. By the exact inversion-window criterion, pc(H)<=2.

Hence exact crossed two-camp polarity closes the grand target directly. No compatibility is required across the four chosen induced Hamilton paths; their only interaction is the equality of camp sizes.

This identifies the quantitative polarity target. It is enough to show that the robust two-camp decompositions on the two sides can be aligned into matched-size camps and corrected along four induced Hamilton backbones with sufficiently few local errors. The exact model itself is solved.
