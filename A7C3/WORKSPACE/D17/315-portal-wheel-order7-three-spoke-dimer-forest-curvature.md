# The order-seven necklace contains an asymmetric P5-dimer forest and unavoidable good-row Reverse-Ear curvature

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-order7-three-spoke-dimer-forest-curvature`

**Summary:** In the order-seven coherent residue Omega=K+{y,z} of SV64567, color the five K-roots by the orientation of the outer-pair turn on {y,d,z}. Three roots share one orientation. The three-spoke P5 lemma of SV58280 gives a Hamilton P5 S on y,z and those three roots, with y,z internal in its explicit order. The two unused roots e,f form a dimer, so S|(e,f)|Q is a literal spanning maximum three-forest. Goodness gives S+e=Omega-f and S+f=Omega-e Hamiltonian, while counterexamplehood forces Q+e and Q+f non-Hamiltonian; hence both dimer vertices witness both reverse boundary dimers of Q. Moreover the actual good puncture paths P_e and P_f have physical endpoints y,z, whereas y,z are internal in S. Therefore neither comparison S versus P_e nor S versus P_f can be R435-quiet. Each emits a selected reversal, reverse trimer, or proper cycle coupled to actual maximum-three-forest representatives with Q fixed. Thus the order-seven necklace is not a terminal fixed-complement shell: it canonically enters a dimer-root maximum-forest state with a bilateral two-probe wall and unavoidable Reverse-Ear curvature.


### 1. Order-seven two-ended coordinates
Retain the bounded residue of SV64567:

  V(H)=Omega disjoint_union V(Q),
  Omega=V(K) disjoint_union {y,z},

where K is a retained Hamilton P5, Q is a literal Hamilton path, Omega is non-Hamiltonian, and for every d in V(K) there is an actual Hamilton puncture path P_d on Omega-d whose two physical endpoints are exactly y,z. Thus every d in K is GOOD:

  Omega-d is Hamiltonian.                                  (OD.1)

We do not assume the bad-pair comparison {y,z} is quiet, and we do not use the overlapping-critical-block promotion. The argument below is already present in the raw two-ended necklace.

### 2. Three like-oriented roots make a second Hamilton P5 with the bad labels internal
For each d in K, boundary antisymmetry chooses exactly one of

  (y,d,z),   (z,d,y)                                       (OD.2)

as tight. Among the five roots, at least three, say r1,r2,r3, have the same orientation. After exchanging y,z if necessary,

  (y,r_i,z) is tight, i=1,2,3.                             (OD.3)

Apply the pure THREE-SPOKE P5 lemma from SV58280 to the outer pair y,z and the three middles r1,r2,r3. Its proof is order-explicit: after relabelling r1,r2,r3 it supplies the Hamilton order

  S=(r1,y,r2,z,r3).                                        (OD.4)

In particular the two bad labels y,z are INTERNAL vertices of this retained P5 order.

Let

  {e,f}=V(K)-{r1,r2,r3}.                                   (OD.5)

The two-set {e,f} is a literal dimer path. Hence

  F_0 = S | (e,f) | Q                                      (OD.6)

is a literal spanning three-path cover of H. Since H is a smallest counterexample and pc(H)=3 by accepted R4, F_0 is an actual maximum spanning three-forest.

### 3. The dimer extends the P5 side and is blocked from the Q side
Because e and f are good roots,

  S+e = Omega-f is Hamiltonian,
  S+f = Omega-e is Hamiltonian.                            (OD.7)

Counterexamplehood forces the reciprocal Q-extensions to fail. Indeed, if Q+e were Hamiltonian, then the two disjoint Hamilton supports

  (Q+e)  and  (S+f)=Omega-e

would span H, a contradiction. Thus Q+e is non-Hamiltonian; symmetrically Q+f is non-Hamiltonian:

  Q+e and Q+f are both non-Hamiltonian.                    (OD.8)

Accepted R533 gives |V(H)|>10, while |Omega|=7, so |Q|>=4. Write

  Q=(q0,q1,...,qm),  m>=3.

The two direct endpoint attachments of e to Q are therefore bad, and R3 gives

  (q1,q0,e),   (e,qm,q_{m-1}) tight.                      (OD.9)

The same holds for f:

  (q1,q0,f),   (f,qm,q_{m-1}) tight.                      (OD.10)

Thus the literal dimer rail {e,f} in F_0 is an exact BILATERAL TWO-PROBE WALL against the same Hamilton rail Q: both dimer vertices tail-witness the reverse initial dimer and head-witness the reverse terminal dimer. Simultaneously, each dimer vertex Hamilton-extends the opposite P5 rail S by OD.7. The 2-by-2 extension pattern is therefore completely asymmetric rather than an arbitrary Hall residue.

### 4. The actual good rows cannot be Reverse-Ear quiet against S
Consider the actual good row for e:

  H-e = P_e | Q,                                          (OD.11)

where P_e is Hamiltonian on Omega-e=S+f and has physical endpoints exactly y,z. Adjoin singleton e to regard

  F_e = P_e | {e} | Q                                     (OD.12)

as another actual maximum spanning three-forest. Likewise

  F_f = P_f | {f} | Q.                                    (OD.13)

Compare the retained path S of OD.4 with P_e by accepted R435. If this comparison were R435-quiet, the S-vertices would occur along P_e in increasing S-order. But y and z occupy the internal positions 2 and 4 of the S-word

  r1, y, r2, z, r3,

whereas P_e has y and z as its two physical path endpoints. If P_e starts at y, then y is encountered before r1 although r1 precedes y in S. If P_e starts at z, then z is encountered before at least one earlier S-contact. Either way the S-contact order is not increasing. Therefore the comparison is necessarily R435-NONQUIET.

Hence S versus P_e emits one of the exact R435 outputs:

- the reversal of an adjacent selected S-state in P_e;
- a tight reverse trimer at an S/P_e seam;
- a vertex-simple proper tight cycle.                      (OD.14)

The same argument applies independently to P_f. Thus the one P5-dimer state F_0 has TWO neighboring actual good-row maximum forests F_e,F_f for which the common S-cell is necessarily Reverse-Ear active.

For an adjacent selected reversal, the old S-state is literally selected in F_0 and its reverse is literally selected in the actual singleton-row forest F_e or F_f. A reverse trimer is a proper graph-intrinsic tight path and currentizes by R4; a proper cycle enters the existing movable-break maximum-forest family. Therefore OD.14 is already coupled to actual/closed maximum-three-forest dynamics with the literal complement Q retained.

### 5. G24 consequence and fence
The order-seven necklace is therefore not a terminal support-only fixed-complement atom. Without using the bad singleton rows at all, its five good punctures force the sharper common parent

  asymmetric P5 | dimer | Q maximum forest
  + bilateral two-probe wall on the dimer/Q side
  + unavoidable R435 curvature toward BOTH dimer-root singleton rows.  (OD.15)

This is a genuine kernel shrink: the seven-vertex puncture necklace has been replaced by one short-rail maximum-forest gate with two forced neighboring curvature representatives. The induced seven-vertex fence SV64875 is compatible with this result because it does not include the external Hamilton rail Q or maximum-forest currentization.

No claim is made that OD.15 by itself closes H, lowers epsilon_*, or extinguishes global maximum-three-forest holonomy. In particular a bare R435 output is not counted as Morse progress. The next consumer should exploit the special dimer gate and the simultaneous two-probe wall, or combine this forest entrance with the bad-row common-center anchor star SV66139.


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
        "revision_id": "R533"
    }
]
```