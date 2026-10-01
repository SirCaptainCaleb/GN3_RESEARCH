# The four top-boundary missing-slot patterns reduce to crossed terminals plus two exact closures

## Statement

For q>=4, the all-visible top-boundary q,(q+1)^3 gadget has the following pattern structure. In abd, z_d is forced left and z_b right; z_a is right, with the only exact central closure z_a=c. In bcd, z_d is forced left and z_b right. In abc, either z_c is forced left or z_a=d, the missing slot. In acd, z_d,z_c are left and z_a right with the two-cell moat bounds. Thus every pattern contains an explicit left/right terminal crossing, and the only central escape states are the exact missing-slot closures z_a=c (abd) and z_a=d (abc).

## Body

Assume q>=4 and retain the all-visible four-slot top-boundary normal form.

Pattern abd.
Since d is occupied and b is also occupied, 94bd984bc952 gives
  z_d has a path occurrence no later than g_{q-3}.         (1)
Apply the bd conflict from 872bb5f4effc. Its alternatives are
  z_b in V(g_{q+1} union ... union g_{2q-3}),              (2)
or
  z_d in V(g_{q+1} union ... union g_{2q-3} union g_{q-1}).(3)
Alternative (3) is incompatible with (1), since a path vertex cannot occur in two nonconsecutive path edges and q-3 is separated from q-1 by at least one edge; more directly the selected left occurrence is the only possible retained occurrence under linearity of h_d with the central path. Hence (2) is forced.
Also 8479f1cdc5d5 gives z_a on the right, and c5b898ec9f36 sharpens the ad conflict: either z_d is left (already true) or z_a=c, the missing slot. Thus abd has one left terminal z_d and two right-side high terminals z_a,z_b, with the only central closure z_a=c.

Pattern bcd.
Again d and b are occupied, so 94bd984bc952 gives z_d by g_{q-3}. The same bd conflict forces
  z_b in V(g_{q+1} union ... union g_{2q-3}).
Thus bcd has the forced crossed pair z_d left, z_b right.

Pattern abc.
Here a is occupied, so 8479f1cdc5d5 puts z_a in the right suffix beginning at g_q. Apply the ac conflict from 872bb5f4effc. Either
  z_c in V(g_1 union ... union g_{q-2}),
or
  z_a in V(g_1 union ... union g_{q-2} union g_q).
By the right-side localization of z_a, the second alternative means z_a in g_q={x,c,d}. Linearity excludes x (low edge e) and c (occupied edge h_c), leaving exactly
  z_a=d,
the unique missing slot.
Hence abc either has a genuine left-crossing z_c or the exact missing-slot closure z_a=d.

Pattern acd.
By 5d36d3a8d0ec/e0bd1cc438eb, z_d and z_c are left while z_a is right, with
  last(z_d)<=q-4,
  last(z_c)<=q-3,
  first(z_a)>=q+2.

Therefore every top-boundary pattern already contains a forced left/right terminal crossing, except for exact missing-slot closures in abc or abd; even there the other occupied conflict pair still supplies a crossed terminal.
