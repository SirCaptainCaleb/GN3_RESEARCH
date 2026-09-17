# A true T+ wrap terminal is a complete three-label anti-extension cell with a forced common-shadow current pair

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-tplus-anti-extension-cell`

**Summary:** Refines the positive-tail failed-wrap branch by the lexicographic coordinate (lambda,tau), where tau counts vertices strictly after the tracked d/y state. Terminal transfer of q lowers tau, while transfer of {s,q} lowers lambda. Hence a true T+ terminal forces every nonempty extension of the literal complement B by {s,q,t} to be non-Hamiltonian. This implies |B|>=4 by R522. Combining B+q non-Hamiltonicity with the endpoint-currentization parent forces BOTH endpoint deletion fibers current on the same triple-deletion shadow M|B. At the active failed-wrap four-set {s,q,p,t}, either a labelled P4 occurs with literal two-path complement, or R516 reduces the P4-free case to signature 11; signature 01 closes H. In signature 11 the exact insertion of t between p,q forces the ancestry-bearing reverse turn (t,p,u), where u immediately precedes p. No generic payment is taken.

### 1. The correct two-coordinate transport
Retain the failed-wrap H-t row from `singleton-deep-wrap-terminal-endpoint-transfer`:

  R=(s,r_1,...,p,q) | B,

with tracked selected state e_0->e_1 in {d->y,y->d}, source distance lambda>0, and (t,e_0,e_1) tight. Define

  tau = number of R-vertices strictly after e_1.

The parent source transport decreases lambda when its tail rotation succeeds. There are two further support-transfer moves that preserve the same physical d/y state.

First suppose tau>0. Then q lies strictly after e_1. If B+q has a Hamilton path B_q, deleting the terminal q from R gives the literal tight path R-q, still selecting e_0->e_1 with the same source distance lambda and with tau decreased by one. Hence

  (R-q) | B_q

is an exact H-t two-cover and gives strict progress in the lexicographic coordinate (lambda,tau).

Second, still with tau>0, if B+{s,q} has a Hamilton path B_sq, then

  M | B_sq,    M=(r_1,...,p),

is an exact H-t two-cover. The tracked d/y state survives because s lies before e_0 and q lies after e_1, and its new source distance is lambda-1. Thus transfer of both active endpoints gives strict primary progress.

Call the positive-tail branch T+ when tau>0 and neither of these support transfers is available after the parent B+s test. A true T+ terminal therefore has

  B+s,  B+q,  B+{s,q}

all non-Hamiltonian.

### 2. Complete three-label anti-extension over B
The omitted label t turns this into a complete anti-extension cell. The parent already gives B+t and B+{s,t} non-Hamiltonian: otherwise R or R-s together with the corresponding Hamilton extension of B would two-cover H. Likewise B+{q,t} is non-Hamiltonian, because a Hamilton path on B+{q,t} together with R-q would be a spanning two-cover of H. Finally B+{s,q,t} is non-Hamiltonian, because it would pair with M=(r_1,...,p) to two-cover H.

Consequently every nonempty subset Z of {s,q,t} satisfies

  B+Z non-Hamiltonian.

This is stronger than the endpoint-sign ledger: it is a support-level seven-cell obstruction attached to one literal Hamilton order B. In particular the three individual failures give, for any retained order B=(b_0,...,b_k), the simultaneous endpoint fans

  (b_1,b_0,s), (b_1,b_0,q), (b_1,b_0,t),
  (s,b_k,b_{k-1}), (q,b_k,b_{k-1}), (t,b_k,b_{k-1})

tight. These are retained as current endpoint data, not paid through same-support collision currency.

### 3. The complement rail has order at least four
Every singleton-deletion rail in a smallest counterexample has order at least three. Suppose |B|=3 and let C be its actual Hamilton trimer order. Since B+s and B+q are non-Hamiltonian, the two four-sets C+{s} and C+{q} have no Hamilton P4. Accepted R522/P537 applies to the same tight trimer C with the distinct fourth vertices s,q and forces a Hamilton P5 on B+{s,q}. This contradicts the T+ anti-extension conclusion above. Therefore

  |B| >= 4.

No edge-orderability hypothesis is used.

### 4. Both endpoint defects are forced current on one common shadow
Retain `singleton-deep-end-direct-pair-deletion-currentization` SV14503. Put

  X=H-{s,q,t},   M=(r_1,...,p).

The literal cover M|B is exact on X. The parent proves that the q-end END-DIRECT fiber is necessarily current on X, while the only quiet s-end outcome would Hamiltonize B+q. In T+ the latter support is non-Hamiltonian by Section 1. Hence the quiet s-end form is impossible as well.

Thus BOTH endpoint deletion fibers currentize on the SAME residue X relative to the SAME ancestral exact cover M|B. At each end the retained outcome is either a component-drop representation carrying an actual selected edge of M|B across its current components, or an exact two-cover with support partition different from M|B and therefore bidirectional physical R410 crossings. No generic R159/R176 descendant is taken.

This is the hard current form of T+: a complete three-label anti-extension over B plus two independently produced but common-residue current defects on M|B.

### 5. The active boundary four-set is P4 or exact signature 11
Write u=r_{m-2}, so the current tail is ...u,p,q. The T+ assumptions imply at least four vertices on R, so u exists. Parent wrap failure and impossible terminal restoration give

  (s,q,p),  (t,q,p)

tight. Outside the already-separated R579 double-wrap P4, the parent also retains

  (q,s,r_1)

tight. Consider F={s,q,p,t}.

If F has a Hamilton P4, retain its exact order. Deleting F leaves the literal two-path forest

  (r_1,...,u) | B.

This cover of H-F is exact: if the complement were Hamiltonian, that Hamilton path together with the retained P4 would two-cover H. Hence this P4 output has a literal two-path complement and must not be merged with the weaker q2 P4 outputs.

Assume instead F is P4-free. Apply R516 to the tight trimer (s,q,p) with fourth vertex t. The right same-polarity sign is supplied by (t,q,p). For the left sign, if both (s,q,t) and (q,s,t) were bad, R3 would give (t,q,s) and (t,s,q), and (t,s,q,p) would already be a P4. Thus the R516 hypotheses hold. Since the alignment bit B=[(t,q,p) tight] equals one, only signatures 01 and 11 are possible.

Signature 01 contains (t,q,s). Together with (q,s,r_1) and the inherited suffix turns of R,

  (t,q,s,r_1,...,p)

is a Hamilton path on V(R)+{t}; paired with B it two-covers H. Therefore signature 01 is impossible in a counterexample. The unique P4-free boundary cell is signature 11.

### 6. Signature 11 forces a predecessor-local reverse tail
In signature 11, R516 gives

  (p,t,q) tight.

Insert t between p and q in the current R order. The proposed spanning active path

  (s,r_1,...,u,p,t,q)

has exactly one uncertified turn: (u,p,t). Every earlier turn is inherited from R and the final turn (p,t,q) is certified by the signature-11 row. If (u,p,t) were tight, this path together with B would be a spanning two-cover of H. Hence

  (u,p,t) bad,
  (t,p,u) tight.

This is an ancestry-bearing obstruction on the actual predecessor u of p. In the minimum positive-tail layer tau=1, the terminal segment is ...e_0,e_1,q, so u=e_0 and p=e_1; the forced turn becomes (t,e_1,e_0), directly reversing the tested d/y dimer at the terminal boundary.

### Scope
This section is a reduction, not closure. It proves that a true positive-tail wrap terminal is far more rigid than a bare failed rotation: every nonempty extension of B by {s,q,t} is non-Hamiltonian; |B|>=4; both endpoint defects are current on one common triple-deletion residue; and the active boundary four-cell is either a cover-aware P4 or the unique R516 signature-11 cell with the explicit predecessor shield (t,p,u). The T0 branch tau=0 is not included because deleting q there can destroy the tracked d/y state.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R516"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    }
]
```
