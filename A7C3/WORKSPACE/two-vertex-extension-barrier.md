# Two-vertex extension barrier over a Hamilton spectator path

Status: **provisional working mathematics** for the G39 parent-extension axis. This document is not an audited reusable result.

## Orientation

### Exact setting

Let `H` be a finite Strong Level-(1) boundary tournament satisfying accepted boundary antisymmetry R3, and let

    B=(b_1,...,b_m)

be a tight Hamilton path on its displayed vertex set. Let `v,s` be two further vertices. Write `Gamma(H)` for R887's comparison orientation on ordinary edges, so a vertex-simple word is tight exactly when its consecutive ordinary edges form a directed chain in `Gamma(H)`.

For the live source-frame application, `s` is one of the three source spokes `p,q,r`, `v` is the common fourth X-vertex, and nonHamiltonicity of every support

    C_s = H[B union {v,s}]

is forced in a counterexample by the complementary source-pair P4 construction recorded in `source-complement-zipper.md`.

### Strongest current conclusions

1. **No monotone-gap theorem is available from R3 plus the Hamilton path B alone.** Even one extra vertex `x` can have an arbitrarily prescribed success/failure pattern for insertion into the interior gaps of `B`. Thus a universal first-loss/last-gain interval for ordinary insertion cannot be derived at this abstraction level.
2. **There is nevertheless a canonical exact cut certificate for two-vertex extension failure in the B-order-preserving subproblem.** A finite prefix automaton has transitions labelled by single R887 comparisons. If no B-ordered Hamilton word on `B union {v,s}` exists, its positive-reachability region has a unique outgoing cut, and every cut edge is an explicitly reversed boundary comparison.
3. **For fixed `B,v` and varying companion `s`, the entire s-free part of that reachability region and its outgoing s-free cut are identical.** Hence the three G39 failures have a genuinely shared backbone; companion-specific obstruction begins only when a path attempts to consume the companion, or after it has done so.

The second and third conclusions are exact reductions, but they do **not** by themselves prove Hamiltonicity of any `C_s` or close G39.

### Trust and scope

The arguments below use audited R3 and R887. The G39 source-frame facts are used only when interpreting the reduction, not in the generic lemmas themselves.

The arbitrary-gap construction is a **fence on R3-only / Hamilton-B abstractions**, not a counterexample to the full live source-frame packet. The old source two-cover `F`, source turns `(A,s,C)`, zipper rectangles, canonical `J`/cut data, and ancestry constraints may impose additional structure that destroys the free construction.

The automaton certificate concerns Hamilton words that preserve the displayed order `b_1,...,b_m`. Full nonHamiltonicity implies failure of this restricted family, so the certificate is a necessary consequence of the live counterexample. The converse is false in general: a Hamilton word may reorder the B-vertices.

### Actual missing step

Exploit full source-frame data to show that the three companion-specific portions of the canonical barriers cannot coexist, or that a common barrier comparison has a physical exchange/descent consumer. The generic comparison geometry alone does not supply the desired interval monotonicity.

### Load-bearing proofs

- `RESULTS/USABLE/ACTIVE/R3.md` — complete-reversal boundary antisymmetry.
- `RESULTS/USABLE/ACTIVE/R887.md` — comparison orientation `Gamma(H)` and the exact tight-word / directed-edge-chain dictionary.
- `WORKSPACE/source-complement-zipper.md` — the live three-complement source-frame interface and its trust fences.

## 1. Arbitrary oscillation of one-vertex insertion sites

The simplest hoped-for extension theorem would make legal insertion sites of one outside vertex form an interval, or at least force a monotone first-loss/last-gain pattern along `B`. R3 alone cannot do this.

Let

    e_i = {b_i,b_{i+1}}  (1 <= i <= m-1).

Assume `m>=4` and take one outside vertex `x`. For every internal B-vertex `b_j`, `2<=j<=m-1`, prescribe in `Gamma` the two comparisons

    e_{j-1} -> {b_j,x} -> e_j.

These prescriptions are mutually compatible with the tightness comparisons `e_{j-1}->e_j`: at the local middle `b_j` the three incident ordinary edges may simply be oriented transitively in the displayed order.

Now inspect insertion of `x` in the interior gap after `b_i`, where `2<=i<=m-2`:

    W_i=(b_1,...,b_i,x,b_{i+1},...,b_m).

All old B-turns survive. The only three comparisons newly required are

    e_{i-1} -> {b_i,x},
    {b_i,x} -> {x,b_{i+1}},
    {x,b_{i+1}} -> e_{i+1}.

The first and third were prescribed positive. Therefore

    W_i is tight  iff  {x,b_i} -> {x,b_{i+1}}.

The right-hand comparison lives in the local tournament at `x`. Orientations of the consecutive pairs

    {x,b_i} versus {x,b_{i+1}}

can be chosen independently as part of that tournament. Consequently, for **any** subset

    I subseteq {2,...,m-2},

there is an R3-compatible comparison orientation in which `W_i` is tight exactly for `i in I`.

In particular the legal gaps may alternate success/failure arbitrarily many times. Any universal monotone-gap, one-crossing, or interval-barrier statement therefore needs hypotheses beyond `R3 + B is tight`.

### Why this is an R3-level construction

Each line-graph adjacency corresponds to one complete-reversal pair of turns. Giving it one direction declares exactly one of those turns tight, as required by R3. The prescriptions above never assign both directions to the same comparison. Nothing here claims compatibility with all extra structure of the live G39 source frame.

## 2. The B-ordered two-vertex prefix automaton

The surviving generic object is not an interval of gaps but a reachability cut.

