# One-eighth paid-cell dichotomy for top-layer switching families

## Statement

Let P=(g_1,...,g_L) be a globally longest L-edge path ending at v, and let F be a family of single blockers through v. Restrict to the interior blocker cells C_i={b_i,z_i}, 1<=i<=L-3, and let s_int be the number of members of F whose unique precursor contact lies in these cells.

Let D be the number of interior cells containing two F-contacts. For each occupied cell C_i, let h_i=g_{i+2} be its rotation-output edge. Let Y be the number of occupied cells for which h_i is not in the forward-flat ascending branch of 09e3d5b2bd6b; equivalently h_i is special or nonspecial nonascending.

Then
  D+Y >= s_int-ceil((L-3)/2).

Moreover:
- every cell counted by D supports a linear 3-cycle consisting of g_i and the two blocker edges through v;
- every nonspecial nonascending output counted by Y is an all-top edge by 57d5e4c71035.

Consequently, for the switching family at a global-top active misaligned center v with phi(v)=L,
  D+Y >= L/8-eta_v-O(1).
Thus every low-defect global-top center forces linearly many units of one of three paid structures: switcher triangles, special rank-L output edges, or all-top nonspecial nonascending rank-L output edges.

## Body

Let C be the number of occupied interior cells. Since each cell contains at most two possible contact vertices and distinct blockers through v have distinct non-v contacts, every occupied cell contributes one blocker and every doubly occupied cell contributes exactly one additional blocker. Hence
  s_int=C+D.                                           (1)

Classify an occupied cell as flat when its output h_i=g_{i+2} is nonspecial ascending in the forward-flat branch of 09e3d5b2bd6b. By 699a1e79304b, two consecutive output edges cannot both be forward-flat ascending. Since consecutive cells C_i,C_{i+1} have consecutive output edges g_{i+2},g_{i+3}, the flat occupied cells form an independent set in the path of L-3 interior cell positions. Therefore the number A of flat occupied cells satisfies
  A<=ceil((L-3)/2).                                    (2)

By definition Y=C-A. Using (1) and (2),
  D+Y
   =D+C-A
   =s_int-A
   >=s_int-ceil((L-3)/2).                              (3)

For the triangle assertion, suppose C_i is doubly occupied. Its two contact vertices are necessarily b_i and z_i. Let the corresponding distinct blocker edges be f_b and f_z. Both contain v; f_b meets g_i at b_i, f_z meets g_i at z_i, and by linearity f_b∩f_z={v}. The host edge g_i avoids v in the precursor and contains b_i,z_i. Thus
  g_i,f_b,f_z
is a linear 3-cycle.

For an occupied cell counted by Y, the top-rank output trichotomy 09e3d5b2bd6b says the output is either special or nonspecial nonascending, because the flat branch is exactly the excluded third possibility. In the latter case 57d5e4c71035 says all three vertices of the output edge have endpoint potential L.

Finally take F to be the switching family supplied by b032348c1a8a at a global-top active misaligned center. Only O(1) switchers can lie in boundary positions outside the interior cell system, so
  s_int>=|F|-O(1)
       >=(5/8)L-eta_v-O(1).
Substituting in (3) gives
  D+Y >= (1/8)L-eta_v-O(1),
as claimed.
