# Side-lifted protected roots remove same-side A3 reversal cancellation — preserved pre-item development

## Composition

(none yet)

## Development


## Side-lifted protected roots remove same-side A3 reversal cancellation

Work with a protected threshold-compatible band and a terminal fully-curved boundary barrier. Normalize every barrier transition to 10. Its physical slide root is
[
ho=e_a-e_d,
]
where (a,b,c,d) are the four consecutive coordinates carrying the boundary transition.

Retain one additional provenance bit:
[
s=
egin{cases}
-1,&	ext{the barrier is the left boundary of the protected band},\
+1,&	ext{the barrier is the right boundary of the protected band}.
end{cases}
]
Define the side-lifted protected root
[
widehatho=(ho,s)in Woplusmathbb R.
]

### Antipodal equivariance

Under global complement-reversal of the protected state, the coordinate order reverses. A 10 transition remains a 10 transition, the dropped and entering coordinates exchange roles, and the left and right band boundaries exchange. Therefore
[
holongmapsto-ho,qquad slongmapsto-s,
]
so
[
widehatholongmapsto-widehatho.
]

Thus the side lift preserves the odd symmetry required by an antipodal carrier.

### Local A3 reversal pairs no longer cancel automatically

Suppose a protected root in an A3 block is carried by the chamber
[
(a,b,c,d)
]
and has root
[
ho=e_a-e_d.
]
The reversed block chamber
[
(d,c,b,a)
]
carries the raw opposite root (-ho).

If both realizations occur on the same side of the same protected threshold band, then the side bit is unchanged. Their lifted labels are
[
(ho,s),qquad(-ho,s).
]
No positive combination of these two vectors is zero: from the last coordinate,
[
lambda s+mu s=0
]
with (lambda,mu>0) is impossible.

Hence the ubiquitous raw A3 reversal pair is not a two-cycle in the side-lifted protected carrier unless the two roots come from opposite band sides.

### Balance law for every positive lifted circuit

If
[
sum_jlambda_j(ho_j,s_j)=0,qquad lambda_j>0,
]
then separately
[
sum_jlambda_jho_j=0
]
and
[
sum_jlambda_js_j=0.
]
Thus every positive lifted circuit is a positive physical-root dependence with equal total coefficient weight on left and right barriers.

In particular:

1. a circuit supported entirely on one band side is impossible;
2. a two-root lifted circuit must have opposite physical roots and opposite side labels;
3. any A3 triangle or four-cycle that survives the lift must mix left and right protected provenance.

### Relation to the protected A3 audit

Raw block reversal does not automatically preserve minimum-first-phase provenance. The side lift does not repair that issue by enlarging the carrier. Instead it records information already present whenever a root is genuinely emitted by threshold-band termination.

Consequently it gives a zero-free replacement for the most troublesome artificial cancellation: even when two opposite raw A3 roots are both genuinely protected, they do not cancel in the lifted carrier if they arise on the same side. A positive zero now certifies a coupling of the two boundary problems rather than a local reversal symmetry.

### Topological use

The price of the lift is one extra target dimension. A direct Borsuk-Ulam argument therefore needs an additional constraint, quotient, or companion section to recover codimension. But the lift identifies a more faithful target for fixed-point constructions: an equivariant zero cannot be produced solely by the automatic A3 reversal pair and must balance the two protected boundaries.

This suggests coupling the lift with the Johnson-cut projection of protected A3 two-cycles. A lifted two-cycle corresponds to opposite roots on opposite sides, so after collapsing same-cut chamber motion the remaining obstruction is a short path coupling the left and right protected cuts, rather than a local six-wall reversal.
