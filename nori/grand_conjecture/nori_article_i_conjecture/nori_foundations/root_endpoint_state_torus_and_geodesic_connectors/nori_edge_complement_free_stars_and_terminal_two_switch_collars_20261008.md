# Single-root reachability collision and exact two-switch terminal collar

# Complement-free geodesic-reachability stars and exact terminal collars (edge case)

Let n>=3 and let c be a binary coloring of the **undirected edges** of Q_n satisfying c(bar e)=1-c(e). For a vertex v and q in {0,1}, define A_q(v) as the family of coordinate supports S subseteq [n] for which there is a monochromatic q-geodesic from v to v XOR S. Include the empty support in both A_q(v), and put U(v)=A_0(v) union A_1(v).

**Theorem 1 (one-root antipodal collision criterion).** The following statements are equivalent:

(a) The coloring has a monochromatic antipodal geodesic.

(b) For some v and some S subseteq [n], both S and [n]\S belong to U(v).

(c) For some v, U(v) contains a complementary pair.

Indeed, if S and its complement are reachable from v by monochromatic paths of colors q and r, reverse the first path and follow the second. Since the direction supports are disjoint, this is an antipodal geodesic with at most one color change. If q=r it is already monochromatic. If q!=r, suppose the first block is q and the second block is 1-q. Starting at the switch vertex, take the latter block followed by the antipodal image of the first block; antipodal oddness colors both pieces 1-q, and their disjoint direction supports give a full antipodal geodesic. Conversely a monochromatic antipodal geodesic from v to bar v witnesses S=empty and its complement [n] in U(v).

Consequently, under a hypothetical counterexample, U(v) is complement-free for **every** v. Thus |U(v)|<=2^(n-1). Still, U(v) contains the empty set and every singleton (an edge always has one of the two colors). This replaces the two-antipodal-roots intersection criterion by one root's union of two actual geodesic-reachability families. Crucially, U(v) cannot be replaced by ordinary graph-component reachability, which forgets disjoint coordinate supports.

**Theorem 2 (rank n-1 exclusion and terminal two-switch collars).** In a hypothetical counterexample, U(v) contains no (n-1)-element set, for any v. Moreover, if P is any monochromatic q-geodesic of length n-2, with endpoints x,y and unused coordinates a,b, then all four fresh-coordinate edges at x and y have color 1-q. Their antipodal opposite edges show that the two exterior {a,b}-squares at x and y are colored 1-q on the two edges incident with x or y respectively, and q on the two edges incident with x XOR {a,b} or y XOR {a,b}. Every full antipodal geodesic obtained by attaching the two missing directions at the two endpoints of P, preserving P as a contiguous subpath, has **exactly two** color changes.

*Proof.* A q-geodesic of length n-1 has just one unused coordinate i. Its two possible extending edges, one at each endpoint, are antipodal and have opposite colors. Thus one extends the path monochromatically to length n. This proves rank n-1 exclusion. For P of length n-2, a q-colored fresh edge at either endpoint would create a q-geodesic of length n-1, contradiction; all four fresh edges therefore have color 1-q. Because bar x=y XOR {a,b} and bar y=x XOR {a,b}, antipodal oddness forces the other two edges of each exterior square to have color q. If both unused directions are attached at one endpoint, the three color blocks are q,...,q;1-q;q (or reversed). If one is attached at each endpoint, they are 1-q;q,...,q;1-q. Each completion has exactly two switches.

**Topological implication and gap.** On the root-endpoint torus, a counterexample forces every diagonal-origin monochromatic reachable state to lie at rank <=n-2. All rank n-2 reachable states are shielded by opposite-color outgoing covers and have an exact two-switch completion collar. A topological contradiction would require a theorem excluding a globally consistent family of such shields under the square-edge consistency and antipodal symmetry of the physical cube. Complement-freeness and torus topology alone have not been proved sufficient. These two theorems do not close the edge conjecture, and therefore do not close ordered-three-face NORI.
