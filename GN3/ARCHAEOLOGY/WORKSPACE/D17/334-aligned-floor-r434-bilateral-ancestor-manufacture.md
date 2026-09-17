# Every aligned floor manufactures a lawful bilateral R434 ancestor packet from one internal middle

**Workspace:** D17
**State:** established
**Key:** `aligned-floor-r434-bilateral-ancestor-manufacture`

**Summary:** Fix any ancestry-bearing floor aligned to E={a,c} and any exact H-E frame with internal middle b, predecessor r and successor s; orient the outer turn as J=(a,b,c). The two raw R434 incidence extractions give a tail-signed dimer D_a=(x,a), x in {r,b}, and a head-signed dimer D_c=(c,y), y in {b,s}. Their supports are disjoint except in the unique double-middle case D_a=(b,a), D_c=(c,b). If disjoint, they form a direct mass-four opposite-sign pair, so R514 pays to an ancestry-bearing floor and R432 steers back to E while both dimers remain historical graph-intrinsic facts. In the hinged case, R547 gives signed singleton descendants (a),(c), but this raw hinge cut is not used as a paid floor. Instead orient the retained tight marker M=(c,b) against tail-signed (a) with witness r. R526 tests exactly (r,c,b): if tight, M is head-signed by r; if bad, R3 gives (b,c,r) and the short support (c,r) is head-signed by b. Either way this creates a genuine balanced-pair birth (a)|Q with nontrivial Q anchored at c. R428 pays that birth while preserving a; if the second singleton is already c we are aligned, otherwise R432 steers the ancestry-bearing floor to E while preserving a. Thus every branch gives TWO-COVER or a lawful same-E return retaining the original endpoint dimers and exact witnesses as historical ancestry. The local SV57993 bilateral seam calculation uses only those dimers and a same-E proper turn, so every later same-E turn yields the same P4/reverse-trimer/adjacent-reversal packet. No completed-anchor status is asserted.

### 1. Input: any ancestry-bearing aligned floor
Let H be a hypothetical smallest Strong Level-(1) counterexample. Fix an ancestry-bearing both-singleton floor aligned to

  E={a,c}.

Choose one exact pair-deletion frame

  H-E=U|V

and an internal vertex b on one displayed rail, with selected predecessor and successor

  r -> b -> s.

By R3 orient the outer triple so that

  J=(a,b,c)

is tight. No assumption is made that a or c has completed a quiet R434 episode. In particular A_E may be empty, one-point, or all of E.

### 2. The two raw R434 endpoint dimers
Use only the literal incidence extraction inside accepted R434, before paying either channel.

For the predecessor r->b, exactly one of

  (r,a,b),   (b,a,r)

is tight. In the first case retain

  D_a=(r,a), tail-signed by b;

in the second retain

  D_a=(b,a), tail-signed by r.

Thus always

  D_a=(x,a),  x in {r,b},

with signed tail anchor a.

The successor channel is the exact dual at c. Exactly one of

  (b,c,s),   (s,c,b)

is tight. In the first case retain

  D_c=(c,s), head-signed by b;

in the second retain

  D_c=(c,b), head-signed by s.

Thus always

  D_c=(c,y),  y in {b,s},

with signed head anchor c.

Because r,b,s are distinct vertices of a vertex-simple rail and none lies in E, the supports V(D_a),V(D_c) are disjoint except in the single pattern

  D_a=(b,a),   D_c=(c,b).                         (BA.1)

### 3. Disjoint case: a direct mass-four paid return
Assume we are not in (BA.1). Then D_a and D_c are physically disjoint signed dimers of opposite polarity. They therefore form a graph-intrinsic balanced opposite-sign pair of total mass four.

Apply accepted R514. It gives a finite chosen certificate-retaining continuation to TWO-COVER or an ancestry-bearing both-singleton floor. In the nonclosing branch apply accepted R432 with prescribed target pair E={a,c}. We return to an ancestry-bearing E-aligned floor.

The original exact frame, J, D_a,D_c and their exact witnesses are separately certified graph-intrinsic static data. R514 explicitly permits such static data to remain historical truth while descendants change representatives, and R432 retains the paid-floor ancestry. Hence at the returned E-floor we possess the two historical signed dimers

  L:=D_a=(p,a)  tail-signed,
  R:=D_c=(c,q)  head-signed,                       (BA.2)

