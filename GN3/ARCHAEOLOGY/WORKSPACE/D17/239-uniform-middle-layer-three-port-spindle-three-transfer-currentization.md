# A three-port spindle is a three-transfer maximum-forest path with the third completion rail frozen

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-three-port-spindle-three-transfer-currentization`

**Summary:** In R927 Arm M, retain a same-role SOURCE completion core R with common order K=(r0,...,rm) and three completion labels p,q,t. The no-(k+1)-path condition makes the terminal wrap seam beta_a=(r_{m-1},r_m,a) bad for every port a. At most one remaining R579 wrap seam alpha_a=(r_m,a,r0) can be tight: two successful alpha seams, together with R3 on the two port labels around r_m, concatenate to a forbidden (k+1)-path. Hence two ports p,q are R579 DOUBLE-FAIL, giving (r0,a,r_m) and (a,r_m,r_{m-1}) for a=p,q. The forbidden two-port extensions force (r0,p,q) and (r0,q,p), and R3 lets us relabel so (p,r0,q) is tight. Thus S=(p,r0,q,r_m,r_{m-1}) is the symbolic spindle P5. Let W be the remaining k-1 vertices outside R,p,q,t and choose any Hamilton path Q_t on W+t. If k=4 then S|Q_t is already a spanning two-cover. Otherwise k>=5 and the singleton-lift F0=(p,K)|Q_t|{q} reaches the spindle forest F3=S|(r1,...,r_{m-2})|Q_t through three literal maximum forests, each obtained by replacing exactly one selected edge: cut r0-r1/add r0-q; cut r_{m-1}-r_m/add q-r_m; cut r_{m-2}-r_{m-1}/add r_m-r_{m-1}. The Q_t rail is literally unchanged throughout. Hence the spindle is not an independent static P5 species: it is already a length-three support-changing path in the actual maximum-three-forest representative space, anchored at a canonical singleton-deletion Johnson row and preserving the untouched middle core and full physical ancestry. No holonomy extinction or O4 closure is claimed.

### 1. Three-port same-role entrance
Work in accepted R927 Arm M:

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.

Retain a (k-1)-set R and three distinct completion labels p,q,t outside R for which one literal core order

  K=(r_0,r_1,...,r_m),   m=k-2,

satisfies

  (a,K)

Hamiltonian for every a in {p,q,t}. This is the same-role SOURCE three-port spindle entrance arising in the degree-three-core router. All labels and the literal order K are retained.

For each port a, the terminal wrap seam

  beta_a=(r_{m-1},r_m,a)

is bad. Indeed, if beta_a were tight, then (r_0,...,r_m,a) would be Hamiltonian; prepending any other port b using the inherited source turn (b,r_0,r_1) would give a tight path

  (b,r_0,...,r_m,a)

on k+1 vertices, forbidden in Arm M. Hence R3 gives

  (a,r_m,r_{m-1}) tight.                              (SP.1)

Apply accepted R579 to the Hamilton path (a,K). Since beta_a is bad, the only remaining distinction is whether

  alpha_a=(r_m,a,r_0)

is tight or bad.

### 2. At least two ports are R579 DOUBLE-FAIL
At most one of alpha_p,alpha_q,alpha_t can be tight. Suppose alpha_a and alpha_b are both tight for two distinct ports a,b. Boundary antisymmetry R3 on {a,r_m,b} makes exactly one of

  (a,r_m,b), (b,r_m,a)

tight. In the first case, concatenate it with alpha_b=(r_m,b,r_0) and the inherited source continuation (b,r_0,r_1), obtaining

  (a,r_m,b,r_0,r_1,...,r_{m-1}),

a tight path on R+{a,b} of order k+1. In the second case use alpha_a symmetrically. Both contradict Arm M.

Therefore at least two ports lie in the R579 DOUBLE-FAIL branch. Relabel them p,q. The proof mechanism of R579 now retains the exact reverse seams

  (r_0,p,r_m), (p,r_m,r_{m-1}),
  (r_0,q,r_m), (q,r_m,r_{m-1})                         (SP.2)

as graph-intrinsic physical turns.

### 3. The symbolic spindle P5
The support R+p+q has order k+1 and is non-Hamiltonian. If (q,p,r_0) were tight, then

  (q,p,K)

would be a forbidden Hamilton (k+1)-path. Hence R3 gives

  (r_0,p,q) tight.                                      (SP.3)

Similarly

  (r_0,q,p) tight.                                      (SP.4)

Apply R3 to the complete-reversal pair with middle r_0. Exactly one of

  (p,r_0,q), (q,r_0,p)

is tight. Relabel p,q if necessary so that

  (p,r_0,q) tight.                                      (SP.5)

Using (SP.5), the q-instance of (SP.2), and its reverse terminal seam, we obtain the literal tight P5

  S=(p,r_0,q,r_m,r_{m-1}).                             (SP.6)

This is the three-port spindle, but we now retain its full R579/R3 ancestry instead of treating S as an anonymous proper path.

### 4. Canonical singleton-row lift and the frozen third-label rail
Put

  W=V(H)-(R union {p,q,t}).

Then |W|=k-1, so W+t is a k-set and is Hamiltonian in Arm M. Choose and retain one actual Hamilton path Q_t on W+t.

The singleton-deletion row

  H-q : (p,K) | Q_t

is a literal two-cover of H-q. Restoring q gives the spanning three-forest

  F_0=(p,r_0,r_1,...,r_m) | Q_t | {q}.                 (SP.7)

If k=4, the spindle S uses all three vertices of R, so

  S | Q_t

is already a spanning two-cover of H, contradiction. Thus any surviving spindle in a hypothetical counterexample has k>=5. In particular the middle core

  M=(r_1,...,r_{m-2})

is nonempty.

### 5. Three exact one-edge support transfers
Define

  F_1=(p,r_0,q) | (r_1,...,r_m) | Q_t,                 (SP.8)

  F_2=(p,r_0,q,r_m) | (r_1,...,r_{m-1}) | Q_t,         (SP.9)

  F_3=(p,r_0,q,r_m,r_{m-1}) | (r_1,...,r_{m-2}) | Q_t. (SP.10)

Every displayed rail is a literal tight path. For F_1 the only new turn is (p,r_0,q), supplied by (SP.5). For F_2 the new turn is (r_0,q,r_m), supplied by (SP.2). For F_3 the new turn is (q,r_m,r_{m-1}), also supplied by (SP.2).

Moreover consecutive representatives differ by exactly one selected physical edge:

  F_0 -> F_1: delete r_0 r_1, add r_0 q;
  F_1 -> F_2: delete r_{m-1} r_m, add q r_m;
  F_2 -> F_3: delete r_{m-2} r_{m-1}, add r_m r_{m-1}. (SP.11)

Each replacement merely cuts one current rail at the named boundary and attaches the detached physical vertex/block at the certified tight seam. Both endpoint representatives are literal spanning three-path covers, so each move is exactly reversible. Since H itself has no spanning two-cover, these are literal maximum-three-forest representatives.

The third-label Hamilton rail Q_t is IDENTICAL in F_0,F_1,F_2,F_3. The path F_3 is precisely

  S | M | Q_t,                                         (SP.12)

so the untouched middle core survives literally as its own rail rather than being discarded by the P5 compression.

### 6. Parent consequence
The three-port spindle is therefore not an independent static P5 obstruction. It is the endpoint of a length-three support-changing walk of actual maximum-three-forest representatives beginning at the canonical singleton-rooted Johnson row F_0, with Q_t frozen and with the two DOUBLE-FAIL ports, all R579 seam certificates, the R3 middle choice, and the untouched core middle M retained physically.

This is stronger than merely currentizing S through an arbitrary two-cover of its complement: it gives an explicit representative path back to the degree-three-core puncture system. It is also compatible with the marked-holonomy normal form: none of the three moves is a same-support fiber reorder.

No claim is made that this three-step path itself has nontrivial marked holonomy, that every global forest loop contracts, or that O4 is closed. The theorem-level output is exact SPINDLE CURRENTIZATION: the symbolic three-port spindle belongs immediately to the existing support-changing maximum-three-forest program.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R579"
    }
]
```