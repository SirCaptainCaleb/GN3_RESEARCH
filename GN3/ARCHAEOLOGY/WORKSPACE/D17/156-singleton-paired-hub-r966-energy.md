# Paired fixed-hub R966 packets have exact cross-energy and one-turn quiet cores

**Workspace:** D17
**State:** established
**Key:** `singleton-paired-hub-r966-energy`

**Summary:** For the four endpoint replacement rows around one fixed hub C_b=P|Q, every cross-side ordered defect is exactly one plus the hub degree in the relevant replacement path, so the four-row internal K contribution is 16+2N_inner. More generally a fully hub-aligned double-star family has a closed K formula depending only on hub degrees. If both source-vs-replacement comparisons on one side are R435-quiet, the two replacement paths have the R966 near-end forms and their mutual conflict reduces to a single hub-closing turn on one contiguous inherited interval: an exact reversed hub state when the interval is one vertex, otherwise either a literal tight hub cycle or the exact reverse closing trimer. In a row-minimal aligned family, an inner quiet replacement therefore means the hub is excluded as an endpoint of every Hamilton path on that support.


### Setup: the paired endpoint packet
Let H be a hypothetical smallest counterexample and retain one fixed singleton source

  C_b=P|Q,
  P=(p_0,p_1,...,p_r),
  Q=(q_0,q_1,...,q_s).

Assume both sides are in the END-R966 branch of `singleton-fixed-hub-endpoint-r966`. Thus there are actual endpoint-replacement covers

  C_{p_0}=L_P|Q,      V(L_P)=(P-p_0)+b,
  C_{p_r}=R_P|Q,      V(R_P)=(P-p_r)+b,
  C_{q_0}=P|L_Q,      V(L_Q)=(Q-q_0)+b,
  C_{q_s}=P|R_Q,      V(R_Q)=(Q-q_s)+b.

The literal oriented rails P,Q are retained in every displayed complementary position. For a path T containing b, write d_T(b)=1 when b is an endpoint and d_T(b)=2 when b is internal.

### Exact cross-side endpoint energy
Fix p in {p_0,p_r} and q in {q_0,q_s}; write T_p for L_P or R_P and U_q for L_Q or R_Q as appropriate.

For the ordered comparison p<-q, the q-row has supports

  P | ((Q-q)+b).

Since p lies on its P rail, deleted-label substitution gives the target partition of H-p

  (P-p+q) | (Q-q+b).

The current p-row has supports

  (P-p+b) | Q.

Along T_p every selected edge not incident with b stays inside P-p and hence inside the first target class, while every selected edge incident with b crosses because b lies in the second target class. Along the literal Q rail, exactly the selected edge incident with endpoint q crosses because q has moved to the first target class. Therefore

  kappa(p<-q)=d_{T_p}(b)+1.                     (1)

The dual argument gives

  kappa(q<-p)=d_{U_q}(b)+1.                     (2)

The two p-endpoint rows are overlap-coherent with each other, and likewise the two q-endpoint rows, so their mutual ordered defects vanish. Summing (1)-(2) over the four cross pairs gives the exact internal contribution of these four endpoint rows:

  K_end = 2[d_{L_P}(b)+d_{R_P}(b)+d_{L_Q}(b)+d_{R_Q}(b)] + 8
        = 16 + 2 N_inner,                       (3)

where N_inner is the number of the four replacement paths on which b is internal. Thus each inner endpoint replacement carries an exact two-unit premium already inside the paired endpoint packet, before any external rows are counted.

### Full hub-aligned double-star energy
Assume now the stronger quiet-hub hypothesis of `singleton-fixed-hub-critical-dichotomy`: every p in P has an actual aligned cover

  C_p=T_p|Q,    V(T_p)=(P-p)+b,

and every q in Q has an actual aligned cover

  C_q=P|U_q,    V(U_q)=(Q-q)+b.

Same-side rows and every row-versus-b comparison are overlap-coherent, hence contribute zero. For arbitrary p in P,q in Q the same support check as above gives

  kappa(p<-q)=d_{T_p}(b)+d_Q(q),
  kappa(q<-p)=d_{U_q}(b)+d_P(p),                (4)

where d_P,d_Q are ordinary selected-edge degrees in the literal source paths. Since

  sum_{p in P} d_P(p)=2(|P|-1),
  sum_{q in Q} d_Q(q)=2(|Q|-1),

