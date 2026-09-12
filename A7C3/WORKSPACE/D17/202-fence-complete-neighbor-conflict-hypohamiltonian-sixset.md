# Complete neighboring-support conflict can occur inside a deletion-Hamiltonian non-Hamiltonian six-set

**Workspace:** D17
**State:** limitation
**Key:** `fence-complete-neighbor-conflict-hypohamiltonian-sixset`

**Summary:** Exact finite fence. There exists a Strong Level-(1) exact-reversal system on six vertices whose full six-set is non-Hamiltonian, every five-vertex puncture is Hamiltonian, yet the Hamilton-order families on the two neighboring punctures V-{0} and V-{1} have disjoint induced orders on their common four-set {2,3,4,5}. Hence every pair of Hamilton representatives across those two supports is R435-active. Complete neighboring-support conflict is therefore locally possible even in a deletion-Hamiltonian non-Hamiltonian block; any Common-Complement Holonomy Contraction theorem must use additional common-complement/currentness geometry.

### Exact certificate and encoding
Use vertices 0,1,2,3,4,5. For every middle vertex m and unordered endpoint pair a<c with a,c distinct from m, index one Boolean variable in lexicographic order of triples (m,a,c). Bit 1 means (a,m,c) is tight; bit 0 means its complete reversal (c,m,a) is tight. The following 60-bit word therefore specifies the entire Strong Level-(1) system:

  010000000010001000000001000011100000111100000000110111111000

Direct exhaustive verification gives:

- the full six-set has 0 Hamilton tight paths;
- each puncture is Hamiltonian, with Hamilton-path counts
  d=0:6, d=1:4, d=2:5, d=3:6, d=4:2, d=5:8;
- for X=V-{0} and Y=V-{1}, let S={2,3,4,5}. X has 6 Hamilton paths and Y has 4 Hamilton paths, but the sets of S-orders induced by those two Hamilton families are disjoint.

By the contact-monotonicity alternative in accepted R435, no Hamilton representative on X can be R435-quiet against any Hamilton representative on Y. Thus the two complete Hamilton-order families are pairwise R435-conflicting.

### Scope
This is a finite negative result, not a smallest-counterexample construction. It proves that deletion-Hamiltonicity plus one-for-one neighboring Hamilton supports does NOT by itself force a quiet pair or a contraction. The additional fixed-complement and source-current representative structure in D17 is genuinely load-bearing.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
