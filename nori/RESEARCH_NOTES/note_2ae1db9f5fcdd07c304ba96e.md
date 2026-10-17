# Two-helper universal profile completion and sharp one-helper passivity

- Stable ID: note_2ae1db9f5fcdd07c304ba96e
- Author: unspecified; session provenance retained
- Primary home: subsection:antipodal_multifacet_bridge_and_seven_coordinate_universality
- Labels: NORI1, two-helpers, unrestricted, profile-support, extension-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11238_1
- Updated session: session_nori_r11238_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

## Sharp one-helper passivity and two-helper universal profile completion

Let n>=2 and let c be any legal antipodally odd binary undirected-edge coloring of Q_n, so c_i(x+e_i)=c_i(x) and c_i(bar x)=1+c_i(x). Write W(c) for the set of direction-indexed binary profiles of full antipodal geodesics.

**Theorem 1 (one-helper extension factorization).** Let C be any legal odd coloring of Q_(n+1), with one new bit z, such that C_i(x,0)=c_i(x) for all original directions i. Then necessarily
\[
C_i(x,z)=c_i(x)\quad\text{for both }z\in F_2,
\tag{EH1}
\]
and
\[
\boxed{W(C)=W(c)\times F_2.}\tag{EH2}
\]
*Proof.* Oddness gives C_i(x,1)=1+C_i(bar x,0)=1+c_i(bar x)=c_i(x). The new-direction edge has rule C_z(x,z)=d(x), independent of z; global oddness forces d(bar x)=1+d(x). Projection of any full extension geodesic onto original directions gives a full base geodesic, proving inclusion in W(c) times F2. Conversely, choose a base geodesic realizing w from root x. Put the new-direction step before all original steps if the desired z-color equals d(x), and after all original steps otherwise. At the latter position its color is d(bar x)=1+d(x). The original profile remains w in either placement. This proves (EH2). \(\square\)

**Theorem 2 (two-helper universal full-profile completion).** Every legal odd coloring c of Q_n, n>=2, admits a legal odd extension C to Q_(n+2), agreeing with c on the auxiliary face (u,v)=00, for which
\[
\boxed{W(C)=F_2^{n+2}.}\tag{EH3}
\]
Such an extension may be defined explicitly by
\[
b_i(x)=x_{i+1\bmod n},\qquad
C_i(x,u,v)=
\begin{cases}
c_i(x),&u=v,\\
b_i(x),&u\ne v,
\end{cases}\ (0\le i<n),
\tag{EH4}
\]
\[
\boxed{C_u(x,u,v)=v,\qquad C_v(x,u,v)=x_0.}\tag{EH5}
\]
For any prescribed target profile, the resulting witness starts in the original auxiliary face 00 and uses just one of the two guard-direction arrangements u, old steps, v or v, old steps, u.

*Proof.* In (EH4), c_i and b_i each ignore their own x_i and are odd under global x complementation; the equality predicate u=v is unchanged when u,v are both flipped. The rule C_u=v ignores u and flips under global antipodality; C_v=x_0 ignores v and flips under global antipodality. Thus C is legal and odd, and agrees with c on the 00 face.

Prescribe an old-direction word w=(w_0,...,w_(n-1)) and new-direction bits (p,q)=(w_u,w_v). Put
\[
\boxed{x_0=1+p+q.}\tag{EH6}
\]
Consider the cyclic-reader coloring b on Q_n. Given any direction permutation pi, its profile equations are
\[
w_i=x_{i+1\bmod n}+[\ i+1\bmod n\text{ appears before }i\text{ in }\pi\ ].
\tag{EH7}
\]
These determine one root x for every pi,w. Choosing pi=(n-1,0,1,...,n-2) gives x_0=w_(n-1), while choosing pi=(0,1,...,n-1) gives x_0=1+w_(n-1). Since n>=2, the two lists are valid, and one of them produces the desired x_0 from (EH6).

Start C at (x,0,0). If p=0, take the complete direction order (u,pi,v). The first new step has color C_u=0, then the original steps are on the face (u,v)=(1,0), where their colors are b and yield w; finally v is used at original endpoint bar x, giving color C_v(bar x,1,0)=1+x_0=q. If p=1, use the order (v,pi,u). Its first new edge has color C_v(x,0,0)=x_0=q; the old steps occur at auxiliary state (0,1), again giving w; the last u-edge has color C_u=1=p. In both cases the path traverses all n+2 directions once, terminates at (bar x,1,1), and realizes (w,p,q). \(\square\)

**Corollary 3 (two auxiliary bits suffice without a partial-prescription theorem).** The active-completion construction in the same subsection that used n-6 helper bits based on the known seven-direction prescription is superseded as an upper bound on the number of helpers: a pair of helpers suffices for all n>=2. In contrast, one-helper extensions have the product property (EH2) and cannot create missing original-direction profiles. In particular, a face-preserving full-profile extension theorem by itself supplies no information about whether W(c) contains a given profile, since (EH3) holds for every legal base c independently of its profile support.

**Finite audit.** The constructive witness formulas were checked against independently generated legal odd base edge colorings for dimensions n=2,3,4,5,6. All 2^(n+2) target profiles were tested for n=2,3,4,5, and 200 sampled targets for n=6, including verification of the returned rooted geodesic endpoint and all edge colors. The dimension-uniform proof does not rely on this enumeration.

**Scope.** The construction requires adding dimensions and modifies old-direction edge colors on auxiliary faces with u different from v. Consequently it is not a counterexample-preserving lift and does not settle unrestricted NORI1. The primary conclusion is a sharp distinction between passive one-helper extensions and programmable two-helper extensions.

**Corollary 4 (uniform factorial witness multiplicity).** For the two-helper extension C in (EH4)-(EH5), every prescribed profile in F2^(n+2) is attained by at least n! rooted, ordered full antipodal geodesics.

*Proof.* Fix a target (w,p,q). Among all n! permutations pi, half place original direction 0 before direction n-1 and half place it after. Equation (EH7) then determines x_0 as one of the two values w_(n-1) or 1+w_(n-1), respectively. Hence n!/2 direction permutations give the root parity (EH6), and each determines a full geodesic starting on the 00 auxiliary face with the target profile. Reversing these paths gives another n!/2 rooted full geodesics starting on the 11 auxiliary face, with unchanged direction-indexed colors. These two classes are disjoint by starting auxiliary state, yielding n! witnesses. \(\square\)

The result counts rooted, ordered paths. In the absence of any assumptions on c it supplies a uniform positive lower bound for every profile of the extension.
