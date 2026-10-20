# Nine-vertex boundary triple exchange trap: reversals and width-four moves

- Stable ID: note_nori_boundary_nine_vertex_width_four_reversal_exchange_barrier_20261020_r11913
- Author: session_nori_r11913_1
- Primary home: subsection:cyclic_variation_selection_for_antipodal_and_boundary_path_galleries
- Labels: boundary-tournament, Hamilton-order, one-change, method-obstruction, nine-vertices, geometric-exchange
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_1
- Updated session: session_nori_r11913_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Boundary nine-vertex strict exchange barrier with a monochromatic Hamilton ordering

Let V={0,...,8}. Specify a reversal-odd coloring b of ordered triples with different original vertices as follows. For middle vertex h, list the 28 unordered outer pairs {a,c} with a<c and a,c different from h, in lexicographic order. The bit indexed by pair {a,c} of the following 28-bit mask is b(a,h,c):
M_0=0x00000FA; M_1=0x0045911; M_2=0x0000083; M_3=0x0440182; M_4=0x0786288; M_5=0x6940100; M_6=0xE006000; M_7=0x8DA0820; M_8=0x6221040.
Define b(c,h,a)=1-b(a,h,c). This specifies a legal reversal-odd coloring with no restrictions on the independently chosen middle-vertex tournaments.

For a Hamilton vertex ordering W, let s(W) count changes in its seven consecutive triple colors. Set W=(0,1,2,3,4,5,6,7,8). Then its color word is 1100011 and s(W)=2.

**Finite proposition (complete computation).** Every proper contiguous segment reversal of W gives at least three color changes; every rearrangement of at most four consecutive entries gives at least three changes; every nontrivial cyclic rotation of W gives at least two changes. There are respectively 35, 113, and 8 distinct resulting orderings in these three classes. Yet the Hamilton ordering (0,1,3,6,2,7,4,8,5) has color word 0000000.

*Reproducible proof.* Enumerate intervals [i,j) with 0<=i<j<=9 and length at least two, omitting [0,9), and reverse their entries. Separately enumerate each interval of length 2,3,4 and all its alternative permutations. For every resulting Hamilton ordering, evaluate each of its seven ordered triple colors using the nine masks and count adjacent inequalities. The respective minima are 3 and 3. Enumerating W[k:]+W[:k] for 1<=k<=8 gives minimum 2. The stated monochromatic word follows by seven direct mask lookups. A standalone Python standard-library verifier performs all the enumerations and checks the claimed cardinalities, inequalities, and full vertex distinctness.

**Sharp scope and neutral escape.** The obstruction disproves a universal *one-step strict-descent* rule based on the listed transformations; it does not disprove monotone multi-step reconfiguration. Specifically, rotating W by two gives (2,3,4,5,6,7,8,0,1) with color word 0001100 (two changes). Rearranging the next four entries gives (2,6,4,5,3,7,8,0,1), color word 1000000 (one change). This is a complete-spanning witness on the original vertices throughout.

The result concerns the unrestricted reversal-odd boundary-triple specialization, not just a quotient/line-graph relaxation. It supplies no general Hamilton one-change theorem, and no NORI1 square-switch preservation theorem.
