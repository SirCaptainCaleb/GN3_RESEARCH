# Two P4-free four-sets sharing a triangle force a Hamilton P5 in every boundary tournament

**Workspace:** D17
**State:** established
**Key:** `order-free-two-p4free-foursets-force-p5`

**Summary:** Let X=T union {x,y} be a five-vertex Strong Level-(1) boundary tournament, where |T|=3, and suppose both four-sets T+x and T+y are P4-free. Then X is Hamiltonian. Indeed, if X were non-Hamiltonian, accepted R902 would make its comparison orientation acyclic, hence X would be representable by one strict edge order. The two induced K4 edge orders remain P4-free, so accepted edge-ordered lemma R963 applies to their common triangle T and forces an increasing Hamilton P5 on X, contradiction. Thus the edge-order hypothesis in R963 can be removed at order five by the nonHamilton-integrability theorem R902. Equivalently, every five-set containing two P4-free four-subsets with three common vertices has a tight Hamilton P5.

### 1. Statement
Let H be a finite Strong Level-(1) boundary tournament and let

  T={u_0,u_1,u_2}

be a three-vertex set. Let x,y be distinct vertices outside T and put

  X=T union {x,y}.                                        (OF.1)

Assume that neither induced four-set

  T+x,   T+y                                               (OF.2)

supports a tight Hamilton P4. Then X supports a tight Hamilton P5.

No smallest-counterexample, cover, source, or deletion hypothesis is used.

### 2. NonHamilton five-sets are integrable
Suppose for contradiction that X has no tight Hamilton P5.

Accepted R902 applies directly to the five-vertex induced boundary tournament H[X]: every nonHamilton five-vertex boundary tournament has acyclic comparison orientation and hence is representable by a strict total order on the ordinary edges of K_X such that

  (a,b,c) is tight  iff  ab<bc.                           (OF.3)

Fix one such realizing edge order.

Because the realization is exact on every turn of X, the induced edge orders on the two K4s T+x and T+y have no increasing Hamilton P4: an increasing Hamilton P4 there would be exactly a tight Hamilton P4 in H, contrary to (OF.2).

### 3. Apply the edge-ordered common-triangle theorem
Accepted R963 is a pure edge-order theorem. It says that two P4-free edge-ordered K4s sharing one triangle force an increasing Hamilton P5 on their five-vertex union.

Apply R963 to the two induced edge orders on

  T+x,   T+y.                                              (OF.4)

It produces an increasing Hamilton path through all five vertices of X. By the realizing dictionary (OF.3), that vertex order is a tight Hamilton P5 of H[X], contradicting the assumed nonHamiltonicity of X.

Therefore X is Hamiltonian.

### 4. Useful contrapositive and role in the curvature program
The theorem may be used in either of the equivalent forms

  TWO P4-FREE K4s WITH A COMMON TRIANGLE  =>  P5,          (OF.5)

or, inside any nonHamilton five-set,

  for any two four-subsets sharing three vertices,
  at least one of them supports a Hamilton P4.             (OF.6)

The point is that R963's numerical edge-order proof is not restricted to the globally edge-orderable branch when the ambient support has order five. If the five-set were nonintegrable, accepted R902 would already make it Hamiltonian. Hence integrable and nonintegrable five-cells are consumed by the same conclusion.

This is a local compiler only. A Hamilton P5 on X need not by itself close a larger counterexample; downstream applications must retain the physical five-set and its literal complement geometry.

Status: complete internal working mathematics, unreviewed exposition. The proof uses only accepted R902 and R963.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R902"
    },
    {
        "relation": "dependency",
        "revision_id": "R963"
    }
]
```