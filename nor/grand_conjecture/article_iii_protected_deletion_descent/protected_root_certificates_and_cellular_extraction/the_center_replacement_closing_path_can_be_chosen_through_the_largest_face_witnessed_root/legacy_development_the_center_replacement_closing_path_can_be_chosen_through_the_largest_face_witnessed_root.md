# The center-replacement closing path can be chosen through the largest-face witnessed root — preserved pre-item development

## Development

## The center-replacement closing path can be chosen through the largest-face witnessed root

Continue with the one-root-per-face Sperner carrier of root §146.

Choose an ambient actual 10 root

r_0=e_s-e_t

as the top-face replacement label. A minimal zero has

lambda_0 r_0 + sum_{i=1}^k lambda_i r_{F_i}=0,

with all lambda_i>0 and a proper face chain

F_1<...<F_k=G.

The selected largest-face root r_G is a STRICT crossing root for the ordered partition

G=B_1|...|B_m.

Every other selected face root r_{F_i}, when viewed in the coarser G block order, is weakly forward: its source block is no later than its target block.

Interpret the dependence as a positive directed flow of physical root edges, with r_0=s->t the unique distinguished backward contribution.

### The strict largest-face edge cannot lie in a circulation component

Let phi_G be the strictly increasing block-rank functional.

Every boundary edge has phi_G>=0, while

phi_G(r_G)>0.

Any directed cycle built only from weakly forward G-edges must have total block displacement zero. Since no edge has negative block displacement, every edge on such a cycle must actually have displacement zero.

Therefore NO directed circulation component of the boundary-root flow can contain r_G.

### Hence r_G lies on a source-to-sink closing path

The boundary-root flow has net divergence

lambda_0(e_t-e_s).

Decompose it into directed t-to-s paths plus directed cycles.

Because r_G cannot occur in a cycle, every positive copy of r_G belongs to some t-to-s path. Choose one such path:

t=x_0 -> ... -> u -> v -> ... -> x_l=s,

where u->v is r_G.

This path is weakly forward in the G-block order.

### Witnessed provenance of the crossing edge

The root r_G was chosen in §146 from ONE explicit full coordinate order refining G:

- for each block B_j, choose a NOR-good spanning order of the proper induced instance on B_j;
- concatenate those block orders in the fixed G order;
- select an actual 10 descent crossing distinct blocks.

Thus the distinguished path edge r_G=u->v is carried by a full order whose restriction to every G-block is already one-change/NOR-good.

This is stronger provenance than an arbitrary actual root from an arbitrary refinement of G.

### Two-shore refinement

Choose any block boundary of G strictly between the source block of u and target block of v, and coarsen to

H=L|R.

Because the chosen t-to-s path is weakly forward and contains u->v, the block containing t is no later than the source block of u, and the block containing s is no earlier than the target block of v. Hence

t,u in L,
v,s in R

after choosing such a boundary.

The path crosses H exactly once, at the distinguished edge u->v=r_G.

Moreover r_G retains its explicit block-good witness order.

### Consequence

The center-replacement Sperner extraction can be sharpened to:

- one backward ambient actual root s->t;
- one forward cross-shore actual root u->v;
- internal root paths t->u in L and v->s in R;
- and the UNIQUE cross-shore edge u->v is witnessed by a refinement assembled from NOR-good orders on every block of a proper ordered partition.

Thus the remaining splice problem is not merely one arbitrary transverse 10 packet. Its transverse packet sits inside an order that is already internally good on every constituent block.

The next extraction target is to exploit this block-good witness to absorb the internal L/R paths or coarsen the good block orders while retaining the single cross-shore 10 packet.
