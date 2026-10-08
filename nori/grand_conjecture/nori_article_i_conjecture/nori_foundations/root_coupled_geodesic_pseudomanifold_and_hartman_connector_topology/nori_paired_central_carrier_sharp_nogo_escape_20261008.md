# Legal odd coloring makes every paired-central geodesic maximally alternating

SHARP NO-GO FOR A FIXED-ROOT PAIRED CENTRAL CARRIER; EXPLICIT ONE-CHANGE ESCAPE.

Fix even n=2r>=4, a balanced root x with r starting zero-bit directions A and r starting one-bit directions B, and any tournament orientation t(a,c) on all distinct pairs of coordinate directions. Write z_v=x_v, and m=n-3=2k+1 with k=r-2. Define the central antisymmetric step function theta(s)=1 if s<=k, and theta(s)=0 if s>=k+1, so theta(m-s)=1-theta(s).

Define a binary coloring c(F,(a,b,d)) of EVERY ordered three-face F, using exterior Hamming weight K(F), according to the bit pattern (z_a,z_b,z_d) of the FIXED balanced root x:
(A) if z_a=z_b and z_b!=z_d, put c=1;
(B) if z_a!=z_b and z_b=z_d, put c=0;
(C) if z_a=z_d and z_a!=z_b, put c=z_a XOR theta(K(F));
(D) if z_a=z_b=z_d, put c=t(a,d), where t(d,a)=1 XOR t(a,d).
These four cases exhaust all 8 bit patterns.

THEOREM (maximally bad connected paired carrier). This is a legitimate antipodal-reversal-odd NORI coloring. For EVERY paired order p=(p1,...,p_(2r)) rooted at x (each consecutive pair contains one zero-bit and one one-bit direction), its ordered-three-face color word is
 (0,1,0,1,...,0,1)
of length n-2, with the MAXIMUM POSSIBLE n-3 color changes. Therefore the entire connected, reversal-invariant balanced paired-order repair graph may contain NO good geodesic, even for a legal NORI coloring.

PROOF OF ODDNESS. Reversing the ordered triple swaps cases A and B and hence complements their constant colors. Case C reverses to itself (z_a=z_d), while antipodal face complementation changes exterior weight K to m-K; theta changes to its complement, and so does c. Case D reverses to itself as a pattern, and the tournament identity t(d,a)=1 XOR t(a,d) complements its color. These are exactly the NORI antipodal-reversal identities.

PROOF OF MAXIMUM SWITCH COUNT. For odd-position windows i=2j-1, the first two free directions are one paired A/B pair and hence have opposite starting bits. If the last two starting bits coincide, case B applies and yields 0. Otherwise the pattern is ABA or BAB (case C). The paired-weight formula yields K_i=(r-1)-z_(p_(i+2)). Since z_(p_i)=z_(p_(i+2)) in case C, K_i=k+1-z_(p_i). If z_(p_i)=0 then K_i=k+1, theta=0, and case C gives 0; if z_(p_i)=1 then K_i=k, theta=1, and case C again gives 0. Thus every odd window has color 0.

For even-position windows i=2j, the final two free directions form one opposite-bit pair. If the first two bits coincide, case A applies and yields 1. Otherwise case C applies. The first free direction is the SECOND member of the preceding pair, so the paired-weight formula gives K_i=k+z_(p_i). If z_(p_i)=0, then K_i=k and theta=1, so case C gives 1. If z_(p_i)=1, then K_i=k+1 and theta=0, again giving 1. Therefore every even window has color 1. The complete word alternates, proving the maximum switch count.

EXPLICIT GOOD ESCAPE OUTSIDE THE CARRIER. Order ALL r zero-bit directions A first, followed by ALL r one-bit directions B. Within A choose a direction order whose consecutive triples have t(first,third)=1, and within B choose one whose consecutive triples have t(first,third)=0. Such orders exist in every tournament: partition the vertices into two directed Hamilton paths and interleave them, so each pair of directions two apart points in the desired direction; reverse the order to switch the desired value. (For r=2 the triple condition is vacuous.) Along the resulting full order, every triple internal to the A block has case D color 1, every triple internal to the B block has case D color 0, the bridge triple AAB has case A color 1, and the next bridge triple ABB has case B color 0. Thus its full window word is (1,...,1,0,...,0), with EXACTLY ONE change. This geodesic is not paired and generally leaves the two-central-layer carrier.

RESEARCH CONCLUSION. Connectivity, antipodal-reversal symmetry, and four-window locality of the fixed-root balanced paired-order graph are INSUFFICIENT to force NORI closure, even for a Hamming-radial coloring. A successful Hartman/Sperner connector must include additional chamber types permitting departures from the paired central geometry, and/or root-changing corridors, then prove a labeled terminal-extraction theorem. This is a counterexample to the restricted carrier strategy, NOT to the grand conjecture.
