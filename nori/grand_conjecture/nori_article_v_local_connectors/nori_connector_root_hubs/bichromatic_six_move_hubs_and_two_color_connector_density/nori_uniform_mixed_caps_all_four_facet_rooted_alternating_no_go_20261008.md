# Uniform four-facet cap bits alone do not force a near-spanning one-change rooted geodesic

# Uniform codimension-two cap labels alone cannot force a rooted one-switch facet geodesic

This construction is an **exact no-go** for an overstrong possible intermediate lemma. It does **not** contradict the proved bichromatic-hub local-cap dichotomy: the example below only prescribes the cap bits and the active antipodal axiom, not the full mixed-direction selector field of a bichromatic hub.

Fix any dimension \(n\ge7\) and two distinct omitted directions \(a,b\). Put \(U=[n]\setminus\{a,b\}\), \(m=|U|=n-2\ge5\), and choose the projected root \(r=0_U\). We construct a **valid active NORI coloring** on physical ordered three-faces satisfying both:

1. For **every** \(i\in U\), and all four choices of fixed omitted bits \(t=(x_a,x_b)\),
\[
c(F(x;\{a,b,i\}),(a,b,i))=1,\qquad
c(F(x;\{a,b,i\}),(b,a,i))=0
\quad\text{whenever }x|_U=r.
\tag{1}
\]
Thus the same four-facet uniform mixed cap packet holds as in the positive cap theorem.
2. For **every** one of the four \(U\)-parallel facets rooted at the \(U\)-projection \(r\), and **every** permutation of all \(m\) directions in \(U\), the full \(U\)-geodesic has a strictly alternating ordered-three-face color word
\[
(k_t,1\oplus k_t,k_t,\ldots).
\tag{2}
\]
Since it has \(m-2\ge3\) windows, each such path has at least two color changes; in particular **no** such facet/root pair has a one-change or monochromatic \(U\)-spanning geodesic.

**Construction and proof.** For any ordered three-face whose three free directions lie *entirely in* \(U\), let \(t=(F_a,F_b)\) be its two fixed omitted bits, and prescribe
\[
c(F,\pi)=
\left(\bigoplus_{j\in U\setminus\operatorname{free}(F)}F_j\right)
\oplus k_t,
\tag{3}
\]
independent of the order \(\pi\) of its three free directions. Choose arbitrary bits \(k_{00},k_{01}\) and set
\[
k_{t\oplus(1,1)}
=1\oplus((m-3)\bmod2)\oplus k_t.
\tag{4}
\]
The active antipodal-reversal law holds on these ordered U-only faces, because antipodal complementation toggles all \(m-3\) fixed U bits and both bits of \(t\), while reversing \(\pi\) does not affect formula (3).

For each face with free directions exactly \(\{a,b,i\}\), and fixed U-coordinate values **all zero** outside \(i\), prescribe the two oriented values (1). Its antipodal physical face has **all one** fixed U-coordinate values outside \(i\), so assign the reversed ordered triples on that antipodal face their complementary colors, as required by the active law. Since \(m\ge5\), these two physical faces are distinct. The two prescribed ordered-face orientations are also distinct involution orbits. Thus the cap assignments are consistent with active antipodal reversal.

All remaining antipodal-reversal ordered-face orbits are disjoint from these assignments and may receive arbitrary opposite bits. This completes a well-defined global NORI coloring satisfying (1), (3), and the active axiom.

Now take any full direction order \(p=(p_1,\ldots,p_m)\) in \(U\), rooted at the physical vertex whose U bits are all zero and whose omitted bits are \(t\). In its \(s\)-th ordered-three-face window (\(1\le s\le m-2\)), exactly the first \(s-1\) previously traversed U directions are fixed to 1 outside the three free directions, while all later fixed U bits remain 0. Formula (3) therefore gives
\[
w_s=(s-1\bmod2)\oplus k_t,
\tag{5}
\]
independent of \(p\). This is the alternating word (2) and has precisely \(m-3\ge2\) changes, proving the asserted obstruction.

**Interpretation.** A color-free cap map with all coordinates uniformly 0 or uniformly 1 may look like a cubical Sperner boundary condition, but it does not force *even a one-change near-spanning geodesic* from the associated projected root. The full hub-mixed selector theorem adds genuine restrictions on **ordered faces whose free triples lie completely inside \(U\)** and on certification of physical center squares. A successful fixed-point proof must exploit those extra constraints (or obtain a carrier with independent root movement), rather than applying a fixed-point theorem to the cap bits alone.

This construction is not claimed to have a bichromatic hub with the requisite \(A/B\) classes at the specified root, nor to refute the grand NORI conjecture: global good geodesics may exist elsewhere.
