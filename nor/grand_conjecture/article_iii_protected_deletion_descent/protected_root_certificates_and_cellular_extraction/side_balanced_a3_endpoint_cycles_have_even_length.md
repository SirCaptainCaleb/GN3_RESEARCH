# Side-balanced A3 endpoint cycles have even length

## Composition

For a simple positive ternary A3 endpoint circuit, all physical-root coefficients are equal. After adjoining the left/right band-side sign, a lifted zero therefore requires the side signs around the circuit to sum to zero. Hence any individually side-balanced A3 circuit has even length with equal left/right counts: only an opposite-side 2-cycle or a balanced 4-cycle can occur, never a triangle. This conclusion concerns a single physical circuit; decomposition of a general lifted zero is handled separately.

## Development


## Side-balanced A3 endpoint cycles have even length

Use the side-lifted protected labels
[
widehatho=(ho,s),qquad sin{-1,+1},
]
where (s) records the left or right terminal boundary of the protected threshold band.

In a ternary A3 block, every internal physical root is an endpoint edge. Let a support-minimal positive **physical** dependence be a directed simple endpoint cycle
[
ho_i=e_{x_{i+1}}-e_{x_i},
qquad iinmathbb Z/kmathbb Z.
]
For a simple directed cycle the positive physical dependence is unique up to scale, so all coefficients are equal:
[
ho_0+cdots+ho_{k-1}=0.
]

Suppose these same protected states also form a zero of the side-lifted labels. Then, after the common positive rescaling,
[
sum_i(ho_i,s_i)=0.
]
The physical coordinates cancel automatically around the cycle, while the side coordinate gives
[
sum_i s_i=0.
]

Since every (s_i) is (+1) or (-1), the cycle length (k) is even and exactly half of its roots come from each protected band side.

### Ternary A3 consequence

The raw A3 endpoint-cycle alternatives have lengths (2,3,4). A simple physical circuit that is itself side-balanced therefore has only two possibilities:

- (k=2): one root comes from the left boundary and the opposite root from the right boundary;
- (k=4): two roots come from each boundary side.

A directed triangle cannot be a zero of the side-lifted protected labels.

Thus the provenance lift removes not only same-side reversal two-cycles but also every individually side-balanced A3 triangle. The first-cell extraction problem for a single lifted physical circuit reduces to opposite-side two-cycles and balanced four-cycles.

### Caveat

A support-minimal zero in the lifted space need not project to one support-minimal physical cycle: its physical positive circulation could decompose into several endpoint cycles whose side imbalances cancel only after summation. Therefore this lemma eliminates triangular circuits only when the physical circuit itself is the lifted zero support, or after a separate argument reduces a lifted zero to one side-balanced physical cycle.

That remaining decomposition issue is now explicit. A useful next theorem would show that a support-minimal lifted A3 zero contains a side-balanced constituent cycle; then triangles disappear entirely from the protected A3 frontier.
