# Bichromatic four-geodesic hub vertices hit every certified antipodal path, with a quantitative density bound

# Bichromatic monochromatic-four-connector hubs form an antipodal separator of certified geodesics

Let n>=5 and let c be ANY ACTIVE reversal-antipodally odd ordered physical three-face binary coloring of Q_n. Let X_c be the genuine certified-center square complex: a physical cube square with free directions {b,c} is included if some actual directed monochromatic four-edge geodesic with middle coordinate pair (b,c) certifies it. The proved global connectedness theorem gives that G=X_c^(1) spans all cube vertices and has minimum degree >=n−1, so its complementary edge set M=E(Q_n)\E(G) is a MATCHING. (These 'uncertified middle-square edges' must be distinguished from physical edges traversed nowhere in ANY monochromatic four-geodesic; the latter potentially smaller dead-edge set is another matching.)

For every cube vertex z let
\[
\mathcal C(z)=\{q∈\mathbb F_2:\text{some actual monochromatic centered four-edge geodesic of color q has middle-pair center square through z}\}.
\]
The centered odd-five-cycle lemma says \mathcal C(z) is nonempty for all z, and NORI reversal oddness implies \mathcal C(\bar z)=1−\mathcal C(z). Put
\[
B=\{z∈Q_n:\mathcal C(z)=\{0,1\}\},
\]
the set of genuinely BICHROMATIC monochromatic-four-connector hubs. It is antipodally invariant.

**THEOREM 1 (CERTIFIED ANTIPODAL-PATH HITTING).** Every ordinary Q_n cube-graph path joining any antipodal vertex pair x,bar x and using ONLY edges from G must meet B. This holds for arbitrary paths, not just Hamming geodesics.

**Proof.** For each physical edge uv∈E(G), choose one actual certified middle square containing uv and a genuine monochromatic centered-four-path witness of that square, of color q. All four vertices of its middle square are eligible centers for the SAME ordered physical window faces and thus have a connector of color q. In particular q∈\mathcal C(u)∩\mathcal C(v). Suppose a G-path from x to bar x avoids B. Every vertex of that path has a nonempty singleton \mathcal C(z)={q_z}. Shared certificates imply q_z=q_{z'} across every path edge, so its singleton bit is constant from x to bar x. But the active NORI antipodal law implies q_{bar x}=1−q_x, contradiction. Thus every certified antipodal path visits B. QED.

**THEOREM 2 (QUANTITATIVE BICHROMATIC-HUB DENSITY).** With M the missing certified-center cube edges,
\[
\boxed{|B|\ge\frac{2^n-2|M|}{n+1}.}
\]
More precisely |B| is even, and its lower bound may be rounded up to the next even integer. In the important DEAD-FREE MIDDLE-SQUARE case M=empty, at least a fraction 1/(n+1) of all cube vertices are bichromatic connector hubs:
\[
\boxed{|B|\ge 2^n/(n+1).}
\]

**Proof.** Sample a uniform root x∈Q_n and a uniform permutation p of all n coordinate directions. The corresponding full antipodal geodesic P(x,p) uses each coordinate once. At its unique step in a direction i, the traversed physical i-edge is uniform among all 2^(n−1) parallel i-edges, so EVERY physical cube edge e is traversed with probability 1/2^(n−1). Hence
\[
\mathbb E\#\{M\text{-edges on }P\}=\frac{|M|}{2^{n-1}}=\frac{2|M|}{2^n}.
\]
Markov's inequality at threshold1 (or union bound) gives
\[
\Pr[P\text{ avoids }M]\ge1-\frac{2|M|}{2^n}.
\]
Every such M-avoiding full antipodal path is a G-path, and by Theorem1 visits B. On the other hand every one of its n+1 vertices is uniformly distributed over Q_n under the joint root-and-permutation sampling, so
\[
\Pr[P\text{ visits }B]\le\mathbb E[\#(V(P)\cap B)]
=\frac{(n+1)|B|}{2^n}.
\]
Combining gives (n+1)|B|/2^n≥1−2|M|/2^n, proving the inequality. B is antipodally invariant and Q_n antipodality has no fixed vertices, hence |B| is even. QED.

**Scope and topology.** The theorem is UNCONDITIONAL for active NORI, using only actual monochromatic four-edge face certificates. It strengthens existence of a bichromatic center (already known) to an antipodal path separator in the physically certified one-skeleton and quantitatively many such centers when the middle-square certificate defect matching is small. It is an actionable set-valued discrete fixed-point obstruction: a connected antipodally paired carrier with locally shared monochromatic certificate colors cannot remain singleton-labeled, and every antipodal path must cross the multivalued locus.

**THE UNRESOLVED GRAND EXTRACTION.** A bichromatic center gives opposite-color short connector witnesses, not a compatible reversed-two-tail complementary-support pair. The hitting property does NOT guarantee monotone monochromatic or one-switch full paths. The remaining target is to orient and synchronize a sequence of these two-color hubs into actual rooted reachability branches with matching reversed two-direction tails.
