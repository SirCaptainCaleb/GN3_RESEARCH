# Deficiency-s residual decomposition around a nonspecial edge

## Statement

Let H be a d-regular linear 3-uniform hypergraph on n=2d+1+s vertices, where s>=0, and let J be its uncovered-pair graph. Then J is s-regular.

Fix an edge e={x,y,z}, put U=V(H)\e, and let R=H[U]. For q∈{x,y,z}, let D_q=N_J(q)⊂U and let F_q be the set of off-q pairs from the d-1 edges through q other than e. Then:

(1) |D_q|=s and F_q is a matching of size d-1 covering exactly U\D_q.

(2) For u∈U, if c(u)=|N_J(u)∩{x,y,z}|, then
    d_R(u)=d-3+c(u).

(3) Every unordered pair from U lies in exactly one of four types: the 2-shadow of R, F_x, F_y, F_z, or J[U]. Thus
    E(K_U)=shadow_2(R) ⊔ F_x ⊔ F_y ⊔ F_z ⊔ E(J[U]).

If moreover e is nonspecial of rank q with unique entrance x and y,z terminal at e, then for every {a,b}∈F_y, R contains no (q-2)-edge linear path ending physically at a while avoiding b, nor one ending at b while avoiding a; likewise for F_z.

## Body

Each vertex of H lies in d triples, and linearity makes the 2d partners appearing in those triples distinct. Among the other n-1=2d+s vertices it therefore has exactly s nonneighbors. Thus the uncovered-pair graph J is s-regular.

Fix e={x,y,z}. Since x,y,z are mutually adjacent in e, none is an uncovered neighbor of another, so D_q=N_J(q) lies in U and has size s.

For q=x,y,z, the d-1 edges through q other than e have pairwise disjoint off-q pairs, by linearity. They therefore cover 2d-2 distinct vertices of U. A residual vertex u belongs to one of these pairs exactly when qu is covered in H, i.e. exactly when u∉D_q. Since
|U|=n-3=2d-2+s,
these d-1 pairs cover precisely U\D_q and form the claimed matching F_q.

Now fix u∈U. For each q∈{x,y,z} adjacent to u, there is a unique edge containing uq. These edges are distinct: an edge other than e cannot contain u and two vertices of e, because it would meet e in two vertices. Thus deleting x,y,z removes exactly 3-c(u) incident edges at u, where c(u)=|N_J(u)∩{x,y,z}|. Hence
d_R(u)=d-(3-c(u))=d-3+c(u).

For the pair decomposition, take any unordered pair {a,b}⊂U. If it is uncovered in H, it lies in J[U]. Otherwise its unique covering triple has third vertex either in U, putting {a,b} in the 2-shadow of R, or equal to exactly one of x,y,z, putting {a,b} in the corresponding F_q. Uniqueness of pair coverage in a linear triple system makes these alternatives disjoint and exhaustive.

Finally suppose e is nonspecial of rank q with unique entrance x, and let {a,b}∈F_y, corresponding to f={y,a,b}. If R contained a (q-2)-edge linear path Q ending physically at a and avoiding b, then Q meets f only at its final vertex a, while f meets e only at y. Therefore
Q,f,e
is a q-edge linear path ending in e through entrance y. Since y is terminal at e, this contradicts nonspeciality and uniqueness of entrance x. Interchanging a,b gives the symmetric assertion; the argument for F_z is identical.