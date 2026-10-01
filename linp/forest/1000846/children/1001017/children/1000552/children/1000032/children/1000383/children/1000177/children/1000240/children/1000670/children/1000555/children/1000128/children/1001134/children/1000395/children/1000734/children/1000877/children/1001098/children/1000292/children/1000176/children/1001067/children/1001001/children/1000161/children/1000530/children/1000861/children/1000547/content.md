# Return-order inversion has an exact two-splice loss identity

## Statement


Let R be a maximum endpoint path ending at y and S a maximum endpoint path ending at x, with x a vertex of R distinct from y. Suppose z_R,z_S are two further common vertices with the following nearest-return order:
- the open R-segment R(z_R,x) contains no vertex of S, and along R the order is z_S,z_R,x;
- the open S-segment S(z_S,x) contains no vertex of R, and along S the order is z_R,z_S,x.

Put
  A=|R[z_S,z_R]|,  B=|R[z_R,x]|,
  C=|S[z_R,z_S]|,  D=|S[z_S,x]|.

Then the two paths obtained by the clean tail switches
  S[start,z_R] followed by R[z_R,x],
and
  R[start,z_S] followed by S[z_S,x] followed by R[x,y]
are linear paths ending at x and y respectively.

Define their losses relative to S and R by
  delta_x=(C+D)-B,
  delta_y=(A+B)-D.
Then
  delta_x>=0,  delta_y>=0,
and exactly
  delta_x+delta_y=A+C.

Consequently
  max{delta_x,delta_y} >= (A+C)/2.
Thus a return-order inversion with a long reversed middle core necessarily incurs a comparably large loss in at least one of the two canonical endpoint-preserving switches.


## Body


Because the open R-segment R(z_R,x) contains no vertex of S, the prefix of S ending at z_R followed by R[z_R,x] is a linear path ending at x. Its length differs from |S| only in that the S-tail from z_R to x, of length C+D, is replaced by the R-tail of length B. Since S is a maximum endpoint path ending at x,
  B <= C+D.
Hence
  delta_x=(C+D)-B >=0.

Similarly, because the open S-segment S(z_S,x) contains no vertex of R, replace in R the segment R[z_S,x] by S[z_S,x]. The resulting edge sequence is the R-prefix ending at z_S, followed by S[z_S,x], followed by the original R-suffix from x to y. It is a linear path ending at y. Maximality of R gives
  D <= A+B,
so
  delta_y=(A+B)-D >=0.

Adding the two displayed losses cancels B and D:
  delta_x+delta_y
   = (C+D-B)+(A+B-D)
   = A+C.
The final inequality follows immediately.
