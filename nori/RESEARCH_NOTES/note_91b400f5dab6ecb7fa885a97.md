# Six-vertex boundary orientation forces at least four cyclic switches

- Stable ID: note_91b400f5dab6ecb7fa885a97
- Author: unspecified; session provenance retained
- Primary home: article:article_xv_projective_face_flag_unification
- Labels: cyclic-variation, boundary-tournaments, counterexample, exhaustive
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7547_2
- Updated session: session_nori_r7547_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

A six-vertex reversal-odd boundary tournament proves that cyclic D <= 2 cannot be guaranteed. Vertices are 0,1,2,3,4,5. For each center h, list q_h(a,c)=b(a,h,c), a<c and a,c !=h, in lexicographic pair order on the remaining five symbols. Rows h=0: 0000011110; h=1: 0000010100; h=2: 1101001011; h=3: 1111101111; h=4: 1000000000; h=5: 0110110000. Define the reversed bits by b(c,h,a)=1-b(a,h,c). For each cyclic order fix first vertex 0 and permute the other five vertices, yielding 120 orders. Compute a_j=b(v_j,v_{j+1},v_{j+2}) with cyclic indices, and D=sum_j(a_j XOR a_{j+1}). Exhaustive evaluation gives precisely 100 orders with D=4, and 20 with D=6; hence minimum cyclic variation is four, never zero or two. The order (0,1,2,3,4,5) has cyclic colors (0,0,1,0,1,1) and cyclic comparisons (0,1,1,1,0,1). Rotating to the order (4,5,0,1,2,3) gives a full Hamilton triple word (1,1,0,0) with only one switch. Thus the second alternative in the Article XV cyclic variation criterion, D=4 with a run of three changes, cannot be omitted. The finding refutes only the stronger cyclic D<=2 assertion, not the original one-switch conjecture.
