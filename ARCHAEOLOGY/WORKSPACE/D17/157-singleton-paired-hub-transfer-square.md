# Opposite hub endpoint replacements form exact transfer squares and cross-splice reversals

**Workspace:** D17
**State:** established
**Key:** `singleton-paired-hub-transfer-square`

**Summary:** For every opposite source endpoint pair, the two fixed-hub replacement fibers induce two exact covers of the same pair-deletion residue, with the physical hub b transferred from one rail to the other while the punctured source rails stay literal. In the source-R435-quiet branch, pairing a left replacement on one side with a right replacement on the other gives a spanning hub splice. Unless both hub insertions are inner, a tight splice would leave only two or three vertices and therefore close H; hence the splice turn is bad and its exact labelled reverse is tight. In the inner/inner case, either the same reverse turn is obtained or the splice is tight and its complement is exactly a non-Hamiltonian four-set consisting of two source endpoint dimers; then R813 supplies a gap-local Hamilton P4 at every gap of the exact merged path. Thus the paired R966 residue reduces to source-relative R435, explicit cross-hub reversals, or a sharply localized four-complement cell.


### Exact same-residue transfer squares
Retain the paired fixed-hub setup

  C_b=P|Q,
  P=(p_0,...,p_r),
  Q=(q_0,...,q_s),

and actual endpoint replacement covers

  C_{p_0}=L_P|Q,      V(L_P)=(P-p_0)+b,
  C_{p_r}=R_P|Q,      V(R_P)=(P-p_r)+b,
  C_{q_0}=P|L_Q,      V(L_Q)=(Q-q_0)+b,
  C_{q_s}=P|R_Q,      V(R_Q)=(Q-q_s)+b.

Delete one P-endpoint p in {p_0,p_r} and one Q-endpoint q in {q_0,q_s}. From C_p, delete q from the literal Q rail; from C_q, delete p from the literal P rail. Contiguous deletion of an endpoint preserves tightness, so on the same proper residue W_{p,q}=H-{p,q} there are two literal two-path covers

  T_p | (Q-q),
  (P-p) | U_q.                                      (1)

They are exact: if W_{p,q} were Hamiltonian, that Hamilton path together with the vacuous tight dimer (p,q) would already be a spanning two-cover of H. Thus pc(W_{p,q})=2. Here T_p is the corresponding P-side replacement rail and U_q the corresponding Q-side replacement rail. The same physical hub b is transferred from the first rail in one exact cover to the second rail in the other, while the two punctured source rails remain literal. This is a cover-current one-vertex transfer square, not merely a support comparison.

R410 applies abstractly because the support partitions differ, but its balanced-pair alternative is not the intended consumer here. The value of (1) is the retained source order and the common transferred hub.

### Quiet near-end forms
Assume now that the four source comparisons

  (P,L_P), (P,R_P), (Q,L_Q), (Q,R_Q)

are all R435-quiet. If any is nonquiet, retain that fixed-complement source-relative R435 output instead. By accepted R966 the quiet forms are

  L_P=(b,p_1,...,p_r) or (p_1,b,p_2,...,p_r),
  R_P=(p_0,...,p_{r-1},b) or (p_0,...,p_{r-2},b,p_{r-1}),
  L_Q=(b,q_1,...,q_s) or (q_1,b,q_2,...,q_s),
  R_Q=(q_0,...,q_{s-1},b) or (q_0,...,q_{s-2},b,q_{s-1}).

Call each first form OUTER and each second form INNER.

### Left-P / right-Q cross splice
Write epsilon_P=0 for OUTER L_P and 1 for INNER L_P, and delta_Q=0 for OUTER R_Q and 1 for INNER R_Q. Put

  a=q_{s-1-delta_Q},
  c=p_{1+epsilon_P}.

Take the prefix of R_Q ending at b and the suffix of L_P beginning at b. Their supports are disjoint except for b. The only new turn needed to merge them through b is

  gamma_{P_L,Q_R}=(a,b,c).                         (2)

