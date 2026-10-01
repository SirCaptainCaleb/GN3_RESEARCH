# Odd-degree repulsion and transfer cliques rigidify radius-three equality

## Statement

In the order-thirteen mu=6 shell, let S be a Hamiltonian six-set, R=V(H)-S its deficient seven-complement, G the Hamiltonian-support odd graph, and Gamma the Johnson-radius-three deficient-support graph. Then deg_G(S) equals the number of r in R for which R-r is Hamiltonian. If a Gamma-neighbor R' of R has degree two, then the acquired triple R-R' consists of Hamiltonian deletion labels of R, so deg_G(S)>=3. Conversely, all legal transfers r with R-r Hamiltonian produce deficient supports S union {r} forming a clique K_deg_G(S) in Gamma. Hence inside a 2-regular Gamma component, disjoint Hamiltonian supports force deg_G(S)=3; in the sliding-triple representation this yields T_{i-2}=T_{i+1}.

## Body

# Odd-degree repulsion and transfer cliques rigidify radius-three equality

Work in the order-thirteen mu=6 shell. Let S be a Hamiltonian six-set and R=V(H)-S its deficient seven-complement. Let G be the Hamiltonian-support odd graph and Gamma the graph on deficient seven-supports joined at Johnson distance at most three.

By the exact odd-graph exchange model, the G-neighbors of S are exactly the Hamiltonian six-subsets of R. Every such subset is uniquely R-{r}. Therefore
deg_G(S)=|{r in R : H[R-{r}] is Hamiltonian}|.                         (1)

Now suppose R' is a Gamma-neighbor of R and deg_Gamma(R')=2. Degree-two rigidity says every edge incident with R' has Johnson distance three. For the neighbor R, the acquired set
Y=R-R'
has order three, and rigidity further says that for every y in Y every exact cover of H-y has support partition
(R-{y}) | S.
Thus R-{y} is Hamiltonian for each y in Y. By (1),
deg_G(S)>=3.                                                         (2)

Equivalently, if deg_G(S)<=2, no radius-three neighbor of R can have Gamma-degree two. Since Gamma has minimum degree at least two, every such neighbor then has degree at least three.

The same deletion labels also give a positive expansion statement. Put
D={r in R : H[R-{r}] is Hamiltonian}.
For each r in D, the transfer
(R-{r}) | (S union {r})
is again a D=1 state: R-{r} is Hamiltonian, while S union {r} cannot be Hamiltonian or these two paths would form a spanning two-cover. Thus each
R_r=S union {r}
is a deficient support.

For distinct r,s in D,
R_r intersect R_s=S,
so d_J(R_r,R_s)=1. Hence
{S union {r}: r in D}
induces a clique K_|D|=K_deg_G(S) in Gamma.                         (3)

Now suppose R and R'=V(H)-S' lie in one 2-regular component of Gamma and S,S' are disjoint. There is a unique x outside S union S'. The odd edge S--S' has label x, equivalently R-{x}=S' is Hamiltonian, so x in D. The corresponding transfer support is
S union {x}=V(H)-S'=R'.
By (3), if d=deg_G(S), then
deg_Gamma(R')>=d-1.
Since the component is 2-regular, d<=3. But d<=2 is excluded by (2), because R has degree-two Gamma-neighbors. Therefore
deg_G(S)=3.

Finally, in a sliding-triple component
S_i=T_{i-1} disjoint-union T_i,
the sliding-triple theorem gives every vertex of
T_{i-2} union T_{i+1}
as a Hamiltonian deletion label of R_i. If S_i is disjoint from another cycle support, the preceding argument gives deg_G(S_i)=3. Both T-sets have order three, so their union has order at most three only if
T_{i-2}=T_{i+1}.

Thus low odd degree strictly repels radius-three equality, while larger deletion multiplicity creates an explicit transfer clique; on a 2-regular branch the two mechanisms meet exactly at odd degree three and force period-three equality.
