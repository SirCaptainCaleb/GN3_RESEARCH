# A universal one-extension four-set creates singleton and pair-deletion universal crossing walls

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-singleton-and-pair-crossing-wall`

**Summary:** If S is a four-set in a smallest counterexample such that S+d is Hamiltonian for every exterior d, then accepted R508 gives a universal crossing wall on every exterior singleton deletion: every exact cover of H-d selects an S|(Y-d) edge. If S itself is non-Hamiltonian, R560 rules out a unique transition, so every exact H-d cover has at least two such crossings. Moreover for every core label s and exterior d, every exact cover of H-{s,d} crosses the surviving trimer (S-s)|(Y-d), since the deleted pair together with that trimer is exactly the Hamilton five-set S+d. Thus a universal one-extension four-set creates a dense family of singleton and pair-deletion universal crossing fibers, strengthening the bounded pair-core holonomy picture. Low-transition pair fibers inherit the accepted R573 Hamilton-boundary collision interface, but no endpoint multiplicity or closure is claimed.


### 1. Universal one-extension setup
Let H be a hypothetical smallest Strong Level-(1) counterexample and let S be a four-vertex set such that

  S+{d} is Hamiltonian for every d in Y:=V(H)-S.          (UC.1)

Retain the consequences already established in SV26947: Y is non-Hamiltonian and every Y-d is non-Hamiltonian. In particular Y is nonempty and |Y|>=7 there, although the crossing arguments below use only (UC.1), smallest-counterexample exact deletion covers, and the named non-Hamiltonicity when explicitly invoked.

### 2. Every singleton exterior deletion is universally crossed by S
Fix d in Y. By accepted smallest-counterexample minimality R4, H-d has an exact two-cover. In fact every literal exact two-cover of H-d is crossed by the fixed bipartition

  S | (Y-d).                                               (UC.2)

To see this, apply accepted R508 with deleted set D={d}, absorbable remainder block S, and any Hamilton path Q_d on D union S=S+d supplied by (UC.1). If an exact two-cover of H-d selected no S|(Y-d) adjacency, its two rails would leave S isolated from Y-d, and replacing the S-side by Q_d would give a spanning two-cover of H, contradiction. Hence every exact H-d cover has at least one selected crossing state.

This is a universal quantifier over the whole singleton fiber d. No representative synchronization is assumed.

### 3. If S is non-Hamiltonian, every singleton fiber has at least two crossings
Assume now that S itself is non-Hamiltonian. Fix d in Y and an arbitrary exact two-cover C of H-d. Let tau_d(C) be the number of selected S|(Y-d) transitions in C.

Section 2 gives tau_d(C)>=1. Suppose tau_d(C)=1. Apply accepted R560 with

  D={d},  block S,  complement C_0=Y-d,

and with the one-rail absorber Q_d on D union S. Since the deletion cover has k=2 rails and exactly one S|C_0 transition, the R560 unique-transition normal form says exactly one rail is mixed, all vertices of S occur in one contiguous S-block on that mixed rail, and the other rail lies wholly in C_0. The unique S-block is therefore a tight Hamilton path spanning all four vertices of S, contradicting the assumed non-Hamiltonicity of S.

Hence

  tau_d(C) >= 2                                           (UC.3)

for every d in Y and for every exact two-cover C of H-d whenever S is non-Hamiltonian.

Thus the extension-only case, where S itself is not Hamiltonian, carries a stronger wall than the Hamilton-four-core case: every singleton deletion fiber is at least doubly crossed.

### 4. Every core/exterior pair deletion is universally crossed by the surviving trimer
Fix s in S and d in Y. Put

  T_s=S-{s},
  C_d=Y-{d}.                                              (UC.4)

The three-set T_s has a Hamilton tight order by boundary antisymmetry. More importantly, the same five-set absorber from (UC.1) is

  {s,d} union T_s = S+d,                                  (UC.5)

which is Hamiltonian.

Accepted pair-deletion rigidity R429 supplies exact two-covers of H-{s,d}, with two nontrivial rails. Apply R508 with deleted set D={s,d} and absorbable block T_s. Every exact two-cover of H-{s,d} must select at least one physical adjacency crossing

  T_s | C_d.                                              (UC.6)

Therefore the universal one-extension four-set creates a full 4 by |Y| array of pair-deletion universal crossing fibers, each anchored on a fixed physical trimer T_s.

### 5. Low-transition pair fibers inherit the accepted Hamilton-boundary collision interface
For a fixed pair (s,d), if an exact two-cover of H-{s,d} has exactly one T_s|C_d transition, accepted R560 puts the entire trimer T_s into one contiguous block on the unique mixed rail. Accepted R573 may then be applied with the five-vertex Hamilton absorber S+d: every Hamilton realization of S+d ending or starting at the T_s endpoint of the actual crossing contributes the corresponding reverse sign on that selected crossing dimer, and two distinct Hamilton boundary neighbors give the accepted same-oriented collision packet.

No endpoint multiplicity is claimed. In particular, local Hamiltonicity of a five-set alone does not force two such boundary realizations, so this paragraph is an interface, not an extinction theorem.

### 6. Holonomy meaning
A universally one-extendable four-set is therefore not only a generator of the bounded pair-core cycle of SV26947/SV29868. It also creates two dense universal-crossing families:

1. for every exterior d, every exact singleton cover of H-d crosses S|(Y-d), and if S is non-Hamiltonian it crosses at least twice;
2. for every s in S and d in Y, every exact pair-deletion cover of H-{s,d} crosses the fixed trimer (S-s)|(Y-d).

These are current universal quantifiers over entire deletion fibers, not witnesses chosen separately along a support cycle. They provide a direct bridge from the G10 small-core holonomy lane to the mature recompletion-crossing and low-transition machinery.

No spanning two-cover, pair-core extinction, or global minimal-holonomy contradiction is asserted here.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R560"
    },
    {
        "relation": "dependency",
        "revision_id": "R573"
    }
]
```