with p,q outside E.

### 4. Hinged case: repair the raw-R547 provenance gap
Now assume (BA.1):

  D_a=(b,a) tail-signed by r,
  D_c=(c,b) head-signed by s.                       (BA.3)

Accepted R547 applies to the two opposite-polarity dimers hinged at b and gives graph-intrinsic signed singleton descendants

  (a) tail-signed by r,
  (c) head-signed by s.                              (BA.4)

The R547 singleton descendants (BA.4), while graph-intrinsic, are not by themselves an active ancestry-bearing paid floor for R432 in this branch. We therefore create a new certified balanced-pair birth before steering.

Use the tight physical dimer

  M=(c,b)

as an R526 actualization marker against the tail-signed singleton (a) of (BA.4). This is legal: M is disjoint from {a,r}, because r is the selected predecessor of b and r,a,b,c are distinct. With marker orientation (c,b), the tail-signed dual of R526 tests

  (r,c,b).

If this is tight, M=(c,b) itself is head-signed by r with signed head anchor c. If it is bad, R3 gives

  (b,c,r) tight,

so the short support (c,r) is head-signed by witness b, again with signed head anchor c. In either case

  (a) | Q

is a genuine graph-intrinsic balanced-pair BIRTH carrying an explicit R526 actualization certificate, where Q is a nontrivial head-signed support anchored at c.

Apply accepted R428 with singleton (a) fixed. Outside TWO-COVER it reaches an ancestry-bearing both-singleton floor (a)|(t). If t=c, this is already the required E-floor. If t!=c, apply accepted R432 to the target pair E={a,c}, using its one-coordinate steering branch that preserves a while installing c. Thus the hinged case also returns lawfully to an ancestry-bearing E-floor.

Crucially, the original D_a,D_c and the R547 hinge-cut certificates remain graph-intrinsic historical data throughout this chosen continuation. The raw-hinge provenance gap has been repaired by the explicit intervening R526 pair birth; no raw-hinge steering is used.

### 5. Manufactured bilateral ancestor packet
Combining Sections 3 and 4 gives the parent statement:

> From any ancestry-bearing E={a,c}-aligned floor and any exact H-E frame with an internal middle b, one finite chosen continuation yields TWO-COVER or a lawful ancestry-bearing return to the SAME E carrying two retained graph-intrinsic endpoint dimers L=(p,a) tail-signed and R=(c,q) head-signed, together with their exact witnesses and source-frame ancestry.

These dimers need not come from completed quiet endpoint episodes. They are manufactured directly from one internal frame.

### 6. The SV57993 replay-breaker calculation now applies verbatim
Inspect the local proof of `fully-anchored-pre-singleton-replay-breaker` SV57993. Its Sections 3--5 use only the existence of graph-intrinsic dimers

  L=(p,a) tail-signed,
  R=(c,q) head-signed,

and a later proper same-E turn

  J'=(a,b',c).

The old completion middles and the fact that L,R originally arose from quiet completion episodes are not used in those seam tests. Therefore the same calculation applies to the manufactured packet (BA.2): independently at each endpoint, every later same-E turn produces a literal P4, a labelled reverse trimer, or an adjacent reversal. If p,q,b' are pairwise distinct and both extension seams pass, one obtains the literal P5 (p,a,b',c,q); if p=q, retain the two overlapping P4s and make no cycle claim without an additional closing turn.

Thus the ancestor-geometry interface needed by G26 does not require A_E=E. Every ancestry-bearing aligned floor can manufacture a typed bilateral ancestor packet before the next reentry.

### 7. Scope fence
This theorem does NOT enlarge the completed-anchor ledger A_E or A_*. The manufactured dimers are historical signed ancestors, not certificates that a quiet protected endpoint episode completed. It does not make the subsequent P4/reverse/reversal packet contradictory, and it does not solve repeated R542/payment return. Its gain is narrower and structural: the virtual-versus-literal gap in availability of the two nontrivial endpoint ancestors is removed. A bottom-family theorem may therefore work with these manufactured R434 ancestors without assuming prior quiet completion.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R432"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    },
    {
        "relation": "dependency",
        "revision_id": "R526"
    },
    {
        "relation": "dependency",
        "revision_id": "R547"
    }
]
```