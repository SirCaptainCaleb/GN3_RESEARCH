# A two-vertex companion around an inseparable increasing triple has a three-way barrier normal form

## Statement

Let G be edge-orderable and let A|{x,y} be a spanning two-cover, with A increasing and three consecutive vertices (a,b,c) of A pairwise inseparable by spanning two-covers. Let E_in be the path edge immediately before a when it exists, and formal -infinity if a is the first vertex of A; let E_out be the path edge immediately after c when it exists, and formal +infinity if c is the last vertex of A. Then at least one of the following holds. (L) Both companion labels are blocked on the left: az<E_in for z=x,y. (R) Both are blocked on the right: E_out<zc for z=x,y. (A) After possibly interchanging x,y, the strict inequalities ay<E_in<ax, xb<ab<bc<yb, yc<E_out<xc, and yc<xy<ax all hold. In particular the triple (a,b,c) cannot itself be one component of a spanning 3|2 two-cover.

## Body

Apply astra005twovertexhall to the cut a|b and to the cut b|c. For the first cut define L_0={z:E_in<az} and R_0={z:zb<bc}; for the second define L_1={z:ab<bz} and R_1={z:zc<E_out}. Each pair (L_0,R_0) and (L_1,R_1) has no distinct-label matching.

Because ab<bc, every z in {x,y} belongs to R_0 union L_1: if bz<bc then z is in R_0, while otherwise bc<bz and hence ab<bz, so z is in L_1.

If L_0 is empty, outcome (L) holds. If R_1 is empty, outcome (R) holds. Assume neither is empty. Then R_0 cannot be empty: otherwise the covering relation R_0 union L_1={x,y} gives L_1={x,y}, and the Hall obstruction for the second cut with nonempty R_1 would be violated. Similarly L_1 cannot be empty. Thus both sides of each Hall pair are nonempty, so the exact 2-by-2 Hall conclusion gives L_0=R_0={x} for one label x and L_1=R_1={y} for one label y. Since R_0 union L_1 contains both companion labels, x and y are distinct.

The singleton identities translate directly into ay<E_in<ax, xb<bc<yb, xb<ab<yb with the sharper middle chain xb<ab<bc<yb because x is not in L_1 and y is in L_1, and yc<E_out<xc. More explicitly, x not in L_1 gives xb<ab, while y not in R_0 gives bc<yb.

It remains to locate the companion edge xy. If ax<xy, then the increasing path obtained by appending x,y to the prefix ending at a, together with the inherited suffix beginning at b, is a spanning two-cover separating a and b, contradiction. Hence xy<ax. If xy<yc, then the inherited prefix ending at b together with the increasing path (x,y,c,...) is a spanning two-cover separating b and c, contradiction. Hence yc<xy. This proves outcome (A).

Finally suppose A=(a,b,c), so E_in=-infinity and E_out=+infinity. Then L_0={x,y}, so (L) is impossible, and R_1={x,y}, so (R) is impossible. Outcome (A) also requires L_0 and R_1 to be singletons. Contradiction. Thus no spanning 3|2 two-cover can have the inseparable triple as its three-vertex component. ∎