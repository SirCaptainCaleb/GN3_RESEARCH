# Potential-charged ascending edges: transversals, central packing, and deficit spacing

## Statement

Let v have p=φ(v). For every potential-charged ascending nonspecial edge e={x,v,u} with v terminal and φ(u)>=p, every p-edge path ending at v contains x or u; for distinct such edges the pairs {x,u} are pairwise disjoint.

If C_Q(v) denotes the charged edges of rank at most Q, where ceil((p+2)/2)<=Q<=p, then
|C_Q(v)|<=4Q-2p-1.
Equivalently, if their ranks are q_1<=...<=q_k, then q_i>=ceil((2p+i+1)/4).

Fix now a maximum p-edge path P=(g_1,...,g_{p-1},h) ending at v and restrict to charged edges e={x,v,u} distinct from h with E(P)∩e represented only by the entrance contact x and v. For two such edges e_1,e_2 whose entrance-contact blocks [a(e_i),b(e_i)] are separated by at least one path edge, one has
b(e_2)-a(e_1) >= p-φ(e_2)+3
after ordering the contacts from left to right. Consequently, for every D>=0, the number of clean entrance-only charged edges of rank at most p-D is O(p/(D+1)+1), with an absolute implied constant.

## Body

For e={x,v,u} of rank q, terminality of v gives q<=p and ascendingness gives φ(x)=q-1<p. If a p-edge v-ending path P contained neither x nor u, then e would not lie on P and could be appended through v, creating a path ending in e longer than q, contradiction. Thus every such P contains x or u. Distinct charged edges through v have disjoint non-v vertex pairs by linearity, yielding pairwise-disjoint two-point transversals.

Fix a p-edge path P ending at v and, for each charged edge e of rank at most Q, choose as witness x if x lies on P and otherwise u. If x is the witness, then φ(x)=q-1. By the half-path endpoint-potential lemma, a private x in g_i satisfies p-q+2<=i<=q-1, while a joint x=g_i∩g_{i+1} satisfies p-q+1<=i<=q-1. If u is the witness, then e meets P exactly in u and v. Prefix and suffix appendability give p-q+1<=i<=q-1 when u is private in g_i, and p-q<=i<=q-1 when u=g_i∩g_{i+1} is a joint. Therefore, for q<=Q, every possible witness lies among the private vertices in edge positions p-Q+1 through Q-1 or the joints in positions p-Q through Q-1. These sets contain (2Q-p-1)+(2Q-p)=4Q-2p-1 vertices in total. The witnesses are distinct, so |C_Q(v)|<=4Q-2p-1. If the charged-edge ranks are q_1<=...<=q_k, then i<=|C_{q_i}(v)|<=4q_i-2p-1, hence q_i>=ceil((2p+i+1)/4).

For the spacing statement, let P=(g_1,...,g_{p-1},h) be a maximum path ending at v. Consider two clean entrance-only charged edges e_i={x_i,v,u_i} with ranks q_i and entrance-contact blocks [a_i,b_i], ordered so a_1+2<=b_2. The prefix through the first entrance, followed by e_1, the last edge h, and the reversed suffix down to the second entrance forms a linear path ending at x_2. Since φ(x_2)=q_2-1, its length gives
a_1+p-b_2+2 <= q_2-1,
hence b_2-a_1 >= p-q_2+3.

When both contacts are private this specializes to the sharper two-chord inequalities with slack variables s_i=q_i-1-j_i. For arbitrary private or joint contacts, greedily select a constant fraction whose one- or two-edge contact blocks are pairwise separated by at least two indices. If every selected edge has rank at most p-D, successive selected blocks advance by at least D+3. Thus there are O(p/(D+1)+1) selected contacts and hence the same order bound for the whole clean entrance-only family.

This result gives structural restrictions on charged edges but does not assert a final local bound.