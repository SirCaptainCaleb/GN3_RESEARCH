# Affine antipodally odd Q4 gives a reachability nerve with Euler characteristic 2 and Lefschetz number 0

# A valid antipodally odd affine edge coloring with reachability nerve chi=2, Lefschetz=0

On Q_4={0,1}^4, define the color of direction-i edges by
\[
c_1(x)=x_3,\qquad c_2(x)=x_4,\qquad
c_3(x)=x_4,\qquad c_4(x)=x_3,
\]
where c_i is independent of x_i as required for an undirected edge coloring. Every c_i depends on exactly one *exterior* bit, so complementing all cube bits flips every edge color: c_i(bar x)=1-c_i(x). Hence the original antipodal-odd edge axiom holds.

For the COLOR-FREE monochromatic geodesic reachability nerve K_R on 16 cube-vertex labels, the exact simplicial face counts are
\[
(f_0,\ldots,f_{15})=
(16,120,560,1820,4368,8008,11440,12870,11440,7992,4320,1752,504,92,8,0).
\]
Therefore
\[
\boxed{\chi(K_R)=\sum_{k=0}^{15}(-1)^k f_k=2.}
\]
The counts of τ-invariant simplices supported on respectively r antipodal vertex pairs, r=1,...,8, are
\[
(a_1,\ldots,a_8)=(8,28,56,70,52,22,4,0).
\]
An invariant simplex with r antipodal pairs has 2r vertices and τ acts as r disjoint vertex transpositions; its contribution to the antipodal Lefschetz number is \((-1)^{(2r-1)}(-1)^r=(-1)^{r+1}\). Hence
\[
\boxed{L(\tau)=\sum_{r=1}^8(-1)^{r+1}a_r=0.}
\]
Nevertheless ALL eight antipodal edges {x,bar x} belong to K_R: R(x)∩R(bar x) is nonempty for every x.

**Exact reproducibility without black-box search.** For each root x, define dynamic Boolean arrays r_q(x,S) on coordinate subsets S⊆[4]:
\[
r_q(x,\varnothing)=1,\qquad
r_q(x,S)=\bigvee_{i\in S}\bigl[
r_q(x,S\setminus\{i\})\ \land\
(c_i(x\oplus(S\setminus\{i\}))=q)
\bigr].
\]
Then R(x) consists exactly of x⊕S for which r_0(x,S)∨r_1(x,S)=1. Enumerating x in binary order 0000 through 1111 and encoding R(x) as a 16-bit mask with target z at bit position z gives
\[
(0fff,0fff,0fff,0fff,\ ff7f,ffbf,ffdf,ffef,\
f7ff,fbff,fdff,feff,\ fff0,fff0,fff0,fff0).
\]
The nerve simplex test is the direct formula
\[
\sigma\in K_R\ \Longleftrightarrow\
\exists z\in Q_4:\ \sigma\subseteq R(z),
\]
using symmetry R(z) as the set of roots that can reach z. Counting nonempty bitmask subsets of the displayed region masks produces exactly the face counts above. Counting masks closed under z→15⊕z produces a_r.

**Implication.** The raw reachability nerve does not universally have odd Euler characteristic, and the antipodal involution need not have nonzero Lefschetz number, EVEN when every antipodal pair has an intersection certificate. Consequently neither invariant alone can prove the grand edge conjecture on this nerve. This is a precise, fully specified counterexample to an overly strong topological forcing hypothesis; it does NOT refute the edge conjecture or the exact fixed-point equivalence. A refined nerve, local carrier condition, or higher-order reachability incidence theorem is necessary.
