# Every minimum counterexample has a reversed pair normalized to one deletion-cover square

## Statement

Let H be a minimum counterexample. Then there exist distinct vertices u,v,a,x such that some tight path of H contains the ordered edge (u,v), a tight triple with third vertex a contains the reversed consecutive pair (v,u), and one of (u,x,v) and (v,x,u) is a tight three-vertex path. Put K=H-{u,v,x} and G=H-x=K union {u,v}. Then K, K union {u}, K union {v}, and G are all non-Hamiltonian with path-cover number two. Consequently at least one of the following holds: (1) some two-cover of H-x has u and v simultaneously as displayed endpoints; (2) one of u,v is internal in every two-cover of H-x; (3) two two-covers of H-x have different unordered support partitions; (4) two Hamilton paths on one common component support of two covers of H-x order some common pair differently.

## Body

Choose u,v,a,x,y,z from reversal_stable_shell01. The alternating Hamiltonian five-path supplied there is either (y,u,x,v,z) or (y,v,x,u,z), so its middle three vertices form the tight path R=(u,x,v) or R=(v,x,u). The same theorem supplies the genuine reversal: another tight path contains (u,v) as an ordered edge and a tight triple with third vertex a contains (v,u) consecutively.

Apply path_induces_a_pathcovertwo_endpoint_square_on_its_complement to the proper tight path R. Its displayed endpoints are exactly u and v, and its complement is K=H-{u,v,x}. Therefore K, K+u, K+v, and K+u+v=H-x are all non-Hamiltonian with path-cover number two. Thus they form a full two-label pc2 square indexed by the actual reversed pair u,v.

Apply pc2_square_topcover_normal01 to the top state G=H-x with labels u,v. Its four alternatives are exactly the four outcomes stated: simultaneous endpoint exposure of u,v in one two-cover of H-x; universal internality of one reversed label; support-partition disagreement between two top-state covers; or relative-order disagreement on one common component support.