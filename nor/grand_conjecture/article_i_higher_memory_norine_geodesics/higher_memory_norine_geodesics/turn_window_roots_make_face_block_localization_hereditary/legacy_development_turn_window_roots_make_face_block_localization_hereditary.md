# Turn-window roots make face-block localization hereditary — preserved pre-item development

## Development

## Turn-window roots repair the boundary leakage in first/last-state localization

Fix coordinate-label arity (rge2) in the directed translation-invariant sector. For a coordinate permutation
[
pi=(v_1,ldots,v_n)
]
write
[
c_i=h(v_i,ldots,v_{i+r-1}),
qquad 1le ile n-r+1.
]
A change between (c_i) and (c_{i+1}) is witnessed by the full ordered ((r+1))-tuple
[
(v_i,v_{i+1},ldots,v_{i+r}).
]

Let
[
	au_i=[v_i,ldots,v_{i+r}]
]
denote its reversal-orbit. If (pi) is bad, let (	au_f(pi)) and (	au_ell(pi)) be respectively the first and last change windows, and define the turn-root label
[
L_{m turn}(pi)=e_{	au_f(pi)}-e_{	au_ell(pi)}.
]

### Lemma 1: reversal oddness
[
L_{m turn}(pi^{m rev})=-L_{m turn}(pi).
]

### Proof
Reversal-complement preserves the set of change positions and reverses their order. The full ((r+1))-coordinate witness of a change is reversed, hence represents the same reversal-orbit (	au). Therefore first and last turn windows swap. (square)

The point of using turn windows rather than the shared ((r-1))-state is that the turn remembers both coordinates entering the two adjacent (r)-windows.

### Lemma 2: positive turn-root balance localizes the entire defect interval

Let
[
F=C_1|cdots|C_s
]
be a face of the permutahedron, and let (b(v)=j) for (vin C_j). For a turn window
[
	au=[a_0,ldots,a_r]
]
define
[
Psi_F(	au)=sum_{j=0}^{r} b(a_j).
]
This is well defined on reversal-orbits.

Along every chamber refining (F),
[
Psi_F(	au_{i+1})-Psi_F(	au_i)
=
b(v_{i+r+1})-b(v_i)ge0.
]
Thus (Psi_F) is nondecreasing along the sequence of turn windows.

Suppose bad chambers (pi_1,ldots,pi_m) refining (F) and coefficients (lambda_j>0) satisfy
[
sum_jlambda_jL_{m turn}(pi_j)=0.
]
Applying the linear functional (e_	aumapstoPsi_F(	au)) gives
[
0=sum_jlambda_jigl(
Psi_F(	au_f(pi_j))-Psi_F(	au_ell(pi_j))
igr).
]
Every summand is nonpositive, so every summand is zero.

Fix one participating chamber and write its first and last change positions as (f<ell). Equality of the endpoint potentials and monotonicity imply
[
Psi_F(	au_t)=Psi_F(	au_{t+1})
qquad(fle t<ell).
]
Hence
[
b(v_t)=b(v_{t+r+1})
qquad(fle t<ell).
]
Because the block-index sequence along a chamber refining (F) is nondecreasing, equality of two entries (r+1) positions apart forces every intervening entry to be equal. Propagating through the interval yields
[
v_f,v_{f+1},ldots,v_{ell+r}
]
all in one block (C_j).

In particular both full change witnesses (	au_f) and (	au_ell), not merely their shared overlap states, are supported entirely inside the same face block.

### Corollary 3: hereditary block localization
For every participating chamber, the restriction of its coordinate order to that block (C_j) is itself bad and has the same first and last turn windows. Hence
[
L_{m turn}(pi)
]
is exactly the first-last turn-root label of the induced bad permutation of (C_j) for the restricted coordinate coloring (h|_{C_j}).

Indeed, the full permutation has no changes before its first turn or after its last turn, while both first and last turn witnesses are wholly internal to (C_j). Therefore the induced status word on the consecutive (C_j)-segment contains these same two changes and no earlier or later internal change.

The turn-root spaces supported on distinct face blocks use disjoint basis coordinates, so any positive zero relation decomposes blockwise exactly as in the state-root argument.

### Significance
The earlier first/last-state root
[
e_alpha-e_eta
]
localized only the shared ((r-1))-states; an extra entering or leaving coordinate could still lie outside the selected face block, preventing honest restriction to the smaller coordinate set. Turn-window roots remove that leakage.

Thus any positive balanced carrier for (L_{m turn}) contains a nonempty blockwise positive balance that is literally a balance of the same defect labels for bad permutations on a proper coordinate subset whenever the carrier lies on the permutahedral boundary. This supplies the hereditary form needed by any carrier-descent or chain-level induction.
