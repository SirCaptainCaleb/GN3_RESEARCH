# Greedy largest-rail slides give a global Morse descent to a genuine ancestry-bearing singleton floor

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-largest-rail-morse-descent`

**Summary:** From any literal maximum spanning three-forest F=A|B|C in a hypothetical smallest counterexample, mark a largest rail A. Each inward endpoint gate from B or C either grows A by the reversible one-edge SLIDE of SV22098 or signs the corresponding reverse boundary dimer of A, so greedily taking available slides strictly decreases d=|V(H)|-|A| and terminates. At a nonclosing terminal state both reverse boundary dimers of A have opposite polarities witnessed by the other two rails. The terminal largest rail cannot have order at most two. If |A|=3, do NOT use raw R547 hinge geometry as a floor: delete the middle vertex a1. The proper residue H-a1 has the literal four-cover {a0}|{a2}|B|C and an exact two-cover by minimality. Some selected state of the two-cover crosses two of those four components; with spare a1, one R3 choice makes that crossing dimer and singleton a1 a genuine opposite-sign singleton+dimer pair, and accepted R428 pays it to an ancestry-bearing both-singleton floor preserving a1 (or closes H). If |A|>=4, the two reverse boundary dimers are disjoint opposite-sign supports of total mass four, and accepted R514 gives closure or an ancestry-bearing both-singleton floor. Hence every maximum-three-forest state has a finite well-founded path to a spanning two-cover or a genuine paid mass-two floor. The remaining global Morse obstruction is extinction of this floor together with the retained terminal-state ancestry; raw R547 pair existence is not used.


### 1. Mark one largest rail and orient four inward endpoint gates
Let H be a hypothetical smallest Strong Level-(1) counterexample. By accepted R4 every maximum compatible spanning forest has exactly three nonempty tight-path components. Retain one literal state

  F=A|B|C

and choose A to have maximum order among the three rails. Orient

  A=(a_0,a_1,...,a_r).

The argument below keeps the physical descendant of A distinguished. Every successful move adds exactly one vertex to this distinguished rail, so it remains a largest component thereafter.

Fix another rail X=(x_0,x_1,...,x_m), where X is B or C. There are two inward endpoint gates.

At the TAIL of A use the physical merge seed a_r -> x_0. When m>=1 its two native turns are

  alpha_X=(a_{r-1},a_r,x_0),
  beta_X =(a_r,x_0,x_1).                                  (GM.1)

At the HEAD of A use the seed x_m -> a_0. When m>=1 its two native turns are

  gamma_X=(x_{m-1},x_m,a_0),
  delta_X=(x_m,a_0,a_1).                                  (GM.2)

The singleton cases use the intrinsic one-hole interpretation of SV22098.

### 2. Each endpoint either moves into A or signs its reverse boundary dimer
Consider the tail seed a_r -> x_0.

If alpha_X is tight and m>=1, beta_X cannot also be tight, because then A followed by X together with the untouched third rail would be a spanning two-cover. Hence beta_X is bad. Section 2 of SV22098 applies literally: delete x_0x_1 and add a_rx_0. The result is

  (A,x_0) | (X-x_0) | (third rail),                       (GM.3)

another literal maximum three-forest. The distinguished rail has gained exactly one vertex.

If alpha_X is bad, R3 gives

  (x_0,a_r,a_{r-1}) tight.                                (GM.4)

Thus x_0 is a HEAD witness on the tested reverse terminal dimer

  D_R=(a_r,a_{r-1}).                                      (GM.5)

If X is a singleton, tightness of the sole turn alpha_X would merge A with X and leave only the third rail, already a spanning two-cover. Therefore in the singleton case alpha_X is necessarily bad and (GM.4) still holds.

So the tail gate has the exact dichotomy

  x_0 slides into A,
  OR x_0 head-signs D_R.                                  (GM.6)

The head gate is dual but keep the exact tested order. If delta_X is tight and m>=1, gamma_X cannot also be tight. Hence gamma_X is bad and the second SLIDE form of SV22098 deletes x_{m-1}x_m and adds x_ma_0, giving

  (X-x_m) | (x_m,A) | (third rail).                       (GM.7)

Again the distinguished rail gains one vertex. If delta_X is bad, R3 gives

  (a_1,a_0,x_m) tight,                                    (GM.8)

so x_m TAIL-signs the tested reverse initial dimer

  D_L=(a_1,a_0).                                          (GM.9)

For singleton X, tightness of delta_X would again give a two-cover, so (GM.8) is forced. Therefore

  x_m slides into A,
  OR x_m tail-signs D_L.                                  (GM.10)

No arbitrary representative replacement has been used: every growth step is the literal reversible one-edge SLIDE of SV22098.

### 3. A genuine well-founded forest gradient
Define the marked largest-rail deficit

  d(F,A)=|V(H)|-|A|.                                      (GM.11)

Whenever any one of the four inward endpoint gates for B,C lies in its SLIDE branch, perform that move and continue with the grown descendant of A. Equations (GM.3) and (GM.7) show

  d -> d-1                                                (GM.12)

at every step. Hence the process is finite.

If it ever merges away one of the other components, H has a spanning two-cover and we are done. Otherwise it terminates at a literal maximum three-forest

  F*=A*|B*|C*                                             (GM.13)

in which none of the four inward endpoint gates slides.

By (GM.6), the two distinct sources b_0,c_0 head-sign the same tested dimer

  D_R*=(a_r,a_{r-1}),                                     (GM.14)

and by (GM.10), the two distinct terminals b_p,c_q tail-sign

  D_L*=(a_1,a_0).                                         (GM.15)

Thus failure of the primary integer gradient does not leave an arbitrary seam wall: it creates opposite-polarity signed supports at the two physical ends of one current tight rail.

### 4. The terminal largest rail has order at least three
Suppose |A*|=2, so A*=(a_0,a_1) and D_R*=D_L*=(a_1,a_0).

If one of B*,C* is nontrivial, say B*=(b_0,...,b_p) with p>=1, then (GM.14)-(GM.15) give

  (b_0,a_1,a_0) tight,
  (a_1,a_0,b_p) tight.

Hence

  (b_0,a_1,a_0,b_p)                                      (GM.16)

is a literal tight P4. Since A* was largest, |B*|<=2, so nontriviality forces |B*|=2 and (GM.16) spans A* union B*. Together with the untouched rail C* this is a spanning two-cover, contradiction.

If both B*,C* are singletons, H is already covered by the dimer A* and the dimer B* union C*. Thus |A*|=2 is impossible. The order-one case is even more immediate. Therefore

  |A*|>=3.                                                (GM.17)

### 5. Order three enters a genuine rooted component-drop payment
Assume |A*|=3 and write

  A*=(a_0,a_1,a_2).                                      (GM.18)

The two opposite-polarity reverse boundary dimers from (GM.14)-(GM.15) hinge at a_1. Accepted R547 would therefore yield a graph-intrinsic opposite-sign singleton pair on a_0,a_2. That raw pair is NOT, by itself, a paid floor and is deliberately not used here.

Instead delete the physical hinge a_1 and put

  W=H-{a_1}.

Trimming A* at a_1 leaves the literal four-cover

  {a_0} | {a_2} | B* | C*                                (GM.19)

of W. By smallest-counterexample minimality, W has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path of W together with singleton {a_1} would be a spanning two-cover of H. Hence W has an exact two-cover T=T_1|T_2.

Some selected directed state alpha->beta of T joins two distinct components of (GM.19). Otherwise every selected T-edge would stay inside one of the four displayed components, so each connected T-rail would lie inside a single displayed component; two T-rails could then cover at most two of the four nonempty components, impossible.

Now a_1,alpha,beta are distinct. Apply R3 to the reversal pair

  (a_1,alpha,beta),  (beta,alpha,a_1).                    (GM.20)

If (a_1,alpha,beta) is tight, the selected dimer (alpha,beta) is head-signed by witness a_1, while the singleton (a_1) is tail-signed by alpha via the vacuously tight dimer (a_1,alpha). If (beta,alpha,a_1) is tight, the selected reverse dimer (beta,alpha) is tail-signed by a_1, while singleton (a_1) is head-signed by alpha. In either branch we obtain physically disjoint opposite-sign supports of sizes two and one, with the actual selected cross-state and its two named four-cover components retained as the pair-birth certificate.

Accepted R428 applies proof-aware to this singleton/nontrivial pair. Its chosen continuation preserves singleton a_1 throughout; every nonclosing step strictly shortens the opposite signed support using the exact outside-reservoir refund mechanism, and the final one-vertex reservoir is handled by its complete two-seam test. Therefore

  |A*|=3  =>  spanning two-cover
             OR a genuine ancestry-bearing both-singleton floor
                containing a_1.                          (GM.21)

This is an actual signed-payment lineage. No raw-hinge-to-floor inference is made.

### 6. Longer largest rails descend from mass four to a genuine paid floor
Assume |A*|>=4. Then the two tested boundary dimers

  D_L*=(a_1,a_0),
  D_R*=(a_r,a_{r-1})                                     (GM.22)

are physically disjoint. By (GM.14)-(GM.15) they have opposite polarity. Choosing any retained witness on each side therefore gives a graph-intrinsic balanced opposite-sign pair of support profile 2+2 and total support mass four.

Accepted R514 applies exactly to this mass-four pair. Its proof classifies the support profile, invokes R427 on the 2+2 pair, and then R428 once a singleton support appears. The continuation is certificate-retaining and gives either

  a spanning two-cover of H,
  OR an ancestry-bearing balanced opposite-sign pair whose two supports are both singletons.   (GM.23)

The original current forest F*, both physical boundary dimers of A*, and all four source/terminal witness turns remain graph-intrinsic historical data; R514 does not assert that the old representative remains simultaneously current during its descendant continuation.

### 7. Global Morse consequence
Combining Sections 2-6 gives a genuine well-founded global reduction from an arbitrary maximum-three-forest state.

Mark a largest rail A. Repeatedly take any inward endpoint SLIDE into A. The nonnegative integer d(F,A)=|V(H)|-|A| decreases by exactly one at every forest transition. Therefore the gradient cannot cycle. If it stops without augmenting to two paths, then:

- |A*|=3 enters the rooted component-drop payment (GM.19)-(GM.21), producing closure or a genuine paid floor;
- |A*|>=4 enters accepted mass-four payment R514, producing closure or a genuine paid floor.

Hence every literal maximum-three-forest state admits a finite path of the form

  maximum forest
    -- strict largest-rail SLIDEs -->
  terminal two-ended signed forest
    -- rooted component-drop or mass-four payment -->
  spanning two-cover OR ancestry-bearing both-singleton floor.      (GM.24)

This repairs the raw-R547 provenance gap in the order-three branch. The final critical species is now genuinely uniform across all terminal rail lengths: a paid mass-two opposite-sign singleton floor with a reconstructible birth ledger. In the |A*|=3 branch that ledger retains the deleted hinge a_1 and an actual two-cover cross-state between named components of (GM.19); in the |A*|>=4 branch it retains the two opposite boundary dimers of the monotonically grown rail and their mass-four payment ancestry.

The next parent theorem should consume this genuine paid floor together with its branch-specific terminal-state ancestry. No further local seam taxonomy is required for the primary gradient.


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
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    }
]
```