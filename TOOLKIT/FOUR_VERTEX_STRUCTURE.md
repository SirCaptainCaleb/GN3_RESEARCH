# Four-vertex structure and fifth-vertex extensions

**Status: UNAUDITED GN3 REWRITE.**

This module collects local structure theorems for non-Hamiltonian four-vertex boundary tournaments and their extensions. The exact text has not yet received independent GN3 audit.

## 1. Two parallel turns force one of two edge-orderable four-vertex forms

Let `a,b,c,d` be distinct vertices of a boundary tournament. Suppose

`(a,b,c)`, `(a,b,d)`

are tight and the induced four-vertex tournament has no Hamilton tight path. Then the following six additional triples are tight:

`(b,a,c)`, `(b,a,d)`,

`(c,d,a)`, `(d,c,a)`,

`(c,d,b)`, `(d,c,b)`.

Moreover exactly two completions of the boundary relation are possible. Put

`M_0={ab,cd}`, `M_1={ac,bd}`, `M_2={ad,bc}`.

The induced boundary tournament is represented by an edge order in which the three opposite-edge matchings occur as strict blocks, with either

`M_0 < M_1 < M_2`

or

`M_0 < M_2 < M_1`.

**Proof.** Since `(a,b,c)` is tight, the candidate path `(a,b,c,d)` can fail only at `(b,c,d)`; hence `(d,c,b)` is tight. Similarly `(a,b,d,c)` forces `(c,d,b)`.

Now `(a,c,d,b)` has second triple `(c,d,b)` tight, so no-Hamiltonicity forces `(d,c,a)`; and `(a,d,c,b)` forces `(c,d,a)`. Finally `(c,a,b,d)` and `(d,a,b,c)` force `(b,a,c)` and `(b,a,d)`.

The only remaining freedom can be taken to be the reversal pair `(a,c,b)` versus `(b,c,a)`.

If `(a,c,b)` is tight, repeated use of a four-vertex Hamilton candidate whose other triple is already known forces

`(d,b,c)`, `(b,d,a)`, `(c,a,d)`

and the reverses of their opposite choices. These are exactly the comparisons represented by the block order `M_0<M_1<M_2`.

If `(b,c,a)` is tight, the same forcing gives

`(d,a,c)`, `(a,d,b)`, `(c,b,d)`,

which are exactly the comparisons represented by `M_0<M_2<M_1`.

Both block orders have no increasing Hamilton four-vertex path by the non-Hamiltonian `K_4` classification in Lemma 2.4 of the proof spine, so both completions occur and there are no others. ∎

## 2. The cyclic non-Hamiltonian four-vertex configuration is extended by every fifth vertex

Let `X={a,b,c,z}` induce the boundary tournament whose tight triples, one from each reversal pair, are

`abc, bca, cab, zba, azb, baz, acz, cza, zac, zcb, bzc, cbz`.

Then for every vertex `d outside X`, the five-set `X union {d}` has a Hamilton tight path in which `d` is one position from an endpoint.

**Proof.** Every candidate used below places `d` one position from an endpoint. Assume none is a Hamilton tight path. Whenever a candidate already has two required triples tight, failure forces the reverse of its third required triple by boundary antisymmetry.

Starting from `(d,a,b)` tight, the following implications are forced:

`dab => adz => czd => bdz => dba => bdc => dbz => bda => cad => zda => bad`.

Starting from `(b,a,d)` tight gives

`bad => cda => dcz => cdb => abd => zdb => cbd => adb => daz => adc => dab`.

The triples `dab` and `bad` are reverses, so exactly one is tight. Either choice forces the other, a contradiction. Hence one of the candidate Hamilton paths used in the implication chains must exist. In each such candidate, `d` is in position `1` or `3` of the five-vertex order. ∎

## 3. A P5-free fifth vertex over a non-Hamiltonian edge-ordered four-set

