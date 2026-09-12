# Near-maximal OUT/OUT families force terminal rigidity and collide inner exceptions

**Workspace:** D17
**State:** working
**Key:** `middle-layer-nearmax-outer-terminal`

**Summary:** In the near-maximal |O|=k-2 branch, the complete OUT stars give dual terminal rigidity on O+h+r and O+t+r. An IL residual forces h second and r terminal; an IR residual forces r initial and t penultimate. The three possible quiet-both combinations IL+ER, EL+IR, and IL+IR each splice explicitly to P_{k+1}, so no residual label is quiet on both sides. Hence all three residual labels are support-wide active on at least one side and two are active on the same side, reducing the branch to the accepted two-active-support alternatives but not closing them. In addition, every Hamilton path on O+a+b has endpoints exactly a,b; these forced endpoints persist in the same-residue exchange covers and supply a common-endpoint complement interface for the next seam consumer.

### Near-maximal OUT/OUT terminal rigidity

Work in the uniform middle-layer residue |H|=2k+1, k>=6. Fix a Hamilton order

  P=(p_0,p_1,...,p_{k-1}),

and put h=p_1, t=p_{k-2}. Let O be the exterior labels x for which both literal OUT endpoint replacements are actual Hamilton paths:

  EL(x)=(x,h,p_2,...,p_{k-1}),
  ER(x)=(p_0,...,t,x).

Assume the extremal surviving size

  |O|=k-2.

Then Omega\O has exactly three labels. The following strengthens the signed-cap section by using each OUT path against every exterior label.

#### 1. Complete exterior star signs

Fix x in O and any exterior y distinct from x, with no assumption y in O. Prepending y to EL(x) would produce a tight path on k+1 vertices if (y,x,h) were tight. Hence that turn is bad, and exact reversal gives

  (h,x,y) tight.                                      (31.1)

Likewise, appending y to ER(x) would produce P_{k+1} if (t,x,y) were tight. Hence

  (y,x,t) tight.                                      (31.2)

Thus every x in O is simultaneously an h-head and t-tail middle label against every other exterior vertex.

#### 2. Two terminal types on X_r=O+h+r

Fix r in Omega\O. The support

  X_r=O union {h,r}

has k vertices, hence is Hamiltonian. Let W be any Hamilton path on X_r.

If h is not among the first two positions, let u,v be its two immediate predecessors, so W contains the tight turn (u,v,h). If v lies in O, then (31.1), applied with x=v and y=u, gives the reverse turn (h,v,u) tight, impossible. Therefore whenever h occurs after position two, its immediate predecessor is r.

If W ends in two exterior vertices y,x with x in O, then (31.2) gives (y,x,t) tight and t appends, producing P_{k+1}. Hence a surviving W with h among the first two positions must end at r.

If h occurs after position two, its predecessor is r. If W has a further final vertex x after h, then x lies in O and W ends (r,h,x). Choose any exterior s outside X_r; two such labels exist because Omega\O has three vertices. By (31.1), applied to x in O and y=s, the turn (h,x,s) is tight, so s appends to W and gives P_{k+1}. Therefore this case is impossible.

Consequently every Hamilton path on X_r has exactly one of two forms:

  TYPE A: h is first or second, and r is the terminal endpoint;
  TYPE B: the path ends with the ordered dimer (r,h).  (31.3)

At most one residual label admits any type-B path. Indeed, if W_r ends (r,h) and W_s ends (s,h) for distinct r,s, exactly one of the reversal-pair turns (r,h,s),(s,h,r) is tight. That turn appends the other residual label to one of W_r,W_s, giving P_{k+1}.

#### 3. An inner-left label is A-only with h second

Suppose r in Omega\O admits the literal inner-left quiet replacement

  IL(r)=(h,r,p_2,...,p_{k-1}).

For every x in O, prepending x to IL(r) is forbidden, so

  (x,h,r) bad, hence (r,h,x) tight.                   (31.4)

A type-B Hamilton path on X_r ends (r,h). Its first vertex is some x in O. Delete that first x and append x using (31.4). This gives a Hamilton path on X_r ending (r,h,x), the already forbidden intermediate type from part 2. Hence type B is impossible.

Now let W be type A. If h were first, write W=(h,x,...,v,u,r) with x,v,u in O. Delete terminal r and prepend r using (31.4), obtaining a Hamilton path on X_r ending with two O-vertices v,u. Then (v,u,t) is tight by the signed-cap signs, so t appends and gives P_{k+1}. Hence h cannot be first. Every Hamilton path on X_r therefore has the exact shape

  W=(x,h,...,v,u,r),                                  (31.5)

with x,v,u in O. In particular h is always second and r is always terminal.

#### 3R. Right-dual terminal theorem

Put

  Y_r=O union {t,r}.

The exact right dual of part 2 says that every Hamilton path on Y_r has one of two forms:

  TYPE A_R: t is last or penultimate, and r is the initial endpoint;
  TYPE B_R: the path begins with the ordered dimer (t,r).

Suppose r admits the literal inner-right quiet replacement

  IR(r)=(p_0,...,p_{k-3},r,t).

For every x in O, appending x to IR(r) is forbidden, hence

  (r,t,x) bad, so (x,t,r) tight.                      (31.6)

A TYPE B_R path begins (t,r) and has terminal endpoint x in O. Delete that terminal x and prepend x using (31.6); the resulting Hamilton path begins (x,t,r). This intermediate type is impossible: choose a residual exterior label s outside its support and prepend s, using the complete star turn (s,x,t) from (31.2), to obtain P_{k+1}. Hence TYPE B_R is impossible.

