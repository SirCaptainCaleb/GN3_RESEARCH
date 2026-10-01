# Universal residual and blocker normal form for punctured-Steiner regular systems

## Statement

Let d>=2 and let H be a d-regular linear 3-uniform hypergraph on 2d+2 vertices. Then the uncovered-pair graph of H is a perfect matching, so H is a one-point puncture of a Steiner triple system on 2d+3 vertices. Suppose moreover that H has global maximum path length d and e={x,y,z} is a nonspecial edge of rank d with unique entrance x. Put R=H-{x,y,z}, and let x*,y*,z* be the uncovered mates of x,y,z. Then:
(1) |V(R)|=2d-1 and |E(R)|=(2d-3)(d-2)/3;
(2) d_R(x*)=d_R(y*)=d_R(z*)=d-2, while every other vertex of R has degree d-3;
(3) for each v in {y,z}, the d-1 edges through v other than e induce a perfect matching F_v on V(R)\{v*};
(4) for every pair {a,b} in F_v, R contains no (d-2)-edge linear path ending at a with a as a last vertex while avoiding b, nor vice versa;
(5) relative to any maximum d-edge path P ending in e, the two terminal double-blocker matchings on W=V(P)\e have union consisting of even alternating cycles together with exactly one or two alternating path components.

## Body

First note that each vertex of H has degree d and hence is paired, across its d incident triples, with exactly 2d distinct other vertices. Since H has 2d+2 vertices, each vertex has exactly one uncovered mate among the other 2d+1 vertices. Symmetry of nonadjacency makes the uncovered-pair graph 1-regular, hence a perfect matching.

Adding a new point infinity and, for each uncovered pair {a,b}, the triple {infinity,a,b}, covers every formerly uncovered pair and every pair involving infinity exactly once. Thus H extends to an STS(2d+3).

Now assume e={x,y,z} is nonspecial of rank d and globally maximum, with unique entrance x. Let x*,y*,z* be the uncovered mates of x,y,z, respectively. Because x,y,z are mutually adjacent inside e, these three uncovered mates are distinct and lie outside e.

Put R=H-{x,y,z}. The union of the three stars at x,y,z has size 3d-2: the edge e is counted three times and every other star edge is distinct by linearity. Since
|E(H)|=(2d+2)d/3,
we obtain
|E(R)|=(2d+2)d/3-(3d-2)
       =(2d-3)(d-2)/3.

For a residual vertex w not among {x*,y*,z*}, the pairs wx,wy,wz are all covered in H, in three distinct edges. Deleting x,y,z removes exactly those three incident edges, so
d_R(w)=d-3.
For x*, there is no edge containing x and x*, while the pairs x*y and x*z are covered in two distinct edges; hence exactly two incident edges are deleted and
d_R(x*)=d-2.
Likewise d_R(y*)=d_R(z*)=d-2.

Fix a terminal v in {y,z}. The d-1 edges through v other than e have pairwise disjoint off-v pairs. They cover exactly the 2d-2 residual vertices other than v*, because v* is the unique vertex outside e not adjacent to v. Hence their off-v pairs form a perfect matching F_v on V(R)\{v*}.

Take {a,b} in F_v, corresponding to the edge f={v,a,b}. If R contained a (d-2)-edge linear path Q ending at a with a as a last vertex and avoiding b, then Q,f,e would be a d-edge linear path ending in e through the entrance label v. Since e is nonspecial of rank d with unique entrance x, this is impossible. The same argument interchanging a,b proves the symmetric prohibition.

Finally let P=(g_1,...,g_{d-1},e) be any globally longest d-edge path ending in e, and put W=V(P)\e, so |W|=2d-2. There is a unique vertex o outside P.

For a terminal v, the d-1 edges through v other than e have disjoint off-v pairs covering all vertices outside e except v*. If v*=o, all d-1 pairs lie in W, so the double-blocker matching M_v has size d-1. If v*!=o, exactly one pair uses o and a vertex of W, while the remaining d-2 pairs lie wholly in W; hence |M_v|=d-2.

The outside vertex o cannot be the uncovered mate of both y and z because the uncovered-pair graph is a matching. Therefore
(|M_y|,|M_z|) is one of
(d-1,d-2), (d-2,d-1), (d-2,d-2).
By the certified alternating-blocker lemma, the number p of alternating path components in M_y union M_z, isolated vertices included, is
p=|W|-|M_y|-|M_z|
 = (2d-2)-|M_y|-|M_z|.
Thus p=1 in the first two cases and p=2 in the last.

So the one-or-two-open-chain topology from the 12-vertex proof is universal throughout the entire punctured-Steiner family; only the cycle lengths grow with d.
