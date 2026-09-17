# Every pair-deletion frame contains a five-root Hamilton crossing and paid-return fan

**Workspace:** D17
**State:** established
**Key:** `closed-return-pair-deletion-five-root-p5-fan`

**Summary:** Fix any exact pair-deletion cover H-{a,c}=U|V in a hypothetical smallest counterexample. Since |H|>10, the two rails have at least five internal vertices in total. Boundary antisymmetry colors each internal b by the tight orientation of the outer-pair turn on {a,b,c}; three internals share one orientation. A pure five-vertex lemma, proved from R887+R902, says three tight turns (a,b_i,c) with common outer pair force a Hamilton P5 on {a,c,b_1,b_2,b_3}. This P5 K has two simultaneous family-level consequences. First, for every d in K, R508 forces every exact singleton-deletion cover of H-d to cross (K-d)|(H-K), giving five universal deletion-crossing walls from one physical K. Second, deleting the three internal middles from U|V leaves at least three nonempty path components on H-K, while minimality gives an at-most-two cover of H-K. The resulting component drop has a selected cross-state, and the fully reconstructed R176 route may choose any d in K as spare, giving a balanced pair with literal singleton d and opposite support of order at most two; R428 therefore gives closure or an ancestry-bearing floor preserving d. Thus one pair-deletion frame supplies five alternative rooted paid-return lineages sharing the same Hamilton P5 and source-frame ancestry. This is a constraint on any closed rank-flat return family, not a proof that such a family is impossible.


### 1. A pure three-spoke five-vertex lemma
Let \(a,c,x,y,z\) be five distinct vertices in a Strong Level-(1) boundary tournament. Assume

  (a,x,c), (a,y,c), (a,z,c)

are all tight. Then the five-set

  K={a,c,x,y,z}

has a Hamilton tight P5.

Suppose not. Accepted R902 makes the induced five-vertex boundary tournament edge-orderable. Let λ be a strict total order on its ordinary edges realizing tight turns through accepted R887. The three displayed tight turns give

  ax < xc,  ay < yc,  az < zc.                           (FR.1)

Choose x so that ax is minimum among ax,ay,az. Relabel y,z so that yc<zc. Then

  ax < ay < yc < zc.                                     (FR.2)

Therefore the vertex order

  (x,a,y,c,z)                                             (FR.3)

has strictly increasing consecutive edge labels, hence is a tight Hamilton P5 by R887, contradiction. The complete-reversal outer orientation (c,*,a) is the exact dual after exchanging a and c.

Call this the THREE-SPOKE P5 lemma.

### 2. Every pair-deletion frame supplies three like-oriented internal middles
Let H be a hypothetical smallest counterexample. By accepted R533, n=|V(H)|>10. Fix arbitrary distinct vertices a,c and any literal exact two-cover

  H-{a,c}=U|V                                             (FR.4)

with both rails nontrivial; accepted R429 guarantees such covers exist and are nontrivial for every physical pair.

Across two nontrivial paths there are exactly four rail endpoints. Hence the total number of vertices internal on their displayed rails is

  (n-2)-4 = n-6 >= 5.                                    (FR.5)

For every such internal vertex b, R3 says exactly one of

  (a,b,c), (c,b,a)                                       (FR.6)

is tight. Thus the internal vertices split into two outer-orientation classes. By pigeonhole, at least three distinct internal vertices b1,b2,b3 lie in one class. After exchanging a,c if necessary,

  (a,b_i,c) is tight, i=1,2,3.                           (FR.7)

Section 1 therefore gives a literal Hamilton P5 K on

  V(K)={a,c,b1,b2,b3}.                                   (FR.8)

The three b_i are retained as actual internal vertices of the one common exact frame (FR.4), not as unrelated representatives.

### 3. One K creates five universal singleton-deletion crossing walls
Fix any d in V(K). Put

  D={d},  S=V(K)-{d}.                                    (FR.9)

The physical path K spans exactly D union S. Since n>10, H-K is nonempty. Apply accepted R508 to any exact two-cover T of H-d. It forces T to select an adjacent state with exactly one endpoint in S and the other in V(H)-V(K). Therefore, simultaneously as graph-intrinsic consequences of the one path K,

  every exact cover of H-d crosses
  (K-d) | (H-K)                                          (FR.10)

for each of the five choices d in K.

Thus K is not merely a local P5 portal. It carries a FIVE-ROOT SINGLETON-DELETION CROSSING FAN.

### 4. The same K creates five rooted component-drop pair births
Now delete the three internal middle vertices b1,b2,b3 from the source frame (FR.4). Because every b_i was internal, every rail from which at least one b_i is deleted splits into at least two nonempty old-order intervals; any untouched rail remains one nonempty component. Hence the old frame restricts to a literal path cover

  R_K of H-K

with at least three nonempty components.                 (FR.11)

On the other hand H-K is a nonempty proper induced subsystem, so accepted minimality R4 supplies a literal cover T_K of H-K by at most two tight paths. Since T_K has fewer components than R_K, some selected state xy of T_K has its endpoints in two distinct R_K-components: otherwise every T_K component would lie inside one R_K component and could not reduce component count.

Now use the fully reconstructed R176/P540 cross-state route. Its spare vertex may be chosen arbitrarily outside H-K. Therefore for EVERY chosen

  d in V(K)                                               (FR.12)

choose the spare to be d. R176 then gives a graph-intrinsic balanced opposite-sign pair whose one support is literally the singleton (d) and whose opposite support has order at most two, retaining the cross-state xy and its source-component ancestry. If the opposite support is already singleton we have an ancestry-bearing floor; if it is a dimer, accepted R428 pays it, preserving (d), to a both-singleton floor or closes H.

Consequently the one source frame and one majority triple produce five alternative certificate-retaining continuations

  d-rooted pair birth -> closure or a floor preserving d,
  for every d in K.                                      (FR.13)

The five paid descendants are alternatives; no simultaneous currentness is asserted. What coexists in the parent is the common exact frame, the physical P5 K, the punctured >=3-component cover R_K, and the permission to choose any of the five physical K vertices as the R176 spare coordinate.

### 5. Closed-return-family consequence
Consider any proposed nonclosing normalized return family in the sense of G22 which is closed under every available certificate-retaining choice and which already contains a genuine paid floor. Accepted R432/R1022 allows a paid floor to be aimed at any prescribed physical endpoint pair and launched through any chosen exact pair-deletion frame. Therefore every chosen frame (FR.4) exposes the common-parent five-root object above.

If none of its five alternatives closes H, the family must be capable of absorbing all five rooted lineages (FR.13), while the common P5 simultaneously retains the five universal deletion-crossing constraints (FR.10). In particular a quotient retaining only a naked tuple (E,A_E,M,S) is not sufficient for sink-family analysis: the liftable state must retain at least the physical K/frame/cross-state ancestry needed to realize these five choices.

This is a FAMILY CONSTRAINT, not a no-sink theorem. It supplies a bounded physical certificate on which the next recurrence argument can demand simultaneous closure under five distinct rooted returns rather than follow one favored middle forever.

### 6. Scope fence
Nothing here counts K, the R176 pair, phase-1 currentization, or a returned floor as strict Morse progress. The theorem does not assert the five paid descendants coexist, does not prove a fixed-E rank decrease, and does not rule out a rank-flat closed family. Its gain is exactly the universal-choice package required by G22: one physically realizable pair-deletion frame exposes a finite five-root family of lawful normalized choices, all sharing one retained Hamilton P5 and one source-frame component-drop certificate.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R533"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```