# Based antipodal geodesics, root charts, and ordered physical-face windows

## Statement

Based permutations and antipodal reversal

## Body

# Based antipodal geodesics and legal ordered-face colorings

Let V be an n-element set and Q_V the Boolean cube. A full geodesic is uniquely (S,π) for a start vertex S⊆V and a permutation π=(v_1,…,v_n), with X_i=S△{v_1,…,v_i}.

**Antipodal reversal.** Define Jγ=(\bar X_n,\bar X_{n-1},…,\bar X_0). It has the SAME start S and direction order π^R. On a directed length-three window P=(X;i,j,k), J acts as
J(P)=(\overline{X△{i,j,k}};k,j,i).
Thus for any J-odd based-window coloring, the word transforms as
w(S,π^R)=complement(reverse(w(S,π))), preserving the number of changes. Ordinary path reversal alone is a different operation.

**Rooted chart.** A≤_S B iff A△S⊆B△S identifies Q_V with the Boolean lattice rooted at S. Its maximal chains are precisely the antipodal geodesics from S. The chart A↦A△S is a coordinate description, not permission to alter the coloring of an actual physical face. One cannot generally fix S=∅ in unrestricted NORI.

**Physical-face model.** An ordered three-face is (F;(i,j,k)), where F is the physical 3-cube with free directions {i,j,k}. Legal active NORI colorings assign ONE color to this ordered face independently of which of its eight corners is taken as the traversal start. In based-window language, the exact condition is
c(X△T;i,j,k)=c(X;i,j,k) for all T⊆{i,j,k}.
In the broader based-window model this is an ADDITIONAL hypothesis, and antipodal J-oddness alone does not imply it. The active NORI oddness condition is c(\bar F;(k,j,i))=1−c(F;(i,j,k)). A direction-only label h(i,j,k) is an even smaller subclass.

**Window supports and memory.** The t-th triple-direction window uses (v_t,v_{t+1},v_{t+2}); two windows with starting indices differing by at least 3 have disjoint direction supports, while indices differing by at least 4 have disjoint vertex-index intervals. Disjoint direction supports do NOT imply independent colors: preceding flips affect actual face location. Exact partial-state extension requires the current cube vertex, used directions, and the last two or three ordered directions as appropriate.

These identities apply to physical-face NORI with the stated invariance, and the indicated based-window statements have the explicitly broader scope. No implication to arbitrary physical-edge NORI1 is asserted.

**Consolidation provenance.** Incorporates nori_freudenthal_charts_at_each_pole, nori_involution_on_paths_and_change_positions, nori_ordered_face_gallery_conditional_model and nori_window_direction_supports, whose original records remain archived for full historical wording.

## Metadata

- ID: nori_based_permutation_symmetry
- Kind: toolkit
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
