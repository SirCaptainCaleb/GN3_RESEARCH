# A degree-three endpoint core in Arm M forces a complementary two-core hexagon; the fully quiet residue has opposite endpoint roles on the two cores

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-degree-three-core-complementary-hexagon`

**Summary:** In R927 Arm M, a (k-1)-core R with three completion incidences R+x,R+y,R+z forces a six-cover complementary-core hexagon with the complementary (k-1)-core W. Outside component-drop/R435, both cores have synchronized Hamilton orders and constant completion roles; equal R/W roles are impossible by one R3 pivot because they force a P_(k+1), so the fully quiet residue has opposite roles and makes W another degree-three completion core. Accepted R933 then supplies sheetwise two-seam reversal packets. Strengthening: in the opposite-role residue, any successful non-forced wrap on a completion support is already same-support order activity. If all such wraps fail, then for every external pair {p,q} both (r0,p,q,wm) and (r0,q,p,wm) are Hamilton P4s. Choosing one exact two-cover of their proper complement currentizes these as two literal maximum three-forests with identical support partition and identical complement rails selecting pq in opposite directions. Thus a degree-three completion core cannot remain static: it yields a forbidden k+1 path, current component-drop/order activity, or an explicit family of maximum-forest selected reversals.


### 1. Setup: one degree-three endpoint core
Assume accepted R927 Arm M:

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.

Let R be a (k-1)-set and let x,y,z be three distinct vertices outside R such that for each p in {x,y,z} there is an actual Hamilton path P_p on R+p having p as an endpoint. Put

  W=V(H)-(R union {x,y,z}).

Then |W|=k-1. Since every k-set is Hamiltonian, each W+p is Hamiltonian as well.

For each deleted label, the two complementary k|k partitions give literal exact singleton-deletion covers. For example

  H-z : (R+x) | (W+y),
  H-z : (R+y) | (W+x),

and cyclically for H-x and H-y. Exactness holds because a Hamilton H-p together with singleton {p} would two-cover H. Thus the six supports form a literal two-sheet complementary-core hexagon.

### 2. The R-side completion paths synchronize or emit R435
Trim the exposed endpoint p from P_p. This gives a Hamilton path on the common support R. Compare the three trimmed Hamilton paths by accepted R435.

If an R435-nonquiet comparison occurs, retain its exact selected reversal / reverse-trimer / proper-cycle geometry. Otherwise all three trimmed paths have one literal core order

  K_R=(r_0,...,r_{k-2}).

The roles of x,y,z at K_R are all the same. Indeed if, say, x is a source extension and y a terminal extension, then

  (x,K_R,y)

is a tight path on R+x+y of order k+1, contradicting Arm M. After duality normalize the common R-role to SOURCE:

  P_p=(p,K_R)   for p=x,y,z.                         (DH.1)

### 3. An internal W-completion is already current component-drop geometry
Choose actual Hamilton paths Q_p on W+p for p=x,y,z and use them in the six singleton rows above.

Suppose some p is internal in Q_p. Choose q distinct from p and the singleton row omitting the third label whose two rails are R+q and W+p. Deleting p from the internal Q_p rail gives a literal three-cover of the proper pair-deletion residue H-{p,third}.

That residue has exact path-cover number two: R4 gives pc<=2, while Hamiltonicity would pair with the omitted physical dimer and two-cover H. Therefore an exact two-cover of the same residue exists, and comparison with the retained literal three-cover gives the current component-drop/R159 mechanism with all physical fragments retained.

Hence outside this explicit component-drop output we may assume every Q_p exposes p as an endpoint.

### 4. The W-side endpoint paths also synchronize
Trim p from Q_p. Outside R435 on the common support W, the three trimmed paths have one literal order

  K_W=(w_0,...,w_{k-2}).

Again the three completion roles are equal: opposite roles for two labels would concatenate to a Hamilton path on W+p+q of order k+1. Thus W has one constant completion role on x,y,z.

### 5. Equal roles on R and W are impossible by one R3 pivot
Assume first that both cores have SOURCE role. Fix one label i in {x,y,z} and let {j,k} be the other two. On the pair-deletion residue H-{j,k} retain the two exact covers

  T_R=(i,K_R) | K_W,
  T_W=K_R | (i,K_W).                                  (DH.2)

Apply R3 to the reversal pair

  (r_0,i,w_0),  (w_0,i,r_0).

If (r_0,i,w_0) is tight, then

  (r_0,i,K_W)

is a tight path on k+1 vertices. If (w_0,i,r_0) is tight, then

  (w_0,i,K_R)

is a tight path on k+1 vertices. Either conclusion contradicts Arm M.

The common TERMINAL/TERMINAL case is the exact dual, using the terminal core vertices.

Therefore equal constant roles on the two cores are impossible.

### 6. Exact surviving quiet residue
Outside the explicit component-drop and R435 outputs, the only possible degree-three-core residue has opposite constant roles on the two cores. After duality:

  (p,K_R) is Hamiltonian on R+p,
  (K_W,p) is Hamiltonian on W+p,

for every p in {x,y,z}.                                 (DH.3)

In particular W is itself a degree-three endpoint core on the same completion triple. Thus the hard object is a PAIRED degree-three-core / two-sheet hexagon, not one spindle against an arbitrary complement.

For each deleted label i, the other two labels occur on opposite rails in opposite endpoint roles in the two sheet choices. Exactly one role-correct singleton trimer through i is tight by R3. Applying accepted R933 to the corresponding sheet gives both residual attachment seams physically present and bad, hence both exact reversed attachment turns simultaneously tight.

Thus the opposite-role residue exports a synchronized family of R933 two-seam packets while retaining both degree-three endpoint cores and all six exact singleton rows.

No claim is made here that these packets already contradict Arm M. The theorem-level conclusion is the exact dichotomy:

  forbidden P_{k+1},
  OR current component-drop/R435 geometry,
  OR a paired opposite-role degree-three-core hexagon carrying sheetwise R933 reversal packets.


### 7. In the opposite-role residue, successful wraps are already order activity
Retain the normalized opposite-role case (DH.3), with

  P_p=(p,r_0,...,r_m),
  Q_p=(w_0,...,w_m,p),

where m=k-2.

On the R-side, the wrap seam

  beta_p=(r_{m-1},r_m,p)

is bad for every p. Indeed if beta_p were tight, the rotation

  (r_0,...,r_m,p)

would be Hamiltonian on R+p; prepending any other completion q using the inherited source turn (q,r_0,r_1) would give a Hamilton path on R+p+q of order k+1. Thus R3 gives

  (p,r_m,r_{m-1}) tight                              (DH.4)

for every p.

Dually, on the W-side the wrap seam

  alpha'_p=(p,w_0,w_1)

is bad for every p, since a successful rotation (p,w_0,...,w_m) could be followed by any other terminal completion q. Hence

  (w_1,w_0,p) tight                                  (DH.5)

for every p.

Apply accepted R579 to each P_p and Q_p. If the remaining wrap seam succeeds for any completion label, retain the original and rotated Hamilton paths on the same k-support as explicit same-support order/endpoint activity. No static quiet residue remains at that label.

Therefore, in the branch avoiding such same-support activity, every completion label is in R579 DOUBLE-FAIL on both cores.

### 8. Full double-fail gives a selected-reversal P4 for every external pair
Assume the fully double-fail branch of Section 7. In addition to (DH.4)-(DH.5), R579 gives

  (r_0,p,r_m) tight,
  (w_0,p,w_m) tight                                  (DH.6)

for every completion p.

Now fix distinct p,q in {x,y,z}. Since R+p+q is a forbidden (k+1)-set, the proposal

  (q,p,K_R)

cannot be tight. Its only new turn is (q,p,r_0), so R3 gives

  (r_0,p,q) tight.                                   (DH.7)

Swapping p,q gives (r_0,q,p) tight.

Dually W+p+q is non-Hamiltonian. The proposal

  (K_W,p,q)

has only one new turn (w_m,p,q), which must be bad; hence

  (q,p,w_m) tight.                                   (DH.8)

Swapping p,q gives (p,q,w_m) tight.

Combining (DH.7)-(DH.8), BOTH literal Hamilton P4 orders

  A_pq=(r_0,p,q,w_m),
  A_qp=(r_0,q,p,w_m)                                 (DH.9)

exist on the same four-set

  X_pq={r_0,p,q,w_m}.

They have the same physical endpoints r_0,w_m and select the physical dimer {p,q} in opposite directions.

### 9. The reversal is current in the maximum-three-forest exchange space
The four-set X_pq is a proper tight path support. Put

  Z=H-X_pq.

If Z were Hamiltonian, either Hamilton P4 in (DH.9) together with a Hamilton path on Z would two-cover H. Hence Z is non-Hamiltonian. By accepted R4, pc(Z)=2 exactly. Choose one literal exact two-cover

  Z=U|V.

Then

  A_pq | U | V,
  A_qp | U | V                                         (DH.10)

are two literal spanning maximum three-forests of H with IDENTICAL support partition and IDENTICAL complementary rails U,V. Their only retained discrepancy needed here is the named selected state pq versus qp inside the same four-rail X_pq.

Thus the fully quiet opposite-role degree-three-core residue is not terminal. For EVERY unordered pair {p,q} of the three completion labels it supplies a current same-support selected reversal inside the actual maximum-three-forest exchange space.

This does not assert R561: the reversed dimer is internal in the four-rail, and the two-rail complement U|V need not be Hamiltonian as one block. The correct output is an explicit current holonomy interface for the global maximum-forest consumer.


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
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R579"
    },
    {
        "relation": "dependency",
        "revision_id": "R933"
    }
]
```
