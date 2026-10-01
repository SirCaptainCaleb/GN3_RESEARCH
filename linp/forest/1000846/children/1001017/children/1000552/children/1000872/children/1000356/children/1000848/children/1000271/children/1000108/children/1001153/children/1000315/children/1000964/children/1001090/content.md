# The rising one-low branch becomes a four-slot oriented-chord conflict system

## Statement

If the low opposite terminal C has phi(C)=2q-2, then on its chosen maximum path the three high rank-(q+1) sources occupy three distinct slots among L=joint(q-2,q-1), A=private(q-1), B=private(q), R=joint(q,q+1), around the central low entrance x. Each high edge is a two-sided chord. A left-joint source L paired with any right source forces either its own terminal into r_q or the right source terminal into the left prefix; symmetrically for R. In source patterns {L,B,R} or {L,A,R}, linearity removes the central escape and forces both opposite terminals across the cut.

## Body

Retain the rising low-terminal branch d734b1420b2f. Thus
  R=(r_1,...,r_{2q-2})
is the chosen maximum path ending at C,
  x=r_{q-1} cap r_q
is the sole contact of the low edge e={x,v,C},
and v is absent from R.

Let h_i={y_i,v,z_i}, i=1,2,3, be the three rank-(q+1) 0-1-1 high edges. By d734b1420b2f, each h_i has exactly one non-v contact in each half
  R_L=r_1,...,r_{q-1},
  R_R=r_q,...,r_{2q-2}.
Its entrance/source satisfies phi(y_i)=q.

Apply the certified half-path endpoint-potential bound 8b1790d79d74 to y_i on the (2q-2)-edge path R. If y_i is private in r_j, then
  max{j,2q-2-j+1}<=q,
so j is q-1 or q.
If y_i=r_j cap r_{j+1}, then
  max{j,2q-2-j}<=q,
so j is in {q-2,q-1,q}.
The central joint j=q-1 is x, but no h_i can contain x because h_i and e already share v. Hence every source y_i belongs to exactly one of the four slots
  L=r_{q-2} cap r_{q-1},
  A=private(r_{q-1}),
  B=private(r_q),
  R0=r_q cap r_{q+1}.

The three source vertices are distinct by linearity of the three edges through v, so they occupy three of these four slots.

Now suppose L is a source, say h_L={L,v,z_L}, and y is a right-side source B or R0 of another high edge h_y={y,v,z_y}. Consider
  r_1,...,r_{q-2}, h_L,h_y,r_q.                      (*)
The displayed sequence has q+1 edges and, if linear, ends physically at
  x=r_{q-1} cap r_q,
contradicting phi(x)=q-1.

The only possible nonconsecutive obstructions are:
- z_L in r_q;
- z_y somewhere in r_1 union ... union r_{q-2}.
All source vertices are already accounted for, v is absent from R, and r_{q-2} is disjoint from r_q because r_{q-1} is omitted. Hence for every right source y,
  z_L in V(r_q)
  OR
  z_y in V(r_1 union ... union r_{q-2}).             (L-conflict)

Symmetrically, if R0 is a source and y is a left-side source L or A, the reversed splice
  r_{2q-2},...,r_{q+1}, h_{R0},h_y,r_{q-1}
has q+1 edges and would end at x. Therefore
  z_{R0} in V(r_{q-1})
  OR
  z_y in V(r_{q+1} union ... union r_{2q-2}).        (R-conflict)

These alternatives sharpen when the two slots of the opposite central edge are themselves occupied by sources. For example, if the source set contains {L,B,R0}, then r_q={x,B,R0}; by linearity z_L can equal none of x,B,R0, so z_L is not in r_q. Hence both z_B and z_{R0} must lie in the left prefix. The symmetric statement holds for source set {L,A,R0}: then z_{R0} cannot lie in r_{q-1}={L,A,x}, so z_L and z_A both lie in the right suffix.
