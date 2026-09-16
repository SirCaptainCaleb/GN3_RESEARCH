# Branch A: fixed-pair return and spent-history obstruction

**Status: active proof-spine reconstruction; unresolved at the final replay-extinction step; this GN3 rewrite is not yet independently audited.**

## 1. Shared starting point

Assume that the two-path-cover theorem is false, and let `H` be a smallest counterexample. The certified small-order argument gives

`|H|>10`.

Fix an arbitrary physical pair

`E={a,c}`.

Every exterior vertex `x∈V(H)-E` has exactly one of the two source orientations

`(a,x,c)` or `(c,x,a)`

tight, by boundary antisymmetry. Thus the exterior vertices split into two orientation classes.

The purpose of this branch is to use one fixed pair `E` as a literal return floor. We repeatedly build a short opposite-sign birth from two same-oriented source vertices, pay that birth back down to the same floor `E`, and retain the fact that the source-boundary dimers have been strictly clipped in the historical ancestry. After enough such returns, almost every exterior vertex has already been spent on both sides. Any genuinely later opposite-sign dimer birth must therefore meet spent history.

The remaining problem is to show that this collision cannot replay forever.

## 2. Two same-oriented source turns give an opposite-sign `2+2`

Choose distinct exterior vertices `s,t` having the same source orientation. After interchanging `a,c` if necessary, suppose

`(a,s,c)` and `(a,t,c)`

are tight.

These two turns display two physically disjoint source-boundary dimers:

- `(a,s)`, carrying the polarity witnessed by `c`;
- `(t,c)`, carrying the opposite endpoint polarity witnessed by `a`.

Their supports are disjoint because `a,c,s,t` are distinct. Hence they form the named opposite-polarity `2+2` birth used below.

This birth is not merely an abstract sign pattern. Both dimers are actual physical subpaths of retained source turns, with their witnesses and source ancestry remembered.

## 3. Endpoint-selected payment returns to the literal floor `E`

The key payment fact is endpoint-selective: from an ancestry-bearing opposite-sign pair of two disjoint dimers, one may prescribe one endpoint of each dimer and continue to either a spanning two-cover or the corresponding pair of singleton rails.

Apply it to the two dimers above, prescribing `a` on `(a,s)` and `c` on `(t,c)`. Unless `H` is already two-covered, the continuation reaches the literal floor

`(a)|(c)`.

The important point is that this payment is lawful. The accepted mechanism does **not** infer a fresh current balanced pair merely from cut memory. In the legacy proof, one first pays one chosen dimer endpoint through the inherited-turn continuation; after a genuine marker/deletion, signed interval rebirth only remembers the surviving signed interval, and a separate step reforms an actual current opposite-sign pair. The fixed-singleton descent then pays the other support down to a singleton. If the second surviving singleton is not the prescribed endpoint, the opposite-singleton replacement theorem moves it to the desired endpoint while keeping the first singleton fixed.

Thus the usable mathematical interface is exactly:

> from the displayed source `2+2`, choose the endpoints `a,c`; then either TWO-COVER occurs or the active state returns to the same literal floor `E={a,c}`.

This distinction matters because an earlier attempted composition incorrectly treated signed cut memory by itself as a complete payment theorem. That reconstruction is not used here.

## 4. The return spends the named source birth

At the floor `(a)|(c)`, compare each active singleton with the corresponding historical source-boundary dimer.

The singleton `(a)` meets the historical dimer `(a,s)` at `a`, which is away from the signed anchor `s`. Signed path-contact protection therefore gives a strict historical clipping of that dimer to the singleton descendant

`(s)`.

Likewise `(c)` meets the historical dimer `(t,c)` away from its signed anchor `t`, giving the strict historical singleton descendant

`(t)`.

Hence the continuation has returned to the same literal active floor `E={a,c}`, while the retained ancestry records that the named opposite-sign `2+2` birth has been physically reduced to strict singleton descendants at its two middle vertices.

This is the one-return mechanism. In legacy notation it is exactly the theorem-level content of PASS R2222:

> if `(a,s,c)` and `(a,t,c)` are same-oriented source turns, there is an ancestry-retaining continuation to TWO-COVER or to the literal floor `{a,c}` carrying strict historical singleton descendants `(s)` and `(t)` of the named opposite-polarity `2+2` birth.

Because any three exterior vertices contain two of the same source orientation, the mechanism is available at every prescribed pair `E` once at least three exterior vertices exist.

## 5. Bilaterally spending almost every exterior vertex

One return spends one boundary side at `s` and the complementary boundary side at `t`. To spend both sides at both vertices, use the same pair twice with the ordered source roles reversed.

For same-oriented `s,t`:

1. apply the return mechanism with roles `(s,t)`, clipping `(a,s)` at `s` and `(t,c)` at `t`;
2. apply it again with roles `(t,s)`, clipping `(a,t)` at `t` and `(s,c)` at `s`.