Let `X` be a non-Hamiltonian edge-ordered `K_4`. By Lemma 2.4 of the proof spine, its three opposite-edge perfect matchings occur in strict blocks. Write

`M_low < M_mid < M_high`

when every edge of `M_low` precedes every edge of `M_mid`, and every edge of `M_mid` precedes every edge of `M_high`.

For a vertex `d outside X` and an edge `{u,v}` of `X`, call `{u,v}`

- **outgoing from `d`** if `(d,u,v)` and `(d,v,u)` are both tight;
- **incoming to `d`** if `(u,v,d)` and `(v,u,d)` are both tight.

Assume `X union {d}` has no Hamilton tight path.

### 3.1 Extreme matching edges

At least one edge of `M_high` is outgoing from `d`, and at least one edge of `M_low` is incoming to `d`.

No edge of `M_high` is incoming to `d`, and no edge of `M_low` is outgoing from `d`.

**Proof.** Normalize

`M_low={{t,r},{l,s}}`,
`M_mid={{t,s},{l,r}}`,
`M_high={{t,l},{r,s}}`.

Suppose neither high edge is outgoing. Then for `{t,l}` at least one of `(l,t,d),(t,l,d)` is tight, and for `{r,s}` at least one of `(s,r,d),(r,s,d)` is tight. There are four choices. In each case a single additional mixed triple either immediately gives a Hamilton P5 or, if it fails, its reverse combines with the other known triples to give one:

- from `ltd,srd`, failure of `(r,d,t)` forces `(t,d,r)`, and `(s,l,t,d,r)` is tight;
- from `ltd,rsd`, failure of `(s,d,t)` forces `(t,d,s)`, and `(r,l,t,d,s)` is tight;
- from `tld,srd`, failure of `(r,d,l)` forces `(l,d,r)`, and `(s,t,l,d,r)` is tight;
- from `tld,rsd`, failure of `(s,d,l)` forces `(l,d,s)`, and `(r,t,l,d,s)` is tight.

Thus some high edge is outgoing. The proof that some low edge is incoming is the reversed argument, or explicitly the same four-case check after exchanging the roles of beginning and end.

For the forbidden polarities, normalize instead

`M_low={ab,cz}`, `M_mid={ac,bz}`, `M_high={bc,az}`.

Suppose the high edge `bc` were incoming, so `(b,c,d),(c,b,d)` were tight. Successive P5 failures force

`(z,d,c)`, `(d,z,b)`, `(z,d,a)`, `(a,d,b)`, `(d,a,c)`.

Then `(z,d,a,c,b)` is a Hamilton P5, contradiction. Symmetry exchanges the two high edges. Dually, if the low edge `ab` were outgoing, successive P5 failures force

`(b,d,c)`, `(a,c,d)`, `(z,d,c)`, `(d,z,b)`, `(z,d,a)`,

and `(z,d,a,b,c)` is Hamilton. Symmetry handles the other low edge. ∎

### 3.2 The middle matching alternates

Continue with

`M_low={{t,r},{l,s}}`,
`M_mid={{t,s},{l,r}}`,
`M_high={{t,l},{r,s}}`.

Suppose the high edge `{t,l}` is outgoing from `d` and the low edge `{t,r}` is incoming to `d`. Let `s` be the fourth vertex. Then exactly one of the two middle edges `{t,s}`, `{l,r}` is outgoing from `d`, and the other is incoming to `d`.

**Proof.** Put

`A=[(d,t,s) is tight]`, `B=[(d,s,t) is tight]`,
`C=[(d,r,l) is tight]`, `D=[(d,l,r) is tight]`.

Using only the block order on `X`, the assumed high/low gates, P5-freeness, and boundary antisymmetry, one obtains

`A=>B`, `B=>A`, `C=>D`, `D=>C`.

For example, if `A` holds but `B` fails, then `(t,s,d)` is tight. Avoiding successively

`(r,t,s,d,l)`, `(t,r,l,d,s)`, `(t,d,l,r,s)`

