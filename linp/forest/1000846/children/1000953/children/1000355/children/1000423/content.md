# Every order-six Latin square has a full-color rainbow path

## Statement

Every proper edge-coloring of K_{6,6} with six colors contains a rainbow path of six edges. Equivalently, every transversal design TD(3,6), or every Latin square of order six, contains a six-edge linear path.

## Body

By 3618afd5f90f, every proper six-coloring of K_{6,6} contains a rainbow P_5. Assume for contradiction that there is no rainbow P_6 and choose such a rainbow P_5.

By 8d4230198b1b, the missing color forces exactly one of two endpoint configurations: the closing-chord form, in which the P_5 closes to a rainbow C_6, or the crossed-chord form.

In the closing-chord form, 81565c9de9a6 reconstructs all eight possible chord-color assignments and shows that, up to the normalized half-turn/color symmetry, the used 3x3 matrix is uniquely
  [ [1,2,6], [2,3,4], [6,4,5] ].
Then f644f80c598e uses the unused columns and two rainbow P_5 rotations to force two distinct color-6 edges incident with one used vertex, contradicting properness. Hence the closing-chord form is impossible.

In the crossed-chord form, b3cf269da794 forces the remaining endpoint chord and reduces the used 3x3 matrix to two possibilities. The lemma bcea35b7916f eliminates both possibilities by forcing a rainbow C_6, which is impossible by the already established closing-chord exclusion.

Thus no counterexample exists: every proper six-coloring of K_{6,6} contains a rainbow P_6.

Under the standard Latin-square/transversal-design correspondence, a colored graph edge xy of color s is represented by the triple {x,y,s}. A rainbow graph path lifts to a linear 3-uniform path with the same number of edges. Therefore every TD(3,6), equivalently every Latin square of order six, contains a six-edge linear path.