Both applications return to the same literal floor `E`, and retained ancestry is cumulative. Unless TWO-COVER appears, both `s` and `t` now carry historical singleton descendants from both of their source-boundary dimers. Call such a vertex **bilaterally spent** for the fixed pair `E`.

Now work separately in the two source-orientation classes. In a class of size at least two, choose a pivot `t` and pair it successively with every other member, applying the two ordered returns above. Every member of that class becomes bilaterally spent. A class of size zero or one contributes at most one unspent vertex.

Since there are only two orientation classes, one can organize the pairings so that, after finitely many same-floor returns, all exterior vertices except possibly one are bilaterally spent. This is the fixed-pair harvesting theorem (legacy PASS R2224).

Therefore:

> after the harvesting sequence, every later physically disjoint opposite-polarity `2+2` birth meets a bilaterally spent exterior vertex.

Indeed, two disjoint dimers use four physical vertices, whereas at most one exterior vertex is unspent and the fixed pair contributes only two vertices. A wholly fresh later `2+2` is impossible.

## 6. What a later collision with spent history gives

Let a genuinely later opposite-sign dimer birth meet a bilaterally spent vertex `s`. The old source turn `(a,s,c)` and both old source-boundary histories at `s` are retained.

There are two qualitatively different possibilities.

### 6.1 Exact old-boundary replay

If the later active support at `s` is exactly one of the old source-boundary supports, namely `{a,s}` or `{s,c}`, then contact with the historical singleton descendant may replay entirely inside the old source trimer `(a,s,c)`.

This is not automatically progress. The exact singleton-contact analysis shows that both old boundary contacts can be realized without creating a new vertex or a longer object. Thus the mere statement “the later birth hits spent ancestry” is insufficient for closure.

This is the genuine equality/replay obstruction.

### 6.2 A new endpoint appears

Suppose instead that a later nontrivial dimer containing `s` has other endpoint

`u∉{a,c}`.

Then contact with the retained old signed source boundary is no longer confined to the exact old two-vertex support. Signed path-contact protection forces strict growth or reverse-contact geometry in which the new endpoint `u` remains visible. Pure replay is possible only on the exact old boundary supports `{a,s}` and `{s,c}`.

So every later remint through a spent vertex has the following dichotomy:

- exact old-boundary replay; or
- genuinely new endpoint-bearing geometry.

The second branch is promising because it creates information not present in the original source trimer. The first branch is the only stationary obstruction.

## 7. A richer harvested configuration is always available

The order gate `|H|>10` gives at least nine vertices outside `E`. One source-orientation class therefore has at least five members. Since harvesting leaves at most one exterior vertex unspent, that larger class contains at least four bilaterally spent vertices.

Among any four same-oriented spokes one can choose three, say `x,y,z`, such that

`(x,a,y,c,z)`

is a literal tight `P5`.

Thus, after fixed-pair harvesting, we may retain a harvested five-vertex path crossing the same anchors `a,c`. The useful point is not the old label attached to this configuration, but the extra physical geometry: three spent spokes are simultaneously arranged around the same fixed pair in a concrete tight path.

This provides more structure with which to attack a later exact-boundary replay or to absorb the new endpoint from the nonreplay branch.

## 8. Exact unresolved step

Everything above is already supported by independently passed A7C3 mathematics. The branch stops at one precise obligation:

> **Spent-history replay extinction.** After the fixed-pair harvesting sequence, take a genuinely later opposite-polarity `2+2` birth. It must meet a bilaterally spent vertex. Prove that the complete later birth, together with the retained spent source history, forces either a spanning two-cover or a strict nonreplayable continuation.

The local analysis has already reduced the problem to two cases:

1. the later dimer through the spent vertex uses a new endpoint, in which case strict growth or reverse-contact geometry is available and must be consumed together with the second dimer of the later birth; or
2. the later dimer is exactly an old source-boundary support, in which case one must use the second dimer, the opposite polarity, the other spent boundary, or the harvested multi-spoke geometry to rule out stationary replay.

No currently accepted theorem completes that last implication. This is the live frontier of this branch.

## 9. Provenance and integrity notes

The mathematical ingredients used above descend from the following legacy results.

- Small-order gate: E8997 / terminal PASS R2152.
- Same-floor strict return: PASS R2222.
- Fixed-pair harvesting: PASS R2224.
- Exact replay-cell warning: PASS R2226.
- New-endpoint contact dichotomy: PASS R2229.
- Harvested multi-spoke `P5`: PASS R2230 and its hypothesis-free parent PASS R2231.
- Endpoint-selective payment interface: PASS R2185, built from the accepted R224 and R433 mechanisms.
- Lawful fixed-singleton payment backbone used by those mechanisms: R175, R427, R428 and the reformation step inside R224.
- Signed contact protection: S9010.
- Signed interval rebirth/cut memory: S9014, used only for the limited cut-memory role it actually proves.

Two later E9007 terminal composition drafts, R2225 and R2228, were invalidated because they attempted to reconstruct the payment layer too aggressively. Their failure does not invalidate R2222 or the branch above. E9006 likewise carried an integrity warning at the migration baseline and is not used as a payment source here.
