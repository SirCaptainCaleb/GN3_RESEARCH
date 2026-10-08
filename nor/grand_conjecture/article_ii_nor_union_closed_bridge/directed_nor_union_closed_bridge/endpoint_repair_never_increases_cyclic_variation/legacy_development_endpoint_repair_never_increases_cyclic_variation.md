# Endpoint repair never increases cyclic variation — preserved pre-item development

## Endpoint repair never increases cyclic variation

Work in a pure alternating ternary orientation. Let a cyclic order contain
[
(ldots,p,a,b,c,d,q,r,s,ldots),
]
and put
[
L=alpha(p,a,b),quad
x=alpha(a,b,c),quad
y=alpha(b,c,d),quad
z=alpha(c,d,q),quad
R=alpha(d,q,r),quad
S=alpha(q,r,s).
]
Assume
[
x
e y,
]
and suppose the last-pair endpoint repair is available:
[
u:=alpha(a,b,d)=x.
]

Swap (c,d). The affected status string changes from
[
(L, x, 1-x, z, R, S)
]
to
[
(L, x, x, 1-z, V, S),
]
where
[
V=alpha(c,q,r)
]
is the fourth changed status that was omitted in the earlier adjacent-swap audit.

The first transition (Lleftrightarrow x) is unchanged, and
[
xoplus(1-z)=(1-x)oplus z,
]
so the transition immediately after the repaired central pair is also unchanged.

Let
[
A=(zoplus R)+(Roplus S)
]
be the old variation across the final two-transition packet, and
[
B=((1-z)oplus V)+(Voplus S)
]
the new one. Then
[
q(C')-q(C)=-1+B-A.
	ag{1}
]

Now (A) is the variation of a binary two-edge path from (z) to (S), while (B) is the variation of a binary two-edge path from (1-z) to the same endpoint (S).

- If (z=S), then (Ain{0,2}), while (B=1).
- If (z
e S), then (A=1), while (Bin{0,2}).

Hence in every case
[
B-Ain{-1,+1}.
]
Substituting into (1) gives the exact monotonicity law
[
oxed{q(C')-q(C)in{-2,0}.}
]

### Theorem

Any endpoint adjacent swap which removes a non-fully-curved central transition can never increase cyclic variation. It either preserves variation or decreases it by exactly two.

By reversal, the same statement holds for a successful first-pair repair.

### Extremal consequences

If (C) is a minimum four-change cycle in a counterexample, every available endpoint repair must preserve (q=4).

For the last-pair repair above this forces:

1. the forbidden old packet
   [
   z, 1-z, z
   ]
   cannot occur at ((z,R,S)), because then (A=2) and the repair lowers (q) by two;

2. if (z
e S), then the new fourth status must satisfy
   [
   V=z,
   ]
   because preservation requires (B=2), not (0).

Thus a non-full transition in an extremal cycle is not merely locally repairable: the far reconnection is forced to absorb the repair without lowering total variation.

### Significance

This repairs the invalid deterministic particle law. The correct statement is monotone rather than positional:

- fully-curved transitions are intrinsically irreducible;
- non-fully-curved transitions admit a full-support adjacent swap that weakly decreases variation;
- in a counterexample at minimum variation, every such repair must lie in the equality case, imposing explicit boundary identities.

Repeated equality-case repairs are therefore a legitimate extremal-descent framework: any strict step closes NOR, while persistent equality produces rigid transported boundary data.
