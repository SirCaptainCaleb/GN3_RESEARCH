# The two-ended fragmented-B transfer has a paired endpoint-transposition gate

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-f1g1-two-ended-b-transposition`

**Summary:** In the Director-v42 F1G1 t=3 cell where B is the unique fragmented coarse block and both exact target rails are mixed, each rail has its active support at one end and therefore has an active endpoint dimer. A rail of order three already gives codimension one or closure by R522 with probes u,v. Otherwise swapping the two endpoint vertices has exactly two new turns. Full success gives two exact same-support covers with the identical other rail and an oppositely selected endpoint dimer, so the fixed-complement selected-reversal consumer applies. Double failure gives genuine R561 on the four-vertex terminal window by reversing the next-inward selected edge; mixed failure gives a complete one-sided Hamilton-boundary lock on that same current edge. Applying the gate to both rails simultaneously yields two retained inward boundary certificates whenever neither rail produces the desired selected reversal. No ancestral interval/order assumption on the two B fragments is used.


### 1. Exact v42 two-ended B-transfer setup
Retain the F1G1 |J|=5 laboratory of exact parent SV11804. Put

  G=H-{u,v},
  A={a,b},  P={j0,j1,m},  Q={c,x},

with retained literal paths

  J=(j0,j1,m,x,c),   L=(a,b,c,x).

Assume the Director-v42 first fragmented-B equality cell: T=T_1|T_2 is an exact two-cover of G with total coarse transition count t=3; B is the unique fragmented coarse cell; A,P,Q are each whole contiguous T-blocks; and B has exactly two B|active transitions, one on each target rail. Cutting those two physical transitions gives nonempty B-blocks B_1,B_2 and nonempty active blocks Z_1,Z_2, with

  V(Z_1) disjoint-union V(Z_2)=A union P union Q.

There is only one active-active coarse transition in T, so the three whole active coarse cells distribute 1+2 between Z_1,Z_2. Equivalently, up to swapping rails, their supports are

  A | (P union Q),
  P | (A union Q),
  Q | (A union P).

No order statement about B_1,B_2 inside the ancestral literal B is made or used. What matters below is only their ACTUAL T-orders and the two physical B|active attachments. Each target rail consists of one B_i block and one Z_i block, in one of the two actual orders B_i Z_i or Z_i B_i. In particular the active block is an endpoint block of its rail and has at least two vertices.

### 2. A three-vertex mixed rail already lowers deletion codimension or closes
Suppose one target rail R has order three. It is a literal tight trimer and the other target rail S is Hamilton on the remaining vertices of G. Probe the trimer R by the two deleted vertices u,v.

If R+u has a Hamilton P4, replace R by that P4 and retain S; this is a literal two-cover of H-v. The dual applies with v. If neither R+u nor R+v has a Hamilton P4, accepted R522/P537 applied to the common tight trimer R and probes u,v gives a Hamilton P5 on V(R)+{u,v}; together with S this is a spanning two-cover of H, contradiction.

Hence every surviving two-ended B-transfer target has both T-rails of order at least four.

### 3. Terminal active endpoint: one two-turn transposition gate
Take one target rail whose active block is terminal, and write its actual last four vertices as

  ... , r,s,h,e,                                           (BT.1)

where h,e are the last two vertices of the active block Z_i. Thus (r,s,h) and (s,h,e) are inherited T-turns and the physical endpoint state h->e is selected in T. Test only the adjacent endpoint transposition

  ... , r,s,e,h.                                           (BT.2)

Its COMPLETE new-turn window is

  alpha=(r,s,e),    beta=(s,e,h).                          (BT.3)

No earlier turn changes.

**SUCCESS.** If alpha,beta are both tight, replacing the rail by (BT.2) gives another exact cover T* of the SAME residue G with the SAME unordered rail supports and the IDENTICAL untouched other Hamilton rail. The endpoint support {h,e} is selected h->e in T and e->h in T*. Thus this is a literal fixed-complement selected reversal on the whole target-rail support, not a graph-intrinsic local reversal detached from the cover. Apply `fixed-complement-selected-reversal-normal-form` SV7559 immediately. Its R548 transport keeps the support, complement, and physical reversed dimer fixed while decreasing its declared boundary distance; if it reaches R561 on the whole rail support, u (or v) Hamilton-extends that rail and the untouched other rail gives an exact singleton-deletion two-cover. If transport blocks first, retain the exact named wrap shield supplied by that consumer.

**DOUBLE FAILURE.** If alpha and beta are both bad, R3 gives

  (e,s,r),    (h,e,s) tight.                               (BT.4)

Hence

  K=(h,e,s,r)                                               (BT.5)

is a Hamilton P4 on the same four-support as the inherited

  P=(r,s,h,e).                                              (BT.6)

P begins with r->s and K ends with s->r, so accepted R561 applies literally on {r,s,h,e}, with the next-inward CURRENT T-edge {r,s} as its boundary-reversed dimer. If the whole rail has order four, this R561 support is the whole rail and immediately absorbs u (or v), giving a codimension-one exact cover with the other target rail unchanged. For a longer rail no such whole-rail extension is asserted; retain the prefix and the local R561 support exactly.

**MIXED FAILURE.** Suppose exactly one of alpha,beta is tight. Then there is NO Hamilton P4 on {r,s,h,e} ending with the reverse boundary state (s,r). There are only two orders of h,e before s,r. The order

  (h,e,s,r)

requires precisely reverse(beta) and reverse(alpha); in the mixed branch exactly one of those two turns is bad. The other order

  (e,h,s,r)

starts with (e,h,s), which is the complete reverse of the inherited tight turn (s,h,e), hence is bad. Thus

  no Hamilton P4 on {r,s,h,e} ends (s,r).                  (BT.7)

So the mixed gate is not an anonymous failed swap: it currentizes a complete one-sided Hamilton-boundary lock on the next-inward selected T-edge r->s.

### 4. Source active endpoint: exact dual
If the active block is the source of its target rail, write the first four actual vertices as

  e,h,s,r,...                                               (BT.8)

with endpoint state e->h selected. Swap only the first two vertices:

  h,e,s,r,...                                               (BT.9)

The complete new window is

  alpha*=(h,e,s),    beta*=(e,s,r).                        (BT.10)

If both pass, this is again an exact same-support/common-complement selected reversal and SV7559 applies. If both fail, their reversals give

  (s,e,h),   (r,s,e)

and hence the Hamilton P4 (r,s,e,h), which begins r->s while the inherited (e,h,s,r) ends s->r; R561 applies on the same four-support. If exactly one passes, the two possible orders beginning with the reverse state r->s are blocked exactly as in Section 3, so

  no Hamilton P4 on {r,s,h,e} begins (r,s).                (BT.11)

Again the output is a one-sided lock on an ACTUAL selected T-edge, not generic sign currency.

### 5. Both physical B attachments survive the reduction
Apply Sections 2-4 independently to the two actual target rails of the v42 cell. The endpoint pair chosen on each rail lies inside its active endpoint block, so the test never assumes that B_i is an interval of ancestral B and never reorders B_i. The other whole target rail is literally unchanged in every SUCCESS branch. Therefore a successful gate on EITHER side already supplies the exact same-support/common-complement reversal required by the named fixed-complement consumer while the second physical B|active attachment remains present in the unchanged complement rail.

If neither side succeeds and no order-three rail exists, the SAME exact target cover T simultaneously retains two inward current-edge certificates, one on each rail. Each certificate is one of:

  (DF) a genuine R561 four-support on the next-inward selected edge, with the complete two-bad-turn ancestry (BT.3) or (BT.10); or
  (MX) a complete one-sided four-support Hamilton-boundary lock on that selected edge, with exactly which transposition seam passed and which failed retained.

Thus the three 1+2 active-support distributions do not require separate B-order taxonomies at this stage. The unresolved two-ended transfer has been reduced to a paired current-boundary state on the two actual rails. This is not declared closure: in particular a local DF support inside a longer rail is not silently promoted to a whole-rail R561 witness, and an MX lock is not spent through R523/R542.

### 6. A locked A-Q specialization eliminates one mixed orientation
One useful source-specific sharpening is available when the two-active-cell side is A union Q. Suppose, in the terminal form (BT.1), the endpoint dimer {h,e} is A and the immediately preceding current dimer {r,s} is Q. In the mixed branch (BT.7), if the current Q order were x->c then the forbidden reverse boundary would be c->x. But the retained literal path

  L=(a,b,c,x)

is a Hamilton P4 on A union Q ending c->x. Hence this mixed orientation is impossible. Therefore a surviving terminal mixed gate with endpoint A and inward Q must carry the current Q orientation c->x.

Dually, in the source form (BT.8), if the endpoint dimer is Q and the immediately inward dimer is A, a current A order b->a would make the forbidden reverse source boundary a->b, contradicted by L, which begins a->b. Hence a surviving source mixed gate in that placement must carry A in the current orientation a->b.

These are orientation restrictions inside the paired boundary state, not a claim that the remaining mixed cases close.

### Scope
This section consumes no generic component-drop/payment output. Its purpose is to use the exact two-ended B-transfer representative itself. A short mixed rail lowers codimension or closes; a successful endpoint transposition gives a legal whole-cover fixed-complement selected reversal with its named consumer applied; and otherwise both rails simultaneously expose exact inward current-boundary geometry. Higher B-contact cells, t>=4, the other F/G cells, long-middle M, and the separate mu=1 start-rigid terminal are outside scope.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