putting m=|P| and n=|Q| yields the exact total defect of this aligned family:

  K = n sum_{p in P} d_{T_p}(b)
      + m sum_{q in Q} d_{U_q}(b)
      + 2m(n-1)+2n(m-1).                       (5)

In particular, once these aligned support partitions are fixed, formula (5) itself shows that changing a single path T_p affects K only through the positive coefficient n d_{T_p}(b), and changing a single U_q affects K only through m d_{U_q}(b). Thus in a K-minimal aligned representative each T_p and U_q independently minimizes its hub degree. Hence if any Hamilton path on (P-p)+b exposes b as an endpoint, a K-minimal aligned representative must use such an endpoint path with d_{T_p}(b)=1. Consequently a K-minimal aligned path having b internal certifies a support-wide terminal exclusion:

  every Hamilton path on (P-p)+b has b internal. (6)

The dual statement holds on Q.

### Quiet source comparisons reduce to one hub-closing turn
Return to one P-side R966 packet. Suppose both comparisons (P,L_P) and (P,R_P) are R435-quiet. The exact R966 proof then forces

  L_P=(b,p_1,...,p_r)              or (p_1,b,p_2,...,p_r),
  R_P=(p_0,...,p_{r-1},b)          or (p_0,...,p_{r-2},b,p_{r-1}).

Let epsilon=0 in the first L form and 1 in the second; let delta=0 in the first R form and 1 in the second. Put

  i=1+epsilon,    j=r-1-delta.

If i>j, only the boundary-overlap cases r=2 or r=3 can occur. For r=2 there are three possibilities. If (epsilon,delta)=(0,1), then R_P=(p_0,b,p_1) and L_P=(b,p_1,p_2) concatenate to the Hamilton path (p_0,b,p_1,p_2) on P+b. If (epsilon,delta)=(1,0), then R_P=(p_0,p_1,b) and L_P=(p_1,b,p_2) concatenate to (p_0,p_1,b,p_2). Both contradict non-Hamiltonicity. If (epsilon,delta)=(1,1), then L_P contains p_1 b while R_P contains b p_1, so the mutual comparison already has an exact reversed old state. For r=3, i>j forces epsilon=delta=1, and the overlapping certified turns give the Hamilton path

  (p_0,p_1,b,p_2,p_3),

again contradicting non-Hamiltonicity. Therefore outside an explicit mutual R435 reversal or a forbidden Hamilton extension, one has i<=j.

If i=j, L_P contains the selected state b p_i while R_P contains its exact reversal p_i b. This is the completely localized mutual R435 output.

Suppose i<j. The literal segment

  (b,p_i,p_{i+1},...,p_j)

occurs in L_P. Moreover R_P certifies the closing predecessor turn

  (p_{j-1},p_j,b),

while L_P certifies the opening turn

  (b,p_i,p_{i+1}).

Thus the cyclic word

  b,p_i,p_{i+1},...,p_j,b

has every required turn certified except exactly

  tau_P=(p_j,b,p_i).                              (7)

If tau_P is tight, this word is a literal vertex-simple tight cycle on {b,p_i,...,p_j}. If tau_P is bad, boundary antisymmetry gives the exact labelled reverse trimer

  tau_P^*=(p_i,b,p_j) tight.                      (8)

Therefore outside source-relative R435 output, the entire P-side R966 packet reduces to one inherited interval and one binary hub-closing turn. The Q-side statement is identical, with its own interval [k,l] and hub turn tau_Q.

Combining this with (3), a paired fixed-hub packet has no featureless quiet residue: each side either already emits source-relative R435 geometry, or is represented by one explicit hub interval packet; and every inner near-end choice has a quantified K premium. In a row-minimal aligned family, any such inner choice additionally carries the terminal exclusion (6).

### Scope
Equations (1)-(5) are exact bookkeeping identities, not a proof that the aligned family is globally K-minimal. The one-turn interval reduction does not by itself consume the two hub turns tau_P,tau_Q into R561 or a spanning two-cover. A tight cycle is retained as a literal vertex-simple tight cycle and is not treated as a boundary-reversed Hamilton dimer. The next consumer should combine the two interval packets with the exact K premium or use an END-DIRECT cross-side defect to perform a genuine support change.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```
