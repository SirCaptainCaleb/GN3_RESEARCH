# Flatness leaves the four full-flat reconnection bits independent — preserved pre-item development

## Composition

(none yet)

## Development

## Flatness does not couple the four exported reconnection bits

Consider the normalized residual full/flat five-set from ternary §27 on internal coordinates
[
0<1<2<3<4,
]
with increasing-triple table
[
012=0, 013=1, 014=1, 023=0, 024=0, 034=0,
]
[
123=1, 124=1, 134=0, 234=0.
]
Adjoin two exterior coordinates (L<M<0) on the left and (4<R<S) on the right. Assume only the old boundary windows on the surrounding target-color carrier:
[
LM0=0,qquad M01=0,qquad 34R=0,qquad 4RS=0.
]

For the right-boundary-preserving color-0 exit ((1,2,0,3,4)), let
[
A=LM1,qquad B=M12
]
be its two exported left reconnection bits. For the left-boundary-preserving color-1 exit ((0,1,4,3,2)), let
[
C=32R,qquad D=2RS
]
be its two exported right reconnection bits.

### Theorem
Subject only to coboundary flatness, the four bits (A,B,C,D) are mutually independent. In particular every one of the (2^4=16) exported boundary patterns is realizable while the internal five-set table and the four old boundary windows above remain fixed.

### Proof
Use the tournament-switching representation. For increasing vertices write (e_{uv}inmathbf F_2) for the forward edge bit. After switching at vertices, take
[
e_{0i}=0quad(1le ile4).
]
Then the displayed internal table is realized by
[
e_{12}=0, e_{13}=1, e_{14}=1, e_{23}=0, e_{24}=0, e_{34}=0,
]
because for every increasing triple (i<j<k),
[
alpha(i,j,k)=e_{ij}+e_{ik}+e_{jk}.
]

On the left, the old constraints give
[
e_{LM}+e_{L0}+e_{M0}=0,qquad e_{M0}+e_{M1}=0.
]
Hence
[
A=alpha(L,M,1)=e_{L0}+e_{L1},
]
while
[
B=alpha(M,1,2)=e_{M0}+e_{M2}
]
since (e_{12}=0). Thus (e_{L1}) and (e_{M2}) prescribe (A) and (B) independently without changing either old boundary constraint.

On the right, write (R=5,S=6). The old constraints are
[
e_{35}+e_{45}=0,qquad e_{45}+e_{46}+e_{56}=0.
]
Now alternation gives
[
C=alpha(3,2,5)=1+alpha(2,3,5)
 =1+e_{25}+e_{35},
]
and
[
D=alpha(2,5,6)=e_{25}+e_{26}+e_{56}.
]
After choosing (e_{45},e_{46}) arbitrarily, choose (e_{25}) to prescribe (C), then choose (e_{26}) to prescribe (D). These choices are disjoint from the left-side choices. Therefore (A,B,C,D) are independent. QED.

### Consequence for the Article III frontier
Ternary §36 correctly reduces the residual full/flat packet to four exported reconnection bits, but flat four-face identities alone cannot force a good exit: there is no hidden algebraic coupling to classify away. Any successful boundary theorem must use additional provenance of the packet—specifically insertion-blocking inequalities, antipodal pair-crossing data, protected-root information, or a common global potential.

This also explains the failure of singleton-defect transport. The outer mismatch exported by a local swap is a genuine independent boundary degree of freedom, not an omitted consequence of flatness. Future transport lemmas should therefore take the complete boundary packet as state rather than a single defect rank.
