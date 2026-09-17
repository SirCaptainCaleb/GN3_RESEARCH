# A Hamilton five-rail supplies three reciprocal replacements per critical vertex

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-six-five-reciprocal-density-threshold`

**Summary:** Let a smallest counterexample split V(H)=Omega disjoint_union Q, where Omega is non-Hamiltonian deletion-Hamiltonian and Q is a Hamilton five-set, with no restriction on |Omega|. For every y in Omega, Q+y is non-Hamiltonian because it would pair with an actual Hamilton puncture Omega-y and close H. Accepted R195 applied proof-aware to the six-set Q+y therefore gives at least three q in Q for which Q-q+y is Hamiltonian. Thus the reciprocal replacement family C has at least 3|Omega| cells in the |Omega| by 5 exchange matrix. If A(y,q) records Hamiltonicity of Omega-y+q, then A and C are disjoint in a counterexample, since a common cell is a pair of complementary Hamilton supports spanning H. Hence |A|<=2|Omega|; contrapositively any 2|Omega|+1 active-side replacement cells force closure. The former six-by-five threshold |C|>=18 and |A|>=13 is the |Omega|=6 corollary, directly consuming the two-shell critical-block output SV20681. This is the complement-size-five dual to the live fixed-six-core arbitrary-complement density program.

### 1. Fixed-complement setup with a five-vertex Hamilton rail
Let H be a hypothetical smallest counterexample and suppose

  V(H)=Omega disjoint_union V(Q),
  |Q|=5,

where Q is a retained literal Hamilton tight path and Omega is non-Hamiltonian but deletion-Hamiltonian. Put r=|Omega|; no assumption r=6 is needed. For every y in Omega choose and retain an actual Hamilton path P_y on Omega-{y}.

For y in Omega and q in V(Q), define reciprocal replacement predicates

  A(y,q):  (Omega-{y}) union {q} is Hamiltonian,
  C(y,q):  (V(Q)-{q}) union {y} is Hamiltonian.             (F5.1)

The two supports in one cell are disjoint and partition V(H). Hence

  A(y,q) and C(y,q)  =>  H has a spanning two-cover.         (F5.2)

In a surviving counterexample the two incidence families are therefore disjoint.

### 2. R195 forces three reciprocal cells in every row
Fix y in Omega. The six-set E=V(Q) union {y} is non-Hamiltonian. Indeed, if E had a Hamilton path K_y, then the retained puncture path P_y on Omega-{y} and K_y would be vertex-disjoint and would partition V(H), giving a spanning two-cover.

Apply accepted R195 to this physical six-set. Its proof is a three-set hitting argument: every three-set T in E has a complementary tight trimer, and R146 forces one of the three associated five-set punctures to be Hamiltonian; hence at most two punctures of E are non-Hamiltonian and at least four are Hamiltonian.

Deleting y gives exactly the already-retained Hamilton support V(Q). Therefore among the five remaining deletion labels q in Q, at least three satisfy

  Q-{q}+{y} Hamiltonian.                                  (F5.3)

Retain an actual Hamilton path K_{y,q} for each such good reciprocal cell. These are physical support witnesses; no common endpoint pair or common Hamilton order is asserted.

Since y was arbitrary, writing C for all good reciprocal cells gives

  |C| >= 3r.                                              (F5.4)

Thus a Hamilton five-rail contributes reciprocal replacement density at least 3/5 against EVERY deletion-Hamiltonian critical block, regardless of the order of that block.

### 3. The active-side threshold is only two cells per critical vertex
The exchange matrix has 5r cells. By (F5.2), a counterexample has A cap C empty. Hence

  |A| <= 5r-|C| <= 2r.                                   (F5.5)

Equivalently,

  |A| >= 2r+1  =>  A cap C nonempty  =>  H is two-covered. (F5.6)

This is deliberately asymmetric. The reciprocal Q-side density is free from R195; an absorption argument only has to manufacture active-side Hamilton replacements in more than two cells per critical vertex on average, or directly hit one of the retained row-wise sets C_y.

### 4. Six-by-five corollary and the order-eleven feeder
When r=6, the matrix has thirty cells and

  |C|>=18,  |A|<=12 in a counterexample.                  (F5.7)

So thirteen active-side replacement supports force closure. The equality branch of `singleton-universal-core-two-shell-r966-criticalblock` produces exactly a non-Hamiltonian deletion-Hamiltonian six-block with a Hamilton five-vertex complement, and therefore enters this corollary immediately.

The C-side count embedded in `singleton-deep-p5-order11-reciprocal-exchange-closure` is another instance of the same R195 mechanism. The present statement extracts the mechanism from short-G1 geometry and makes it available to arbitrary fixed-complement critical blocks whenever the complementary rail has order five.

### 5. Strategic duality and fence
The live R1 density program fixes a six-vertex short-G1 core and seeks enough reciprocal support as the complement order grows. The present theorem is its geometric dual boundary case: the Hamilton complement is fixed at order five while the deletion-Hamiltonian critical block may have arbitrary order. It therefore belongs naturally between the reciprocal-density and CBCA fronts without replacing either.

No lower bound on A is claimed here. No anchored-triangle, transfer-chain, or endpoint-role statement is used. The only theorem dependency is accepted R195, applied with its proof mechanism reconstructed above. The short-G1 and two-shell section versions are retained solely as provenance for the motivating applications.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R195"
    }
]
```
