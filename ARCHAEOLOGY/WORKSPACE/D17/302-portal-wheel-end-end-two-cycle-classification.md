# An END-END root-capture 2-cycle is same-fiber disagreement, Reverse-Ear geometry, or a shared-exterior R407 rim interaction

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-end-end-two-cycle-classification`

**Summary:** Classify the shortest G23 rim atom when both opposite root-capture arcs d->k and k->d are END-currentized. Puncturing the captured endpoints gives two exact covers of the same pair-deletion residue H-{d,k}. If their support partitions differ, accepted R410/R471 gives a current same-fiber crossing and balanced-pair birth. If the partitions agree, nonclosure forces d and k to extend the same Hamilton block A with a common Hamilton complement B. Comparing the two endpoint-extension paths by R435 either gives explicit Reverse-Ear geometry or synchronizes one common A-order. Opposite endpoint roles then concatenate to a Hamilton path on A+d+k and close H with B. Same roles force both orientations of the rim dimer {d,k} to have the same polarity under one common boundary witness, so accepted R407 applies. Moreover that boundary witness is literally the common exterior endpoint of the two original selected K|(H-K) capture crossings. Thus an END-END rim 2-cycle has no anonymous coherent residue: its quiet same-partition branch collapses to an ancestry-pinned bidirectional rim interaction.


### 1. Setup: an END-END root-capture 2-cycle

Retain the root-capture construction of `closed-return-p5-root-capture-currentization-circuit` SV60333 from one Hamilton P5 \(K\). Suppose its chosen rim circuit has length two on distinct roots \(d,k\in V(K)\):

\[
 d\to k,\qquad k\to d.
\]

Thus the \(d\)-root arc comes from an actual exact singleton-deletion cover

\[
 T_d=P_d\mid Q_d\quad\text{of }H-d
\]

with a selected \(K-d\mid(H-K)\) crossing whose \(K\)-endpoint is \(k\); dually the \(k\)-root arc comes from an exact cover \(T_k\) of \(H-k\) with a selected crossing whose \(K\)-endpoint is \(d\).

Assume both arcs are in the END currentization branch of SV60333: \(k\) is a physical rail endpoint of \(T_d\), and \(d\) is a physical rail endpoint of \(T_k\). Puncturing those endpoints gives literal exact two-covers

\[
 F_d:=T_d-k,\qquad F_k:=T_k-d
\]

of the same proper residue

\[
 W=H-\{d,k\}.
\]

Exactness follows exactly as in SV60333 from accepted pair-deletion rigidity R429.

### 2. Different rim partitions are already a current same-fiber portal

Compare \(F_d\) and \(F_k\) on the common residue \(W\). If their unordered rail-support partitions differ, accepted R410/R471 applies directly. One of the two exact covers contains a selected adjacency whose endpoints lie in different components of the other cover, and accepted R176 yields a graph-intrinsic balanced opposite-sign pair.

Thus the 2-cycle itself is already a current same-rim-fiber partition-disagreement portal. No payment/currentization is needed to manufacture this disagreement: both exact representatives are literal endpoint punctures of the two root-capture source rows.

Hence only the common-partition branch remains.

### 3. Common partition forces both roots onto one common Hamilton block

Assume the two exact covers \(F_d,F_k\) have the same unordered support partition. Relabel its two nonempty blocks as \(A\mid B\).

Because \(k\) was an endpoint of its \(T_d\)-rail, restoring it to \(F_d\) places it at one end of exactly one block. After exchanging \(A,B\) if needed, write

\[
 T_d:(A+k)\mid B,
\]

where \(A+k\) denotes the actual Hamilton rail support carrying \(k\). Likewise \(T_k\) has support either

\[
 (A+d)\mid B
\]

or

\[
 A\mid(B+d).
\]

The second possibility closes \(H\): the actual Hamilton rail on \(A+k\) from \(T_d\) and the actual Hamilton rail on \(B+d\) from \(T_k\) are disjoint and together span all vertices of \(H\). Therefore a nonclosing 2-cycle forces

\[
 T_d:(A+k)\mid B,\qquad T_k:(A+d)\mid B. \tag{PW2.1}
\]

Consequently \(A,B,A+k,A+d\) are all Hamiltonian supports. Put

\[
 \Omega=A\cup\{d,k\}.
\]

The support \(\Omega\) is non-Hamiltonian, since a Hamilton path on \(\Omega\) together with the retained Hamilton path on \(B\) would two-cover \(H\).

Because \(F_d\) is an exact pair-deletion cover, R429 gives \(|A|\ge2\). Retain actual endpoint-extension paths

\[
 R_k\text{ on }A+k\quad\text{from }T_d,
\qquad
 R_d\text{ on }A+d\quad\text{from }T_k.
\]

### 4. Reverse-Ear comparison or one common literal A-order

Compare \(R_k\) and \(R_d\) by accepted R435. If the comparison yields a reversed old state, a tight reverse trimer, or a proper tight cycle, retain that explicit R435 geometry and stop.

Otherwise R435 monotonicity says that the common \(A\)-vertices occur in the same order in both paths. Since the only noncommon vertex of each path is its root label and that root is an endpoint, there is one literal Hamilton order

\[
 Q=(q_0,q_1,\ldots,q_r)\quad\text{on }A,
\]

with \(r\ge1\), such that

\[
 R_k\in\{(k,Q),(Q,k)\},\qquad
 R_d\in\{(d,Q),(Q,d)\}. \tag{PW2.2}
\]

### 5. Opposite endpoint roles close immediately

If the two special labels occupy opposite ends in (PW2.2), the certified path pieces concatenate without a new seam:

\[
 (k,Q,d)\quad\text{or}\quad(d,Q,k)
\]

is a Hamilton tight path on \(\Omega\). This contradicts the non-Hamiltonicity of \(\Omega\), equivalently closes \(H\) together with the common complement rail \(B\).

Therefore every nonclosing R435-quiet common-partition 2-cycle has the SAME endpoint role.

### 6. Same HEAD role gives a bidirectional head-signed rim dimer

Assume

\[
 R_k=(k,q_0,q_1,\ldots,q_r),\qquad
 R_d=(d,q_0,q_1,\ldots,q_r).
\]

If the turn \((k,d,q_0)\) were tight, then

\[
 (k,d,q_0,q_1,\ldots,q_r)
\]

would Hamiltonize \(\Omega\), because every later turn is certified by \(R_d\). Hence \((k,d,q_0)\) is bad. Boundary antisymmetry R3 gives

\[
 (q_0,d,k)\text{ tight}.
\]

Similarly \((d,k,q_0)\) must be bad, so

\[
 (q_0,k,d)\text{ tight}. \tag{PW2.3}
\]

Thus the two tested orientations \((d,k)\) and \((k,d)\) of the same physical rim dimer are both HEAD-signed by the same witness \(q_0\). Accepted R407 therefore gives its bidirectional same-witness dimer interaction at \(q_0\).

The witness has stronger source provenance here. In \(T_d\), the selected root-capture crossing has \(K\)-endpoint \(k\). Since \(k\) is an endpoint of \(R_k=(k,Q)\), the only selected state incident with \(k\) is \(kq_0\). Hence that original selected crossing is literally

\[
 kq_0,
\]

and \(q_0\in V(H)-V(K)\). Dually the original crossing generating \(k\to d\) is literally

\[
 dq_0.
\]

So the common R407 witness \(q_0\) is not an anonymous later vertex: it is the SAME exterior endpoint of the two source root-capture crossings.

### 7. Same TAIL role is the exact dual

If

\[
 R_k=(q_0,\ldots,q_r,k),\qquad
 R_d=(q_0,\ldots,q_r,d),
\]

then Hamiltonicity of \(\Omega\) forbids both final turns \((q_r,k,d)\) and \((q_r,d,k)\). R3 gives

\[
 (d,k,q_r),\qquad(k,d,q_r)
\]

both tight. Thus both rim-dimer orientations are TAIL-signed by the same witness \(q_r\), and R407 applies. Exactly as above, endpointness shows that the two original selected root-capture crossings are literally

\[
 q_rk,\qquad q_rd,
\]

so \(q_r\notin K\) is their common exterior endpoint.

### 8. Resulting shortest-rim normal form

Every END-END root-capture 2-cycle therefore has one of the following outputs:

1. **SAME-FIBER DISAGREEMENT:** the two punctured exact \(H-\{d,k\}\) covers have different support partitions, giving the current R410/R176 portal;
2. **R435:** the two reciprocal endpoint-extension paths emit a reversed state, reverse trimer, or proper cycle;
3. **TWO-COVER:** opposite endpoint roles Hamiltonize the common active block and close with the common complement;
4. **SHARED-EXTERIOR R407:** same endpoint roles make both orientations of the rim dimer same-polarity under one common witness, and that witness is exactly the shared exterior endpoint of the two original selected root-capture crossings.

This does not yet extinguish the final R407 branch. Its gain for G23 is that the shortest rim cannot remain an anonymous coherent pair-return loop: even the fully quiet common-partition END-END residue collapses to one physically pinned three-vertex reversal cell sitting directly on both source capture markers.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R407"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    }
]
```