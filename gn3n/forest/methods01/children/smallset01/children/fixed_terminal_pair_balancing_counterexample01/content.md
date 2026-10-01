# Balanced repartitions need not preserve a prescribed terminal pair

## Statement

For every integer m>=6 there is a boundary tournament H_m with a spanning two-cover X|P, where X is a Hamiltonian four-set and P=(p_1,...,p_m) is a tight path, such that no two-cover of component orders 5,m-1 has its (m-1)-vertex path ending in any ordered pair of distinct vertices from V(P).

Equivalently, every 5|(m-1) repartition in this construction must use at least one vertex of X in the terminal ordered pair of its long component. For m=6, no 5|5 cover has a component whose displayed terminal pair lies entirely in P.

Hence not only preservation of one prescribed terminal pair but preservation of any terminal pair wholly inside the old long path can fail universally. A successful bounded replacement must allow terminal data to mix with the old four-side, or use a different attachment mechanism.

## Body

We first construct a non-Hamiltonian edge-ordered five-set B on Z/5Z with a Hamiltonian four-subset. Color an ordinary edge {i,j} by i+j modulo 5. Each color class is a matching. Order the five color classes as 0<1<3<2<4, and order the two edges within each color class arbitrarily. Declare (u,v,w) tight when the ordinary edge uv precedes vw.

There is no Hamilton five-path. Consecutive edges of a vertex-simple path cannot have the same color, because each color class is a matching. An increasing four-edge Hamilton word would therefore have one of the five increasing color sequences listed below. If the initial vertex is t, the consecutive vertices satisfy v0=t and v_i=c_i-v_(i-1) modulo 5. The following table gives a repeated pair of vertex positions for every starting vertex. Positions are numbered 0,...,4.

Color sequence | t=0 | t=1 | t=2 | t=3 | t=4
0,1,3,2 | (0,4) | (0,4) | (0,4) | (0,4) | (0,4)
0,1,3,4 | (0,1) | (0,3) | (1,2) | (2,3) | (1,4)
0,1,2,4 | (0,1) | (1,4) | (1,2) | (0,3) | (3,4)
0,3,2,4 | (0,4) | (0,4) | (0,4) | (0,4) | (0,4)
1,3,2,4 | (0,3) | (1,4) | (1,2) | (0,1) | (2,3)

Thus no such word has five distinct vertices. This is a fixed five-vertex verification, uniform across the entire construction, not an instance-order search. On the other hand (1,4,2,0) is a Hamilton path on X={0,1,2,4}: its edge colors are 0,1,2, in strictly increasing class order. The omitted vertex of B is 3.

Now take X and m new vertices p1,...,pm. Define the boundary tournament by specifying all reversal pairs on each type of three-set.

On X, use the restriction of B. On any three-set containing two vertices of X and one pi, copy the triples of B with pi replacing vertex 3. In particular every induced X+{pi} is isomorphic to B and is non-Hamiltonian.

On P={p1,...,pm}, order ordinary edges by the lexicographic keys (max{i,j},min{i,j}) and use the resulting edge-order boundary tournament. The displayed sequence (p1,...,pm) is tight since its consecutive ordinary edges strictly increase.

For a three-set containing one x in X and two distinct pi,pj, declare both (pi,pj,x) and (pj,pi,x) tight, and declare their reverses non-tight. For the remaining reversal pair, declare (pi,x,pj) tight exactly when i<j. These choices specify all three reversal pairs consistently. Together with the previous cases they define a boundary tournament on the whole vertex set.

Any tight path ending in two vertices of P contains no vertex of X. Indeed, if it contained one, choose its last occurrence x. Since the last two vertices of the path lie in P, x is followed by at least two vertices pi,pj of P. The consecutive triple (x,pi,pj) is non-tight by construction, a contradiction.

Suppose a two-cover of orders 5,m-1 had its (m-1)-vertex path ending in (p(m-1),pm). That path therefore uses only vertices of P, so it uses m-1 of the m vertices of P. The remaining five-vertex support is X+{pi} for the single unused vertex pi. That support is non-Hamiltonian, contradicting that it is a path of the two-cover. This proves the general assertion. For m=6 either five-path could be the anchored path, so there is no anchored 5|5 cover at all.

The obstruction concerns the specified terminal pair, not balanced covers without that requirement. The displayed X|P is already a two-cover. In particular this construction does not contradict the grand two-cover conjecture or the unanchored order-ten equitable-cover theorem. It rules out proving four-side descent by a universal first-six-vertices replacement that retains the original terminal pair on the growing path. A successful bounded replacement must have more flexible attachment data or use the opposite end in a way that is justified for the actual configuration.