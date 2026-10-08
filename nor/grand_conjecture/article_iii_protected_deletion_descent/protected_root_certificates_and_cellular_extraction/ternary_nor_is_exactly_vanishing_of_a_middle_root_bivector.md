# Ternary NOR is exactly vanishing of a middle root bivector

## Composition

(none yet)

## Development

## Ternary NOR is exactly vanishing of a middle-root bivector

Let
[
pi=(v_1,ldots,v_n)
]
be a coordinate order in ternary arity, with status word
[
w_1,ldots,w_{n-2}in{0,1}.
]

For every change between consecutive statuses, use the ordered shared pair of the two ternary windows:
[
eta_i=e_{v_{i+1}}-e_{v_{i+2}}.
]
These are simple type-A roots in the order (pi).

Define
[
D_{10}(pi)=sum_{i:w_iw_{i+1}=10}eta_i,
qquad
D_{01}(pi)=sum_{i:w_iw_{i+1}=01}eta_i.
]

### Theorem

[
D_{10}(pi)wedge D_{01}(pi)=0
]
if and only if the status word of (pi) has at most one change.

### Proof

For a fixed permutation, the roots
[
e_{v_j}-e_{v_{j+1}},qquad j=1,ldots,n-1,
]
are a simple-root basis of the type-A root space. Every (eta_i) is one of these basis roots.

The supports of (D_{10}) and (D_{01}) in that basis are disjoint, because a status boundary cannot simultaneously have types 10 and 01. Every nonzero coefficient equals 1.

Hence, if both sums are nonzero, they are linearly independent: two nonzero vectors with disjoint support in a fixed basis cannot be scalar multiples. Therefore their wedge is nonzero.

Conversely, if either sum vanishes, the binary word has no transition of that orientation. A binary linear word with no 10 is of the form (0^*1^*), while one with no 01 is of the form (1^*0^*). In either case it has at most one change.

Thus wedge vanishing is exactly the ternary NOR condition for the order.

### Reversal

Under full coordinate reversal, the ternary status word becomes complement-reverse. A 10 boundary maps to a 10 boundary, and a 01 boundary maps to a 01 boundary. The shared middle pair reverses order, so
[
D_{10}(pi^{rev})=-D_{10}(pi),
qquad
D_{01}(pi^{rev})=-D_{01}(pi).
]
Consequently
[
D_{10}wedge D_{01}
]
is reversal-even.

### Significance

This gives a canonical global algebraic obstruction with no nearest-violation choice and no protected-fiber patching:
[
pi	ext{ is NOR-good}
iff
D_{10}(pi)wedge D_{01}(pi)=0.
]

It also explains why a direct antipodal argument on the bivector is unavailable: reversal negates both factors, so the wedge is even. A topological proof would need an additional switch/sign parameter or a lift retaining the ordered pair ((D_{10},D_{01})), rather than only its wedge.

The construction is naturally related to the signed-middle program: each transition is represented by the physical ordered middle pair shared by its two consecutive ternary windows, so every root lies on an actual adjacent Coxeter wall.
