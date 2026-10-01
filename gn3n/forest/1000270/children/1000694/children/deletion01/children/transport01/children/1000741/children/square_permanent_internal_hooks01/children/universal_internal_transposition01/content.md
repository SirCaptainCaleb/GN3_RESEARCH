# Universal internality across deletions transposes to mutual internality or cover disturbance

## Statement

Let H be a minimum counterexample, let d be a vertex, and let T be a set of r>=2 vertices disjoint from {d}. Suppose that for every t in T, the vertex d is internal in every two-cover of H-t. Then for two-covers of H-d at least one of the following holds: (1) some two-cover has two distinct labels of T simultaneously as displayed endpoints; (2) two two-covers have different unordered support partitions; (3) two Hamilton paths on one common component support exhibit order disagreement; (4) there is a set I subseteq T with |I|>=r-1 such that every t in I is internal in every two-cover of H-d. In outcome (4), d and each t in I are mutually internal across the paired deletions H-t and H-d; consequently every two-cover of H-{d,t} satisfies the four-end Hamiltonian-K4-or-doubled-reverse-barrier conclusion of mutual_internal_endpoint_grid01.

## Body

By codim3_deletion_pc2_01, for every unordered pair {s,t} subseteq T the four states H-d, H-{d,s}, H-{d,t}, and H-{d,s,t} are non-Hamiltonian with path-cover number two. Apply pc2_square_topcover_normal01 to the top state H-d for every pair {s,t}. If any pair gives simultaneous endpoint exposure, support-partition disagreement, or order disagreement, we obtain (1), (2), or (3).

Otherwise, for every pair {s,t}, at least one of s,t is internal in every two-cover of H-d. Let I be the set of labels in T that are internal in every two-cover of H-d. Then I meets every edge of the complete graph on T, so |I|>=r-1. This gives (4).

The original hypothesis says that d is internal in every two-cover of H-t for every t in T, in particular for every t in I. Thus for each t in I the pair d,t has mutual deletion internality: d is universally internal in H-t and t is universally internal in H-d. Apply mutual_internal_endpoint_grid01 to any two-cover of H-{d,t}; at all four displayed ends it yields a Hamiltonian four-window with path-cover-two complement or a doubled reverse barrier.