If gamma is tight, the merged path covers every vertex of H except

  p_0, q_s,
  and additionally p_1 when epsilon_P=1,
  and additionally q_{s-1} when delta_Q=1.         (3)

When epsilon_P+delta_Q<=1, the omitted set in (3) has order two or three and therefore has a tight Hamilton path: dimers are vacuous and every three-set has a tight ordering. Hence a tight gamma would give a spanning two-cover of H. Counterexamplehood forces

  gamma_{P_L,Q_R} bad,
  gamma^*_{P_L,Q_R}=(c,b,a) tight                  (4)

unless BOTH forms are INNER.

If both are INNER, a tight gamma gives a long tight path whose complement is exactly

  X_{P_L,Q_R}={p_0,p_1,q_{s-1},q_s}.              (5)

Thus the exact inner/inner alternative is:

  gamma bad, hence (p_2,b,q_{s-2}) tight by R3; or
  gamma tight and X_{P_L,Q_R} is non-Hamiltonian. (6)

Indeed Hamiltonicity of the four-set in the second branch would again pair with the merged path to two-cover H.

### Right-P / left-Q cross splice
The exact dual uses delta_P=0/1 for OUTER/INNER R_P and epsilon_Q=0/1 for OUTER/INNER L_Q. Put

  a'=p_{r-1-delta_P},
  c'=q_{1+epsilon_Q}.

The prefix of R_P ending at b and suffix of L_Q beginning at b merge with sole new turn

  gamma_{P_R,Q_L}=(a',b,c').                       (7)

Unless both forms are INNER, this turn is bad and

  (c',b,a') tight.                                 (8)

In the double-INNER case, either (8) still holds or gamma is tight and the exact four-vertex complement

  X_{P_R,Q_L}={p_{r-1},p_r,q_0,q_1}               (9)

is non-Hamiltonian.

### Four-complement amplification of the only quiet exception
Suppose one of the double-INNER seams in (6) or (9) is tight and its displayed four-set X is non-Hamiltonian. Let K be the corresponding merged tight path. Then V(H)-V(K)=X has exactly four vertices and pc(H)>2. Accepted R813 therefore applies to this exact K: EVERY gap of K carries a graph-intrinsic Hamilton P4 on a four-set meeting both sides of that gap and at least one vertex of X. In particular both gaps adjacent to the hub b have labelled local P4 outputs.

This does not automatically replace X by one Hamilton rail; R813 explicitly does not synchronize its P4s across gaps. But it means the double-INNER cell is not an anonymous no-P4 remainder: it carries a complete four-complement gap-P4 fan on the same merged path.

### Consequences for the paired hub packet
Outside the four source-relative R435 comparisons, each of the two opposite-role diagonals has the exact alternative

  labelled cross-hub reverse turn
  OR
  double-INNER tight splice + non-Hamiltonian four-complement + R813 gap-P4 fan.

Therefore if not all four endpoint replacement paths are INNER, at least one diagonal necessarily supplies an explicit cross-hub reversal. If both diagonals enter the exceptional branch, all four endpoint replacements are INNER. In a fixed-support K-minimal aligned family, `singleton-paired-hub-r966-energy` then upgrades this to support-wide hub terminal exclusion on all four endpoint-replacement supports and records the maximal endpoint-packet premium N_inner=4.

### Scope
The cross-hub reverse turns in (4) and (8) are current and source-labelled but are not yet a fixed-support R561 certificate. The double-INNER R813 fan is likewise a bounded consumer interface, not closure. No path is reversed, and no Hamilton order is transported between fibers. The next target is to combine the two diagonal reverse turns, or one reverse turn with the opposite R813 fan, into a fixed-support boundary reversal, a legal support transfer lowering total K, or a spanning two-cover.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "related",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R813"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```
