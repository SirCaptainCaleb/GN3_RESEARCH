# Binary valuation hierarchy for interior exchange defects in both classes

- Stable ID: note_8cbafb65d96d93a8b2baaaa6
- Author: unspecified; session provenance retained
- Primary home: section:nori_type_a_rook_gallery_topology
- Labels: wu-yang, formal-deformation, boundary-tournaments, nori1, full-rank
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7547_3
- Updated session: session_nori_r7547_3
- Disposition: none
- Successor: none

## Related references

- subsection:formal_switch_deformation_and_the_quadratic_exchange_defect

## Research note

**Theorem (2-adic order of the formal exchange defect).** Work over \(\mathbb F_2[u]\), put \(t=1+u\), and let \(P,P'\) be any two complete paths in the same admissible class whose numbers of color switches are \(S,S'\). Write \(m=|S-S'|\) and \(h=\min(S,S')\). Their paired weighted-chain coefficient is
\[
t^S+t^{S'}=t^h(t^m+1).
\]
If \(m=0\) this vanishes. Otherwise the lowest nonzero power of \(u\) occurring in the polynomial is
\[
\boxed{\operatorname{ord}_u(t^S+t^{S'})=2^{v_2(m)}.}
\]

*Proof.* Write \(m=2^kq\), where \(q\) is odd. In characteristic two, \((1+u)^{2^k}=1+u^{2^k}\) by Frobenius. Therefore
\[
t^m+1=(1+u^{2^k})^q+1
=u^{2^k}+\text{terms of strictly higher }u\text{-degree},
\]
since the linear binomial coefficient \(q\) is one modulo two. As \(t^h\) has constant term one, multiplication does not change the lowest nonzero degree. \(\square\)

**Corollary (both original classes have first-order interior cancellation).** In NORI1, exchanging two consecutive dimensions in nonterminal positions \(2\le j\le n-2\) preserves the first and last geodesic edge colors, with switch-count difference \(0\) or \(\pm2\). Hence the paired interior facet coefficient is either zero or divisible by \(u^2\), with first nonzero coefficient at order two.

For ordinary boundary 3-tournaments on \(n\ge8\) vertices, exchanging consecutive Hamilton positions \(i,i+1\) with \(4\le i\le n-4\) preserves the first and last triple-window colors and changes the switch count by an even integer of absolute value at most four. The paired weighted coefficient is therefore zero, has its first nonzero term at \(u^2\) when \(|\Delta S|=2\), or at \(u^4\) when \(|\Delta S|=4\). Every exchanged order is still a Hamilton permutation.

**Interpretation.** The same one-parameter formal chain deformation detects a parity-preserving interior exchange hierarchy in both unrestricted problems. An odd switch jump is a first-order phenomenon; a two-switch jump starts in degree two; a four-switch jump starts in degree four. Endpoint exchanges and cube root changes can have different behavior. The valuation formula alone does not construct an equivariant chain-map correction or force a one-switch complete path; its significance is that it supplies a common quantitative organizing law for the local chain defects, retaining full path simplicity.
