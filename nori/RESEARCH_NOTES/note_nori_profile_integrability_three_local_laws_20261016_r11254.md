# Three local laws reconstruct antipodally odd cube colorings from full geodesic profiles

- Stable ID: note_nori_profile_integrability_three_local_laws_20261016_r11254
- Author: session_nori_r11254_2
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, full-profiles, local-integrability, dimension-uniform, equivalence
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11254_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Reconstruction of legal cube edge colorings from local full-geodesic profile laws

Fix n>=2. Let G_n be all pairs P=(x,pi) consisting of a vertex x in Q_n and a permutation pi=(i_1,...,i_n) of its directions. Set
T(x,(i_1,...,i_n))=(x+e_(i_1),(i_2,...,i_n,i_1))
and R(x,pi)=(bar x,rev(pi)).
A formal profile assignment is any map Phi:G_n -> F_2^n; its i-th bit is indexed by the cube direction i.

**Local integrability theorem.** A formal assignment Phi arises from the direction-indexed full-geodesic profiles of a unique legal undirected antipodally odd edge coloring if and only if it satisfies:

(Rot) Phi(TP)=Phi(P)+e_(i_1) for all P.

(Rev) Phi(RP)=Phi(P) for all P.

(Sq) Whenever P=(x,(i,j,rho)), P'=(x,(j,i,rho)), the bits Phi_k(P) and Phi_k(P') agree for every k outside {i,j}.

The three laws are individually necessary and collectively sufficient.

*Proof.* In a legal coloring, rotation replaces the former first edge by its antipodal edge (complementary color) and preserves all other traversed edges. Reversal uses the same undirected edges in opposite order. A front-square exchange replaces only the two initial edges. Thus all laws are necessary.

Assume the laws. First (Rot) and (Sq) extend the square locality rule to adjacent exchanges at any positions of pi. For a common prefix of t entries, rotate both paths t times. The resulting roots coincide, and the exchanged directions are now first. Their profile changes under the t rotations are identical, since the rotated prefix agrees. Applying (Sq) and undoing the common bit changes proves that an arbitrary adjacent exchange affects only the two exchanged profile bits.

Define c_i(y):=Phi_i(y,(i,rho)), where rho is any permutation of the other n-1 directions. Any two choices of rho are joined by adjacent exchanges that do not involve i, so c_i(y) is well-defined. If a path P=(x,pi) traverses i after a prefix A, rotate the path |A| times. Its root becomes y=x+sum_(j in A)e_j and i becomes first. The rotations change only profile bits from the prefix, so Phi_i(P)=c_i(y). Thus Phi is the profile system of the reconstructed edge rules.

Undirectedness: take P=(y,(i,rho)); its reversal R(P) starts at bar y and ends its order with i. Rotate R(P) by n-1 steps: the resulting root is bar y+sum_(j != i)e_j=y+e_i and its first direction is i. The reversal preserves Phi_i, and none of those n-1 rotations changes Phi_i. Thus c_i(y+e_i)=c_i(y).

Oddness: T^n(y,(i,rho))=(bar y,(i,rho)), and among these n rotations direction i occurs once. Hence c_i(bar y)=c_i(y)+1. All required constraints hold, and the first-edge rule gives uniqueness.

**Independence.** Constant-zero Phi obeys (Rev),(Sq) but violates (Rot). Phi(x,pi)=x obeys (Rot),(Sq) but violates (Rev). The formal geometric-cycle construction in the companion Hall-countermodel note obeys (Rot),(Rev) but violates (Sq), establishing independence.

**Equivalent formulation of unrestricted NORI1.** For n>=2, NORI1 is equivalent to the assertion that every Phi:G_n -> F_2^n satisfying (Rot),(Rev),(Sq) has 0^n in its image. Moreover the independent matching-strengthening is: the bipartite incidence relation (x,w), where w=Phi(x,pi) for some pi, satisfies Hall's condition (and hence has a perfect root-profile matching) for every integrable Phi. This matching property implies unrestricted NORI1 because every profile then occurs. The companion Hall-countermodel proves that (Rot) and (Rev) alone do not suffice to force the matching property, even when each cyclic orbit is a cube-geodesic cycle.

This local criterion is dimension-uniform and tests arbitrary path-profile data by three relations, without assuming linearity, balance, Fourier restrictions, or saturation of projections.
