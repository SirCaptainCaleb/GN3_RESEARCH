# R511 bridge geometry alone does not force an opposite-row support copy

**Workspace:** D17
**State:** limitation
**Key:** `singleton-r511-opposite-row-local-fence`

**Summary:** Explicit 8-vertex exact-reversal assignment realizing an R511 bridge pair and the seam-free repair of one deletion row, while the opposite support-aligned block has no Hamilton path. Therefore the second-row support copy is not a consequence of local R511 geometry alone; coordinated repair must use additional family-level data.

### Weakened local exchange claim is false
The seam-free R511 bridge repair of one singleton row does not, from that local path data alone, force an actual support-aligned replacement in the opposite deletion row. The following explicit exact-reversal assignment is a finite witness. No claim of pc(H)>2 or smallest-counterexample realizability is made.

Use vertices

  a=0, b=1, S={2,3}, T_1={4,5}, T_2={6,7}.

A boundary assignment can be specified by one bit for each complete-reversal pair (x,y,z)<->(z,y,x). For endpoints x<z, the default rule declares (z,y,x) tight. Override the following 16 pairs, declaring instead the increasing-endpoint representative (x,y,z) tight; each triple below is written as (middle; low,high):

  (2;0,3), (3;0,2),
  (0;2,4), (0;2,5), (2;0,5), (5;0,2),
  (0;3,4), (3;0,4), (0;3,5), (3;0,5),
  (4;2,3), (2;4,5),
  (5;4,6), (6;5,7), (1;3,4), (4;1,5).

All unlisted reversal pairs use the default. This defines a complete boundary tournament. Direct substitution gives the following literal tight paths:

  Q=(0,2,3),
  T=(4,5,6,7),
  M=(2,3,1,4,5),
  K=(6,7).

Hence the two deletion rows

  C_b = Q | T

and

  C_a = M | K

realize the R511 bridge pattern: M has S-block (2,3), then b=1, then T_1=(4,5), while K=T_2. There is no selected S|T_0 adjacency in C_a; the unique defect relative to (S+b)|T_0 is the b--T_1 bridge. The seam-free repair is literal:

  C'_a=(2,3,1) | (4,5,6,7).

### Opposite aligned support is non-Hamiltonian
An opposite-row support copy aligned with the original sigma_a would require a Hamilton path on

  X={0,2,3,4,5}

(the complementary support T_2={6,7} is already a dimer). Exhaustive verification of all 5!=120 vertex orders on X under the assignment above gives zero Hamilton tight paths. Equivalently, every order of X has at least one bad consecutive triple.

Thus the full local bridge packet plus the successful seam-free a-row repair does not imply a Hamilton path on the opposite target support S+a+T_1. Any theorem coupling an actual opposite-row support change must use additional family-level information, smallest-counterexample structure, or another current seam.

### Scope
This is a local exact-reversal fence to a weakened exchange theorem only. It is not a counterexample to O4, does not satisfy or test pc(H)>2, and does not refute coordinated K-repair using additional deletion fibers. Its purpose is to prevent repeated attempts to manufacture the second support copy from R511 data alone.
