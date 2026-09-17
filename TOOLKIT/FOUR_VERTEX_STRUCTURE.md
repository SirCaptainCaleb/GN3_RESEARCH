# Four-vertex structure and fifth-vertex extensions

**Status: REVISED AFTER AUDIT; PENDING RE-AUDIT.**

This module collects local structure theorems for non-Hamiltonian four-vertex boundary tournaments and their extensions. The revised exact text makes the finite forcing steps explicit and awaits independent re-audit.

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

Now `(a,c,d,b)` has second triple `(c,d,b)` tight, so non-Hamiltonicity forces `(d,c,a)`; and `(a,d,c,b)` forces `(c,d,a)`. Finally `(c,a,b,d)` and `(d,a,b,c)` force `(b,a,c)` and `(b,a,d)`.

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

**Proof.** Write `uvw` for the assertion that `(u,v,w)` is tight. Assume for contradiction that no Hamilton tight path on `X union {d}` places `d` one position from an endpoint.

Exactly one of `dab` and `bad` is tight. We treat the two cases separately. In each row below, two consecutive triples of the displayed five-vertex order are already tight. Since the order is not Hamiltonian, its third consecutive triple is non-tight, and boundary antisymmetry gives the forced triple in the last column.

If `dab` is tight, the following implications hold successively:

| known tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `dab, abc` | `z d a b c` | `adz` |
| `adz, zcb` | `a d z c b` | `czd` |
| `acz, czd` | `a c z d b` | `bdz` |
| `cab, bdz` | `c a b d z` | `dba` |
| `dba, baz` | `c d b a z` | `bdc` |
| `azb, bdc` | `a z b d c` | `dbz` |
| `dbz, bzc` | `a d b z c` | `bda` |
| `bda, acz` | `b d a c z` | `cad` |

Now `bca`, `cad`, and `adz` are all tight, so

`(b,c,a,d,z)`

is a Hamilton tight path, a contradiction.

If `bad` is tight, the analogous explicit chain is

| known tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `zba, bad` | `z b a d c` | `cda` |
| `bzc, cda` | `b z c d a` | `dcz` |
| `dcz, cza` | `b d c z a` | `cdb` |
| `cdb, baz` | `c d b a z` | `abd` |
| `cab, abd` | `c a b d z` | `zdb` |
| `zdb, bca` | `z d b c a` | `cbd` |
| `zcb, cbd` | `z c b d a` | `adb` |
| `cza, adb` | `c z a d b` | `daz` |

Now `cda`, `daz`, and `azb` are all tight, so

`(c,d,a,z,b)`

is a Hamilton tight path, again a contradiction.

Every five-vertex order displayed in the two tables, as well as the final path in each case, places `d` in position `1` or `3` when positions are numbered `0,...,4`. ∎

## 3. A non-Hamiltonian five-set over a non-Hamiltonian edge-ordered four-set

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

Suppose neither edge of `M_high` is outgoing from `d`. For `{t,l}`, at least one of `ltd,tld` is tight; for `{r,s}`, at least one of `srd,rsd` is tight. The four possibilities give contradictions as follows:

| tight triples | if this were tight | Hamilton path | forced reverse | Hamilton path |
| --- | --- | --- | --- | --- |
| `ltd, srd` | `rdt` | `l s r d t` | `tdr` | `s l t d r` |
| `ltd, rsd` | `sdt` | `l r s d t` | `tds` | `r l t d s` |
| `tld, srd` | `rdl` | `t s r d l` | `ldr` | `s t l d r` |
| `tld, rsd` | `sdl` | `t r s d l` | `lds` | `r t l d s` |

In each row the first displayed Hamilton path uses the two assumed mixed triples and one tight triple inside `X`. Since that path cannot exist, the middle mixed triple is non-tight and its reverse in the fourth column is tight; the last displayed order is then Hamiltonian. Thus some edge of `M_high` is outgoing.

Now suppose neither edge of `M_low` is incoming to `d`. For `{t,r}`, at least one of `drt,dtr` is tight; for `{l,s}`, at least one of `dsl,dls` is tight. Again the four possibilities are exhaustive:

| tight triples | if this were tight | Hamilton path | forced reverse | Hamilton path |
| --- | --- | --- | --- | --- |
| `drt, dsl` | `rds` | `r d s l t` | `sdr` | `s d r t l` |
| `drt, dls` | `ldr` | `l d r t s` | `rdl` | `r d l s t` |
| `dtr, dsl` | `tds` | `t d s l r` | `sdt` | `s d t r l` |
| `dtr, dls` | `tdl` | `t d l s r` | `ldt` | `l d t r s` |

Thus some edge of `M_low` is incoming.

For the forbidden directions, normalize instead

`M_low={ab,cz}`, `M_mid={ac,bz}`, `M_high={bc,az}`.

Suppose first that the high edge `bc` is incoming to `d`, so `bcd,cbd` are tight. The following five non-Hamiltonian candidate orders force the displayed reverses in sequence:

