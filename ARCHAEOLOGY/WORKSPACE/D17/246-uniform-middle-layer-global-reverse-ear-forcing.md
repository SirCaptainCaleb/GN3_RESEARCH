# For k at least five, every Arm-M endpoint system is Reverse-Ear active

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-global-reverse-ear-forcing`

**Summary:** In accepted R927 Arm M with k>=5, form the complete all-endpoint incidence graph and choose an inclusion-minimal Hall-deficient family F. Assume all path comparisons used below are R435-quiet. Same-support R435 monotonicity then makes every Hamilton k-support in F have one unique oriented Hamilton word, hence left degree exactly two. At each right core R, trimming the exposed completion from its incident support words gives one common Hamilton order K_R; opposite completion roles would concatenate through K_R to a forbidden (k+1)-path, so all completions at R have one role and one common opposite endpoint p_R. Along every support edge the two endpoint cores therefore satisfy R-p_R=R'-p_R'. Connectedness propagates one fixed (k-2)-set M and one literal Hamilton order P on M; the endpoint-core roles alternate, and every circuit edge has word (a,P,b) after orienting its two role classes. Choose any such edge ab and any c outside M+a+b. Uniformity Hamiltonizes M+a+c and M+b+c. R435-quietness makes these paths insert c into (a,P) and (P,b). Avoiding a forbidden (k+1)-path after appending b traps c in the last two insertion slots of the first path; avoiding one after prepending a traps c in the first two slots of the second. Trimming a and b gives two Hamilton paths on the identical support M+c with c respectively in positions {s,s+1} and {1,2}, where s=|M|=k-2>=3. They cannot be the same word, so R435 must fire. Thus every Arm-M system with k>=5 emits explicit R435 reversal/reverse-trimer/proper-cycle geometry. This bypasses the degree-three/spindle/universal-core router as an entrance to the global maximum-three-forest program.

### 1. Complete endpoint incidence and the quietness hypothesis
Assume accepted R927 Arm M:

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian,

and suppose k>=5.

Form the COMPLETE all-endpoint incidence graph B exactly as in the current uniform-layer Hall setup: every k-set is a left vertex, and a left support S is joined to the right core R=S-{x} whenever some actual Hamilton path on S exposes x as a physical endpoint. Since

  binom(2k+1,k) > binom(2k+1,k-1),

the full left family is Hall-deficient. Choose an inclusion-minimal Hall-deficient family F and put N=N(F). Accepted R934 gives

  |N|=|F|-1,

and, crucially, B[F,N] is connected.

Assume for contradiction that every application of accepted R435 made below is quiet: no adjacent reversal, reverse trimer, or proper tight cycle is emitted. We show that this global quietness is impossible.

### 2. R435-quietness makes every left Hamilton word unique
Fix S in F and let P,Q be two actual Hamilton paths on S. Apply R435 with ancestral path P and comparison path Q. Since Q meets every vertex of P, quietness says that the P-vertices occur along Q in increasing P-order. The supports are identical, so there is no room for any extra vertex between them. Hence

  Q=P

as literal oriented vertex words.

Thus every S in F has one unique oriented Hamilton word. Its only endpoint-deletion neighbors are obtained by deleting its two physical endpoints, so

  deg_B(S)=2.                                             (RE.1)

### 3. Every right core has one order, one role, and one physical port
Fix R in N. For every incident support S_x=R+{x}, retain its unique Hamilton word P_x exposing x. Delete the endpoint x from P_x. This leaves a Hamilton path K_x on the common support R.

For two incident labels x,y, compare K_x and K_y by R435. Quietness and equal support force K_x=K_y. Write the common literal core order as K_R.

Because x is an endpoint of P_x, the unique support word is either (x,K_R) or (K_R,x). All incident completions must use the SAME one of these two roles. Indeed, if x occurred before K_R and y after K_R, then (x,K_R,y) would be a tight path on the forbidden (k+1)-support R+{x,y}.

Let p_R be the endpoint of K_R opposite the completion side. Every incident support word therefore has endpoint pair

  {x,p_R}.                                                (RE.2)

### 4. One fixed (k-2)-core propagates through the whole Hall circuit
Let S be a left support with its two right neighbors R,R'. Write x=S-R. By (RE.2), the unique word on S has endpoints x and p_R. By (RE.1), its two endpoint-deletion cores are exactly R=S-{x} and S-{p_R}. Hence R'=S-{p_R}.

From the R' side, the completion is p_R. Applying (RE.2) there to the same unique support word shows that its other endpoint is p_{R'}=x. Consequently

  R-{p_R}=R'-{p_{R'}}=S-{x,p_R}.                         (RE.3)

Since B[F,N] is connected, (RE.3) propagates along every support edge. There is therefore one fixed set M of order k-2 such that

  R=M+{p_R}                                               (RE.4)

for every R in N.

Suppress each left support to an edge between its two right cores, and label the right core M+{a} simply by a. Along an edge ab the unique support is M+{a,b}. The completion roles at a and b are opposite, because the same unique Hamilton word cannot have both a and b at the same end. Thus the suppressed graph is bipartite by endpoint role.

Choose the orientation of the two role classes so that for an edge ab the completion b is terminal at core a and the completion a is initial at core b. Then the unique support word has the form

  (a,P_ab,b),                                             (RE.5)

where P_ab is a Hamilton order of M. Its trims give K_a=(a,P_ab) and K_b=(P_ab,b). At a second edge incident with a, K_a is unchanged, so the M-order is again P_ab. Connectedness propagates this equality across the whole circuit. Hence there is one literal order

  P=(m_1,...,m_s),  s=k-2,                               (RE.6)

of M such that every oriented circuit edge has word

  (a,P,b).                                                (RE.7)

### 5. A third label is trapped at opposite ends
Choose any circuit edge ab and orient it as in (RE.7), so (a,m_1,...,m_s,b) is tight. Because |V(H)-M|=k+3, choose a physical label c notin M union {a,b}.

Uniformity gives an actual Hamilton path Q_a on M+{a,c}. Compare Q_a with K_a=(a,P). Quiet R435 says that the K_a-vertices occur along Q_a in exactly that order. Since c is the only additional vertex, Q_a is obtained by inserting c into the literal word (a,P).

If c is inserted anywhere except between m_{s-1},m_s or after m_s, then Q_a still ends with the consecutive pair m_{s-1},m_s. Appending b uses the tight inherited turn (m_{s-1},m_s,b) from (RE.7), and therefore produces a forbidden Hamilton path on the (k+1)-set M+{a,b,c}. Hence c must occupy one of those final two insertion slots. In particular a is the first endpoint of Q_a. Deleting a gives a Hamilton path T_a on M+c in which c occupies position

  s or s+1.                                               (RE.8)

Dually, take an actual Hamilton path Q_b on M+{b,c} and compare it with K_b=(P,b). Quietness makes Q_b an insertion of c into (P,b). If c is inserted anywhere except before m_1 or between m_1,m_2, then Q_b begins with m_1,m_2. Prepending a uses the tight inherited turn (a,m_1,m_2) from (RE.7), again producing a forbidden Hamilton path on M+{a,b,c}. Therefore c occupies one of the first two insertion slots. The vertex b is the last endpoint, and deleting b gives a Hamilton path T_b on M+c in which c occupies position

  1 or 2.                                                 (RE.9)

### 6. Opposite-end insertion clash forces R435
The paths T_a and T_b are Hamilton paths on the SAME support M+c. Under our global quietness hypothesis, R435 therefore forces them to be the identical literal word.

But s=|M|=k-2>=3. The possible positions of c in (RE.8) are {s,s+1}, while those in (RE.9) are {1,2}. These sets are disjoint. Thus T_a and T_b cannot be the same word. This contradiction proves that at least one of the R435 comparisons above must emit explicit Reverse-Ear geometry.

### 7. Parent consequence
Therefore every accepted R927 Arm-M system with k>=5 is R435-active. More precisely, the complete endpoint system necessarily yields at least one graph-intrinsic R435 output: an adjacent selected reversal, a reverse tight trimer, or a proper tight cycle.

This is a direct global entrance into the existing maximum-three-forest / movable-break / selected-reversal program. It does not need a degree-three completion core, the complementary hexagon, the selected-reversal triangle, a universal one-extension four-core, or the three-port spindle.

The result is a parent reduction, not O4 closure: R435 geometry still requires its global forest consumer. For k=5 the entire Arm-M case is already eliminated canonically by accepted R957; the new value is the general k>=6 entrance and, in particular, a shorter route than the k>=8 spindle/C4 compression.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R934"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```