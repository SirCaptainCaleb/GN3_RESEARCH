# Matched-cut splicing and the two-by-two Hall obstruction

**Summary:** Matched prefix sets permit crossing-cover splicing; the remaining concatenation test is a two-by-two Hall obstruction determined by at most eight boundary labels.

## Statement

Two deletion covers with matched prefix sets yield a spanning two-cover whenever the two prefixes and two opposite tails admit a perfect matching of tight concatenations. Failure of such a matching forces an isolated prefix or tail. Shared ordered boundary pairs give an automatic matching.

## Body

## Matched prefix sets reduce crossing-cover conversion to a two-by-two Hall obstruction

Let F_a=P_1|P_2 cover H-a and F_b=R_1|R_2 cover H-b, a!=b. Choose cuts P_i=L_i T_i and R_i=M_i N_i such that
V(L_1) union V(L_2) = (V(M_1) union V(M_2)) union {b}.
No agreement of boundary edges, support partitions, or internal orders is assumed.

Then L_1,L_2,N_1,N_2 partition V(H) into four disjoint tight path blocks, with empty blocks allowed. Indeed the prefixes partition B union {b}, where B is the union of the M-prefix supports, and the N-tails partition its complement in H. In particular the prefixes restore b and the tails restore a.

Form the bipartite graph with left vertices L_1,L_2 and right vertices N_1,N_2. Put an edge L_i N_j exactly when the actual concatenation (L_i,N_j) is tight. An empty block gives a vacuous concatenation.

If this graph has a perfect matching, the corresponding two concatenations are a spanning two-cover. Consequently, in a no-two-cover H it has an isolated vertex: some prefix fails to join both tails, or some tail fails to accept both prefixes.

Proof of the last assertion. A bipartite graph on two vertices in each class has a perfect matching whenever all four vertices have positive degree. Otherwise, if a left vertex has only one neighbor, the other left vertex must have access to the other right vertex because that right vertex has positive degree; and if a left vertex has two neighbors, match the other left vertex first. Thus absence of a matching is equivalent to an empty row or column.

Each concatenation requires only its defined seam triples:
h(penultimate L_i,last L_i,first N_j)=1 when |L_i|>=2 and N_j nonempty;
h(last L_i,first N_j,second N_j)=1 when L_i nonempty and |N_j|>=2.
All interior triples are inherited. Hence the complete closing test uses at most the final two vertices of each prefix and initial two vertices of each tail: at most eight labels, regardless of how dissimilar or fragmented the original covers are.

### Ordered-edge corollary

Under the same prefix-set identity, suppose after pairing the paths that L_i and M_i both end in the same ordered pair for i=1,2. Then (L_i,N_i) is tight: every triple crossing the cut is inherited from R_i. Hence the diagonal matching gives a spanning two-cover. There is no need for the original support partitions or their orders away from these edges to agree.

### Scope

The prefix-set identity must be verified globally. Favorable seam triples on eight labels alone do not imply it. The isolated-vertex conclusion describes failure of this concatenation strategy; it does not characterize failure of every possible two-cover.

Origin: Article VII development [[matched_prefix_sets_reduce_crossing_cover_conversion_to_a_two_by_two_hall_obstruction]] and [[two_aligned_ordered_edge_cuts_splice_arbitrarily_dissimilar_deletion_covers]].

## Metadata

- ID: matched_cut_splicing_and_the_two_by_two_hall_obstruction
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
