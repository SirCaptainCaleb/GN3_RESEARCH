# Two-label one-defect bridge — preserved pre-item development

## Composition

(none yet)

## Development

### The opposite-endpoint residue is a two-label completion problem

**Lemma 34 (one-defect bridge with two one-label completions).** In the opposite-endpoint case of Lemma 27, normalize the common slot orders so that
[
C=(c_1,c_2,c_3,c_4),qquad D=(d_1,d_2,d_3,d_4),
]
with
[
(c_1,c_2,c_3,c_4,p),qquad
(c_1,c_2,c_3,c_4,x),
]
and
[
(q,d_1,d_2,d_3,d_4),qquad
(x,d_1,d_2,d_3,d_4)
]
Hamiltonian. Then, unless (H) already has a two-cover, Lemma 27 gives
[
(d_1,x,c_4)
]
tight and
[
(c_4,x,d_1)
]
non-tight.

The following three orderings have the indicated defect-line structure.

1. On (H-{p,q}),
   [
   sigma_0=(c_1,c_2,c_3,c_4,x,d_1,d_2,d_3,d_4)
   ]
   has exactly one defect triple, namely
   [
   (c_4,x,d_1).
   ]
   Hence
   [
   
u(L_{sigma_0})=1.
   ]

2. On (H-q),
   [
   sigma_p=(c_1,c_2,c_3,c_4,p,x,d_1,d_2,d_3,d_4)
   ]
   has no possible defect triples except
   [
   (c_4,p,x),qquad(p,x,d_1).
   ]
   These are consecutive, so
   [
   
u(L_{sigma_p})le1.
   ]

3. On (H-p),
   [
   sigma_q=(c_1,c_2,c_3,c_4,x,q,d_1,d_2,d_3,d_4)
   ]
   has no possible defect triples except
   [
   (c_4,x,q),qquad(x,q,d_1).
   ]
   Again these are consecutive, so
   [
   
u(L_{sigma_q})le1.
   ]

**Proof.** In (sigma_0), every triple wholly inside (C) or (D) is tight, and the slot assumptions give
[
(c_3,c_4,x),qquad(x,d_1,d_2)
]
tight. The only remaining junction triple is ((c_4,x,d_1)), which is non-tight by Lemma 27. This proves (1).

For (sigma_p), the displayed Hamilton path (C+p) gives
[
(c_3,c_4,p)
]
tight, while (D+x) gives
[
(x,d_1,d_2)
]
tight. Thus the only undecided consecutive triples are the two displayed in (2), and their defect-line edges are adjacent. The proof of (3) is identical, using (C+x) and (q+D). (square)

Thus the terminal opposite-endpoint state is much narrower than a generic external reversal. There is a common nine-vertex ordering with one defect, and each of the two missing labels can be restored separately without increasing the defect-line matching number above one.

### Three simultaneous completions and the coherent failure residue

The simultaneous insertion problem has only three relevant orders.

**Lemma 35 (three-order completion criterion).** Under the hypotheses of Lemma 34, consider
[
egin{aligned}
sigma_1&=(c_1,c_2,c_3,c_4,p,x,q,d_1,d_2,d_3,d_4),\
sigma_2&=(c_1,c_2,c_3,c_4,p,q,x,d_1,d_2,d_3,d_4),\
sigma_3&=(c_1,c_2,c_3,c_4,x,p,q,d_1,d_2,d_3,d_4).
end{aligned}
]
If any one of these has defect-line matching number at most one, then (H) has a two-cover.

If all three have defect-line matching number two, then the six triples
[
egin{gathered}
(c_4,p,x),qquad (x,q,d_1),\
(c_4,p,q),qquad (q,x,d_1),\
(c_4,x,p),qquad (p,q,d_1)
end{gathered}
]
are all non-tight. Hence their boundary reversals
[
egin{gathered}
(x,p,c_4),qquad (d_1,q,x),\
(q,p,c_4),qquad (d_1,x,q),\
(p,x,c_4),qquad (d_1,q,p)
end{gathered}
]
are all tight.

Moreover, unless
[
(p,x,q),qquad(p,q,x),qquad(x,p,q)
]
are all tight, (H) contains a Hamiltonian five-support
[
F={c_4,d_1,p,q,x}
]
whose complement has path-cover number two.

**Proof.** In (sigma_1), every possible defect lies among
[
(c_4,p,x),qquad(p,x,q),qquad(x,q,d_1).
]
The corresponding defect-line edges form three consecutive edges. Their matching number is two exactly when the first and third triples are both non-tight. Thus failure of (sigma_1) to have defect matching number at most one forces
[
(c_4,p,x),qquad(x,q,d_1)
]
non-tight. The identical argument for (sigma_2,sigma_3) gives the other four failures. Boundary antisymmetry gives the six displayed reverse triples.

Now suppose at least one of
[
(q,x,p),qquad(x,q,p),qquad(q,p,x)
]
is tight. Respectively, one of
[
(d_1,q,x,p,c_4),qquad
(d_1,x,q,p,c_4),qquad
(d_1,q,p,x,c_4)
]
is a Hamiltonian path on (F), because its first and last triples are among the six forced reverse triples above. Hence (F) is Hamiltonian.

Its complement is covered by the inherited paths
[
(c_1,c_2,c_3)mid(d_2,d_3,d_4).
]
If that complement were Hamiltonian, it together with a Hamilton path on (F) would two-cover (H). Therefore its path-cover number is exactly two.

Finally, for each choice of middle vertex in the three-set ({p,q,x}), exactly one of an ordered triple and its boundary reverse is tight. Thus if none of
[
(q,x,p),qquad(x,q,p),qquad(q,p,x)
]
is tight, their reverses are precisely
[
(p,x,q),qquad(p,q,x),qquad(x,p,q),
]
and all three are tight. (square)

Consequently the two-label completion problem has only one genuinely coherent failure pattern left. After excluding a direct one-cut order and a bounded Hamiltonian five-support, the root triple must satisfy
[
(p,x,q),qquad(p,q,x),qquad(x,p,q)
]
tight simultaneously, together with the six forced bridge reversals above.

This finite oriented configuration is the exact terminal residue of the order-eleven route.
