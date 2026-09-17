# Above order eleven every pair frame has a five-root P5 avoiding any prescribed singleton deletion, forcing row component drop

**Workspace:** D17
**State:** established
**Key:** `pair-frame-avoid-one-five-root-singleton-instability`

**Summary:** Let H be a hypothetical smallest counterexample of order n>=12, fix any physical pair E={a,c}, any exact two-cover H-E=U|V, and any prescribed x outside E. The two nontrivial rails have n-6>=6 internal vertices. Excluding x leaves at least five internal vertices; coloring each b by which of (a,b,c),(c,b,a) is tight gives three of one orientation. The three-spoke lemma inside SV58280 therefore gives a Hamilton P5 K_x on E plus those three middles, with x notin K_x. Now take ANY exact two-cover C_x of H-x. All five K_x vertices survive in C_x, but two rails have at most four physical endpoints, so some f in K_x is internal. Puncturing f gives a literal three-cover of H-{x,f}; R429 gives an exact two-cover of the same residue and R159/R176 gives a selected component-crossing balanced-pair birth with source ancestry. Thus no exact H-x row can be a terminal quiet species relative to the chosen pair frame: it universally exposes one of five rooted component drops. At n=11 this counting argument can fail only when x itself is one of the five internal vertices of the source frame and the remaining four split 2+2 between the two outer-orientation classes; no order-eleven closure is claimed.

### 1. Pair frame and one forbidden singleton label
Let H be a hypothetical smallest Strong Level-(1) counterexample of order

  n>=12.                                                   (AO.1)

Fix any distinct physical pair

  E={a,c}                                                  (AO.2)

and any literal exact two-cover

  H-E=U|V.                                                 (AO.3)

Accepted R429 makes both rails nontrivial. Fix any prescribed vertex

  x outside E.                                             (AO.4)

The aim is to choose the five-root P5 of SV58280 so that it avoids x.

### 2. At least five internal middles remain after forbidding x
Because U,V are two nontrivial vertex-disjoint paths spanning n-2 vertices, they have exactly four physical rail endpoints in total. Hence the number of internal rail vertices is

  (|U|-2)+(|V|-2)=n-6>=6.                                (AO.5)

If x is internal in (AO.3), discard x from this pool. At least five internal vertices remain. If x is a rail endpoint, no internal vertex is discarded, so at least six remain. Thus in every case there is a set B_x of at least five internal vertices, all distinct from x.

For each b in B_x, boundary antisymmetry R3 makes exactly one of

  (a,b,c),
  (c,b,a)                                                  (AO.6)

tight. Two colors on at least five vertices give three distinct middles

  b_1,b_2,b_3 in B_x                                      (AO.7)

with one common outer orientation. Exchange the display names a,c if necessary so that

  (a,b_i,c) is tight,  i=1,2,3.                           (AO.8)

### 3. Three-spoke lemma gives a P5 avoiding x
Section 1 of `closed-return-pair-deletion-five-root-p5-fan` SV58280 is the pure THREE-SPOKE P5 lemma: three tight turns (a,b_i,c) force a Hamilton tight P5 on

  K_x={a,c,b_1,b_2,b_3}.                                  (AO.9)

By construction every b_i avoids x and x is outside E, so

  x notin K_x.                                            (AO.10)

Thus one and the same exact pair frame (AO.3) supplies, for every prescribed x outside E, a five-root Hamilton P5 whose support avoids x.

### 4. Every exact H-x row has an internal K_x root
Now choose ANY literal exact two-cover

  C_x=P|Q of H-x.                                         (AO.11)

All five vertices of K_x survive in H-x by (AO.10). A two-path cover has at most four distinct physical rail endpoints. Therefore at least one

  f in V(K_x)                                              (AO.12)

is internal on its C_x rail. Write locally

  (...,r,f,s,...).                                         (AO.13)

Deleting f splits that rail into two nonempty inherited tight intervals while the other rail survives. Hence

  R_{x,f}=C_x-f                                            (AO.14)

is a literal three-cover of

  W_{x,f}=H-{x,f}.                                         (AO.15)

Accepted pair-deletion rigidity R429 gives an exact two-cover

  T_{x,f} of W_{x,f}.                                      (AO.16)

Accepted R159 now applies to the three-versus-two component drop. Its fully reconstructed proof selects an actual T_{x,f}-state crossing two distinct R_{x,f}-components and invokes R176 on that exact state. Thus retain a source-visible balanced-pair birth together with

- the original pair frame H-E=U|V;
- the avoiding P5 K_x;
- the exact singleton row C_x;
- the internal root f and its two cut sides;
- the exact pair-deletion cover T_{x,f};
- the selected component crossing and R176 birth certificate.          (AO.17)

### 5. Universal singleton-row instability above order eleven
Therefore:

> For n>=12, every exact pair-deletion frame H-E and every prescribed x outside E determine a five-root Hamilton P5 K_x avoiding x such that EVERY exact singleton-deletion row H-x has at least one K_x-root internal and therefore exposes a source-visible R159/R176 component-drop portal on H-{x,f}.

This is stronger than an existential choice of a convenient singleton row. Once the source pair frame and x are fixed, no exact H-x representative escapes the five-root internal-root pressure.

In particular, whenever a G26 local compiler built over one fixed pair frame emits an exact H-x row with x outside that pair, the row is not a new terminal current species. Before payment it already re-enters the finite rooted component-drop alphabet.

### 6. Exact order-eleven fence
At n=11 the source frame has exactly

  n-6=5                                                    (AO.18)

internal rail vertices. If x is a rail endpoint, all five internal vertices remain and the proof above still works. If x is internal, only four internal vertices remain after forbidding x. The pigeonhole step can then fail only when those four vertices split exactly

  2+2                                                      (AO.19)

between the two outer-orientation classes in (AO.6).

Thus the precise failure of this proof mechanism at order eleven is:

  x is internal in the chosen source frame,
  and the other four internal vertices have a 2+2 orientation split.   (AO.20)

No claim is made here that this order-eleven cell is impossible. Accepted R957 eliminates n=11 only in the separate uniform middle-layer arm; it is not used here.

### 7. Scope fence
The resulting R159/R176 pair may still pay and return flat at phase zero. This theorem is therefore a bottom-family alphabet reduction, not a numerical Morse descent. Its content is that exact singleton rows generated from a fixed pair-frame lineage cannot become ancestry-free sinks above order eleven: they must immediately expose one of five rooted current component drops.

R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```