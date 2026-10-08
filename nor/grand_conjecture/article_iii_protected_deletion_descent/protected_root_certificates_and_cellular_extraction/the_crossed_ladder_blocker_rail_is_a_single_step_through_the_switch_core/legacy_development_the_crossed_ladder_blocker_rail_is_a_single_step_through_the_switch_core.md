# The crossed ladder blocker rail is a single step through the switch core — preserved pre-item development

## The crossed ladder blocker rail is a single step through the switch core

Use the normalization of §310:
[
X_1=0,quad Z_1=1,qquad
X_{m-1}=1,quad Z_{m-1}=0,
]
for a good middle order
[
O=(w_1,ldots,w_m),qquad w(O)=0^p1^q.
]
The rung bits satisfy (R_1=R_m=0).

Then
[
xO,qquad Ox
]
are both NOR-good deletion witnesses omitting (z).

### The two z-scans are endpoint paddings of one rail

For (xO), the (z)-insertion scan begins with
[
alpha(z,x,w_1)=1-alpha(x,z,w_1)=1-R_1=1,
]
followed by
[
Z_1,ldots,Z_{m-1}.
]
Thus
[
operatorname{scan}_z(xO)=1,Z.
]

For (Ox), the final scan bit is
[
alpha(z,w_m,x)=alpha(w_m,x,z)=R_m=0
]
by cyclic invariance. Hence
[
operatorname{scan}_z(Ox)=Z,0.
]

Since every insertion of the omitted coordinate (z) into either good deletion witness would be a full ambient order, (z) blocks every insertion into both carriers.

### The same five-bit core is constrained twice

The switch rank of (xO) is (p+1). Applying the arbitrary blocking-scan theorem to its scan (1Z) gives
[
Z_{p-1}ge Z_pge Z_{p+1}ge Z_{p+2}ge Z_{p+3}.
]

The switch rank of (Ox) is (p). Applying the same theorem to its scan (Z0) gives exactly the same five inequalities.

Therefore
[
oxed{
Z_{p-1}Z_pZ_{p+1}Z_{p+2}Z_{p+3}
	ext{ is a binary step word }1^a0^{5-a}.
}
]

### Consequence for the binary ladder

The unresolved two-row ladder of §310 is not arbitrary near the only middle transition of (O). Its blocker rail (Z) has one of only six switch-core forms:
[
00000, 10000, 11000, 11100, 11110, 11111.
]

The common middle bit (Z_{p+1}) also determines the synchronized replacement branch of §§308–309:

- (Z_{p+1}=1): both endpoint rotations choose the same left replacement;
- (Z_{p+1}=0): both choose the same right replacement.

Thus the crossed shortcut residue has a one-dimensional blocker threshold through the switch core. The remaining data are the rung bits and the compatible rail (X); no second arbitrary blocker scan remains.
