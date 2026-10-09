# Six-transition physical reversal certificate for global missing-direction exclusion (alternative proof)

# A six-comparison proof that a direction cannot be globally uncertified

This is an ALTERNATIVE SHORT PROOF of the global missing-direction exclusion already established in Item nori_certified_square_complex_connected_antipodal_one_class_20261008, Theorem 3. It avoids constructing or proving connectedness of the entire middle-direction window shift graph H_i. Together with that Item's independently proved seven-cycle/minimum-degree lemma, it yields its established connectedness theorem. It is NOT a new claim of connectedness.

Let n>=5, and c be a physical ordered-three-face coloring obeying c(bar F,reverse pi)=1-c(F,pi). Fix a coordinate i. Suppose there is no monochromatic centered four-edge connector whose two middle directions include i. Then for every physical hub z and distinct coordinates a,b,c,d with i in {b,c}, the actual face colors h_z(a,b,c) and h_z(b,c,d) are different.

**Exterior-bit independence.** Under this supposition, every ordered face containing i is independent of each of its exterior fixed bits. For an exterior direction d and distinct other directions a,b, use the following comparisons:
 (a,i,b) versus (i,b,d),
 (a,b,i) versus (b,i,d),
 (d,i,a) versus (i,a,b).
These are actual centered four-geodesic comparisons, each with i in the middle pair and hence with unequal colors. Change ONLY the hub bit z_d. The compared window having d FREE remains the SAME physical ordered face and retains its color; therefore the other window, which has d fixed, must also retain its color. This works for every d not in the triple and for all positions of i. Thus define h(a,b,c) as the physical-face-independent color on each ordered triple containing i. Active antipodal reversal now imposes h(c,b,a)=1-h(a,b,c).

**Six-comparison certificate.** Choose a,b,d,e pairwise distinct and outside i, and take
 T0=(i,a,b), T1=(d,i,a), T2=(b,d,i),
 T3=(d,i,e), T4=(i,e,b), T5=(a,i,e), T6=(b,a,i).
The six successive comparisons are respectively supplied (in either direction) by the actual four-direction words
 (d,i,a,b), (b,d,i,a), (b,d,i,e),
 (d,i,e,b), (a,i,e,b), (b,a,i,e).
Every four-word has i among its two middle coordinates, so each step flips the bit h. Six steps yield h(T0)=h(T6). Since T6 is EXACTLY the reverse of T0, the antipodal-reversal oddness says h(T6)=1-h(T0). Contradiction.

**Conclusion.** Every coordinate i occurs as the middle direction of an ACTUAL monochromatic four-edge connector somewhere in Q_n. Combining this with the existing seven-window proof that at most one direction is isolated in each certified-square link, and the cube isoperimetric equality classification, recovers the known global connectedness of the certified-square complex for all active NORI colorings, n>=5.

**Role.** A finite six-shift reversal certificate replaces the larger H_i connectivity-and-bipartition argument for excluding a globally missing coordinate. It does not force compatible long monochromatic paths, and does not improve the sharp equivariant index-one bound on the certified-square complex (Item nori_actual_nori_coloring_sharp_certified_square_index_one_20261008).
