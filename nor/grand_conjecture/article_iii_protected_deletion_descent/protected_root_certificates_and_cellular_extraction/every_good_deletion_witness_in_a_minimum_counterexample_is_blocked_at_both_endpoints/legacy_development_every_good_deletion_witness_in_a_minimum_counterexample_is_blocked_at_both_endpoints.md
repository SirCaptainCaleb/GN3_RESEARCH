# Every good deletion witness in a minimum counterexample is blocked at both endpoints — preserved pre-item development

## Every good deletion witness in a minimum counterexample is blocked at both endpoints

Work in the coboundary-flat alternating ternary sector of a minimum counterexample.

Fix a coordinate (x) and any NOR-good deletion order
[
O=(v_1,ldots,v_m)
]
of (Vsetminus{x}).

### The deletion word is genuinely bichromatic

If (O) were monochromatic, then prepending or appending (x) would create only one new ternary window and hence a full order with at most one change, contradicting counterexamplehood.

Therefore (O) has exactly one change. After reversal and global color normalization, write
[
w(O)=0^p1^q,qquad p,qge1.
]

By the short-phase closure theorem §259, in a minimum counterexample one in fact has
[
p,qge3.
]

### Prepending the omitted coordinate

The full order
[
(x,v_1,ldots,v_m)
]
has the old deletion word as its suffix and only one new initial ternary window.

By §282 every full order obtained from a good deletion witness in a minimum counterexample must have exactly two changes. Hence the new initial bit cannot be (0); otherwise the full word would remain one-change.

Therefore
[
alpha(x,v_1,v_2)=1
]
and the full profile is exactly
[
oxed{1,0^p1^q.}
]

### Appending the omitted coordinate

Similarly,
[
(v_1,ldots,v_m,x)
]
adds only one new final ternary window. Exact variation two forces that bit to differ from the old final color (1). Hence
[
alpha(v_{m-1},v_m,x)=0
]
and the full profile is exactly
[
oxed{0^p1^q,0.}
]

### Two-ended insertion scan consequence

Define the insertion scan
[
s_i^x=alpha(x,v_i,v_{i+1}).
]
Cyclic invariance gives
[
s_1^x=1,qquad
s_{m-1}^x=alpha(x,v_{m-1},v_m)
=alpha(v_{m-1},v_m,x)=0.
]

Thus **every** good deletion witness in a minimum counterexample has an (x)-scan beginning at (1) and ending at (0). In particular the scan has at least one (1	o0) descent.

### Consequence

The arbitrary-scan endpoint problem has no free endpoint data once minimum counterexamplehood is imposed:

- every deletion witness has two nontrivial phases, each of length at least three;
- insertion of the omitted coordinate is blocked at both ends in opposite colors;
- every insertion scan has a genuine descent from 1 to 0.

This places every omitted coordinate directly inside the protected insertion/scan machinery, without choosing a special perfect-blocker scan or a minimum-first witness.
