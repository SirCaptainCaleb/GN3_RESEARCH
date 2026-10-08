# First-last turn roots localize balanced defects to one face block — preserved pre-item development

## Composition

(none yet)

## Development

## First–last turn roots and face-block localization

Fix coordinate-label arity (r\ge2), so we are in the directed sector of (N_{r+1}). Use the quotient-overlap graph (mathcal G_{n,r}) whose vertices are reversal-orbits of ordered ((r-1))-tuples.

For a coordinate permutation
[
pi=(v_1,ldots,v_n),
]
write its distinguished state path as
[
z_i=[v_i,ldots,v_{i+r-2}],
qquad
1\le i\le n-r+2,
]
and its status word as
[
c_i=h(v_i,ldots,v_{i+r-1}),
qquad
1\le i\le n-r+1.
]
A status change between (c_i) and (c_{i+1}) occurs at the intermediate state (z_{i+1}).

Assume (pi) is bad, so its status word has at least two changes. Let
[
alpha(pi)
]
be the state at the first change and
[
eta(pi)
]
the state at the last change. Then (alpha(pi)) occurs strictly before (eta(pi)) on the distinguished state path.

Define the root label
[
L(pi):=e_{alpha(pi)}-e_{eta(pi)}
]
in the real vector space with basis indexed by vertices of (mathcal G_{n,r}).

### Lemma 1: reversal oddness

For permutation reversal,
[
L(pi^{m rev})=-L(pi).
]

### Proof

Reversal-complement sends the status word to its complemented reverse. The set of change positions is therefore reflected, while change/nonchange is preserved. Because quotient states identify an ordered ((r-1))-tuple with its reversal, the distinguished state path of (pi^{m rev}) is the reverse of the state path of (pi). Hence the first change state of (pi^{m rev}) is (eta(pi)), and its last change state is (alpha(pi)). The displayed identity follows.

Thus a hypothetical counterexample supplies a nonzero reversal-odd type-(A) root label on every permutation chamber.

### Lemma 2: positive root balance localizes every participating defect interval to one face block

Let
[
F=C_1|cdots|C_s
]
be a face of the permutahedron, written as an ordered partition of the ground set. Every chamber refining (F) lists all coordinates of (C_1) first, then (C_2), and so on, with arbitrary order inside each block.

Let (b(v)=j) for (vin C_j), and for a quotient state
[
z=[a_1,ldots,a_{r-1}]
]
define
[
Phi_F(z):=sum_{ell=1}^{r-1} b(a_ell).
]
This is well defined on reversal-orbits.

Along the distinguished state path of every chamber refining (F), (Phi_F) is nondecreasing. Indeed,
[
Phi_F(z_{i+1})-Phi_F(z_i)
=
b(v_{i+r-1})-b(v_i)
ge0,
]
because a chamber refining (F) has nondecreasing block indices.

Now suppose chambers (pi_1,ldots,pi_m) refining (F) and positive coefficients (lambda_j>0) satisfy
[
sum_{j=1}^m lambda_j L(pi_j)=0.
]
Applying the linear functional (e_zmapstoPhi_F(z)) gives
[
0=
sum_jlambda_jigl(Phi_F(alpha(pi_j))-Phi_F(eta(pi_j))igr).
]
Every summand is nonpositive because (alpha) precedes (eta). Positivity of the coefficients therefore forces equality term by term:
[
Phi_F(alpha(pi_j))=Phi_F(eta(pi_j))
qquad	ext{for every }j.
]

Since (Phi_F) is nondecreasing along the whole state segment from (alpha) to (eta), it is constant there. For every sliding step in that segment,
[
b(v_i)=b(v_{i+r-1}).
]
Because the block-index sequence itself is nondecreasing, equality of the two endpoints (r-1) positions apart forces all intervening block indices to be equal. Propagating through the segment shows:

> For every chamber occurring with positive coefficient in the balance relation, all coordinate positions from its first change state through its last change state lie in a single block (C_j) of (F).

In particular (alpha(pi_j)) and (eta(pi_j)) are states supported wholly inside that same block.

### Corollary: blockwise decomposition of a balanced carrier

The root spaces supported on different face blocks use disjoint basis states. Hence any positive zero relation among the first–last turn roots decomposes as a direct sum of zero relations, one for each face block. At least one block therefore supports a nonempty positive zero relation entirely among roots whose first-to-last defect intervals are internal to that block.

### Significance

The standard face-average construction applied to (L) is a continuous reversal-odd map on the barycentric subdivision of the permutahedral sphere. Any topological zero gives a positive root balance in a carrier face. The localization lemma says such a balance cannot mix genuinely separated regions of that face: some block already contains a complete balanced recurrence of first/last defect states.

This isolates a sharper closure target. To finish the directed sector by this route, it would suffice to prove a carrier-descent statement turning a block-internal balanced recurrence into either a good chamber or a zero on a proper subface. The odd defect map is canonical, and any zero of a suitable compression would produce the localized recurrence above. A topological zero is not automatic here because the full state-root target is high-dimensional. The remaining tasks are therefore to find a dimension-efficient compression that retains this localization and then prove descent from the resulting balanced internal recurrence to a smaller carrier.

### Audit

The root label is defined only on bad chambers, so the construction is used under the counterexample hypothesis, where every chamber is bad. No computation, generic-position assumption, or literature input is used.
