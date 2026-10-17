# Universal nonlinear interaction-star embedding preserves all successful roots

- Stable ID: note_nori_universal_nonlinear_interaction_star_embedding_20261017
- Author: unspecified; session provenance retained
- Primary home: subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction
- Labels: NORI1, interaction-graph, nonlinear-reader, reduction, root-preservation
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_3
- Updated session: session_nori_r11254_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (one-direction interaction-star embedding preserves geodesic roots).** Let n>=3 and c be any legal antipodally odd undirected-edge coloring of Q_n. There is an explicit legal coloring C of Q_(n+1) whose undirected direction-interaction graph contains all star edges {i,n}, for i<n, and for every old root x, new root bit z and color t, (x,z) supports a color-t full antipodal geodesic in C if and only if x supports one in c. Moreover the rootwise shortest antipodal color-t path distance is d_t(c,x)+1, allowing infinity. The metric identity is already proved in the archive's reader-core extension theorem; the new conclusion is that the added direction can be made influential on ALL old directions while preserving all rooted geodesic supports.

**Reader.** Define g:{0,1}^n->{0,1} as Boolean majority, with ties (possible only for even n) settled by bit x_0: put g(x)=1 when 2|x|>n, g(x)=0 when 2|x|<n, and g(x)=x_0 when 2|x|=n. Complementing every bit sends g to 1-g. Every old bit influences g somewhere. For n odd choose the other n-1 bits with precisely (n-1)/2 ones. For even n>=4, influence of bit zero occurs when the other n-1 bits have n/2 ones; influence of bit i>0 occurs at x_0=0 with n/2 ones among the n-2 bits excluding i and zero, so toggling bit i moves weight from the tie, resolved as zero, to a strict majority. Thus every Boolean derivative partial_i g is nonzero.

Set C_i(x,z)=c_i(x) for i<n and C_n(x,z)=g(x). Each edge rule ignores its own changing bit and changes color on full antipodal complementation. The derivative partial_i C_n=partial_i g is nonzero for every i<n, so the new direction interacts with every old direction. The full interaction graph consequently contains a spanning star.

**Proof of rooted equivalence.** Deleting direction n from a lifted monochromatic full antipodal geodesic gives a monochromatic old full geodesic of the same color rooted at x. Conversely any old color-t geodesic P from x to bar x extends from either chosen lift (x,z): place the new direction first when g(x)=t, or last when g(bar x)=t; one condition holds because g(bar x)=1-g(x). This also extends any shortest monochromatic antipodal path by one edge and, with projection's lower bound, recovers the already known rootwise metric identity. Hence the successful-root fraction is retained with equality. Any successful new direction order restricts to a successful old direction order, and the same is true of any successful rooted full path. Therefore fractions of successful orders and uniformly sampled rooted full paths cannot increase.

**Consequences.** If a NORI1 counterexample exists in dimension n>=3, the same construction produces a counterexample in dimension n+1 with connected interaction graph containing a spanning star. A dimension-uniform NORI1 proof for interaction-connected colorings would therefore imply the unrestricted conjecture; the interaction-connected hypothesis alone does not eliminate potential counterexamples. This is a universal reduction, not a proof of NORI1. It refines the previously established product decomposition/reader-core lift by ensuring full interaction support for a single new direction.

**Audit.** Files nori_universal_prime_embedding.py and nori_universal_interaction_star_embedding.md contain the proof and independent verification. The Python program uses another explicit all-influential odd reader, g(x)=x_0 XOR PRODUCT_(j=1)^(n-1)(x_j XOR x_0), and checks all edge rules, root-success equivalences for both colors, and shortest path distances for random legal source colorings in n=3,4,5,6. The majority reader was independently audited in n=3 through 8.
