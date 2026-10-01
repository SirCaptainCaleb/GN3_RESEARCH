# The surviving one-low odd-boundary state forces D terminal-only

## Statement

In the sole surviving p=2q-3 one-low all-single pattern, the contacts are A,B,C,D with the rank-q edge terminal-only at C. The rank-(q+1) edge using D=private(g_{q-1}) is also necessarily terminal-only. If D were its clean entrance, the occupied earlier A-contact lies only two path positions earlier, contradicting the quantitative clean-contact separation requirement k-j>=q-1 for q>=4.

## Body


Retain the surviving one-low odd-central all-single pattern of 45efc91c2ba8:
  p=phi(v)=2q-3, q>=4,
  P=(g_1,...,g_p),
and the occupied single-contact slots are
  A=g_{q-3} cap g_{q-2},
  B=private(g_{q-2}),
  C=g_{q-2} cap g_{q-1},
  D=private(g_{q-1}).
The low rank-q edge uses C terminal-only.

Let h_D be the rank-(q+1) high edge whose sole P-contact is D. Suppose for contradiction that D is its visible unique entrance. Then h_D is a clean single-contact edge on P with a private entrance at path position
  k=q-1.

The occupied A-edge is another single-contact ascending edge through v. Its contact A first occurs on
  g_{q-3},
so in the notation of the quantitative clean-contact separation lemma 65894e91ed50 we may take
  j=q-3.

Since k=j+2, part (a) of 65894e91ed50 applies and gives
  k-j >= p-phi(h_D)+3.
Here
  p=2q-3,
  phi(h_D)=q+1,
so the required gap is
  p-(q+1)+3=q-1.
But the actual gap is
  k-j=2,
and q>=4 gives q-1>=3. Contradiction.

Therefore D cannot be the entrance of h_D. Since h_D is single-contact on P, its sole P-contact D is its opposite terminal, while its unique entrance is absent from P.
