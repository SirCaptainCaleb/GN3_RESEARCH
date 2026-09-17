# A Hamilton-cycle complement puts every puncture path inside a rim-wide two-ended P6 shell

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-hamilton-cycle-puncture-p6-shell`

**Summary:** In a smallest-counterexample fixed-complement critical block V(H)=Omega disjoint-union Q, assume the Hamilton complement support Q carries a tight Hamilton cycle, so every cyclic break is a literal Hamilton path. Fix any Hamilton puncture path P_x=(h,r,...,s,t) on Omega-x with at least four vertices. For every rim vertex q, counterexamplehood plus the Hamilton path Q-q forces the reverse endpoint turns (r,h,q) and (q,t,s). Applying the full critical-block boundary wall to cyclic breaks of Q also gives both turns (h,q_i,q_{i-1}) and (q_i,q_{i-1},t) at every oriented rim edge. Hence (r,h,q_i,q_{i-1},t,s) is a literal tight P6 for every rim edge. Moreover both K=(h,q_i,q_{i-1},t) and K^op=(t,q_i,q_{i-1},h) are tight P4s with the same middle dimer. For any nontrivial exact two-cover T of its deletion, R833 gives the common identity b_T(h,t)=deg_T(h)+deg_T(t)-1_{ht selected}>=2; at the equality floor b_T=2, the two opposite R833 applications cannot both escape through reverse-chord/ANTI-ENDS, so at least one produces a named reverse endpoint seam. This is a cycle-branch currentization interface, not CBCA closure.


### 1. Fixed-complement cycle setting
Let H be a hypothetical smallest Strong Level-(1) counterexample and suppose

  V(H)=Omega disjoint_union V(Q),

where Omega is non-Hamiltonian but deletion-Hamiltonian. Assume the complement support Q carries a vertex-simple tight Hamilton cycle with cyclic order

  C_Q=(q_0,q_1,...,q_{m-1}),

indices modulo m, so every cyclic break of this order is a literal Hamilton path on V(Q). Fix x in Omega and an actual Hamilton puncture path

  P_x=(h,r,...,s,t)

on Omega-x. Assume P_x has at least four vertices, so the displayed source and terminal dimers are disjoint and the P6 below is vertex-simple.

### 2. Every rim vertex reverse-signs both puncture-path endpoint dimers
Fix q in V(Q). If

  (q,h,r) tight,

then (q,h,r,...,s,t) is a Hamilton path on (Omega-x)+q. Since deleting q from the tight Hamilton cycle C_Q leaves a Hamilton path on Q-q, these two paths form a spanning two-cover of H, contradiction. Therefore (q,h,r) is bad, and boundary antisymmetry R3 gives

  (r,h,q) tight.                                           (RC.1)

Dually, if

  (s,t,q) tight,

then (h,r,...,s,t,q) together with the Hamilton path Q-q two-covers H. Hence (s,t,q) is bad and R3 gives

  (q,t,s) tight.                                           (RC.2)

Thus every physical rim vertex simultaneously tail-signs the reverse source dimer (r,h) and head-signs the reverse terminal dimer (t,s) of every retained puncture path P_x.

### 3. Every rim edge supplies a literal two-ended P6 shell
Fix an oriented rim edge

  D_i=(q_i,q_{i-1}).

Apply the established full critical-block boundary wall SV23225 to the cyclic break of C_Q ending at q_i. Its reverse terminal boundary gives, for every y in Omega,

  (y,q_i,q_{i-1}) tight.                                  (RC.3)

Apply the same wall to the cyclic break beginning at q_{i-1}. Its reverse source boundary gives

  (q_i,q_{i-1},y) tight.                                  (RC.4)

Taking y=h in (RC.3), y=t in (RC.4), and adjoining (RC.1)-(RC.2), the four consecutive turns

  (r,h,q_i),
  (h,q_i,q_{i-1}),
  (q_i,q_{i-1},t),
  (q_{i-1},t,s)

are all tight. Hence

  S_i=(r,h,q_i,q_{i-1},t,s)                               (RC.5)

is a literal vertex-simple tight P6 for every rim edge D_i.

The same wall also gives the opposite endpoint P4

  K_i^op=(t,q_i,q_{i-1},h),                               (RC.6)

while the middle four vertices of S_i give

  K_i=(h,q_i,q_{i-1},t).                                  (RC.7)

Thus every rim dimer is the common middle dimer of two tight P4s with the puncture endpoints exchanged.

### 4. Paired R833 at one rim dimer
Fix i and let T=T_1|T_2 be any literal exact two-cover of

  H-{q_i,q_{i-1}}

whose two rails are nontrivial. Apply accepted R833 first to K_i and then to K_i^op. Both applications use the same endpoint pair {h,t}, the same deleted middle dimer D_i, and the same literal cover T. Therefore both share the exact block-count identity

  b_T(h,t)=deg_T(h)+deg_T(t)-epsilon_{ht} >= 2,            (RC.8)

where epsilon_{ht}=1 exactly when {h,t} is a selected T-state.

Suppose the equality floor b_T(h,t)=2 holds. Then at least one of the two R833 applications is in a reverse-seam branch.

Indeed, if epsilon_{ht}=1, then deg_T(h)+deg_T(t)=3. ANTI-ENDS is impossible because it requires h,t nonadjacent. If neither orientation produced a reverse seam, K_i would therefore force the selected reverse chord t->h, while K_i^op would force the selected reverse chord h->t, impossible in one path cover.

If epsilon_{ht}=0, then deg_T(h)=deg_T(t)=1. Reverse-chord is unavailable. If neither orientation produced a reverse seam, both applications would be ANTI-ENDS. The K_i orientation would make h a rail start and t a rail end, while K_i^op would make t a rail start and h a rail end. Thus each of h,t would have to be both the first and last vertex of its fixed T-rail. Since both T-rails are nontrivial, this is impossible.

Consequently b_T(h,t)=2 forces at least one of the four source-visible R833 seam alternatives:

  selected c->h with (q_i,h,c) tight,
  selected t->c with (c,t,q_{i-1}) tight,
  selected c->t with (q_i,t,c) tight,
  selected h->c with (c,h,q_{i-1}) tight,

for a physical c outside {h,t,q_i,q_{i-1}} in the corresponding complementary block.

### 5. Scope and moonshot interface
This does not close the Hamilton-cycle complement branch and does not prove Critical-Block Complement Absorption. Its point is family-level synchronization. One fixed puncture path is not merely decorated by two outer witnesses: the entire Hamilton rim signs both reversed endpoint dimers, and every rim edge creates the same two-ended P6 shell. After deleting that rim dimer, the two opposite P4 orientations feed the same exact representative T into R833. At the minimum two-block floor, a genuine reverse seam is unavoidable.

The next global consumer should combine these paired R833 constraints over an endpoint-return Hall cycle or an extremal family of puncture paths. Persistent b_T>=3 is then the only way to avoid the equality-floor seam, so fragmentation itself becomes the candidate holonomy measure rather than another local signed packet.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R833"
    }
]
```
