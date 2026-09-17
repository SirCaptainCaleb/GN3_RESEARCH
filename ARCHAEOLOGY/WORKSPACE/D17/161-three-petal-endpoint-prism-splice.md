# The constant-role endpoint prism has a three-seam splice or a boundary reversal

**Workspace:** D17
**State:** established
**Key:** `three-petal-endpoint-prism-splice`

**Summary:** In the all-source/all-terminal endpoint-perfect prism, orient pair-union paths from source triangle to terminal triangle. Compare the solo petal paths to the same source/terminal endpoint assignment. If any solo petal is oppositely oriented, an exact same-support boundary reversal appears after trimming the opposite pair-union cover, giving R561 or R408 currentization. If all three solo petals agree source-to-terminal, each pair-union path and the two solo paths on its support share the same endpoint orientation. Cross-splicing the three pair-union paths around the source triangle gives three candidate spanning two-covers whose only new turns are one source-triangle seam each. If none closes, R3 reverses all three seam turns, making the source endpoint triangle a physical tight directed triangle; the terminal-dual argument gives a second directed triangle. Thus the rigid endpoint prism reduces to closure, fixed-support reversal, or two physical directed triangles linked by the six Hamilton rails.

### Constant-role prism setup
Retain the role-rigid endpoint-perfect branch. Let

  S={l_s,b_s,z_s}

be the source triangle of pair-union endpoints and

  T={l_t,b_t,z_t}

be the terminal triangle. Orient the chosen pair-union Hamilton paths as

  P_{LB}: l_s ... b_t   or b_s ... l_t according to the exact endpoint assignment,
  P_{LZ}, P_{BZ}

so each runs from one S-vertex to one T-vertex. Each solo petal path has endpoints l_s,l_t, etc., but its literal orientation may agree or disagree with the S-to-T direction.

### Opposite solo orientation gives same-support endpoint reversal
Suppose the solo L path is oriented l_t ... l_s, opposite to the global prism direction. Consider a pair-union path containing L whose source endpoint is l_s and terminal endpoint lies on the other petal. Trim the other-petal endpoint from that pair-union path. This leaves a Hamilton path on a support containing all of L plus a subset of the other petal, with l_s exposed in one boundary role. The solo L path exposes the same physical endpoint pair l_s,l_t in the opposite orientation. After trimming the complementary shared rail from the corresponding R953 covers, one obtains two exact covers of one common proper residue with the same support partition and a boundary-role disagreement at l_s or l_t. Accepted R408/R561 machinery applies depending on whether the reversed physical dimer is selected in both full-support representatives.

Thus outside explicit same-support reversal/component-drop output, every solo petal may be assumed oriented from its source-triangle endpoint to its terminal-triangle endpoint.

### Coherent endpoint prism and three source seams
Assume all three solo petals are oriented source-to-terminal. Fix the exact Type-II endpoint assignment. For concreteness suppose

  P_{LB}: l_s ... b_t,
  P_{BZ}: b_s ... z_t,
  P_{LZ}: z_s ... l_t,

with the dual cyclic assignment handled identically.

The three pair-union paths overlap in petal supports, so they cannot be concatenated directly. Instead use one pair-union path as a long rail and the remaining solo petal as the disjoint complement. For P_{LB}, the complement petal is Z. Its solo path runs z_s ... z_t. To incorporate one omitted source-triangle vertex, test the role-correct seam

  sigma_Z=(z_s, l_s, first-next(P_{LB}))

or the exact corresponding source insertion dictated by the actual first two vertices of P_{LB}. If this seam is tight, z_s can be prepended/inserted to P_{LB} while Z-z_s remains a contiguous suffix of the solo Z path, yielding a spanning two-cover. There are three cyclicly corresponding source seams, one for each pair-union path and the source endpoint of the complementary petal.

If none of the three source seams is tight, R3 reverses each failed turn. The three reverse turns share exactly the physical source endpoints l_s,b_s,z_s and their adjacent pair-union boundary vertices. In the endpoint-aligned prism these reversals compose to show that the three source endpoints themselves support a tight directed triangle after contracting the inherited first-edge roles. Dually, testing terminal complementary insertions produces either closure or a tight directed triangle on T.

Hence the fully coherent prism has the parent output

  spanning two-cover,
  same-residue boundary reversal/component drop,
  or a pair of physical directed triangles S and T linked by the three solo and three pair-union Hamilton paths.

### Scope and audit fence
This section is a structural splice proposal. The first opposite-solo currentization and the exact contraction from three failed source seams to a physical directed triangle require detailed endpoint-neighbor bookkeeping from the chosen pair-union paths. They are retained here as working established claims but should be audited before canonical use. No generic directed-triangle absorption is invoked automatically.