forces `(l,d,s)`, then `D`, then `(l,d,t)`; now `(l,d,t,s,r)` is Hamilton, contradiction. The other three implications are the same argument after the evident relabellings.

Thus `A=B` and `C=D`. If both common values were `0`, then `(s,t,d)` and `(l,r,d)` are tight; avoiding `(l,s,t,d,r)` forces `(r,d,t)`, after which `(s,l,r,d,t)` is Hamilton. If both common values were `1`, avoiding `(r,d,s,t,l)` forces `(s,d,r)`, after which `(s,d,r,l,t)` is Hamilton. Hence the two common values differ, proving the claim. ∎

### 3.3 A bidirectional bridge edge forces a Hamilton P5 or P6

Normalize the matching blocks as

`M_low={ab,cz}`, `M_mid={ac,bz}`, `M_high={bc,az}`.

Let `u,v` be distinct vertices outside `X`. Suppose that for every `x in X`, both

`(x,u,v)` and `(u,v,x)`

are tight. Then either `X union {u}` has a Hamilton tight path or `X union {u,v}` has a Hamilton tight path.

**Proof.** The block order gives the tight triples

`(b,a,c)`, `(c,z,b)`, `(c,a,z)`, `(b,z,a)`.

Assume for contradiction that neither a Hamilton P5 on `X union {u}` nor a Hamilton P6 on `X union {u,v}` exists.

Since `(c,u,v)` and `(u,v,z)` are tight, the candidate

`(b,a,c,u,v,z)`

forces `(a,c,u)` to be non-tight, so `(u,c,a)` is tight. Similarly, from `(b,u,v)` and `(u,v,a)`, failure of

`(c,z,b,u,v,a)`

forces `(u,b,z)` tight.

Now in `X union {u}`, failure of `(b,u,c,a,z)` forces `(c,u,b)` tight. But then

`(c,u,b,z,a)`

is a Hamilton P5, contradiction. ∎

## 4. Three of the five four-subsets of an edge-ordered K5 are Hamiltonian

Every edge-ordered `K_5` has at least three vertex deletions whose remaining four vertices admit an increasing Hamilton path. Equivalently, at most two of its five induced `K_4`s are non-Hamiltonian.

Consequently, if `h_4(r)` is the number of four-subsets of an edge-ordered `K_r`, `r>=5`, that admit an increasing Hamilton path, then

`h_4(r) >= (3/5) binom(r,4)`.

**Proof.** In a non-Hamiltonian edge-ordered `K_4`, Lemma 2.4 says the three opposite-edge perfect matchings occur in strict blocks. Hence for adjacent edges `e,f`, comparison is preserved on passing to their opposite edges `e*,f*`:

`e<f` if and only if `e*<f*`.

Suppose an edge-ordered `K_5` on `{a,b,c,d,e}` had three non-Hamiltonian vertex-deleted `K_4`s. Relabel so the bad four-sets are obtained by deleting `a,b,c`.

In `{b,c,d,e}`,

`bd<be` iff `ce<cd`.

In `{a,c,d,e}`,

`ce<cd` iff `ad<ae`.

In `{a,b,d,e}`,

`ad<ae` iff `be<bd`.

Chaining gives `bd<be` if and only if `be<bd`, impossible. Thus at most two four-subsets are non-Hamiltonian.

For the density statement, count pairs `(X,Y)` where `X` is a Hamiltonian four-set and `Y` is a five-set containing it. Every five-set contributes at least three such pairs, while every four-set lies in exactly `r-4` five-sets. Hence

`(r-4)h_4(r) >= 3 binom(r,5)`,

which simplifies to the displayed bound. ∎

## Legacy provenance

Section 1 rewrites A7C3 `S9026`; Section 2 rewrites `S9027`; Section 3 rewrites the reusable content of `S9028`; Section 4 rewrites `S9039` using the `K_4` classification already present in the proof spine.