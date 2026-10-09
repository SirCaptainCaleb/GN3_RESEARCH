# Every insertion into a near-spanning one-switch core can be bad in a valid reversal-odd coloring

# All-dimensional sharp insertion obstruction: a near-spanning one-switch core whose EVERY single-direction insertion has at least TWO switches

Active NORI reversal-odd ordered physical 3-face coloring; the construction is even coordinate-only, so automatically valid on every physical root. This refutes an attractive snake/Pósa shortcut: from a one-switch (n−1)-geodesic, simply inserting its single missing direction somewhere WITHOUT reordering existing directions need not produce ANY full good antipodal geodesic. It does NOT refute unrestricted NORI, since other complete direction orders may be good.

**THEOREM.** For EVERY n>=5 there exists a valid active NORI coordinate-only binary coloring c(a,b,c), with c(c,b,a)=1−c(a,b,c), such that:
 (i) the direction word P=(1,2,...,n−1), starting from ANY cube vertex, is a one-switch (n−1)-edge geodesic, whose n−3 ordered-window color word is (0,1,1,...,1);
 (ii) for EVERY j=0,...,n−1, the n-edge antipodal full word obtained by inserting the missing coordinate n after the first j entries of P (and keeping ALL other directions in their original order) has AT LEAST TWO three-window color switches, at EVERY cube root.
In particular the two endpoint insertions have 0→1→0 and 1→0→1 patterns, and each internal insertion is deliberately assigned either a consecutive alternating 0,1,0 block or 1,0,1 block. The construction is entirely compatible with full antipodal-reversal oddness.

**Proof/construction.** First assign c(i,i+1,i+2)=0 for i=1, and =1 for 2<=i<=n−3. This colors P with exactly one switch. For all n-containing ordered triples that arise from insertion of n into P, prescribe as follows (all coordinate names denote actual distinct directions):
 (A) insertion at j=0: c(n,1,2)=1; then the full path's first three windows are 1,0,1.
 (B) insertion at j=1: c(1,n,2)=1 and c(n,2,3)=0; then the first three windows are 1,0,1 (as c(2,3,4)=1).
 (C) insertion at every j=2,...,n−3: prescribe
   c(j−1,j,n)=0,  c(j,n,j+1)=1, c(n,j+1,j+2)=0.
   These are THREE CONSECUTIVE actual full-path window colors 0,1,0, forcing two switches, regardless of other windows.
 (D) insertion j=n−2: prescribe
   c(n−3,n−2,n)=1,  c(n−2,n,n−1)=0.
   Because the unchanged initial triple (1,2,3) still appears and has color0, this yields at least two switches: an initial zero, a later one, and a final zero. This holds also for n=5, when these form the last two windows.
 (E) insertion j=n−1: prescribe
   c(n−2,n−1,n)=0.
   The original P window word begins0 and ends1, so appending this 0 creates a second switch.

Consistency: Each newly prescribed n-containing directed triple is UNIQUE (by position of n and its two adjacent numerical neighbors), so there is no conflict between the insertions' prescriptions. Further, no one prescribed directed triple is the REVERSAL of another prescribed directed triple: n-first triples have their two following directions strictly increasing, n-last triples have the two preceding directions strictly increasing, and n-middle triples have increasing outer directions; reversing ANY such triple reverses that order, which is absent from the prescription set. The old increasing triples (not involving n) also have no reversals in the assignment. Therefore the partial bits extend to a GLOBAL reversal-odd coloring by choosing arbitrary bits on every remaining pair {v,reverse v} of directed triples and giving its mate the complementary bit. Finally set the color of EVERY actual physical 3-face with ordered free-direction triple v equal to this c(v). This is a fully valid active NORI coloring for all n and every root.

**Scope.** P is terminally and initially BLOCKED against one-switch one-letter extensions, just as the globally longest-good snake lemma predicts; nevertheless the coloring DOES have some unrelated full good NORI paths (mandatory by low-n results and conjecturally in all n). Hence a maximal-length good-path descent cannot be obtained merely by inserting a missing direction into its word without reordering other directions or coordinating roots. No assertion that P is globally maximal as a good partial geodesic: other full good paths are allowed. This blocks only an insertion-preserving local proof step.
