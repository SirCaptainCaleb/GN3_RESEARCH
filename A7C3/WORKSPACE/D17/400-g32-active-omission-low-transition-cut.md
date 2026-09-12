# Every nonexported G32 packet has a B-active omission with a low-transition endpoint cut

**Workspace:** D17
**State:** established
**Key:** `g32-active-omission-low-transition-cut`

**Summary:** Retain the G32 static spectator frame after SV100744, SV101535 and SV102330. Outside the crossed rigid exception (extinguished) and aligned rigid exception (exported to maximum-forest reversal transport), the pair-target forcing chains of SV100744 can be chosen so that every candidate Hamilton P5 omitting a B-active source spoke has an R540 endpoint cut with at most two selected X|B transitions. Hence some actual endpoint-favorable K_s omitting a B-active spoke s has such a low-transition cut. The path construction uses only the top fiber G=H-{A,C}: it yields a literal spanning two-path proposal with one uncertified seam eta. If eta is tight, this is an exact top-fiber cover T with tau_X|B(T)<=2, whereas the actual old source cover has tau_X|B(U|V)>=3 by SV100350, giving a strict integer-valued source-transition descent on the same fixed physical partition X|B. If eta is bad, R3 gives its exact reverse, with the chosen K_s, cut endpoint, omitted B-active spoke, and old s-B incidence retained. Thus the direct G32 branch reduces to strict old-source descent or one named low-cut reverse seam; no generic certificate output is counted as progress.

### 1. Input and notion of a low-transition cut
Retain the G32 transitive singleton-star spectator frame with

  G=H-{A,C}=X union V(B),
  X={v,p,q,r},
  B=(L=b_0,b_1,...,b_{m-1},R=b_m),

and the actual old source cover F=U|V. By SV100350,

  tau_F := tau_{X|B}(F) >= 3.

Retain the source-active reduction SV100744. The crossed rigid exception has been extinguished by SV101535, while the aligned rigid exception has been exported from the static G32 program by SV102330. Therefore in the remaining direct branch the B-active source-spoke set meets one of the pair-target forcing chains of SV100744.

For a Hamilton P5 K on {L,R} plus three vertices of X, call an endpoint cut LOW when the literal R540 path construction on the top fiber G has exactly one uncertified seam and the resulting two-path forest, if that seam is tight, has at most two selected X|B states. Only the path construction and complete seam ledger of R540 are used here; its pc(ambient)>2 bad-hole conclusion is not imported.

### 2. Transition count for an endpoint cut
Write the five positions of K as 0,1,2,3,4 and mark L,R as B-type and the three cell vertices as X-type.

A left cut at L is one-hole exactly when pos(L) is 0,3,or 4. It keeps the K-prefix through L, appends B[1,m-1], and puts the omitted spoke before the K-suffix. A right cut at R is one-hole exactly when pos(R) is 0,1,or 4, with the exact dual construction. The number of selected X|B states in the completed proposal is obtained by counting type changes along the retained K pieces plus the single omitted-spoke attachment; the B-interior contributes none.

For the candidate words used below this count is at most two. We record the relevant words explicitly, so no general classification is needed.

### 3. Aligned pair-target chains are already low
Use the normalized notation of SV100744:

  M_R={ab,cz}>M_S={ac,bz}>M_L={bc,az},

with aligned middle gates. Outside the exported exceptional active edge {a,c}, at least one B-active source spoke is b or z.

If b is B-active, SV100744 uses only the candidate words

  L R c a z,
  z c a L R,
  z c R L a,
  R c z a L,
  c R L a z,

all omitting b. Their minimum one-hole cut transition counts are respectively

  2,2,1,2,1.

Thus assuming no LOW endpoint-favorable P5 omits b reproduces exactly the same forced-reversal chain as SV100744 and ends with the final tight candidate, contradiction. Hence some LOW endpoint-favorable K_b exists.

If z is B-active, the dual SV100744 chain

  L R a c b,
  b a c L R,
  b a R L c,
  R a b c L,
  a R L c b

has the same transition-count pattern 2,2,1,2,1 and yields a LOW K_z.

Therefore every nonexported aligned packet has a LOW endpoint-favorable K_s omitting a B-active source spoke s.

### 4. Crossed pair-target chains are already low
In the crossed gate, SV101535 removes the rigid same-M_S active exception. Hence the B-active source set meets both M_S edges, and we may choose a cross-pair target. The four pair-target chains in SV100744 are:

  {a,b}: R z c a L; z c a L R; c z R L a; L R z b c,
  {a,z}: L R z b c; b a c L R; R z b c L; z R L c b,
  {b,c}: L R b z a; R b z a L; b R L a z; z c a L R,
  {c,z}: R b a c L; b a c L R; a b R L c; L R b z a.

The respective minimum one-hole cut transition counts are

  2,2,1,2;
  2,2,2,1;
  2,2,1,2;
  2,2,1,2.

Thus every candidate in every cross-pair forcing chain is LOW. Repeating the SV100744 forcing argument under the stronger assumption that no LOW endpoint-favorable candidate omits either active target spoke gives the same contradiction. Consequently every crossed direct packet has a LOW K_s omitting a B-active source spoke s.

### 5. The one-seam descent alternative
Fix such a LOW K_s and choose one of its one-hole endpoint cuts realizing at most two X|B transitions. Let eta be the complete uncertified-turn set; by construction eta consists of exactly one ordered turn.

If eta is tight, the displayed proposal is a literal exact two-cover T of the SAME top fiber G=H-{A,C}. Since its selected X|B transition count satisfies

  tau_{X|B}(T) <= 2 < 3 <= tau_{X|B}(F),

this is a strict source-transition descent measured directly against the actual old source representative on the fixed physical partition X|B. The measure is an ordinary nonnegative integer attached to literal exact covers of this fixed residue, so the decrease is genuine and cannot be replay-equivalent to F. If desired, comparison with F may separately expose an endpoint/internal or support/order disagreement, but no such secondary certificate is needed to certify the strict numerical drop.

If eta is bad, exact reversal R3 gives the tight reverse bar(eta). Retain simultaneously:

- the omitted B-active source spoke s;
- its actual old selected source incidence s-h with h in B;
- the literal K_s and which endpoint cut was chosen;
- the complete one-hole proposal; and
- the exact reverse seam bar(eta).

This bad-seam branch is the only remaining direct static G32 splice problem.

### 6. Relation to the source-mate wrap theorem
SV102728 is the particularly strong subcase in which the LOW candidate is of source-mate form (t,R,L,x,y) or (x,y,R,L,t). Its unique bad seam is then a pure spectator wrap seam, and the anchors are absorbed by the source four-set Hamilton P4. The present theorem does not require source-mate placement; it shows that every remaining direct packet reaches either strict old-source transition descent or one named low-cut reverse seam.

### 7. Scope
This theorem supplies one of the explicit G32 success signals when eta is tight: a strict improvement measured from the actual old source. It does not declare the reverse seam in the bad branch to be progress, and it does not convert it into R159/R407/R523/PAYABLE-FOUR currency. No finite search is used in the proof; the low-transition property is read directly from the same explicit human forcing chains already established in SV100744. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R540"
    }
]
```
