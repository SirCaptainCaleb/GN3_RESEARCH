# Mixed endpoint packets exclude neighboring shared bridges

## Metadata

- ID: mixed_endpoint_packets_exclude_neighboring_shared_bridges
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 76
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Mixed endpoint packets exclude a shared bridge across the last two monotone cuts

Let
[
C=(c_1,ldots,c_N)
]
be a genuine two-deletion monotone corridor with status word
[
1^u0^v,qquad u,vge4.
]
Assume (vge5). Consider the neighboring legal cuts (u+1) and (u+2), and put
[
A={x,y,c_1,c_N},
]
[
T=(c_2,ldots,c_{u+1}),qquad
U=(c_{N-1},c_{N-2},ldots,c_{u+5}),
]
[
r=c_{u+2},qquad z=c_{u+3},qquad s=c_{u+4}.
]
Then (T,U) are tight paths of order at least two, ((T,r)) is tight, and ((U,s)) is tight.

Form the neighboring packets
[
S_s=Acup{r,z},qquad
S_r=Acup{z,s}.
]
Suppose (z) is a bridge in both packet tests. Then the full reflected-double span has a two-cover.

**Proof.**
If either packet test already has Hamiltonian deletion at (z), its bridge gives a two-cover. Assume both fail. By [[a_shared_bridge_at_neighboring_cuts_exposes_four_new_repair_labels]], the third packet
[
S_z=Acup{r,s}
]
has
[
S_z-wquad	ext{Hamiltonian for every }win A.
]

For the first packet (S_s), the bridge (z) has one of two orientations.

If
[
(T,z,U,s)
]
is tight, then
[
R=(T,z,U)
]
is a tight path on the complement of (S_z). Since the original corridor begins with tight status,
[
(c_1,c_2,c_3)
]
is tight, and (T) begins (c_2,c_3). Hence
[
(c_1,R)
]
is tight. Since (S_z-c_1) is Hamiltonian, these two paths two-cover the whole span.

Therefore a residual obstruction forces the first bridge orientation to be
[
(U,s,z,T).
]

Now inspect the second packet (S_r). Its bridge orientations are
[
(T,r,z,U)
qquad	ext{or}qquad
(U,z,T,r).
]
The first is impossible, because it contains the consecutive triple
[
(c_{u+1},c_{u+2},c_{u+3}),
]
whose status is the first (0) after the (1^u) run.

Thus the second bridge would have to be
[
(U,z,T,r).
]
Its contiguous subpath
[
R'=(U,z,T)
]
is tight and is again exactly the complement of (S_z). Since the final corridor status is (0),
[
(c_N,c_{N-1},c_{N-2})
]
is tight by boundary reversal, and (U) begins (c_{N-1},c_{N-2}). Hence
[
(c_N,R')
]
is tight. Since (S_z-c_N) is Hamiltonian, this again gives a spanning two-cover.

All bridge orientations lead to a two-cover. Therefore (z=c_{u+3}) cannot be a bridge in both neighboring packet tests of a genuine obstruction. (square)

By reversing the left/right roles, if (uge5) the analogous shared-bridge configuration across the first two legal cuts is also impossible.

Thus every monotone genuine two-deletion corridor of order greater than twelve has at least one side on which neighboring-cut bridge repetition is forbidden. At the first possible order (12), the only unresolved monotone exponent pair is (u=v=4), where the above two-tail packet has one tail of order one and needs a separate endpoint version.

## Frontier

- Development version when composed: None
- Development version now: 1
