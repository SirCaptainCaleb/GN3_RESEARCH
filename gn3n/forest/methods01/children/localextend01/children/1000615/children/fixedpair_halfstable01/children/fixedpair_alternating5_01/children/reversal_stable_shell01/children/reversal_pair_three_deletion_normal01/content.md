# A genuine reversed pair normalizes across three deletions to windows, disturbance, one reverse-cross residue, or repeated internality

## Statement

Let H be a minimum counterexample. Then there exist distinct vertices u,v,a,x,y,z such that a tight triple with third vertex a reverses an ordered edge (u,v) of a tight path, and for each t in T={x,y,z}, one of (u,t,v),(v,t,u) is a tight three-vertex path with the same orientation for all three t. For every t in T, writing K_t=H-{u,v,t} and G_t=H-t, the four states K_t, K_t+u, K_t+v, and G_t are non-Hamiltonian with path-cover number two. Consequently at least one of the following holds: (1) H has relative-order disagreement arising in one G_t or between the original (u,v)-path and an exposed-endpoint component; (2) for some t, H contains a proper positioned Hamiltonian four- or five-set containing t,u,v with non-Hamiltonian path-cover-two complement; (3) for some t, u and v are the two displayed endpoints of one component of a two-cover of H-t, that component orders u before v, and the reverse triple (v,t,u) is tight; (4) for some t, two two-covers of H-t have different unordered support partitions; (5) one fixed label d in {u,v} is internal in every two-cover of H-t for at least two distinct t in T.

## Body

Choose u,v,a,x,y,z from reversal_stable_shell01. Its proof places T={x,y,z} inside one fixed-pair orientation class for {u,v}; hence either (u,t,v) is tight for every t in T or (v,t,u) is tight for every t in T. The same theorem supplies the genuine reversal of the ordered edge (u,v).

Fix t in T and apply 1000156 to the tight three-path on {u,t,v}. With K_t=H-{u,v,t}, the four states K_t,K_t+u,K_t+v,G_t=H-t are all non-Hamiltonian with path-cover number two. Thus each deletion G_t carries a full pc2 square indexed by the same reversed pair u,v.

Apply pc2_square_topcover_normal01 to each G_t. A support-partition disagreement gives (4), while common-support relative-order disagreement gives (1). If a square gives simultaneous endpoint exposure of u,v, apply reversal_pair_endpoint_geometry01 with omitted label t. It yields either relative-order disagreement (1), a positioned Hamiltonian four/five-window with pc2 complement (2), or the same-component reverse endpoint cross (3).

If none of (1)-(4) occurs, then for each t the square normal form must select a label d_t in {u,v} that is internal in every two-cover of G_t. Three deletions and two possible values imply by pigeonhole that one fixed d occurs for at least two distinct t, giving (5).
