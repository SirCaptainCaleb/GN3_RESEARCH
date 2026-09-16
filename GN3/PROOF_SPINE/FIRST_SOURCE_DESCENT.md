# Branch B: Boolean-cube classification and first-source descent

**Status: active proof-spine reconstruction; unresolved at the phase-zero recursion step; this GN3 rewrite is not yet independently audited.**

## 1. Shared starting point

Assume that the two-path-cover theorem is false, and let `H` be a smallest counterexample. The certified small-order argument gives

`|H|>10`.

Minimality has an immediate useful consequence. For any distinct vertices `x,y`, the proper subsystem `H-{x,y}` has path-cover number exactly two, and neither rail of an exact two-cover is a singleton. A Hamilton path of the pair-deleted subsystem, or a singleton rail in an exact two-cover, could be combined with a tight trimer on the deleted pair and one suitable retained vertex to two-cover `H`.

This branch uses that rigidity to build a small cube of related exact two-covers. A finite comparison of the cube must produce a genuine source-visible path or cycle. Once such a birth appears, a marked-rail growth argument either closes `H` or descends in a strict phased rank below every source configuration that participated in the comparison.

Unlike the fixed-pair branch, this route therefore carries a genuine monotone quantity. Its present defect is that the proven descent theorem is deliberately source-relative: it is not yet a recursive rule after the first transition to phase zero.

## 2. Three same-oriented spokes

Choose distinct anchors `a,c` and an exact two-cover

`H-{a,c}=U|V`.

Both rails are nontrivial. At most four vertices are rail endpoints, so because `|H|>10` there are at least five internal vertices in this cover.

For every internal vertex `x`, exactly one of

`(a,x,c)` and `(c,x,a)`

is tight. Hence three internal vertices `p,q,r` have the same orientation. After interchanging `a,c` if needed, assume

`(a,p,c), (a,q,c), (a,r,c)`

are all tight.

Put

`P={p,q,r}`

and

`K={a,c,p,q,r}`.

A direct boundary-antisymmetry argument shows that `K` has a Hamilton tight `P5`. The same is true for every smaller complementary anchor/spoke support `K-J`, `J⊆P`: the support of order three is one of the source trimers, the support of order four has a Hamilton `P4`, and the full five-set has a Hamilton `P5`.

Now set

`W=V(H)-K`

and for every `J⊆P` define the cube fiber

`G_J=H[W∪J]`.

Because `K-J` has a tight Hamilton path, `G_J` cannot be Hamiltonian: otherwise the two complementary Hamilton paths would form a spanning two-cover of `H`. Since `G_J` is proper, minimality gives

`pc(G_J)=2`

for all eight fibers.

Thus we have a complete Boolean cube of exact two-cover residues tied to one retained three-spoke source configuration.

## 3. Comparing the cube

The cube comparison is best understood by deleting the roots `J` from a chosen exact two-cover of `G_J` and observing what remains on the common core `W`.

The surviving maximal `W`-segments are the blocks of that cover.

### 3.1 Too many blocks

If at least three `W`-blocks remain, then the same residue `W` is simultaneously displayed as a literal cover by at least three inherited tight paths and, from the bottom cube fiber, as an exact two-cover.

This is the first certificate: a literal component drop on one common residue.

### 3.2 Two blocks: compare the singleton rows

Outside the component-drop case, every trim leaves exactly two `W`-blocks.

For a singleton fiber `J={s}`, the root `s` can attach only as an endpoint. Deleting it leaves a literal exact two-cover `F_s` of `W`.

Compare `F_p,F_q,F_r`.

If two have different unordered support bipartitions of `W`, we obtain the second certificate: two exact covers of one residue with different support bipartitions.

If the support bipartitions agree but a common support carries different literal Hamilton orders, we obtain the third certificate: same support but different literal rail orders. Comparing the two orders produces a selected reversal, a reverse tight trimer, or a proper tight cycle.

Outside these two branches, after exchanging whole rails if necessary, all three singleton rows trim to the same literal exact cover

`F=A|B`.

Each spoke `s` has a definite endpoint port `e_s` of `F` to which it attaches.

### 3.3 Compare the two-root rows

Now take a rank-two fiber `W∪{s,t}`.

If one root is internal on its rail, deleting it splits that rail into two nonempty pieces and immediately gives the component-drop certificate on the corresponding singleton residue. Thus, outside the already-declared branch, both roots are endpoints.

Comparing their one-root trims with the retained singleton rows shows that, outside support or order disagreement, the two-root cover is literally obtained from `F` by the two certified endpoint attachments

`s e_s` and `t e_t`.

