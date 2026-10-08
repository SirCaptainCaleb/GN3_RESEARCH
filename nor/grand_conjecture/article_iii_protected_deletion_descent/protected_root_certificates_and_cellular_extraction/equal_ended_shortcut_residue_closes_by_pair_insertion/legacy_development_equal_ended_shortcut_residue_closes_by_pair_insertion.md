# Equal-ended shortcut residue closes by pair insertion — preserved pre-item development

## Equal-ended shortcut residue closes by pair insertion

Continue with §299. Let O=(w_1,...,w_m) have word 0^p1^q, and suppose both middle orientations fail to close or realize x->z. Then
A=B and C=D,
where
A=alpha(x,w_1,w_2),
C=alpha(z,w_1,w_2),
D=alpha(w_{m-1},w_m,x),
B=alpha(w_{m-1},w_m,z).

Assume first A=C=0. Then A=B=C=D=0.

Put
c=alpha(x,z,w_1).
For the full order
x,z,O
the first two statuses are
alpha(x,z,w_1)=c,
alpha(z,w_1,w_2)=C=0,
followed by the old zero prefix of O.
If c=0, this is compatible with the old 0^p1^q word and x,z,O is spanning NOR-good.

If c=1, reverse the inserted pair. The order
z,x,O
has first two statuses
alpha(z,x,w_1)=1-c=0,
alpha(x,w_1,w_2)=A=0,
again followed by the old zero prefix. Hence z,x,O is spanning NOR-good.

Thus the all-zero endpoint residue closes.

Now assume A=C=1, so A=B=C=D=1.

Put
d=alpha(w_m,x,z).
For
O,x,z
the final two statuses are
D=1, d.
If d=1, the old terminal 1-phase extends and O,x,z is spanning NOR-good.

If d=0, reverse the appended pair. The order
O,z,x
has final two statuses
B=1,
alpha(w_m,z,x)=1-d=1.
Hence O,z,x is spanning NOR-good.

Thus the all-one endpoint residue also closes.

Therefore the equal-ended case A=C is impossible in a counterexample.

### Consequence

After using both O and O^rev, every surviving three-block shortcut failure has necessarily
A != C.
After swapping names/colors if needed, normalize
A=B=0,
C=D=1.
Then the x-scan runs 0->1 and the z-scan runs 1->0 across O, and both
x O
and
O x
are NOR-good deletion orders omitting z.

So the entire unresolved shortcut problem is reduced to the oppositely-directed two-exterior scan case.
