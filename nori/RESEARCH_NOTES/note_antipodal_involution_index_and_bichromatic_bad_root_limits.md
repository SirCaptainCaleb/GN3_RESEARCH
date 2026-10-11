# Antipodal-involution index differences and bichromatic bad-root limitations

- Stable ID: note_antipodal_involution_index_and_bichromatic_bad_root_limits
- Author: NORI editorial extraction; mathematical proofs from cited original composition
- Primary home: subsection:two_sided_helly_root_sheets_and_high_index_support_selection
- Labels: obstruction, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:two_sided_helly_root_sheets_and_high_index_support_selection, exact version 1
- subsection:two_sided_helly_root_sheets_and_high_index_support_selection, exact version 2

## Research note

# Editorial scope and exact provenance

Full exact source of topological and root-hub obstructions. Positive macroscopic-cut Tucker and two-sided Helly theorems remain in the Subsection manuscript.

Copied verbatim from Subsection `two_sided_helly_root_sheets_and_high_index_support_selection`, publication composition v1. The original complete composition remains retrievable.

## The two antipodal involutions have radically different indices: a concrete mobile-root obstruction

Let n≥8 be EVEN and fix rho∈F2^n. Take the valid active NORI coloring
\[
c_\rho(F,(a,b,c))=\bigoplus_{i\notin\{a,b,c\}}(F_i\oplus\rho_i),
\tag{1}
\]
independent of the ordered free triple's orientation. It is antipodally reversal odd because the number n−3 of fixed exterior coordinates is odd. For any full direction permutation p, let B_p⊆Q_n be the set of starting roots x whose ACTUAL full p-geodesic has opposite first and last ordered three-face colors.

**Theorem (complete topology of the same-order balanced-root locus).** For every full order p=(p1,...,pn),
\[
\boxed{
B_p=\Bigl\{x:\bigoplus_{j\in\{1,2,3,n-2,n-1,n\}}
(x_{p_j}\oplus\rho_{p_j})=0\Bigr\}.
}
\tag{2}
\]
Thus, as an induced physical cube-edge graph, B_p is exactly the disjoint union of 32 full coordinate (n−6)-cubes, indexed by the even six-bit assignments to the FIRST and LAST three directions of p. Under physical root complement x↦bar x, these 32 components are paired, with **no antipodally invariant connected component**. In particular:
- Every x∈B_p has bar x∈B_p, so **same-order antipodal root-pair endpoint synchronization is perfect** for this coloring.
- Yet no edge of the root cube in any of the six distinguished directions joins two B_p vertices; thus there is NO physical cube path lying entirely in B_p from x to bar x.
- The geometric cubical realization of B_p has an equivariant continuous map to S⁰, by assigning a sign to the two members of each paired component. Consequently the cohomological index under PHYSICAL ROOT complement is **zero**, even though the separate fixed-root PERMUTATION-REVERSAL carrier has topological index at least n−3.

**Proof.** Put s_i=x_i⊕rho_i. Along a p-geodesic from x, the initial physical ordered face has fixed exterior coordinates p4,...,pn, so
\[
w_1=\bigoplus_{j=4}^n s_{p_j}.
\]
The terminal physical ordered face has fixed exterior coordinates p1,...,p(n−3), all of which have been flipped once, hence
\[
w_{n-2}=(n-3\bmod2)\oplus\bigoplus_{j=1}^{n-3}s_{p_j}
=1\oplus\bigoplus_{j=1}^{n-3}s_{p_j}.
\]
Therefore
\[
w_1\oplus w_{n-2}
=1\oplus\bigoplus_{j\in\{1,2,3,n-2,n-1,n\}}s_{p_j},
\]
since the middle direction positions 4,...,n−3 appear twice and cancel. This is one precisely when the six-bit parity is zero, proving (2).

Within B_p the six distinguished starting bits can never change along a physical cube edge, because flipping one of them changes their parity from even to odd. All n−6 middle root bits are unconstrained, so every even assignment of the six distinguished bits defines an entire connected (n−6)-cube, and no edge connects different assignments. There are 2^5=32 even assignments. Physical antipodality complements all six distinguished bits; complementing SIX bits leaves parity even and sends every six-bit pattern to a DISTINCT pattern. Hence components occur in antipodal pairs and admit a componentwise ±1 equivariant map to S⁰. This proves all claims. \(\square\)

