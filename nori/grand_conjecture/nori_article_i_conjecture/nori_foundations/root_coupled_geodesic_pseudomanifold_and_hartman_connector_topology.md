# Root-coupled geodesic pseudomanifold and Hartman connector topology

# Root-coupled geodesics and topological carriers

Let \(Q_n=\mathbb F_2^n\), and let \(c\) color ordered three-faces so that \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). A complete antipodal geodesic with initial root \(x\) and direction permutation \(p\) has successive vertices \(x\oplus\{p_1,\ldots,p_j\}\). The physical positions of its ordered faces matter.

**The all-root complex.** Let \(K_n\) be the simplicial complex whose facets are vertex sets of full cube geodesics. Each facet contains just one antipodal pair, its endpoints \(e_x=\{x,\bar x\}\). The subcomplex of paths with this pair of endpoints is
\[
K_x=e_x*\operatorname{sd}(\partial\Delta^{n-1}),
\]
an \(n\)-ball: its intermediate vertices are the nonempty proper subsets of the direction set ordered by inclusion. A codimension-one face obtained by omitting an interior path vertex has precisely two fillings, corresponding to swapping adjacent directions. Omitting an endpoint gives two possible completions at opposite ends. Root slides connect the various \(K_x\), proving that \(K_n\) is a connected closed pure \(n\)-dimensional pseudomanifold.

**No free global antipodality.** The action \(v\mapsto\bar v\) is simplicial on \(K_n\), but every antipodal endpoint-edge midpoint is fixed, and these are its only fixed points: a simplex contains no second antipodal pair. Thus a free Borsuk–Ulam argument on the entire \(K_n\) is inapplicable without a relative boundary theorem, a puncturing construction, or a different carrier.

**Local exchanges do not yet descend.** A forward root slide removes the first direction and appends it after the old endpoint. Its color word changes from \((w_1,\ldots,w_{n-2})\) to \((w_2,\ldots,w_{n-2},b)\). If \(D(P)=\sum_i[w_i\ne w_{i+1}]\), then
\[
D(P^+)=D(P)-[w_1\ne w_2]+[w_{n-2}\ne b].
\]
An adjacent transposition alters at most four consecutive windows. These are local moves on **actual** geodesics in every dimension, but do not furnish a monotone defect reduction by themselves.

**The doubled root–progress cube.** Represent a rooted partial geodesic by a root \(r\) and used-coordinate support \(S\). Its actual location is \(r\oplus\chi_S\). The vertical Boolean-root charts in the \(2n\)-cube \([0,1]^n_r\times[0,1]^n_s\) carry the usual Freudenthal chains and thereby all genuine rooted geodesics. The coordinatewise continuous map \(\Psi_i(r,s)=r_i+s_i-2r_is_i\) interpolates physical locations, but an interpolated crossing does not automatically represent a compatible path witness.

A second model records both *moving endpoints* \((x,y)\). At each step one may extend a partial geodesic at either endpoint in a previously unused coordinate. Monochromatic chains from a diagonal state \((z,z)\) produce genuine monochromatic geodesics. The resulting order complex triangulates \((\partial[0,1]^2)^n\), an \(n\)-torus—not a \(2n\)-ball—so ball-specific fixed-point indices and boundary conditions cannot be assumed.

**Certified root slides.** In the full ordered-three-face problem, a monochromatic witness with direction order \((u_1,\ldots,u_k,a,b)\) may drop its first \(t<k\) moves. The remaining suffix remains monochromatic, starts at \(x_t=x\oplus\{u_1,\ldots,u_t\}\), ends in \((a,b)\), and has the same absolute endpoint:
\[
x_t\oplus\{u_{t+1},\ldots,u_k,a,b\}
=x\oplus\{u_1,\ldots,u_k,a,b\}.
\]
The certified support rank strictly decreases. Its endpoint invariant \(y_i=x_i\oplus S_i\) makes these slides run along *opposite diagonals* of the geometric root/support square for the two endpoint values. A topological intersection of projected diagonals is not by itself an intersection of genuine witness sheets, and moving two witnesses independently may destroy their shared root.

**The extraction frontier.** A valid dimension-independent fixed-point theorem must force a root \(x\), two terminal directions \(J=(a,b)\), and actual monochromatic witnesses with nonempty complementary supports \(U,V\subseteq[n]\setminus J\), ending respectively in \(J\) and \(\operatorname{rev}J\). The exact reversed-two-tail splice then yields a full geodesic with at most one color change; merely obtaining a balanced simplex or interpolated zero does not. The missing ingredients are a proved equivariant boundary condition and a certificate-preserving common-root connector. Rooted charts, the all-root pseudomanifold, and the two-end torus supply faithful candidates, but none alone is grand closure.