Call a word `W` **B-ordered** if it uses distinct vertices from `B union {v,s}` and the B-vertices occurring in `W` appear in the order `b_1,...,b_m`. The two outside vertices may occur anywhere and in either order.

Construct a finite acyclic automaton `A(B;v,s)` as follows.

A raw state records the data needed to continue a B-ordered prefix:

- the number `i` of B-vertices already consumed, necessarily `b_1,...,b_i`;
- which of `{v,s}` have been consumed;
- the ordered suffix of length at most two of the prefix.

Equivalently, raw prefixes having the same consumed data and the same final two vertices are identified. This quotient is safe because future tightness depends only on the current last ordinary edge and the next appended vertex.

From a state, a raw transition appends any still-permitted next vertex: `b_{i+1}` if `i<m`, or either unused outside vertex. If fewer than two vertices were present before the append, the transition has no turn condition. Otherwise, if the old suffix is `(a,b)` and the appended vertex is `c`, label the transition by

    {a,b} -> {b,c}

in `Gamma(H)`, equivalently by tightness of `(a,b,c)`.

Call such a transition **positive** when the displayed comparison points forward. A state is **positive-reachable** if it can be reached from the empty start state using only positive transitions. Terminal states are precisely states in which all `m+2` vertices have been consumed.

Because each transition consumes one new vertex, the automaton is acyclic. Its number of quotient states is `O(m)`: for each `i` and consumed subset of `{v,s}`, only constantly many ordered suffixes are possible.

### Prefix-automaton lemma

A terminal state is positive-reachable if and only if there is a tight B-ordered Hamilton word on `B union {v,s}`.

**Proof.** Reading any B-ordered word from left to right gives a raw path in the automaton. After the first two vertices, each append is positive exactly when the newly created consecutive triple is tight, by R887. Hence all transitions are positive exactly when every consecutive triple is tight. Conversely, a positive start-to-terminal automaton path spells a vertex-simple B-ordered word using every vertex once, and all of its consecutive triples are tight. `square`

## 3. Canonical barrier cut

Let `R_s` be the set of all positive-reachable states of `A(B;v,s)`. This set is canonical: it depends only on the displayed comparison data, not on a choice of failed candidate word.

Suppose there is no tight B-ordered Hamilton word. Then `R_s` contains the start state and no terminal state. Consider every raw automaton transition

    q -> q'

with `q in R_s` and `q' notin R_s`. Every such transition is negative. Indeed, if its label were positive, appending it to a positive path reaching `q` would positively reach `q'`, contradiction.

Thus the outgoing boundary

    C_s = delta^+(R_s)

is an exact comparison barrier: every start-to-terminal raw path crosses `C_s`, and every crossing edge is certified by one explicit reversed boundary comparison.

Conversely, any state set `R` containing the start, excluding all terminals, and having every outgoing raw transition negative certifies that no positive start-to-terminal path exists. Choosing the full positive-reachability set gives the unique maximal such reachable side and hence a canonical barrier.

This is the clean replacement for a nonexistent universal interval barrier. It is still local: every element of the cut is one turn comparison involving the last two vertices of a reachable prefix and its proposed next vertex.

## 4. Three companions share the same backbone exactly

Now fix `B` and `v`, and vary the companion `s`.

Inside `A(B;v,s)`, take the induced raw subautomaton on states that have **not** consumed `s`, together with transitions that do not append `s`. This is exactly the one-outside-vertex prefix automaton `A(B;v)`. In particular it does not depend on which companion is named `s`.

Let `R_0` denote its positive-reachability region. Then for every companion `s`,

    R_s intersect A(B;v) = R_0.

The reason is exact and one-way: a path reaching an s-free state cannot previously have consumed `s`, because consumed vertices are never removed. Therefore its entire history lies in the common s-free subautomaton.

It follows that the s-free part of the canonical barrier is also common:

    delta^+(R_s) restricted to s-free transitions
      = delta^+(R_0).

Any companion-specific cut edge must therefore be either

1. a transition that attempts to append `s` from a shared s-free state, or
2. a transition after `s` has already been consumed.

This is a genuine coupling of the three G39 obstruction certificates. The three supports do not begin as three unrelated Hamiltonicity problems: they have one identical forward-reachability geometry until their companion is used.

## 5. Consequence for the live G39 source frame

In the live counterexample interface, each of

    H[B union {v,p}],
    H[B union {v,q}],
    H[B union {v,r}]

is nonHamiltonian. Hence each companion yields a canonical B-ordered barrier `C_p,C_q,C_r` as above. All three contain the same s-free backbone barrier `delta^+(R_0)` and can differ only across/after the companion-insertion layer.

This suggests a sharper target than an unrestricted first-loss search:

- first compute or reason about the common reachable backbone for `B union {v}`;
- then use the actual source turns, old `F`, zipper rectangle, or gate/wall data to constrain the three companion-entry/post-entry barriers;
- seek a pigeonhole or switch only among those companion-specific cut comparisons.

The arbitrary-gap lemma warns against expecting those comparisons to line up monotonically merely because they occur at ordered positions of `B`. Any such alignment must be paid for by source-frame structure.

## 6. What would materially strengthen this development

A useful next lemma would use one of the full live hypotheses to collapse the companion-specific barrier. Examples of sufficient progress would be:

- a source-frame rule forcing all positive companion-entry transitions into one interval of the common backbone;
- a proof that a v-containing D17.421 rectangle bypasses every cut of one companion unless a specific source-frame comparison reverses;
- a three-companion pigeonhole showing that the required post-entry cut comparisons cannot all be negative in the same actual old-F/source configuration;
- or a full-data construction showing that even the canonical-cut interface is too weak, thereby identifying another indispensable hypothesis.

Until such an input is proved, generic monotone first-loss/last-gain reasoning should not be treated as available.