**Why this matters for the topology-first NORI program.** The previously proved same-order joint endpoint-balance theorem \`nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008\` establishes actual full-path packet synchronization at x and bar x for all n≥10, and the high-index permutohedral theorem gives large index under DIRECTION-ORDER REVERSAL at each fixed x. Neither fact alone supplies an antipodally connected set of physical roots for a fixed order: the full-parity coloring realizes both phenomena while B_p has physical-root antipodal index ZERO.

The two involutions are categorically different:
(i) π↦rev π at fixed root x acts on a HIGH-INDEX permutohedral sphere; and
(ii) x↦bar x at fixed permutation π acts on a possibly disconnected ROOT-cube endpoint-balance locus.
They commute but their cohomological indices do NOT transfer. A grand proof must use legitimate root/order transition **cells coupling the two actions**, or the exact color-free reversed-two-tail support extraction, rather than infer physical-root connectedness from permutohedral high index or antipodal endpoint balance alone.

The construction is NOT a grand counterexample: by the already proved three-residue-chain affine theorem, each full permutation admits eight FULL MONOCHROMATIC roots elsewhere. It is a topological obstruction to a proposed fixed-order root-connection lemma, not a failure of NORI.

## Elevation: extremely bichromatic physical hubs can both be bad roots

The same valid parity NORI coloring (1) proves a sharper, more physical obstruction to a topological one-hub extraction.

**Theorem 2 (antipodal pairs of highly overlapping bichromatic hubs without good rooted full paths).** Let n≥8 be EVEN, and let \(i\in[n]\) be any coordinate. Put
\[
z=\rho\oplus e_i.
\]
Then:

1. At the physical vertex z, **every** middle-direction square involving i is a genuine MONOCHROMATIC 4-edge connector square of color 0 (some appropriate outer directions certify it). Every middle-direction square NOT involving i is a genuine MONOCHROMATIC 4-edge connector square of color 1. More precisely, every unordered coordinate pair \(\{i,j\}\) is color-0-certified, every pair \(\{j,k\}\subseteq[n]\setminus\{i\}\) is color-1-certified.
2. Consequently every physical incident cube edge in direction \(j\ne i\) has **BOTH** colors of genuine centered-mono4 square certificates. The edge in direction i has at least a color-0 certificate. So z is a strongly bichromatic hub with at least n−1 **doubly certified incident physical edges**; its antipode \(\bar z\) enjoys the same property with the two colors interchanged.
3. Nevertheless, for **every possible full direction permutation p**, BOTH actual rooted full antipodal geodesics from z and from \(\bar z\) have at least
\[
\boxed{D(z,p)=D(\bar z,p)\ge n-5\ge3}
\tag{8}
\]
ordered-three-face color changes. In particular NEITHER bichromatic hub supports any one-change FULL geodesic, despite its abundant opposite-color square overlaps.
4. In dimensions n≥8 the Kneser-strengthened theorem \`nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008\` also supplies a *single identical complete direction permutation* p for which both z and bar z have opposite first/last face colors. These actual simultaneously endpoint-balanced paths still have at least n−5 changes.

**Proof.** At z the exterior difference \(z\oplus\rho\) has bit1 ONLY in direction i. For any physical ordered three-face THROUGH z whose free direction set is T, parity coloring (1) therefore assigns 0 when i∈T and 1 when i∉T, independent of the free direction order. A centered 4-edge connector with ordered directions (a,b,c,d) has two physical ordered three-face windows through z with free triples \(\{a,b,c\}\) and \(\{b,c,d\}\). They are BOTH color0 when the special i lies in the common inner pair \(\{b,c\}\); they are BOTH color1 when the four directions avoid i. All required distinct outer coordinates exist since n≥8. This proves (1) and the first assertions of (2). Antipodal reversal gives the claims at bar z.

For an arbitrary rooted full order p, use the exact rank-parity switch formula proved in \`nori_even_parity_bad_root_maximal_permutohedral_index_linear_radius_no_go_20261008\`:
\[
s_j(z,p)=1\oplus \mathbf1_{\{p_j=i\}}\oplus\mathbf1_{\{p_{j+3}=i\}},
\quad j=1,\ldots,n-3.
\]
Because i occurs at exactly ONE position in the permutation, at most TWO of the n−3 switch bits can be zero (those with i at position j or j+3). Hence at least n−5 switch bits equal1. At bar z the root-difference bit vector relative to rho is the complement of the singleton support, and both comparison terms \(s_{p_j},s_{p_{j+3}}\) are complemented, so their XOR is unchanged. Therefore the switch vectors of the two antipodal rooted paths are identical, proving (8). The final endpoint-balance claim follows from the Kneser theorem as already established. \(\square\)

**Sharp topological lesson.** Local *bichromatic hub overlap* can be nearly maximal at BOTH antipodal endpoints, and same-order endpoint-opposed packets can coexist at the pair, while every rooted full path at those physical vertices remains catastrophically multi-switch. Consequently neither the local doubly-certified-edge alternative nor fixed-antipode-pair permutohedral high index can be a universal direct extraction theorem. Successful grand closure must engage a third/moving root, a certificate-preserving global root-order orbit, or exact complementary-support monochromatic witness intersection elsewhere. The obstruction is a valid NORI coloring that DOES have good full paths at other roots; no grand counterexample is claimed.
\n\n**Direct certificate for part (4).** The shared endpoint-opposed order in this explicit parity example needs no appeal to the general Kneser theorem: choose any full permutation placing the unique exceptional direction i in one of the MIDDLE positions 4,...,n−3 (available for n≥8). Formula (2) then assigns even parity zero to the six first/last position bits at root z; the antipodal root has the same even parity because six bits are complemented. Hence both rooted full paths have opposite endpoint colors in that identical direction order. Their lower bound n−5 on internal switches continues to apply. This gives a completely explicit obstruction certificate.

The strong antipodal index of an ambient path complex does not guarantee a selector into the low-dimensional subset of compatible terminal memories. A valid proof must provide that selector or a replacement certificate.

Additional extracted proof/scope from two_sided_helly_root_sheets_and_high_index_support_selection, source composition v2

THEOREM 4 (the universal index-FOUR CEILING: short physical root sheets cannot supply an index-n proof). Assume the GRAND conjecture FAILS, hence no admitted path is full, U is off the diagonal and swap acts FREELY. Let U_3 be the union of boxes B(P) for length-THREE (one-window) paths. These paths are automatically admitted for EVERY ordered triple, root, and physical exterior assignment. Consequently
 U_3 = ⋃_(W⊂[n], |W|=3; exterior bits ε∈{0,1}^([n]\W))
        F_W(ε) × F_W(1−ε),
where F_W(ε) is the full 3-dimensional root coordinate face with bits ε fixed outside W. This is coloring-independent.

Put δ(a,b)=b−a. Each 3-path box has δ_i=±1 outside its three free directions and arbitrary δ_i∈[−1,1] in those three directions. Hence δ(U_3) is PRECISELY the THREE-SKELETON X_3=(∂[−1,1]^n)^(3) of the centrally antipodal cube boundary. The map
  s(δ)=((1−δ)/2,(1+δ)/2)
is an equivariant section X_3→U_3 of δ. The homotopy keeping δ fixed and moving the midpoint (a+b)/2 linearly to (1/2,...,1/2) remains IN THE ORIGINAL BOX: outside W the two bits are already complementary endpoints, while inside W both coordinates are free. Thus U_3 Θ-equivariantly STRONGLY deformation retracts onto the section s(X_3).

The free antipodal three-skeleton X_3 has cohomological Z2 index EXACTLY 3 for n>=4. Upper bound: dim X_3=3. Lower bound: X_3/Θ is the 3-skeleton of ∂[−1,1]^n/Θ≅RP^(n−1), with its ordinary quotient cubical CW structure. Inclusion of a CW 3-skeleton into RP^(n−1) induces an INJECTION in H³(F2), so the third power of the first antipodal-cover class survives.

Now every LONGER admitted path (k>=4) has root-sheet dimension m(k)<=2, so B(P) has dimension at most FOUR (k=4:4; k=5:2; k>=6:0). The finite union U is a Θ-invariant cubical CW complex obtained by attaching to U_3 ONLY cubical cells of dimension <=4 (some attachments may share faces), hence its free-action quotient (U/Θ,U_3/Θ) has no relative cochains above degree4. Therefore H^j(U/Θ,U_3/Θ;F2)=0 for j>=5. Since U_3/Θ≃X_3/Θ has no cohomology above degree3, the long exact pair sequence gives
   H^j(U/Θ;F2)=0 for ALL j>=5.
So ind_Z2(U)<=4. Conversely U_3⊂U has w_1^3≠0, so ind_Z2(U)>=3. By equivariant nerve equivalence E≃_Θ U,
   3 <= ind_Z2(E) <= 4.
This is UNIFORM in cube dimension n and in the physical NORI coloring under the grand no-closure assumption.

**CRUCIAL TOPOLOGICAL CONSEQUENCE.** The universal 3-face geometry furnishes exactly a genuine index-3 antipodal base, and longer fixed-window root sheets can raise it at most to index4. For n>=5, the exact signed-unused Tucker closure criterion demands index>=n to force a zero in R^n. Therefore NO argument operating solely on the static two-sided root-invariance boxes of certified <=1-switch paths can provide such a high-index proof. To reach the unrestricted GRAND NORI conjecture, one MUST adjoin genuinely NEW topological cells coming from ORDER/PREFIX EXCHANGES, WITNESS-PRESERVING TRANSPORT, root/support memory holonomy, or higher-dimensional compatible repairs whose equivariant topology is not captured by the boxes. The theorem is an exact constructive carrier and an exact sharp dimensional NO-GO, not a counterexample to grand NORI.
