# Global switch-density theorem: every ordered-three-face cube coloring has a full antipodal geodesic with at most floor(4(n−3)/5) changes

# Universal full antipodal geodesic switch bound from local odd-cycle physical root transport

Let r>=2 and n>=2r-1. Color all physical ordered r-faces of Q_n by arbitrary binary values (NO antipodal oddness assumption). For a rooted full n-coordinate geodesic (x,p) with direction word p=(p1,...,pn), its actual consecutive ordered-r-face colors form a word of length n-r+1, with exactly m=n-r potentially switching adjacent pairs. Let D(x,p) count their total number of switches.

**THEOREM (universal all-dimensional linear full-switch bound).** Under these completely arbitrary colorings,
\[
\boxed{\mathbb E_{X\in Q_n,\ P\in S_n}D(X,P)\ \le\ \frac{2r-2}{2r-1}(n-r).}
\]
Consequently there exists an ACTUAL full antipodal n-edge geodesic with
\[
\boxed{D(x,p)\ \le\ \left\lfloor \frac{2r-2}{2r-1}(n-r)\right\rfloor.}
\]
More quantitatively, for every integer q>=0 with q+1>(2r-2)(n-r)/(2r-1), the fraction of all 2^n n! rooted full antipodal geodesics having at most q switches is at least
\[
\boxed{1-\frac{(2r-2)(n-r)}{(2r-1)(q+1)}.}
\]
All three statements hold without any reversal-odd coloring assumption.

**PROOF.** The team's proved ordered-r odd-cycle root-transport theorem nori_ordered_r_face_odd_cycle_root_transport_two_r_minus_one_seed_20261008 says: fix any q0=2r-1 distinct coordinate directions B and any physical reference root z. Among the (q0)! orders of B, at least (q0-1)! have the first TWO actual r-face windows EQUAL on the rooted q0-edge geodesic that starts at z XOR its first direction, uses that direction order, and passes through z after its first step. The equality follows from odd-cycle alternation of the q0 genuine ordered r-face colors THROUGH z. Indeed an odd cycle of binary vertex colors must have two adjacent equal colors, and each such equal pair is an actual root-neighbor transported (2r-1)-edge witness. The map (z,pi)->(x=z XOR first(pi),pi) is a BIJECTION for each fixed B. Summing over z therefore proves that for a uniformly random starting root X and uniformly random permutation of B, the first TWO actual ordered-r-face window colors of that (2r-1)-edge path agree with probability AT LEAST 1/(2r-1).

Now choose a uniformly random full n-coordinate direction permutation P and independent uniform full-cube root X. Fix any switch location j∈{1,...,n-r}. Consider the consecutive block of r+1 distinct directions (P_j,...,P_(j+r)), and the true physical root Y of this block, reached after the first j-1 directions from X. The joint law of Y and this ordered direction block is uniform over all physical cube roots and all ordered (r+1)-tuples of distinct coordinates: conditioned on P, XOR with the preceding used-support is a bijection on the uniform cube roots. For any ordered (r+1)-tuple, extend it by q0-(r+1)=r-2 distinct unused coordinate directions to an ordered (2r-1)-tuple, chosen uniformly and independently of Y. This is possible because n>=2r-1. The equality of the first TWO r-face windows depends ONLY on Y and the first r+1 ordered directions; it is unaffected by the auxiliary appended r-2 directions. Sampling the entire q0-block uniformly (via a random B and its random order) has exactly the same initial (Y,ordered r+1 tuple) distribution. Therefore the root-transport theorem forces
\[
\Pr[w_j(X,P)=w_{j+1}(X,P)]\ge\frac1{2r-1},
\qquad
\Pr[w_j\ne w_{j+1}]\le\frac{2r-2}{2r-1}
\]
for EVERY j.

Sum over all m=n-r adjacent switch indicators and apply linearity of expectation. Some genuine full rooted path attains at most the integer floor of the expectation bound. Finally apply Markov to the nonnegative integer random variable D:
\[
\Pr[D\ge q+1]\le \frac{\mathbb E D}{q+1}\le
\frac{(2r-2)(n-r)}{(2r-1)(q+1)},
\]
which yields the stated quantitative fraction. QED.

**ACTIVE NORI CASE r=3.** Every binary physical ORDERED three-face coloring of Q_n, n>=5, with or WITHOUT antipodal-reversal oddness, has SOME full n-edge antipodal geodesic with at most
\[
\boxed{\left\lfloor\tfrac45(n-3)\right\rfloor}
\]
three-face window-color changes. In particular for n=5, \(\lfloor\frac45\cdot2\rfloor=1\), immediately reproving the UNRESTRICTED dimension-five NORI theorem from physical root-transport parity + averaging. The result is nontrivial in all dimensions and supplies a positive fraction of moderately low-defect FULL paths, but does not give a ONE-switch full path for n>=6.

**NEAR-OPTIMAL INTERPRETATION AND NEXT TOPOLOGICAL TASK.** This elementary proof demonstrates that literal five-cycle physical root transports can be integrated along the ENTIRE n-coordinate permutation distribution WITHOUT assuming independent local repairs or splicing separately shifted short paths. It gives a correctly glued GLOBAL expectation statement, unlike naive concatenation of independently repaired five-blocks. However a high-index topological proof of grand NORI closure would need to leverage DEPENDENCES between the m switch indicators more strongly than this separate-marginal bound. The odd pentagon identity supplies a universal degree-one cohomological certificate; the missing step is to build a genuine high-dimensional overlapping-pentagon carrier whose nonzero cup product forces sufficiently many ZERO switches in the SAME full direction order, or to force one-switch via the reversed two-tail exact reachability splice. This theorem does not close unrestricted NORI.
