# Third-vertex resource labels: sharp two-window decoding and four-vertex one-switch barrier

- Stable ID: note_xiii_third_vertex_rainbow_decoding_two_loss_20261013
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: resource-rainbow, boundary-tournament, decoding, obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7442_1
- Updated session: session_nori_r7442_1
- Disposition: none
- Successor: none

## Related references

- article:nori_article_xiii_binary_involutive_rainbow_paths
- article:nori_article_ix_unification

## Research note

Let V be an n-element set with n>=4. The ordered-pair graph S(V) has states (a,b), a!=b, with forward arc (a,b)->(b,c) for every triple of distinct symbols. Give the arc resource label lambda=c and binary label B(a,b,c). For boundary tournaments B(c,b,a)=1-B(a,b,c). The deck map tau(a,b)=(b,a) exchanges an edge labeled by (a,b,c) with one labeled by (c,b,a), so it complements B. It changes the lambda-label c to a. At state (a,b), outgoing lambda-values are V\{a,b}; all incoming arcs have lambda=b. Its undirected incident palette is V\{a}, hence the minimum resource color degree is n-1.

Let R_s(B) be the maximum number of edges in a vertex-simple, forward-directed, lambda-rainbow state path with at most s binary switches. Let H_s(B) be the maximum number of triple windows in an original-vertex-injective tight word with at most s changes of B.

THEOREM (sharp two-window decoding). For all B and s>=0, R_s(B)-2 <= H_s(B) <= R_s(B). A forward path of r arcs is a word v_1,...,v_{r+2}, and its resource list is v_3,...,v_{r+2}. A rainbow path thus has an injective suffix on r original vertices. The suffix v_3,...,v_{r+2} has r-2 triple windows and its binary word is obtained by deleting the first two entries from the original binary word. The switch count cannot increase. Conversely, each injective word on original vertices produces a forward state-simple rainbow path with its number of triple windows. A rainbow path of n-1 arcs therefore forces a tight path on at least n-1 distinct original vertices, while one of n arcs forces a Hamilton tight path. A rainbow path of n-2 arcs corresponds to a Hamilton original-vertex path if its initial two vertices are absent from the lambda-list (then they are the two missing symbols).

SHARPNESS under reversal oddness. Set V={0,1,2,3,4}. Prescribe B=0 on all consecutive triples of W=(0,1,2,0,3,1,4) and U=(0,1,2,3,4), and B=1 on the reversed triples. There are seven distinct positive triples and none is the reverse of another; extend B arbitrarily to all other reversal pairs. W has six pairwise distinct ordered-pair states and its five resources are (2,0,3,1,4), hence R_0=5, the upper bound given by the five possible resources. The injective U has three zero-labeled windows, giving H_0=3, its maximum possible value on five original vertices. Thus R_0-H_0=2.

FOUR-VERTEX BARRIER. Set V={0,1,2,3}, and let h(a,b,c) be the inversion parity of (a,b,c,d), with d the fourth symbol. This coloring is reversal-odd. For two consecutive valid triples (u,v,w),(v,w,z), their h-bits agree iff z=u: if z=u the corresponding four-permutations differ by a 3-cycle, whereas if z is the fourth distinct symbol they differ by a 4-cycle. Suppose a simple rainbow forward state path with four arcs and at most one switch were represented by v_1,...,v_6. Rainbowness implies v_3,v_4,v_5,v_6 are all distinct. The third bit comparison is therefore a switch, so the first two must be non-switches, implying v_1=v_4 and v_2=v_5. The ordered-pair state (v_1,v_2) then repeats at (v_4,v_5), contradiction. Thus R_1(h)<=3; W'=(0,1,2,0,3) has distinct states, distinct resources (2,0,3), and bit word 001, so R_1(h)=3. Every injective four-vertex word has only two triple windows and automatically at most one switch; hence H_1(h)=2.

Thus the stronger hypothesis asserting an n-arc one-switch rainbow state path for every ordinary boundary tournament is false already on four vertices, while the original Hamilton one-switch conclusion remains valid there. These results require coherent forward paths and third-vertex resources and do not assume lambda is invariant under deck reversal.
