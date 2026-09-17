# Endpoint-perfect assignment on the three-petal row is a doubled endpoint triangle

**Workspace:** D17
**State:** established
**Key:** `three-petal-endpoint-perfect-triangle`

**Summary:** In the endpoint-perfect R953 three-petal branch, each solo petal endpoint appears exactly once among the two adjacent pair-union endpoint sets. Hence the three pair-union paths define a 2-regular bipartite incidence on the six solo endpoints whose three edges are exactly the pair-union paths. Up to relabelling, either the endpoint incidences form one 6-cycle alternating petals, or two disjoint 3-cycles each choosing one endpoint from every petal. The 6-cycle branch forces an endpoint/internal disagreement after deleting one solo endpoint, producing a literal same-residue two-cover versus three-cover. Thus outside R408/R159 output, only the two-triangle endpoint assignment survives; each of its two triangles supplies one endpoint from L,B,Z to the three pair-union paths in cyclic order.

### Endpoint-perfect setup
Retain the R953 three-petal cover row and the endpoint-perfect branch of `three-petal-cover-row-endpoint-dichotomy`. Let

  E_L={l_0,l_1},
  E_B={b_0,b_1},
  E_Z={z_0,z_1}

be the endpoint pairs of chosen Hamilton paths on the solo petals L,B,Z. Let the endpoint pairs of chosen Hamilton paths on L+B, L+Z, B+Z be respectively

  F_Z, F_B, F_L.

Endpoint-perfect means every F_* consists only of solo endpoints and every solo endpoint occurs in exactly one of the three F_*.

Build an ordinary graph G_ep on the six solo endpoints by making each pair-union endpoint pair F_* an edge. Because every solo endpoint occurs exactly once, G_ep is a matching of three edges. The petal partition gives three disjoint color-pairs E_L,E_B,E_Z, and no F_Z edge can have both ends in E_Z because F_Z lies in L+B; dually for the others.

Equivalently contract each petal color-pair to a color vertex. The three pair-union edges become one edge labelled by each omitted petal. Each edge joins two of the three color classes. There are exactly two possible incidence types.

### Type I: one doubled triangle
Each pair-union edge joins different petal colors, so after relabelling

  F_Z={l_0,b_0},
  F_B={l_1,z_0},
  F_L={b_1,z_1}.

The remaining unmatched solo endpoints within each color are exactly the partners shown. On the six physical endpoints the alternating pattern around petal-pair and pair-union incidence is one 6-cycle.

### Type II: two endpoint triangles
One pair-union endpoint pair lies inside a single allowed petal color, forcing the dual internal placement on the opposite side. Up to relabelling the endpoint sets split into two triples

  T_0={l_0,b_0,z_0},
  T_1={l_1,b_1,z_1},

such that each pair-union path takes its two endpoints from one of these triples in cyclic fashion. Concretely one may write

  F_Z={l_0,b_0},
  F_B={l_1,z_1},
  F_L={b_1,z_0},

or the exact switched assignment. The incidence graph is two disjoint 3-cycles when petal-pair edges and pair-union endpoint edges are both drawn.

### The 6-cycle branch gives a same-residue component drop
Retain the Type-I labelling above. Consider the physical endpoint l_0 of the solo L path. It is an endpoint of the L+B path by F_Z, but endpoint-perfect places the other L endpoint l_1 on L+Z and therefore l_0 is not an endpoint of L+Z. Hence l_0 is internal on the chosen Hamilton path on L+Z.

Delete p and l_0. From the exact source cover

  (L+B)|Z

trimming endpoint l_0 leaves an exact two-cover of H-{p,l_0}. From

  (L+Z)|B

deleting internal l_0 splits the first rail and gives a literal three-cover of the SAME residue. Thus accepted R159/R408 applies with full source orders retained.

The same argument works at every solo endpoint around the 6-cycle: each endpoint is used in exactly one of its two adjacent pair-union paths and is therefore internal in the other. Hence Type I produces six candidate same-residue component drops.

Therefore outside explicit R159/R408 output, the endpoint-perfect branch must be Type II, the two-triangle assignment.

### Remaining two-triangle endpoint geometry
In Type II each triangle T_i contains one endpoint from each petal. Every pair-union path uses one edge of one triangle, and the complementary pair-union path uses an edge of the other. Thus the three pair-union Hamilton paths carry a cyclic endpoint assignment across the three petals.

This is the exact residual endpoint combinatorics. No claim is made that a triangle T_i is a tight directed triangle or that its three physical vertices form a Hamilton trimer in a prescribed order. The next consumer should compare the role orientations of the three pair-union paths around one endpoint triangle. An odd role mismatch may force a boundary-reversed Hamilton dimer or an R933/R961 packet; a role-consistent orientation is the natural endpoint analogue of the paired constant-role hexagon.

Status: complete elementary endpoint-incidence reduction from the endpoint-perfect branch; working exposition, unreviewed.
