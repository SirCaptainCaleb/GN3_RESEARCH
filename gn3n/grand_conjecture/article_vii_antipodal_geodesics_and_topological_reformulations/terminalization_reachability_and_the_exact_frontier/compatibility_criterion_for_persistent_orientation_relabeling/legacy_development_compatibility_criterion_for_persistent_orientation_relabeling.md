# Compatibility criterion for persistent orientation relabeling — preserved pre-item development

## Development

## Exact global criterion for the proposed change of labels

Fix one reflected positive span-two depth r. Let A be an invariant finite family of protected faces, none of which contains an outward chamber, and each of which has a nonempty set O(F) of orientations occurring in every chamber. Faces with determining span at least thirteen satisfy this last condition by [[separated_protected_determining_windows_force_a_persistent_witness_or_same_face_escape]].

Form the graph whose vertices are faces in A, with adjacency when two faces have a chamber in common. Reversal acts on the graph and sends O(F) to -O(F). For a component C put
\[
O(C)=\bigcap_{F\in C}O(F).
\]

**Proposition.** There is a chamber sign assignment on the union of these faces which is constant on every F in A, uses an available witness orientation in every chamber of F, and is odd under reversal, if and only if:
1. O(C) is nonempty for every component C;
2. reversal fixes no component setwise.

**Proof.** A common chamber forces the constants on two overlapping faces to coincide. Hence a valid assignment is one constant s_C for each component, belonging to O(C). Oddness gives s_{tau C}=-s_C, which is impossible if tau C=C.

Conversely, pair the components under reversal. Choose s_C in O(C) on one component of each pair and set s_{tau C}=-s_C. Any chamber in several faces sees the same component and hence the same sign. The chosen sign is persistent on each such face, and oddness holds. ∎

This is a criterion, not an assertion that its conditions always hold.

Since O(F) is one of {+},{-},{+,-}, emptiness of O(C) is equivalent to a finite chain of overlapping faces joining a face with forced persistent sign + to a face with forced persistent sign -. A reversal-invariant component is the second possible obstruction: a face can be joined to its antipode through such a chain. The local twelve-vertex bound alone rules out neither chain.

## Where an incompatibility can be resolved

Let F and G have opposite forced persistent signs, and suppose their smallest containing permutahedron face H is protected at depth r and has determining span at least thirteen. Then H has an outward chamber.

Indeed O(F)={+} gives a chamber of F where the right occurrence is absent, while O(G)={-} gives a chamber of G where the left occurrence is absent. These are also chambers of H. The separated-window product splice in the preceding theorem combines their prefix and suffix orders to produce a chamber of H with both occurrences absent.

Thus opposite local choices are not automatically a new long-span surgery problem. When their hull is protected they expose a pre-existing outward chamber. If their hull is not protected, that failure must be retained explicitly; one cannot apply the splice inside X_r or treat the hull as an available source carrier.

The resulting attack is precise: remove tie-induced sign changes on coherent families of persistent faces, and use protected outward hulls to patch incompatible local choices. A remaining chain with no such protected patch, or an antipodally invariant component, is an actual global obstruction to this particular relabeling scheme. Arbitrary independent face signs do not solve it.