Now let W be TYPE A_R. If t were last, delete the initial r and append r using (31.6). The resulting Hamilton path begins with two O-labels, so h prepends by (31.1), again giving P_{k+1}. Therefore every Hamilton path on Y_r has the exact shape

  W=(r,u,...,t,x),                                     (31.7)

with u,x in O. In particular r is always initial and t always penultimate.

#### 4. Distinct inner-left and inner-right labels are impossible

Suppose distinct residual labels r_L,r_R admit

  IL(r_L)=(h,r_L,p_2,...,p_{k-1}),
  IR(r_R)=(p_0,...,p_{k-3},r_R,t).

Choose any Hamilton path on X_{r_L}. By (31.5),

  W=(x,h,z,...,v,u,r_L)

for O-labels x,z,v,u as displayed. Delete first x and terminal r_L. The remaining path is

  (h,z,...,v,u).

Prepend r_L: (r_L,h,z) is tight by (31.4). Append t: (v,u,t) is tight by the signed-cap signs. Finally append r_R. Appending u to IR(r_R) would Hamiltonize the corresponding forbidden (k+1)-set, so (r_R,t,u) is bad and exact reversal gives

  (u,t,r_R) tight.

Thus

  (r_L,h,z,...,v,u,t,r_R)

is a literal tight path on k+1 vertices, contradiction. Therefore distinct IL and IR labels cannot coexist in the |O|=k-2 branch.

#### 5. No residual label is quiet on both sides

Let D be the exterior labels for which both endpoint-replacement sides admit at least one P-quiet Hamilton order. Fix r in Omega\O. Since r is not in O, the pair EL(r)+ER(r) is unavailable. Thus if r lay in D\O, one of exactly three quiet combinations would occur.

(IL+ER) Assume IL(r) and ER(r). By part 3, every Hamilton path on X_r has shape

  W=(x,h,...,v,u,r).

Appending u to the literal ER(r) would Hamiltonize a forbidden (k+1)-set if (t,r,u) were tight. Therefore (u,r,t) is tight. Appending t to W gives P_{k+1}, contradiction.

(EL+IR) Assume EL(r) and IR(r). By part 3R choose

  W=(r,u,...,t,x)

on Y_r. Prepending u to literal EL(r) would Hamiltonize a forbidden (k+1)-set if (u,r,h) were tight. Therefore (h,r,u) is tight. Prepending h to W gives P_{k+1}, contradiction.

(IL+IR) Assume IL(r) and IR(r). Choose the part-3 path

  W=(x,h,...,v,u,r).

The complete OUT star gives (v,u,t) tight. From IR(r), appending u is forbidden, so (r,t,u) is bad and exact reversal gives (u,t,r) tight. Delete the terminal r of W and append t,r. The resulting word

  (x,h,...,v,u,t,r)

is a literal tight P_{k+1}, contradiction.

Hence

  D\O = empty.                                         (31.8)

Every one of the three residual labels therefore has a support-wide active endpoint-replacement side. By pigeonhole, at least two residual labels are support-wide active on the SAME side. Thus the near-maximal branch always enters the accepted exact two-active-support reduction; no purely crossed-only existence case remains. This is a reduction, not closure: COMPLETE CROSS-CONFLICT and the CLUSTERED CELL still require a terminal-state or cover-valued consumer.

#### 6. Residual-pair endpoint rigidity

For distinct residual labels a,b put

  Z_ab=O union {a,b}.

This is a k-set and therefore Hamiltonian. Every Hamilton path on Z_ab has endpoints exactly a and b. Indeed, if an endpoint x lay in O and were initial, its next vertex y is exterior and (h,x,y) is tight by (31.1), so h prepends and gives P_{k+1}. If x in O were terminal with predecessor y, then (y,x,t) is tight by (31.2), so t appends and again gives P_{k+1}.

Consequently any Hamilton order on Z_ab is oriented either a-to-b or b-to-a. Moreover an oriented path

  (a,x_1,...,x_{k-2},b)

simultaneously manufactures two actual terminal-rigid Hamilton paths:

  (h,x_1,...,x_{k-2},b) on O+h+b,
  (a,x_1,...,x_{k-2},t) on O+t+a,

using only (31.1) and (31.2).

The inner quiet types therefore orient every residual-pair path. If IL(a) holds, b-to-a would manufacture an h-first Hamilton path on X_a, contradicting part 3, so every Z_ab Hamilton path is a-to-b. Dually, if IR(a) holds, every Z_ab Hamilton path is b-to-a.

These forced endpoints are also current in the singleton-deletion exchange covers. If r,s,q are the three residual labels and r,s are left-active, arbitrary Hamilton paths L_r on (P-p_0)+r and L_s on (P-p_0)+s give exact covers of the SAME residue H-p_0:

  C_r = L_r | Z_sq,
  C_s = L_s | Z_rq.

Every Hamilton representative of Z_sq has endpoint pair {s,q}, and every representative of Z_rq has endpoint pair {r,q}. Thus the one-for-one support swap on the active rail comes with forced exchanged-label endpoints and one common complementary endpoint q. This extra terminal data is the next consumer interface.

Status: complete symbolic working argument. It is not part of the pending signed-cap exact review unit and should be reviewed separately before canonical use.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R927"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R966"
    }
]
```
