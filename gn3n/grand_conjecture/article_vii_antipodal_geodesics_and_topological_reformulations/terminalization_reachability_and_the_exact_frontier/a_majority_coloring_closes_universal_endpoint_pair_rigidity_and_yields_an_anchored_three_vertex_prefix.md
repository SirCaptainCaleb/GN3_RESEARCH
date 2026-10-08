# A majority coloring closes universal endpoint-pair rigidity and yields an anchored three-vertex prefix

### Fence: universal endpoint-pair rigidity is impossible

Assume the odd uniform residue on (n=2r+1) vertices: every (r)-set is Hamiltonian and every ((r+1))-set is non-Hamiltonian.

Choose one Hamilton order (P_S=(a,b,ldots)) for each (r)-set (S). Suppose, toward a contradiction, that for every chosen word the first vertex (a) is a universal source in the centered tournament (T_b), i.e. ((a,b,z)) is tight for every (z\notin\{a,b\}).

For every vertex (b) that occurs second in a chosen word, let (f(b)=a). This is well-defined because a tournament has at most one universal source. Regard (b\mapsto f(b)) as a partial functional digraph, with vertices outside its domain having outdegree zero.

Every finite partial functional digraph admits a 2-coloring such that:
1. no directed walk of two edges is monochromatic;
2. every edge entering an outdegree-zero vertex is bichromatic.

Indeed, color trees by parity toward their terminal vertex; on a cycle component alternate around the cycle, allowing exactly one monochromatic edge when the cycle is odd, and color attached trees oppositely to their parent.

One color class has size at least (lceil n/2ceil=r+1), hence contains an (r)-set (S). Its chosen Hamilton order is ((a,b,ldots)), so (a,b) have the same color and (b\to a) is an edge of the functional digraph. Property 2 forces (a) to lie in the domain of (f). Put (z=f(a)). Then (b\to a\to z) is a directed 2-walk, so property 1 forces (z) to have the opposite color. Therefore (z\notin S).

Because (z=f(a)), (z) is a universal source of (T_a), hence ((z,a,b)) is tight. Thus
[
(z,a,b,ldots)
]
is a vertex-simple tight path of order (r+1). Its complement has (r) vertices and is Hamiltonian by the odd uniform hypothesis, yielding a spanning two-cover, contradiction.

Therefore universal initial-pair rigidity is impossible. There exists a maximum (r)-path
[
P=(a,b,p_3,ldots,p_r)
]
and a vertex (u\notin\{a,b\}) such that ((u,b,a)) is tight. The terminal analogue holds symmetrically.

This is a scale-independent fence: any branch that tries to make every maximum path's first pair universally rigid is already closed by an actual spanning two-cover.
