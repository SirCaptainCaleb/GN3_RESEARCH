# A Phi-minimum containing a three-path has order at most thirteen

**Summary:** In a minimum counterexample, if a Phi-minimal spanning three-cover has a component of order three, then the other two components have orders at most five. Since every component has order at least three and |V(H)|>10, the only possible size multisets are 3|3|5, 3|4|4, 3|4|5, and 3|5|5.

## Statement

Let H be a minimum counterexample and let C be a spanning three-cover minimizing Phi in its pairwise-repartition component. If one component of C has order three, then |V(H)|<=13. More precisely, the size multiset of C is one of {3,3,5}, {3,4,4}, {3,4,5}, {3,5,5}.

## Body

By toolkit_minimal_three_covers_have_no_components_of_order_one_or_two, every component of C has order at least three. Let one component T have order three. By three_vertex_component_long_neighbor_rotation01, T cannot sit beside a path of order at least six in a Phi-minimal state. Therefore each of the other two components has order at most five.

Hence |V(H)|<=3+5+5=13. On the other hand mincex01 gives |V(H)|>10. Writing the other two component orders as 3<=a<=b<=5 and requiring 3+a+b>10 leaves exactly

(3,3,5), (3,4,4), (3,4,5), (3,5,5).

Thus every Phi-minimal state of order at least fourteen has all three component orders at least four, and the entire three-component residue is confined to these four bounded profiles.

## Metadata

- ID: toolkit_a_phi_minimum_containing_a_three_path_has_order_at_most_thirteen
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
