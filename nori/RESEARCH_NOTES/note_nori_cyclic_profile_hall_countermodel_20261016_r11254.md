# Rotation and reversal admit all-dimensional root-profile Hall countermodels

- Stable ID: note_nori_cyclic_profile_hall_countermodel_20261016_r11254
- Author: session_nori_r11254_2
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, profiles, Hall, formal-countermodel, local-integrability, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11254_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_profile_integrability_three_local_laws_20261016_r11254

## Research note

# All-dimensional Hall countermodels on geodesic rotation cycles

Let T(x,(i_1,...,i_n))=(x+e_(i_1),(i_2,...,i_n,i_1)) and R(x,pi)=(bar x,rev pi), on rooted ordered full geodesics. A formal direction-indexed profile Phi need not come from a legal edge coloring.

**Theorem.** For every n>=4 a formal Phi satisfies Phi(TP)=Phi(P)+e_(i_1) and Phi(RP)=Phi(P), attains all 2^n profiles, but its root-profile incidence graph violates Hall: there exists a root set A_n of size 14*2^(n-4) with profile neighborhood of size 12*2^(n-4). The failure is caused by a front-square exchange discrepancy.

*Four-direction model.* Let q:F_2^4 -> H=F_2^3 be q(x)=(x_0+x_3,x_1+x_3,x_2+x_3), whose fibers are antipodal vertex pairs. Rotating each rooted 4-direction geodesic generates an eight-edge cube cycle. Its four root classes under q form a 4-cycle D of H, with the four differences 1,2,4,7, each used once. There are 24 such cycle four-sets, each containing a pair differing by 1.

Let F={0,1} be the forbidden quotient profile classes, A=H\{0}. For each cycle D choose a translation z_D in H with
(D\{0})+z_D contained in H\F.                                      (1)
The choice exists: if 0 belongs to D, at most six shifts are forbidden, namely (D\{0}) union ((D\{0})+1). Otherwise the forbidden shifts comprise D union (D+1), fewer than eight elements because D contains two vertices differing by 1.

Require the two choices D0={0,2,3,4}, z_D0=0, and D1={0,4,6,7}, z_D1=1. Both satisfy (1), and the translated four-sets D0+z_D0 and D1+z_D1 partition H.

Each unoriented cube cycle C gives two opposite cyclic-rotation orbits of rooted orders. Choose one positive orientation and a four-bit lift v_C of z_(q(C)). Assign Phi(x,pi)=x+v_C on the positive orbit and Phi(x,pi)=x+v_C+1^4 on the negative orbit. Rotation changes the root by its first direction and leaves the orbit translation fixed, so it toggles that profile bit. Reversal changes both the root and the chosen translation by 1^4, so the profile is unchanged.

Root-profile quotient incidences are (t,t+z_D) for t in D. D0 and D1 imply every quotient profile is reached and both representatives of every antipodal quotient class occur. Thus all 16 profiles occur. Equation (1) guarantees that the fourteen roots q^(-1)(A) have neighbors only in the twelve profiles q^(-1)(H\F). The special cycles realize all these twelve profiles. This violates Hall.

*Lift to n>4.* Project a rooted ordered n-direction geodesic to directions 0,1,2,3 by deleting the other steps. Its projected oriented cube cycle C is preserved by cyclic rotation and its orientation is reversed by path reversal. Attach the lift (v_C,0^(n-4)) to the positive orientation, and its bitwise complement to the reverse orientation. Set Phi(x,pi)=x+the attached lift. Both rotation and reversal identities still hold. All profiles are reached by choosing the first four root bits and projected order as above, appending extra directions, and freely choosing their initial bits. For A_n={x:q(x_0,x_1,x_2,x_3) !=0}, the first four profile bits have q-image outside F; all allowed classes and arbitrary extra profile bits occur. Consequently |A_n|=14*2^(n-4) and |N(A_n)|=12*2^(n-4).

*Square exchange certificate.* Orient D={0,1,3,7} through (0,(0,1,2,3)) and D'={0,2,3,7} through (0,(1,0,2,3)), and choose numerically least admissible translations for unspecified cycles. The first pair has translations z_D=4,z_D'=0. Their profiles are e_2 and 0 although the two paths merely exchange initial directions 0 and 1; direction 2 should have stayed fixed for any edge coloring. Thus front-square locality fails. By the local integrability theorem in the companion note, this formal construction cannot arise from a legal edge coloring. QED.

Independent enumeration of the 48 oriented rotation orbits in Q4 verifies the cycle counts, the two formal symmetries, profile surjectivity and Hall deficits for n=4,5,6, and the stated square discrepancy. The proof is dimension-uniform. Hence even complete profile coverage, antipodal symmetry, cyclic path rotation, and cube-geodesic orbits cannot force a root-profile perfect matching without adjacent-square consistency.
