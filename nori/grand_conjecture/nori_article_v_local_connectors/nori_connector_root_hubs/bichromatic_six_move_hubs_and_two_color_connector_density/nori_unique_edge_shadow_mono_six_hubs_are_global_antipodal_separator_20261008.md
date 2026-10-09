# Every certified antipodal route in unique-color NORI crosses a genuine monochromatic six-geodesic hub

# Topological global consequence: monochromatic six-geodesic hubs meet every certified antipodal path in the unique-color edge-shadow regime

Let n>=10 and let c be an ACTIVE NORI binary coloring of physical ordered three-faces. Assume the GLOBAL unique-color certified-square edge-shadow case B: no physical cube edge receives square certificates from monochromatic centered four-edge connectors of both colors. Let X_c be the genuine certified-center-square complex, let G_c=X_c^(1) be its spanning cube subgraph, and write M=E(Q_n)\E(G_c). By proved NORI theorems, M is an antipodally invariant matching, G_c is connected, and every vertex has certified-center degree at least n−1. Define the bichromatic hub set
\[
B=\{z: \text{genuine centered monochromatic four-edge connectors of BOTH colors exist at z}\},
\]
and the MONOCHROMATIC SIX-HUB set
\[
H_6=\{z: \text{there exists an ACTUAL monochromatic six-edge cube geodesic with ALL FOUR ordered-three-face windows physically containing z}\}.
\]

**THEOREM 1 (unavoidable monochromatic six-hub separator).** Under the stated assumptions,
\[
\boxed{B\subseteq H_6.}
\]
Moreover every G_c-graph path from any cube vertex x to its antipode bar x intersects H_6. In particular, for EVERY root x∈Q_n there exists a FULL antipodal n-edge cube geodesic from x to bar x (whose edges all belong to G_c) that passes through at least ONE vertex z∈H_6.

**Proof.** At each bichromatic hub z, the no-common-edge assumption splits the incident certified directions into two classes A,B, each of size at least2, of total size at least n−1. Since n>=10, the larger class has cardinality at least5. The proved five-majority odd-cycle theorem (Item nori_majority_five_bichromatic_hub_odd_cycle_forces_monochromatic_six_20261008) constructs a genuine monochromatic six-edge geodesic through z. Thus B⊆H_6.

The separate, unconditional bichromatic-hub antipodal separator theorem (Item nori_bichromatic_mono_four_hubs_hit_every_certified_antipodal_path_density_20261008) states that EVERY G_c-path from x to bar x meets B, since physical square certificates share a common monochromatic color across each G_c-edge, but the hub singleton color label flips under antipodality. Such a path consequently meets H_6.

Finally the general cube matching-avoidance theorem (Item nori_matching_avoidance_every_root_full_geodesic_20261008) says any cube matching that is NOT the entire set of parallel edges of one coordinate can be avoided by SOME full antipodal geodesic from ANY prescribed root x. Our matching M cannot be that entire parallel matching because G_c is CONNECTED and would otherwise split into opposite coordinate facets. Therefore from every x there is a full M-avoiding geodesic P(x), which is a G_c-path. It meets H_6. QED.

**THEOREM 2 (quantitative density of monochromatic six-hubs).** The same model satisfies
\[
\boxed{|H_6|\ge |B|\ge
\frac{2^n-2|M|}{n+1}.}
\]
Both hub sets are antipodally invariant. In the special case M=∅, at least a fraction 1/(n+1) of all Q_n vertices are centers of GENUINE monochromatic six-edge geodesics:
\[
|H_6|\ge 2^n/(n+1).
\]

**Proof.** Apply B⊆H_6 to the existing quantitative bichromatic-hub separator bound. Global antipodal reversal carries every monochromatic six-edge path through z to a complementary-color monochromatic six-edge path through bar z; hence H_6 is antipodally invariant. QED.

**Conceptual topological result.** This produces, in one structural branch of arbitrary ACTIVE NORI colorings, a physical Q_n antipodal hitting set of ACTUAL SIX-edge monochromatic paths. Its strength is global and root-mobile: the center of such a path is encountered by a fully spanning antipodal route from EVERY starting cube root, but the mono-six direction word may not match the route's entering/leaving used-direction support, and the route's unrelated local certificates need not share the mono-six color. The unproved GRAND-EXTRACTION step is to synchronize at least one of these mono-six hubs with a full legal root/terminal-memory geodesic so that its entire ordered-three-face word has <=1 switch. This theorem does not assert such synchronization.
