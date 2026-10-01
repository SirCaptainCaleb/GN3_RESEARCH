# Outside-vertex deficiency equals open blocker-chain deficiency

## Statement

Let H be d-regular on 2d+1+s vertices and let e be a nonspecial edge of global maximum rank d. Relative to any globally longest d-edge path ending in e, if S_y,S_z are the numbers of terminal single blockers and p is the number of path components in the union of the two terminal double-blocker matchings, then U_v=S_v for each terminal v and p=S_y+S_z<=2s. Thus s=0 gives only alternating cycles, s=1 gives one or two open chains, and fixed s gives at most 2s open defects.

## Body


Let H be a d-regular linear 3-uniform hypergraph on n=2d+1+s vertices, where s>=0. Let e={x,y,z} be a nonspecial edge of global maximum rank d, with unique entrance x, and choose a globally longest d-edge path
  P=(g_1,...,g_{d-1},e)
ending in e through x. Put
  W=V(P)\e,
so |W|=2d-2, and let O=V(H)\V(P), so |O|=s.

Fix a terminal v in {y,z}. Every edge f!=e through v must meet W. Indeed, if f met V(P) only at v, then appending f after P would give a (d+1)-edge linear path, contradicting maximality of d.

Since H is linear, the off-v pairs f\{v} over the d-1 edges f!=e through v are pairwise disjoint. Each such pair therefore has either:
- two vertices in W (a double blocker), or
- one vertex in W and one vertex in O (a single blocker).
It cannot have zero vertices in W by the preceding paragraph.

Let B_v and S_v be the numbers of double and single blockers. Then
  B_v+S_v=d-1.
The W-vertices used by these d-1 pairwise-disjoint off-v pairs number exactly
  2B_v+S_v.
Hence the number U_v of W-vertices unused by the double/single blocker pairs is
  U_v=(2d-2)-(2B_v+S_v)
     =2(d-1)-2B_v-S_v
     =S_v.
Thus every single blocker is balanced by exactly one unused precursor vertex.

Moreover distinct single blockers through v use distinct outside vertices, because their off-v pairs are disjoint. Therefore
  S_v<=|O|=s.

Now let M_y,M_z be the double-blocker matchings on W. By linearity they are edge-disjoint, and their union is a graph of maximum degree at most two whose components are alternating paths or even cycles. By the standard path-component identity,
  p=|W|-|M_y|-|M_z|
   =(2d-2)-B_y-B_z.
Using B_v=d-1-S_v gives
  p=S_y+S_z.
Consequently
  p=S_y+S_z<=2s.

Thus the entire open-defect topology is controlled exactly by outside-vertex deficiency: the number of alternating path components equals the total number of terminal single blockers, and is at most twice the number s of vertices outside a longest path.

In particular:
- s=0 forces M_y union M_z to be a disjoint union of alternating even cycles;
- s=1 forces exactly the one-chain/two-chain alternatives from the 12-vertex punctured-Steiner analysis;
- for fixed s, a maximum-rank nonspecial edge has only O(s) open alternating defects regardless of d.
