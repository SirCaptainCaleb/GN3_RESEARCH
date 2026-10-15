# Switch-filtered Rees chains and root contraction

# A switch-filtered Rees chain complex with a rank-preserving contraction

The formal switch-weighted Freudenthal chain of the preceding subsection is useful for locating exchange defects, but it is not a chain complex with a switch-sensitive differential. This subsection constructs one. The construction is natural for every unrestricted binary cube-edge coloring and every root, and retains dimension-simple geodesic witnesses for all its simplices.

Fix a root \(x\) of \(Q_n\), and let \(T_x\) denote the rooted Freudenthal triangulation of the entire geometric cube. For a simplex \(\tau\in T_x\), define its **minimum switch grade** by
\[
\nu_x(\tau)=\min\{\operatorname{sw}(P):
P\text{ is a rooted dimension-simple geodesic prefix from }x
\text{ and its Freudenthal simplex contains }\tau\}.
\tag{1}
\]
Every simplex of \(T_x\) occurs in some rooted saturated chain from \(x\), so this minimum exists. The prefix complexes of Article XIV satisfy
\[
K_x^{[r]}=\{\tau\in T_x:\nu_x(\tau)\le r\}.
\tag{2}
\]
The grade is nonincreasing under taking simplicial faces: if \(\eta\subseteq\tau\), then \(\nu_x(\eta)\le\nu_x(\tau)\).

Put \(R=\mathbb F_2[t]\). Define the **Rees chain complex** as the \(R\)-submodule
\[
\boxed{
\mathscr R_xC_k=
\bigoplus_{\substack{\tau\in T_x\\\dim\tau=k}}
R\cdot(t^{\nu_x(\tau)}\tau)
\subseteq C_k(T_x;\mathbb F_2)\otimes R,
}
\tag{3}
\]
and use the ordinary simplicial boundary, extended \(R\)-linearly.

**Theorem 1 (filtered chain structure).** The modules (3), together with the inherited boundary, form an augmented chain complex of free \(R\)-modules. On a weighted simplex generator,
\[
\boxed{
\partial(t^{\nu_x(\tau)}\tau)=
\sum_{\eta\lessdot\tau}
t^{\nu_x(\tau)-\nu_x(\eta)}
\bigl(t^{\nu_x(\eta)}\eta\bigr).
}
\tag{4}
\]
In particular, the boundary never increases the minimum required number of switches. The specialization at \(t=1\) gives the ordinary Freudenthal simplicial chains. The specialization at \(t=0\) gives the associated graded complex of the switch filtration, whose boundary retains only faces with the same minimum switch grade.

*Proof.* Every exponent in (4) is nonnegative by face monotonicity. Thus the ordinary boundary preserves \(\mathscr R_x\). Since it squares to zero in the ambient chain complex, it does so on this submodule. Its generators form a free \(R\)-basis. At \(t=1\), each generator maps to the corresponding unweighted simplex. At \(t=0\), the coefficient in (4) vanishes when \(\nu_x(\eta)<\nu_x(\tau)\), retaining the grade-preserving part of the boundary. This is the usual associated graded chain differential. \(\square\)

**Theorem 2 (rank-preserving filtered cone contraction).** The augmented Rees complex \(\mathscr R_xC_*\) has a chain contraction over \(R\), preserving the minimum switch grade. In particular its augmented homology vanishes, and the associated graded complex at \(t=0\) is also acyclic.

*Proof.* Every generating rooted geodesic-prefix simplex contains the apex \(x\). Hence for every simplex \(\tau\) not containing \(x\), the join \(x*\tau\) is a simplex of \(T_x\) with
\[
\boxed{\nu_x(x*\tau)=\nu_x(\tau).}
\tag{5}
\]
Indeed any admissible prefix simplex witnessing \(\tau\) already contains \(x\), so adjoining \(x\) neither creates nor removes any candidate witnesses. Define the cone operator \(h(\tau)=x*\tau\) when \(x\notin\tau\), and \(h(\tau)=0\) when \(x\in\tau\), with \(h(\varnothing)=[x]\) in the augmented complex. The standard simplicial cone identity over \(\mathbb F_2\) gives
\[
\partial h+h\partial=\mathrm{id}.
\tag{6}
\]
Equation (5) ensures that this homotopy preserves the Rees submodules and requires no extra powers of \(t\). It therefore contracts the augmented Rees chain complex over \(R\). Specializing (6) at \(t=0\) also contracts the associated graded complex. \(\square\)

If the coloring is antipodally odd, antipodal inversion carries the rooted switch filtration for \(x\) to that for \(\bar x\), because every path's color word is complemented without altering its switches. Thus it supplies natural isomorphisms \(\mathscr R_xC_*\to\mathscr R_{\bar x}C_*\).

## A deterministic one-edge switch update

Let \(xy\) be a cube edge of color \(a\) in dimension \(i\). Suppose \(P\) is a nonempty dimension-simple geodesic prefix from \(y\) avoiding dimension \(i\), with \(r\) switches, first edge color \(b\), and last edge color \(\beta\). Prepending \(x\to y\) preserves independence and yields
\[
\operatorname{sw}\bigl((x,y)\cdot P\bigr)=r+(a\oplus b).
\tag{7}
\]
For every nonempty binary word, \(b\oplus\beta=r\bmod2\). Hence
\[
\boxed{
\operatorname{sw}\bigl((x,y)\cdot P\bigr)
=r+\bigl(a\oplus\beta\oplus(r\bmod2)\bigr).
}
\tag{8}
\]
The last color remains \(\beta\). For an empty \(P\), prepending simply creates a one-edge path of color \(a\), with zero switches.

**Proposition 3 (terminal-color state suffices for root extension).** The integer switch count \(r\), the terminal color \(\beta\), and the prepended edge color \(a\) determine both the new switch count and the new terminal color. No independent initial-color state is needed once the switch parity is recorded.

*Proof.* The bit of the first edge of \(P\) is \(b=\beta\oplus(r\bmod2)\). Substitute this into (7). The terminal edge does not change on prepending. \(\square\)

## What this resolves and what it does not

The Rees model provides an honest filtered chain complex, with a boundary and contraction that use only full-rank path witnesses. By contrast, multiplying every maximal simplex by the formal unit \((1+u)^{S(\pi)}\) near \(u=0\) is an invertible diagonal basis change over \(\mathbb F_2[[u]]\); that alone cannot create a new homological obstruction. The nonunit parameter \(t\) in (3) retains information at its monochromatic specialization \(t=0\).

Theorem 2 simultaneously shows that **individual rooted filtrations have no homological obstruction at any switch level**: each one has the same apex-preserving contraction. The missing Wu–Yang theorem must therefore concern the relative geometry of different roots, their antipodes, or their intersections, not ordinary homology of a single root filtration.

The update law (8) identifies a two-state endpoint refinement for root-transport maps. It does not yet give an equivariant chain map across mixed-color squares: different witnessing paths for the same Freudenthal simplex can have different terminal colors, and selecting terminal colors is not generally closed under simplicial deletion. A suitable path-flag resolution, or equivalent chain-level correspondence retaining witnesses, is still required.
