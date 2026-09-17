# A retained tight path turns complement component-drop into a current crossing portal

**Workspace:** D17
**State:** established
**Key:** `retained-path-complement-crossing-portal`

**Summary:** In a smallest counterexample, any proper tight path K has an exact two-covered complement W and restoring K gives a minimum spanning three-cover by R4/P601. If W also carries a literal c-cover R with c>2, then every exact two-cover T of W selects a physical adjacency joining two distinct R-components by the first step of R159/P555. The useful output is the ancestry-bearing cell (K,R,T,xy); R176/payment is optional downstream, not part of the representation.

### 1. Retained-path complement exactness
Let H be a smallest Strong Level-(1) counterexample and let K be any nonempty proper graph-intrinsic tight path. Put W=H-V(K). Suppose W also has a literal c-cover

  R=R_1|...|R_c,   c>2.

Apply accepted R4 through its selected proof P601. Because K is a proper tight path, W cannot be Hamiltonian: a Hamilton path of W together with K would two-cover H. Minimality gives pc(W)<=2, hence pc(W)=2. Choose any exact two-cover

  T=T_1|T_2.

The same proof preserves K literally: K|T_1|T_2 is a minimum spanning three-cover of H. Thus the complementary path K is current data, not an anonymous spare vertex or discarded puncture.

### 2. The component drop has a current selected crossing before payment
Use only the first, purely combinatorial step of accepted R159/P555. If no selected adjacent state of T joined two distinct R-components, then every T-rail would lie wholly inside one R-component: along a T-path, the first departure from one R-component to another would itself be such a selected crossing. Since the c nonempty R-components partition W and the two T-rails cover W, every R-component would have to contain a distinct T-component, forcing 2>=c, contradiction.

Therefore T selects an actual directed state

  x -> y

whose endpoints lie in two distinct components of R. Retain the physical vertices x,y, their selected orientation and position in the actual T-rail, the complete exact cover T, the c-cover R with the two crossed components identified, and the complementary tight path K. The minimum spanning three-cover K|T remains simultaneously available.

This is exactly the current-state core that P555 subsequently feeds to R176. For proof-aware use in D17, stop before that downstream conversion unless the balanced-pair output itself is the intended consumer.

### 3. Scope
The portal does not assert that the crossing is unique, boundary-adjacent, reversible, or immediately closing. It does not assert that different exact complement covers select the same crossing. Its gain is preservation: any structured component-drop in the complement of a retained path automatically has an exact current representative and a selected cross-component adjacency while the retained path and the corresponding minimum spanning three-cover remain live. In the frequent c=3 case the complete current object is therefore (K; R_1|R_2|R_3; T_1|T_2; x->y), rather than an anonymous R159 descendant.

## References

```json
[
    {"relation":"dependency","revision_id":"R4"},
    {"relation":"dependency","revision_id":"R159"}
]
```
