# Every front circuit already carries a canonical four-change cycle — preserved pre-item development

## Every front circuit already carries a canonical four-change cycle

Work in ternary arity in a directed NOR counterexample. Let
\[
P=(f_1,f_2,\ldots,r_1,r_2)
\]
be an inclusion-maximal \(\sigma\)-tight path, put \(\tau=1-\sigma\), and let \(X=V\setminus V(P)\). Let
\[
U\subseteq X,\qquad |U|=d\ge2,
\]
be any minimal infeasible front circuit in \(\mathcal F_{\tau,(f_1,f_2)}\). No whole-front assumption \(U=X\) is made. Put \(p=|P|-2\).

Fix \(x\in U\) and choose a \(\tau\)-tight facet witness
\[
W_x=(u_1,\ldots,u_{d-1},f_1,f_2)
\]
for \(U\setminus\{x\}\). Since \(U\) itself is infeasible, prepending \(x\) is blocked at the exposed front:
\[
h(x,u_1,u_2)=\sigma
\]
(with the evident \(d=2\) interpretation \(h(x,u_1,f_1)=\sigma\)). Therefore the order
\[
S_x=(x,u_1,\ldots,u_{d-1},P)
\]
on the vertex set \(V(P)\cup U\) has linear status word
\[
\sigma,\tau^{d-1},\sigma^p.
\tag{1}
\]

### Theorem: the induced cyclic carrier has exactly four changes
Because \(P\) is maximal, its reversal is a maximal \(\tau\)-tight path. Applying front blocking to the reversed path gives, for every omitted vertex and in particular for \(x\),
\[
h(x,r_2,r_1)=\sigma.
\]
Reversal antisymmetry yields
\[
h(r_1,r_2,x)=\tau.
\tag{2}
\]
Thus, when \(S_x\) is read cyclically, its first wrap status after the linear word is forced to be \(\tau\). The second wrap status
\[
z=h(r_2,x,u_1)
\]
is arbitrary. Hence the cyclic word is
\[
\sigma,\tau^{d-1},\sigma^p,\tau,z.
\tag{3}
\]
If \(z=\tau\), the cyclic run lengths are
\[
1,d-1,p,2.
\]
If \(z=\sigma\), the final \(\sigma\) merges cyclically with the initial singleton \(\sigma\), giving
\[
2,d-1,p,1,
\]
which after reversal has canonical form
\[
1,p,d-1,2.
\]
Thus in either case the cyclic variation is exactly four, with canonical profile
\[
1,p,d-1,2.
\tag{4}
\]
The carrier uses precisely \(V(P)\cup U\); the exterior set is \(X\setminus U\). \(□\)

### Consequence
Whole-frontness is not needed to reach the four-change geometry. Every punctured-Boolean front circuit already determines a canonical four-change cyclic carrier; the only role of \(U=X\) is to make that carrier spanning.

Accordingly the Article II promotion problem can be reformulated more geometrically:

> Given a canonical four-change carrier on \(V(P)\cup U\) with profile \(1,p,|U|-1,2\), absorb the exterior vertices \(X\setminus U\) without increasing cyclic variation beyond four, or use a failed absorption to produce a strictly stronger obstruction.

This matches the cycle-absorption and interval-reversal tools already present elsewhere in the project more directly than trying to turn \(U\) into the whole omitted set first.
