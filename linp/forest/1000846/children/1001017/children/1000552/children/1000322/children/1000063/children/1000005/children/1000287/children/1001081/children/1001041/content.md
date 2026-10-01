# Colored-complement decomposition of the general punctured-Steiner residual

## Statement

In the residual system R from efe44a01f2dc, every unordered pair of residual vertices belongs to exactly one of five disjoint classes: it is covered by a triple of R; it belongs to exactly one of the three off-star matchings F_x,F_y,F_z induced by the deleted vertices x,y,z; or it belongs to the surviving leave matching L_R of size d-2. Equivalently, the complement of the 2-shadow of R is the edge-disjoint union F_x∪F_y∪F_z∪L_R, where |F_x|=|F_y|=|F_z|=d-1 and |L_R|=d-2.

## Body

Let H be d-regular on 2d+2 vertices, let e={x,y,z}, and put R=H-{x,y,z} as in efe44a01f2dc.

Because H has a perfect-matching leave, after deleting x,y,z and their three distinct leave-mates x*,y*,z*, the leave pairs that remain entirely inside V(R) form a matching L_R of size
(d+1)-3=d-2.

For each q∈{x,y,z}, the d-1 edges through q other than e induce an off-star perfect matching F_q on V(R)\{q*}, hence |F_q|=d-1.

These four matchings are pairwise edge-disjoint and are also disjoint from the 2-shadow of R. Indeed:
- a pair in F_q is already covered in H by a triple through q, so linearity forbids it from occurring in any residual triple or in another deleted star;
- a leave pair is uncovered in H and therefore lies in neither a residual triple nor any star matching.

It remains only to count. From efe44a01f2dc,
|E(R)|=(2d-3)(d-2)/3,
so the 2-shadow of R contains
3|E(R)|=(2d-3)(d-2)
pairs.

The four complementary matchings contribute
3(d-1)+(d-2)=4d-5
pairs.

Their total is
(2d-3)(d-2)+(4d-5)
=2d^2-3d+1
=(2d-1)(d-1)
=C(2d-1,2).

Thus every residual pair appears in exactly one of these classes. Hence
E(complement of shadow_2(R))=F_x disjoint-union F_y disjoint-union F_z disjoint-union L_R.

In particular the residual obstruction is equivalently a partial Steiner triple system whose leave graph has a canonical proper four-color decomposition into three near-perfect matchings (each missing one distinguished high vertex) and one perfect matching on the 2d-4 low vertices.