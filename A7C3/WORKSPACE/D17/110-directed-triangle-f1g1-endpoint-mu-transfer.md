# The quiet endpoint-only F1G1 transfer has a two-step support descent

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-f1g1-endpoint-mu-transfer`

**Summary:** In the endpoint-only pair-deletion cell obtained after puncturing the restored labels a,b back to literal old rails J|B, the terminal c-x lock prevents either restored label from being appended after c. Let mu count restored labels on the B-side. Then mu=2 or 1 admits an explicit one-turn transfer lowering mu by one; failure gives an exact ancestral/current boundary reversal. At mu=1, R573 compresses the blocker to a two-witness current-boundary fan or a start-rigid trimer state. Thus mu is a genuine bounded support coordinate; the role-rigid terminal remains unconsumed.

### 1. Exact endpoint-only cell and support coordinate
Retain the terminal c-x one-sided-lock ancestry from `directed-triangle-r846-weave-restoration` SV11804. In particular J is the literal old current rail ending (...,x,c), B is the literal old complement rail, and the two restored triangle labels are A={a,b}. The lock gives

  (a,c,x), (b,c,x) tight,

hence by R3 both (x,c,a) and (x,c,b) are bad. Work only in the quiet endpoint-only pair-deletion class: T is an exact two-cover of H-{u,v}, deleting a,b from T leaves exactly the literal old orders J|B, and the restored labels occur only in endpoint blocks of those two rails. Since neither label can be appended after terminal c, every restored label lying on the J-side is a source prepend.

Define

  mu(T)= number of vertices of {a,b} lying on the rail containing literal B.

Then mu is in {0,1,2}; mu=0 already preserves literal B and is the desired exit from this endpoint-only cell.

### 2. mu=2 lowers to mu=1 or gives an ancestral J shield
Assume mu=2. Choose an outermost restored endpoint label z on the B-rail so that deleting z leaves a Hamilton path on B together with the other restored label. Such z exists whether a,b occupy opposite B ends or one two-label endpoint block. Test the single source-prepend turn

  theta=(z,j0,j1),

where J=(j0,j1,...,x,c). If theta is tight, replace z on the B-side by the rail (z,J), leaving the post-deletion B-side rail literally unchanged. This is an exact H-{u,v} cover with mu=1. If theta is bad, R3 gives

  (j1,j0,z) tight,

an exact reversal of the ancestral selected source dimer j0->j1 with the actually transferred label z retained as witness. If a,b occupy opposite B ends then either is outer-removable; a mu-minimal choice forces both corresponding tests to fail and gives two named witnesses on that same reverse J boundary.

### 3. mu=1 lowers to mu=0 or gives a current-boundary shield
Assume mu=1. Write the J-side rail as (w,J), where w is one restored label, and let z be the unique restored label on an endpoint of the B-side rail. Deleting z leaves literal B. The candidate

  (z,w,J) | B

introduces exactly one new turn, (z,w,j0), because (w,j0,j1) is inherited from T. If this turn is tight, the candidate is an exact H-{u,v} cover with mu=0. If it is bad, R3 gives

  (j0,w,z) tight.

The current T boundary is w->j0, so this is an exact reversal on the same physical boundary pair with the other restored triangle label z retained as witness.

Thus every successful transfer strictly lowers the integer coordinate 2->1->0. No reversible rotation is counted as progress.

### 4. R573 compresses the mu=1 terminal
At a mu=1 failure set D={u,v}, S={w}, and let C be the remaining vertices of H-D-S. The exact target cover has the unique S|C transition w->j0, and X=D union S={u,v,w} is Hamiltonian. If X has a Hamilton path ending (p,w), accepted R573/P648 applied to the actual transition gives

  (j0,w,p) tight.

Together with (j0,w,z), this is a two-witness same-orientation fan on the same current reversed boundary dimer j0->w. If no Hamilton path of X ends at w, then the two possible orders (u,v,w) and (v,u,w) are both bad; R3 gives both

  (w,v,u), (w,u,v) tight.

Thus w is a literal START-RIGID three-vertex absorber state.

### 5. Exact scope
This section proves only the bounded endpoint-only support transfer. Its terminal outputs are: literal-B mu=0 representative; ancestral j0j1 reverse shield; current wj0 two-witness fan; or start-rigid {u,v,w}. The fan and start-rigid state are retained unconsumed. No R523/R542 payment and no spanning closure is asserted from them.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R573"
    }
]
```