Two roots cannot share a nontrivial endpoint of `F`, since that endpoint would then have selected degree three. If they share a port at all, that port must therefore be an isolated singleton rail `(v)` of `F`, and their component is the physical tight trimer on `{s,v,t}`.

### 3.4 Install all three roots

Install all three certified attachments simultaneously.

Unless all three roots attach to the same isolated singleton `v`, this produces an exact top-fiber two-cover in which at least one of `p,q,r` is a rail endpoint. But the retained original top cover `U|V` had all three spokes internal. Hence we obtain the fourth certificate: two exact top-fiber covers with an endpoint/internal discrepancy at a spoke.

The only remaining possibility is the synchronized form

`F=(v)|B`,

with every singleton row equal to a dimer on `{v,s}` plus `B`, and every two-root row equal to a tight trimer on `{s,v,t}` plus `B`.

Moreover the four-set

`{v,p,q,r}`

has no Hamilton tight `P4`; otherwise that `P4` together with `B` would give another top-fiber exact two-cover with a spoke endpoint, returning to the previous discrepancy case.

This is the fifth and final cube certificate.

The classification is exhaustive. Starting from the three-spoke cube, one must obtain exactly one of:

1. a common-residue component drop;
2. same-residue support disagreement;
3. same-support literal order disagreement;
4. a top endpoint/internal discrepancy; or
5. the synchronized singleton-star configuration.

## 4. Every cube leaf produces a source-visible proper path or cycle

The point of the classification is not the labels themselves. What matters is that every leaf can be turned, before any payment or replay, into a graph-intrinsic proper tight path or a proper tight cycle with a named break, while retaining the source packet that created it.

For the first four leaves this is direct.

- In a component-drop comparison, an edge of an exact two-cover must cross two components of the inherited multi-path cover. Combining that selected crossing with an inherited neighboring edge and applying boundary antisymmetry gives a proper tight trimer.
- Under support disagreement, a selected edge of one exact cover crosses the support components of the other. Again, an inherited neighbor plus the crossing gives a source-visible proper tight trimer.
- Under literal order disagreement on one support, compare the two Hamilton orders. A first inversion yields either a reversed selected edge, a reverse tight trimer, or a vertex-simple proper tight cycle.
- Under top endpoint/internal discrepancy, the two nonidentical exact covers of the same residue feed the same exact-cover comparison mechanism.

The synchronized singleton-star leaf also enters the same downstream theorem. Fix a source spoke `s`. Puncture `s` from the retained top cover and compare the resulting three-component inherited cover with the complementary rank-two fiber. A crossing again emits a source-labelled proper tight path. This is the content of legacy PASS R2153.

Thus **all five cube leaves have the same usable output**:

> either `H` is already two-covered, or the retained phase-one source packet emits an actual proper tight path `K`, or a proper tight cycle with a named break producing such a path `K`.

That is the only information needed for the next stage.

## 5. Currentize the proper path

Let

`F_1,...,F_r`

be the finite retained packet of phase-one source checkpoints that participated in the comparison. In each `F_i`, mark a longest rail of order `M_i`, and define the coarse phase-one rank

`rho(F_i)=(1,n-M_i)`,

where `n=|H|`.

Let

`M_*=max_i M_i`.

Take the emitted proper path `K`. If it came from a cycle, cut at the certified break.

If `K` spans `H`, we are done. Otherwise, by minimality, `H-V(K)` has a path cover by at most two paths. It cannot be Hamiltonian, since a Hamilton path of the complement together with `K` would already two-cover `H`. Hence

`H-V(K)=U'|V'`

is an exact two-cover, and

`K|U'|V'`

is a spanning three-path forest retaining the original source ancestry.

Mark a longest rail `A` of this forest and write `L=|A|`.

If

`L>M_*`,

then

`(1,n-L)<(1,n-M_*)≤rho(F_i)`

for every participating source. We have already descended strictly below the entire source packet.

So the only interesting case is `L≤M_*`.

## 6. Grow the marked rail

Write the current forest as

`A|B|C`.

Try to transfer an endpoint of either donor rail into either end of `A`.

At the right end, if the relevant joining turn is tight and the donor is a singleton, the two rails merge and `H` is two-covered. If the donor is nontrivial, a second turn either concatenates the whole donor to `A`, again giving a two-cover, or allows one donor endpoint to be transferred to `A`. In that transfer, the marked rail grows by exactly one while the donor remains a path.

The left end is dual.

Perform any available growth greedily. Every successful step strictly increases `|A|`. Stop if:

1. a spanning two-cover appears;
2. `|A|` first reaches `M_*+1`; or
3. no inward endpoint transfer is possible at either end.

In the second case the phase-one rank is at most

`(1,n-M_*-1)`,

strictly below every source rank.

It remains to understand the no-slide terminal wall.