| known tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `abc, bcd` | `a b c d z` | `zdc` |
| `abz, zdc` | `a b z d c` | `dzb` |
| `dzb, zbc` | `a d z b c` | `zda` |
| `zcb, cbd` | `z c b d a` | `adb` |
| `zca, adb` | `z c a d b` | `dac` |

Then `zda,dac,acb` are tight, so `(z,d,a,c,b)` is Hamiltonian, a contradiction. The permutation exchanging `a` with `c` and `b` with `z` preserves all three matching blocks and exchanges the two edges of `M_high`, so neither high edge can be incoming.

Suppose next that the low edge `ab` is outgoing from `d`, so `dab,dba` are tight. The corresponding forcing chain is

| known tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `dba, baz` | `c d b a z` | `bdc` |
| `bdc, caz` | `b d c a z` | `acd` |
| `bac, acd` | `b a c d z` | `zdc` |
| `abz, zdc` | `a b z d c` | `dzb` |
| `dzb, zbc` | `a d z b c` | `zda` |

Then `zda,dab,abc` are tight, so `(z,d,a,b,c)` is Hamiltonian. The same permutation `(a c)(b z)` exchanges the two edges of `M_low`, so no low edge is outgoing. ∎

### 3.2 The middle matching alternates

Continue with

`M_low={{t,r},{l,s}}`,
`M_mid={{t,s},{l,r}}`,
`M_high={{t,l},{r,s}}`.

Suppose the high edge `{t,l}` is outgoing from `d` and the low edge `{t,r}` is incoming to `d`. Let `s` be the fourth vertex. Then exactly one of the two middle edges `{t,s}`, `{l,r}` is outgoing from `d`, and the other is incoming to `d`.

**Proof.** Put

`A=[(d,t,s) is tight]`, `B=[(d,s,t) is tight]`,
`C=[(d,r,l) is tight]`, `D=[(d,l,r) is tight]`.

The block order gives the tight triples

`rts, trl, lrs, lst, tsr, rlt, slr, stl`.

We prove the four implications explicitly.

**`A=>B`.** Suppose `A` holds and `B` fails. Then `tsd` is tight. If `sdl` were tight, `(r,t,s,d,l)` would be Hamiltonian, so `lds` is tight. If `rld` were tight, `(t,r,l,d,s)` would be Hamiltonian, so `D=dlr` is tight. If `tdl` were tight, `(t,d,l,r,s)` would be Hamiltonian, so `ldt` is tight. But now `(l,d,t,s,r)` is Hamiltonian, using `ldt`, `A=dts`, and `tsr`. Thus `A=>B`.

**`B=>A`.** Suppose `B` holds and `A` fails. Then `std` is tight. If `tdr` were tight, `(l,s,t,d,r)` would be Hamiltonian, so `rdt` is tight. If `lrd` were tight, `(s,l,r,d,t)` would be Hamiltonian, so `C=drl` is tight. If `sdr` were tight, `(s,d,r,l,t)` would be Hamiltonian, so `rds` is tight. But then `(r,d,s,t,l)` is Hamiltonian, using `rds`, `B=dst`, and `stl`. Thus `B=>A`.

**`C=>D`.** Suppose `C` holds and `D` fails. Then `rld` is tight. If `sdr` were tight, `(s,d,r,l,t)` would be Hamiltonian, so `rds` is tight. If `dst` were tight, `(r,d,s,t,l)` would be Hamiltonian, so `tsd` is tight. If `sdl` were tight, `(r,t,s,d,l)` would be Hamiltonian, so `lds` is tight. But then `(t,r,l,d,s)` is Hamiltonian, using `trl`, `rld`, and `lds`. Thus `C=>D`.

**`D=>C`.** Suppose `D` holds and `C` fails. Then `lrd` is tight. If `tdl` were tight, `(t,d,l,r,s)` would be Hamiltonian, so `ldt` is tight. If `dts` were tight, `(l,d,t,s,r)` would be Hamiltonian, so `std` is tight. If `tdr` were tight, `(l,s,t,d,r)` would be Hamiltonian, so `rdt` is tight. But then `(s,l,r,d,t)` is Hamiltonian, using `slr`, `lrd`, and `rdt`. Thus `D=>C`.

Therefore `A=B` and `C=D`. If both common values were `0`, then `std` and `lrd` would be tight. Non-Hamiltonicity of `(l,s,t,d,r)` forces `tdr` to be non-tight, hence `rdt` is tight; then `(s,l,r,d,t)` is Hamiltonian. If both common values were `1`, then `B=D=1`; non-Hamiltonicity of `(r,d,s,t,l)` forces `rds` to be non-tight, hence `sdr` is tight; then `(s,d,r,l,t)` is Hamiltonian.

Thus the two common values differ. If `A=B=1`, the middle edge `{t,s}` is outgoing from `d`; if `A=B=0`, boundary antisymmetry makes both `tsd,std` tight, so `{t,s}` is incoming. The same statement holds for `{l,r}` using `C=D`, and the two directions are opposite. ∎

### 3.3 An ordered exterior edge extending in both directions forces a Hamilton P5 or P6

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