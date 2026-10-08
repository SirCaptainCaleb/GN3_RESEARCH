# Crossed blocker replacements synchronize across the two endpoint rotations — preserved pre-item development

## Crossed blocker replacements synchronize across the two endpoint rotations

Work in the Type-I crossed blocker normalization of §304. Let
[
O=(w_1,ldots,w_m)
]
have word
[
0^p1^q,
]
and suppose
[
A=alpha(x,w_1,w_2)=1,qquad
B=alpha(z,w_1,w_2)=0,
]
[
C=alpha(w_{m-1},w_m,x)=0,qquad
D=alpha(w_{m-1},w_m,z)=1,
]
with pair bits
[
E=alpha(x,z,w_1)=1,qquad
F=alpha(w_m,x,z)=1.
]

Then both
[
H_L=zO,qquad H_R=Oz
]
are NOR-good deletion witnesses omitting (x).

Their words are
[
w(H_L)=0^{p+1}1^q,qquad
w(H_R)=0^p1^{q+1}.
]

### The x-scans have one common core

Let
[
s_i=alpha(x,w_i,w_{i+1})
]
be the x-scan along the common middle order (O).

For (H_L=zO), the scan of the omitted coordinate (x) is
[
(E,s_1,s_2,ldots,s_{m-1})
=
(1,s_1,ldots,s_{m-1}).
]

For (H_R=Oz), the final scan bit is
[
alpha(x,w_m,z)=1-alpha(w_m,x,z)=1-F=0,
]
so its scan is
[
(s_1,s_2,ldots,s_{m-1},0).
]

Thus the two scans differ only by the endpoint padding:
[
oxed{
operatorname{scan}_x(H_L)=1,s,qquad
operatorname{scan}_x(H_R)=s,0.
}
]

### The protected replacement coordinate is identical

The switch rank of (H_L) is (p+1), while that of (H_R) is (p).

In the arbitrary-scan replacement theorem, the decisive five-bit core for (H_L) is
[
s_{p-1},s_p,s_{p+1},s_{p+2},s_{p+3},
]
after shifting the scan index by the initial coordinate (z).

For (H_R) the decisive five-bit core is the same five bits.

Hence both witnesses choose the same branch:

- if the middle scan bit selects the left replacement, both replace the same physical coordinate (w_p) by (x);
- if it selects the right replacement, both replace the same physical coordinate (w_{p+3}) by (x).

In either case the newly omitted coordinate is the same in both outputs.

### Rotation-pair invariance

Let the common replacement transform the middle coordinate order (O) into (O'), with newly omitted coordinate (u).

The two resulting good deletion witnesses are again
[
zO',qquad O'z,
]
now both omitting (u).

Their phase profiles still differ by exactly one endpoint window:
[
(P+1,Q),qquad(P,Q+1)
]
for the new middle profile (0^P1^Q).

Therefore the crossed-blocker replacement dynamics can be iterated **synchronously** on the pair of endpoint rotations.

### Consequence

The crossed shortcut residue carries a stronger invariant than one frozen endpoint:

[
oxed{	ext{the same distinguished coordinate }z	ext{ can be kept at either global endpoint throughout the entire replacement trajectory}.}
]

Any local recurrence, phase drift, or protected-root exit produced by the arbitrary-scan dynamics occurs in the common middle coordinates and is witnessed simultaneously with (z) placed on either side.

Thus a terminal protected-root exit from the crossed residue comes with two full provenance carriers differing only by moving (z) from the first endpoint to the last. This is the natural input for the final relative splice.
