# The terminal double-matching five-bridge canonically generates a coherent two-label square

## Statement

In the all-the-way propagation branch of 8797f79d4a78, put
C=(q_1,q_0,p_r,x,p_0),
A=(p_1,...,p_{r-1}),
B=(q_2,...,q_s).
Then C|A|B is a spanning three-cover. Define
D={q_0,p_r,x}, a=q_1, b=p_0, and K=H-(D union {a,b})=H-V(C).
Then D, D+a, D+b, and D+a+b are all Hamiltonian. Moreover K has the inherited two-cover A|B, and K+a+b has the endpoint-coherent two-cover
(b,A) | (a,B).
Deleting a, b, or both from that displayed cover realizes the other three pc-two square states. Hence this residue is exactly a coherent two-label endpoint square over the Hamiltonian three-core D.

## Body

The terminal branch of 8797f79d4a78 gives the tight five-path
C=(q_1,q_0,p_r,x,p_0).
Therefore its consecutive subpaths
D=(q_0,p_r,x),
D+a=(q_1,q_0,p_r,x),
D+b=(q_0,p_r,x,p_0),
and D+a+b=C
are all Hamiltonian.

Removing C from H leaves exactly
A=(p_1,...,p_{r-1})
and
B=(q_2,...,q_s),
both inherited tight paths, so K=H-C has displayed two-cover A|B.

Now consider K+a+b=H-D. The path
(b,A)=(p_0,p_1,...,p_{r-1})
is inherited from P after deleting p_r, while
(a,B)=(q_1,q_2,...,q_s)
is inherited from Q after deleting q_0. Thus
(b,A)|(a,B)
is a two-cover of K+a+b in which b and a are displayed endpoints of their respective components. Deleting a gives (b,A)|B, deleting b gives A|(a,B), and deleting both gives A|B. All four induced subtournaments are proper; Hamiltonicity of any would combine with the complementary Hamiltonian support D plus the appropriate subset of {a,b} to two-cover H, so each square state is non-Hamiltonian and has path-cover number exactly two.

Thus the terminal double-matching residue realizes precisely the endpoint-coherent square geometry, with no appeal to a migration or existence argument.