## 7. The terminal wall creates a certified phase-zero birth

At a wall, failure of rightward growth gives a reverse terminal dimer at the right end of `A`, certified by a donor source. Failure of leftward growth gives a reverse initial dimer at the left end, certified by a donor terminal vertex. The witnesses have opposite endpoint polarities.

A genuine wall has `|A|≥3`; order two would itself force a two-cover.

### 7.1 Marked rail of order at least four

If `|A|≥4`, the reverse boundary dimers at the two ends of `A` are physically disjoint. Their donor witnesses certify opposite polarities. Hence the wall contains a concrete opposite-sign `2+2` birth.

Retain that birth, its witnesses, the no-slide forest, and one actual tight turn `J` of `A`.

### 7.2 Marked rail of order three

If

`A=(a_0,a_1,a_2)`,

delete the hinge `a_1`. The residue inherits the literal four-cover

`{a_0}|{a_2}|B|C`.

Minimality gives an exact two-cover of the residue. Some selected edge of that two-cover must cross two components of the inherited four-cover. Boundary antisymmetry with the deleted hinge then gives a certified signed dimer of one polarity against the hinge singleton of the opposite polarity.

Thus the order-three wall yields a concrete opposite-sign `1+2` birth, again with the no-slide forest, the crossing data, and the fixed tight turn

`J=(a_0,a_1,a_2)`

retained.

### 7.3 The phase drop

Define this certified terminal-wall state to be the phase-zero entrance. Its coarse rank has leading coordinate `0`, whereas every source checkpoint had leading coordinate `1`.

Therefore

`(0,...)<(1,n-M_i)`

for every source `F_i`.

We have proved the first-source descent theorem:

> from a retained phase-one source packet that emits a source-visible proper path or certified cycle break, there is a finite continuation to TWO-COVER or to a retained checkpoint whose phased rank is strictly below every participating source.

The strictness is genuine. It comes either from increasing the marked rail beyond the old maximum `M_*`, or from the certified transition from phase one to phase zero.

## 8. Why this does not yet finish the theorem

The theorem above is intentionally source-relative.

It does **not** say that any proper path anywhere in `H` may restart the argument. It does not say that an arbitrary later opposite-sign pair automatically gives a new phase-zero descent. Most importantly, it is not a replay rule from a checkpoint already in phase zero.

So after the first strict descent, the proof still needs a recursive continuation theorem.

A historical attempt routed this continuation through the old E9006 payment layer. That proof carried an integrity warning at the migration baseline: it used signed interval rebirth as though cut memory alone created the current balanced pair needed for payment. That inference is not valid. E9006 must therefore not be used as the missing recursive bridge in its published form.

The accepted payment technology that any repaired continuation may use is narrower and more explicit: genuine marker/deletion events, signed cut memory only after those events, actual reformation of a current opposite-sign pair, and the lawful fixed-singleton descent machinery represented in the legacy chain R175/R427/R428, together with endpoint selection through R224/R433 when needed.

## 9. Exact unresolved step

Everything through the first strict phased-rank descent is supported by independently passed A7C3 mathematics. The remaining obligation is:

> **Recursive phase-zero continuation.** Starting from the certified terminal-wall phase-zero entrance, prove a lawful continuation that either produces TWO-COVER or reaches a genuinely smaller state in a well-founded global order, without pretending that the first-source descent theorem can simply be replayed.

There are at least two plausible forms such a theorem could take.

1. Repair the old phase-zero payment/continuation route using only the accepted marker, reformation, and fixed-singleton payment machinery.
2. Relate the phase-zero replay obstruction directly to the fixed-pair spent-history branch, showing that a would-be replay at phase zero necessarily consumes history in a way that cannot occur indefinitely.

The second possibility is especially attractive because the two active branches fail for complementary reasons: this branch has a strict rank but lacks a recursive replay theorem, while the fixed-pair branch has strong replay-history control but lacks a global monotone.

## 10. Provenance and integrity notes

The mathematical ingredients used above descend from the following legacy results.

- Small-order gate: E8997 / terminal PASS R2152.
- Three-spoke Boolean-cube classifier: E8998 / terminal PASS composition R2143.
- Nonsynchronized cube leaves entering first-source descent: PASS R2136 and the exact path/cycle constructors incorporated into E8998/E9003.
- Synchronized singleton-star entrance: PASS R2153.
- First-source prepayment phase descent: E9003 / whole-document PASS recomposition R2147.

The legacy chain `E9003 -> E9006 -> E9007` is **not** treated here as a certified continuation. E9006 is only a historical repair target until its payment argument is replaced or independently revalidated. This branch therefore ends honestly at the first certified phase-zero entrance rather than hiding the missing recursive step behind an Engine edge.
