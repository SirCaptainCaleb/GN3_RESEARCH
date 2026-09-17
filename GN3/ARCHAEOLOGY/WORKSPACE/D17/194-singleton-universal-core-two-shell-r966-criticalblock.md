# Two universal-core donor shells collapse to R966 or a fixed-complement critical six-block

**Workspace:** D17
**State:** working
**Key:** `singleton-universal-core-two-shell-r966-criticalblock`

**Summary:** In the order-eleven short-G1 universal-core shell, compare the audited cores X_sq={t,p,u,v} and X_su={q,t,p,v} on the common five-vertex donor rail B. A direct seven-vertex exact-reversal computation shows that if one physical B-pair {a,b} is donor-good in both shells, then at least one of the non-Hamiltonian six-sets X_sq+{a,b}, X_su+{a,b} has an R966 endpoint-replacement trigger; this finite step is computational evidence only, not yet canonically certified. Symbolically, if no B-pair is donor-good in both shells, then the two donor graphs restricted to B are complementary C5s. Since every B-vertex has full donor degree at least four and only two deleted labels are available outside B, each B-vertex is adjacent to both deleted labels in each shell. Hence B+s is non-Hamiltonian but deletion-Hamiltonian, while U-s is Hamiltonian: the equality branch lands exactly in the fixed-complement critical-block parent.

### 1. Two audited donor shells
Retain the order-eleven universal-core shell SV17264 and the audited short-G1 pair-support data SV16347. Use the two cores

  X_sq={t,p,u,v},   D_sq={s,q},
  X_su={q,t,p,v},   D_su={s,u},

with common literal Hamilton donor rail B of order five. Let G_sq be the donor graph on B union {s,q} and G_su the donor graph on B union {s,u}; as in SV17264 every vertex of either donor graph has degree at least four.

### 2. Shared B-donor edge: finite R966 compression
Fix a physical pair {a,b} subset B and suppose it is donor-good in both shells. Then

  Omega_sq=X_sq union {a,b},
  Omega_su=X_su union {a,b}

are non-Hamiltonian, while deleting a or b from either six-set is Hamiltonian. R195 supplies at least two further Hamilton core punctures in each six-set.

A direct exact-reversal finite computation on the seven labels {q,t,p,u,v,a,b}, retaining the literal Hamilton/core-star turns from SV16347, was run with exact Hamilton-puncture status variables and with every possible R966 endpoint-replacement trigger forbidden. The resulting 1557-binary, 10105-constraint MILP is infeasible under scipy.optimize.milp/HiGHS. Thus the current computational conclusion is:

  shared B-donor edge => an R966 trigger in Omega_sq or Omega_su.

This is NOT yet a canonically certified theorem. It should be independently reconstructed, preferably by a small deterministic SAT/DPLL certificate or a symbolic endpoint-role argument, before theorem-level use.

### 3. No shared B-donor edge forces complementary C5s
Now assume the two restricted donor graphs G_sq[B] and G_su[B] are edge-disjoint. Each b in B has at most two donor neighbors outside B in either shell and total degree at least four, hence

  deg_{G_sq[B]}(b)>=2,   deg_{G_su[B]}(b)>=2.

Because K_B has degree four and the restricted edge sets are disjoint, equality holds everywhere: both restricted graphs are 2-regular and partition E(K_5). Therefore each is a 5-cycle and they are complementary C5s.

### 4. Equality manufactures a full fixed-complement critical block
Fix b in B. In G_sq, b has exactly two neighbors inside B and still needs total degree at least four. The only two outside labels are s,q, so both bs and bq are donor-good. In particular bq donor-good means

  (B-{b}) union {s}

is Hamiltonian. This holds for every b in B. Deleting s from B+s leaves the literal Hamilton path B. On the other hand the universal-core shell for X_sq says

  B+s = (B union {s,q})-{q}

is non-Hamiltonian. Hence

  Omega=B+s

is a non-Hamiltonian deletion-Hamiltonian six-vertex block. Its complement in H is U-s, Hamiltonian by the accepted short-G1 puncture theorem SV16094. Thus the no-shared-edge branch lands exactly in the fixed-complement critical-block setting.

### 5. Consequence and next consumer
The two-shell order-eleven lane is compressed to two global outputs:

  (A) a shared B-donor edge and a computationally forced R966 endpoint-replacement trigger on one named six-set; or
  (B) complementary donor C5s and the full fixed-complement critical block (B+s)|(U-s).

The finite implication in (A) remains uncertified. The symbolic implication in (B) is exact from the retained shell. Neither branch is claimed to close H. The intended moonshot consumer is one parent absorbing fixed-complement R966/critical-block geometry rather than further donor-edge taxonomy.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R195"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```
