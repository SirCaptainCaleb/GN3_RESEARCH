# Ported homogeneous-module substitution preserves connectors and two-path covers

## Composition

**Homogeneous-module expansion lemma.** Let \(T\) be a tournament on shore \(A\), let \(\varnothing\ne M\subset A\) be a homogeneous module, and write \(Q=T/M\) for the quotient obtained by replacing \(M\) with a single vertex \(m\). Adjoin to \(T\) and \(Q\) the same special vertices \(z,x\), with \(z\to A\to x\) and \(z\to x\). Write \(\alpha(a,b,c)=t(a,b)+t(b,c)+t(c,a)\pmod 2\), where \(t(u,v)=1\) for \(u\to v\).

Suppose \(P=(p_1,\ldots,p_s)\) lists all of \(M\), satisfies \(\alpha(p_i,p_{i+1},p_{i+2})=0\) for every available index, and has forward first and last edges whenever defined. Then replacing \(m\) by the entire block \(P\) in any compatible zero connector \(C\) of \(Q\cup\{x,z\}\) produces a compatible zero connector of \(T\cup\{x,z\}\). Likewise this substitution carries any partition of \(Q\) into at most two fully ported zero paths to such a partition of \(T\).

**Proof.** Homogeneity means that, for any outside vertex \(u\), including \(x,z\), the incidence \(t(u,p_i)\) is independent of \(i\). Consequently a triple with precisely one block coordinate keeps its value when that coordinate is replaced by \(m\): \(\alpha(u,v,p_i)=\alpha(u,v,m)\) and \(\alpha(p_i,u,v)=\alpha(m,u,v)\). At a crossing containing two consecutive block coordinates, \(p_i\to p_{i+1}\) for \(i=1,s-1\); writing \(e=t(u,p_i)=t(u,p_{i+1})\), one has
\[
\alpha(u,p_i,p_{i+1})=e+1+(1-e)=0,\qquad
\alpha(p_i,p_{i+1},u)=1+(1-e)+e=0\pmod2.
\]
The other new triples are wholly internal to \(P\), hence have label zero. Unchanged triples retain their original labels. Original exposed pairs not meeting \(m\) stay forward; exposed pairs meeting \(m\) become uniformly oriented crossing pairs or forward endpoint edges of \(P\). Thus the expanded connector is compatible. The argument for two ported paths is identical, applied only to the one path containing \(m\). A singleton block is immediate.

**Consequence (global minimum-order reduction).** Choose a tournament of minimum order among all shore tournaments lacking a compatible connector. It has no proper nontrivial homogeneous module admitting a fully ported zero Hamiltonian path: otherwise contract the module, use minimality on the smaller quotient, and expand. Every homogeneous pair and every transitive module satisfies the path hypothesis. The conclusion is about cardinality-minimal tournaments across the entire class, not inclusion-minimal shores inside a fixed tournament. A cyclic three-vertex module fails the path hypothesis, so it remains possible.

This reduction permits internal substitution at arbitrary connector positions. It complements ordered-join closure, which treats extreme modules, and leaves the genuinely non-ported-module obstruction for further work.

## Development

Let T be the switching-normalized shore tournament, M a nonempty homogeneous subset, and Q=T/M the quotient tournament obtained by contracting M to a vertex m. Assume M has a ported zero Hamiltonian path P: every consecutive ternary tournament label α is 0, and its first and last directed edges are forward when defined. Then (a) replacing m by P in any compatible monochromatic-zero connector of Q∪{x,z} produces a compatible monochromatic-zero connector of T∪{x,z}; (b) replacing m in its member path extends any two-path cover of Q by ported zero paths to such a cover of T. All other vertex orders are preserved. This is an internal homogeneous-module substitution, requiring no source/sink location of M and allowing x,z anywhere in the connector. Corollary: a minimum-cardinality shore tournament lacking a compatible connector has no nontrivial homogeneous module with a ported zero Hamiltonian path, in particular no homogeneous pair or proper transitive module. Minimality here is among ALL shore tournaments by cardinality, not inclusion-minimality inside a fixed shore. The reduction leaves modules lacking such a path, including cyclic three-vertex modules, as genuine unresolved cases.
