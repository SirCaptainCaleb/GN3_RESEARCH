# A seven-vertex puncture-density certificate forces reciprocal exchange and closes the order-eleven short G1 cell

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-order11-reciprocal-exchange-closure`

**Summary:** In the short G1 six-vertex universe U={s,q,t,p,u,v} with |B|=5, a finite exact-reversal calculation on U+b shows that for every exterior b at least three of the six supports U-x+b are Hamiltonian. The calculation uses only the retained short-G1 U-geometry: 105 reversal-pair variables on seven vertices, the 19 forced tight turns obtained from SV16094 plus the two one-hole reversals already reconstructed in SV16347, non-Hamiltonicity of U, and for each chosen four-set T subset U the hypothesis that U-x+b is non-Hamiltonian for all x in T. Each of the 15 choices of T gives a deterministic DPLL UNSAT instance; the aggregate certificate visited 59 nodes with maximum depth 12. Separately, for every x in U, SV16094 gives B+x non-Hamiltonian while B is Hamiltonian, so accepted R195 forces at least three b with B-b+x Hamiltonian. Thus in the 6x5 reciprocal incidence matrix A_{xb}=[U-x+b Hamiltonian], C_{xb}=[B-b+x Hamiltonian], one has |A|>=15 and |C|>=18 in 30 cells. Hence some cell lies in both families, and the two complementary Hamilton supports U-x+b and B-b+x partition H, giving a spanning two-cover. Therefore the order-eleven short-G1 cell is closed conditional only on the finite seven-vertex certificate. The computational lemma is retained as a target for human reconstruction: identify the rotation/reversal structure forcing four bad punctures to conflict, with the expectation that this structure may generalize beyond order seven.

### 1. Short-G1 setup and the reciprocal supports
Retain the accepted exact short-G1 universe `singleton-deep-p5-short-r961-currentization` SV16094. Thus

  U={s,q,t,p,u,v}

is a non-Hamiltonian six-set, B is a literal Hamilton complement, every puncture U-x is Hamiltonian, and

  B+x is non-Hamiltonian for every x in U.                    (RX.1)

Now specialize to the order-eleven laboratory |B|=5. For x in U and b in B define two complementary five/six-support predicates

  A(x,b): U-x+b is Hamiltonian,
  C(x,b): B-b+x is Hamiltonian.                               (RX.2)

The supports in A(x,b) and C(x,b) are disjoint and partition V(H). Hence if both predicates hold for one cell (x,b), their witnessing Hamilton paths form a spanning two-cover of H. A hypothetical surviving counterexample must therefore make the two incidence families disjoint.

### 2. Nineteen pinned short-G1 turns on U
The exact SV16094 geometry supplies the five cycle turns

  (s,q,t),(q,t,p),(t,p,u),(p,u,s),(u,s,q),

the reverse-cycle signs through v

  (v,q,s),(q,s,v),(v,t,q),(t,q,v),(v,p,t),(p,t,v),
  (v,u,p),(u,p,v),(v,s,u),(s,u,v),

and the retained H-t path turns

  (s,v,u),(v,u,p),(u,p,q).

After removing the duplicate (v,u,p), these give seventeen distinct pinned tight turns. Two further turns follow by the same one-hole reversal calculation reconstructed in SV16347. If (p,q,t) were tight then the actual path (s,v,u,p,q,t) would Hamiltonize U, so non-Hamiltonicity of U and R3 force

  (t,q,p) tight.                                             (RX.3)

Then the proposal (s,u,v,t,q,p) has all turns certified except possibly (u,v,t). If that turn were tight U would again be Hamiltonian, so R3 forces

  (t,v,u) tight.                                             (RX.4)

Thus the local seven-vertex calculation below pins nineteen distinct turns on U.

### 3. Computational seven-vertex puncture-density lemma
Fix one new vertex b outside U. The following local statement has been exhaustively verified under exact reversal:

**SEVEN-VERTEX SHORT-G1 PUNCTURE DENSITY.** Among the six supports U-x+b, x in U, at least three are Hamiltonian. Equivalently, no four distinct labels x_1,x_2,x_3,x_4 in U can all have U-x_i+b non-Hamiltonian.

The verification is finite and completely explicit. Encode each complete-reversal pair {(a,c,d),(d,c,a)} of ordered triples on the seven vertices U union {b} by one Boolean variable. There are 7P3/2=105 variables. Use the lexicographically smaller ordered triple in each reversal pair as canonical representative and order variables lexicographically. A turn literal is the variable or its negation according to whether the displayed turn is canonical or reversed.

Add unit clauses for the nineteen tight turns of Section 2. Add, for every one of the 6!=720 vertex orders of U, the four-literal clause saying that not all four consecutive turns are tight; this encodes the already-known non-Hamiltonicity of U. For a fixed four-subset T subset U, and for every x in T and every one of the 6!=720 orders of the six-set U-x+b, add the analogous four-literal non-Hamiltonicity clause. Thus each four-bad instance has

  105 Boolean variables,
  19 unit clauses,
  720 clauses forbidding a Hamilton P6 on U,
  4*720 clauses forbidding a Hamilton P6 on U-x+b for x in T,

for 3619 clauses total.

Run deterministic DPLL: repeatedly unit-propagate; if several unit clauses are present, process the smallest-index variable first; on a branch choose the smallest-index unassigned variable occurring in a remaining clause and branch False before True. All C(6,4)=15 four-subset instances are UNSAT. The regenerated aggregate search visits 59 DPLL nodes, with maximum branch depth 12.

This is computational/certificate evidence, not yet a human structural proof. The local theorem should be regarded as established working mathematics pending independent exact review or replacement by a conceptual proof.

### 4. Reciprocal incidence forces a spanning two-cover
For each fixed b in B, Section 3 gives at least three x in U with A(x,b). Since |B|=5,

  |A| >= 5*3 = 15.                                         (RX.5)

For each fixed x in U, apply accepted R195 to the non-Hamiltonian six-set B+x from (RX.1). The proof mechanism of R195 says that at least four singleton punctures of any six-set are Hamiltonian. Deleting x gives B itself, which is already Hamiltonian. Therefore at least three of the five remaining punctures are Hamiltonian:

  #{b in B : B-b+x Hamiltonian} >= 3.                       (RX.6)

Hence

  |C| >= 6*3 = 18.                                         (RX.7)

But A and C are subsets of the same 6*5=30 reciprocal cells. Since

  |A|+|C| >= 33 > 30,

they intersect. Choose (x,b) in A cap C and retain actual Hamilton paths on

  U-x+b,
  B-b+x.                                                    (RX.8)

These supports are disjoint and their union is V(H), so (RX.8) is a spanning two-cover of H, contradiction. Thus the order-eleven short-G1 configuration cannot survive.

### 5. Human-proof target and possible higher-order mechanism
The counting closure in Section 4 is conceptual; the only finite black box is Section 3. The unusually tiny DPLL search strongly suggests that the local lemma is driven by a short rotation/reversal obstruction rather than accidental seven-vertex enumeration. The next research target is therefore to HUMANIZE the certificate.

For four hypothesized bad punctures x, each non-Hamiltonian U-x+b forbids every insertion/rotation of b into the many Hamilton five-paths already forced inside U-x. Exact reversal turns each failed insertion into a directed local constraint involving b. The nineteen U-turns form an overlapping comparison-cycle skeleton, so constraints coming from four different punctures should collide on a shared middle vertex or shared boundary dimer and either reconstruct a Hamilton P6 on one punctured extension or Hamiltonize U itself.

The desired replacement theorem is not merely the seven-vertex numerical bound. Seek a structural principle of the form: a deletion-Hamiltonian non-Hamiltonian core carrying a sufficiently connected cyclic comparison skeleton cannot have one exterior vertex simultaneously block more than half of its puncture extensions. Such a statement would turn the finite density 3-of-6 into a higher-order complementary-exchange engine. No such general theorem is claimed here.

### 6. Status
The reciprocal incidence deduction from the seven-vertex density statement and accepted R195 is a complete literal closure argument. The seven-vertex density statement is currently supported by the explicit deterministic finite UNSAT certificate above, not by a human proof. Preserve this distinction. No claim is made that the same density bound holds for arbitrary six-vertex deletion-Hamiltonian cores or at higher order without the short-G1 comparison skeleton.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R195"
    }
]
```
