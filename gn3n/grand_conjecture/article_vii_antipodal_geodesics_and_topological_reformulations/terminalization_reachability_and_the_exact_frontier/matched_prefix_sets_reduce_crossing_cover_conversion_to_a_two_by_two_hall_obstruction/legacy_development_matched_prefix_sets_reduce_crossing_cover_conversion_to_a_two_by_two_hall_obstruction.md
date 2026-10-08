# Matched prefix sets reduce crossing cover conversion to a two by two Hall obstruction — preserved pre-item development

## Composition

(none yet)

## Development

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

This strengthens [[two_aligned_ordered_edge_cuts_splice_arbitrarily_dissimilar_deletion_covers]] by removing its shared-edge assumption. It also preserves global incidence information: the prefix-set identity is essential and is not implied merely by having eight locally favorable labels.

The useful no-two-cover consequence is synchronized rather than four independent seam failures: at every matched cut there is one whole prefix or tail blocked against both alternatives. Neither existence of such cuts nor elimination of their isolated-vertex obstruction is yet proved. Those are the genuine crossing-cover obligations, not bare bounded-support outputs.
