# Every pre-pivot defect position has a strict-descent closing shortcut

**Workspace:** D17
**State:** established
**Key:** `g35-prepivot-low-transition-shortcut-fan`

**Summary:** In zipper coordinates for the unique G35 augmenter, let r be the first positive prefix index from SV110451. For every q<r, nonnegativity of the prefix transition count and first-positive minimality force S_q in {-1,0}. The moving unmatched out-copy is a_q,out and the far unmatched in-copy remains b_m,in. If a_q and b_m are distinct, adding the direct shortcut g_q=a_q->b_m gives a matching of exact two-cover cardinality. Zipper parity gives chi(g_q)=(S_q mod 2) xor (w(C*) mod 2), hence tau(M_q+g_q)<=2 in both S_q=0 and S_q=-1 cases, strictly below tau(F)>=3. The physical labels a_q are pairwise distinct, so at most one pre-pivot index has the loop coincidence a_q=b_m. Whenever M_q is a literal tight three-forest, the shortcut has only the two endpoint seam turns as new obligations: if both pass and the endpoints lie on different rails it is an exact strict-descent two-cover; a bad seam yields its exact R3 reverse trimer, while same-rail passage creates exactly one directed cycle closed by g_q. Thus the whole corridor before the first positive pivot is a fan of strict-descent closure attempts, with at most one singleton-defect loop exception.


### 1. Zipper input
Retain the G35 zipper coordinates of SV111278 on the unique F-heavy augmenting path

  C_* = e_1,f_1,...,f_{m-1},e_m,

with

  e_i=a_{i-1}->b_i,   f_i=a_i->b_i     (1<=i<m),
  e_m=a_{m-1}->b_m.

The canonical proper-prefix matching M_q of SV109629 has the same cardinality as J, its unmatched OUT copy on C_* is a_q,out, and the far unmatched IN copy b_m,in has not moved. Put

  S_q=sum_{i<=q}(chi(e_i)-chi(f_i)),

so

  tau(M_q)=tau(J)+S_q=1+S_q.                              (PF.1)

Let r be the least proper index with S_r=1 from SV110451.

### 2. Before the first positive pivot the ledger has only two values
For every q<r, minimality of r gives

  S_q<=0.                                                  (PF.2)

But M_q is an actual selected matching, so its number of X|B selected edges is nonnegative. By (PF.1),

  1+S_q>=0.                                                (PF.3)

Hence the pre-pivot ledger is completely rigid:

  S_q in {-1,0} for every q<r.                             (PF.4)

No deeper negative transition debt can occur before the first positive pivot.

### 3. Every non-loop pre-pivot defect has a direct closing edge
Fix q<r and suppose the physical vertices a_q and b_m are distinct. Both corresponding matching copies are free in M_q, so the ordinary directed edge

  g_q := a_q -> b_m                                        (PF.5)

can be added without matching competition. Put

  N_q := M_q + g_q.                                        (PF.6)

Then

  |N_q|=|M_J|+1=|M_F|,                                     (PF.7)

so N_q has exactly the selected-edge cardinality of a spanning two-path cover.

Use the zipper parity identities of SV111278:

  S_q mod 2 = sigma(a_0) xor sigma(a_q),
  w(C_*) mod 2 = sigma(a_0) xor sigma(b_m).

Therefore

  chi(g_q)=sigma(a_q) xor sigma(b_m)
          =(S_q mod 2) xor (w(C_*) mod 2).                 (PF.8)

Combining (PF.1), (PF.4), and (PF.8):

- if S_q=0, then tau(N_q)=1+(w(C_*) mod 2), hence tau(N_q) is 1 or 2;
- if S_q=-1, then tau(N_q)=1 xor (w(C_*) mod 2), hence tau(N_q) is 0 or 1.

Thus in every case

  tau(N_q)<=2<3<=tau(F).                                   (PF.9)

Every non-loop pre-pivot defect position therefore carries a matching-level strict old-source descent obtained by one direct edge to the fixed far endpoint. This is stronger than the first-positive shortcut bound: before r there is no tau-three numerical hard cell at all.

### 4. There is at most one loop coincidence in the fan
The out-copy vertices

  a_0,out,a_1,out,...,a_{m-1},out

appearing along the matching path C_* are pairwise distinct. Hence the physical labels a_q are pairwise distinct. The fixed physical label b_m can therefore equal a_q for at most one index q.

Consequently at most one pre-pivot member of the shortcut fan can fail for the purely formal reason

  a_q=b_m.                                                 (PF.10)

At such an index both copies of that physical vertex are unmatched in M_q, so the selected matching isolates it. This is exactly the singleton-defect coincidence already identified in SV111278, now seen to occur at most once along the whole pre-pivot corridor.

### 5. Physical realization when the prefix is a tight forest
Assume additionally that M_q is realized as a literal spanning tight three-path forest T_q. Then a_q is the terminal of one displayed rail and b_m is the source of one displayed rail. Adding g_q creates no new turn except, when the relevant neighboring vertices exist, the predecessor seam at a_q and the successor seam at b_m.

If a seam is bad, R3 gives its exact complete reversal on the same three-vertex support. If both defined seams are tight and the two endpoint vertices lie on different T_q rails, g_q joins those rails, creates no directed cycle, and N_q is a literal exact two-cover. By (PF.9) it is a strict old-source transition descent.

If both seams are tight but a_q and b_m are the terminal and source of the same T_q rail, adding g_q closes exactly that rail to one directed tight cycle; the other two rails remain paths. Thus the only acyclic obstruction after both seam tests pass is the single cycle closed by g_q itself.

Therefore every physically realized pre-pivot prefix has the exact alternative:

1. strict old-source two-cover descent;
2. an exact R3 reverse seam trimer at one shortcut endpoint;
3. one directed tight cycle whose closing edge is g_q; or
4. the unique possible loop coincidence a_q=b_m.

These are witnesses to failure of a member of one closing fan, not separate parent obstruction species.

### 6. G35 consequence and scope
The first-positive index r is not the first place where a low-transition closing attempt exists. Every earlier defect position already admits a size-two-cover shortcut of transition count at most two, and all such shortcuts share the same far unmatched endpoint b_m while their near endpoint moves strictly forward through the distinct labels a_q.

Hence a surviving G35 packet must physically block an entire moving fan of strict-descent closures before the canonical tau-two pivot is reached, except for at most one singleton-defect coincidence. This supplies a sharper corridor interface for a blocker-transport theorem: compare consecutive failed shortcuts rather than treating the first-positive pivot in isolation.

This section does not yet prove that one fan member is physically realizable and does not consume its reverse seam or cycle witness. It uses no R24, R5, payment, replay, MILP, SAT, or seam taxonomy.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
