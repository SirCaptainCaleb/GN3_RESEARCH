# Maximum-rank uncolored reachability supports lie in two principal filters and admit a two-coordinate transversal

# Two principal-filter theorem for maximum-length color-free reachability

Let an arbitrary binary UNDIRECTED edge coloring of Q_n be given (antipodal oddness is NOT required). Let m<n be the largest length of any monochromatic geodesic anywhere in the cube. For root x and edge color q∈{0,1}, write
\[
I_q(x)=\{i\in[n]:c(\{x,x\oplus e_i\})=q\}.
\]
Thus I_0(x) and I_1(x) partition the n coordinate directions. Define the UNCOLORED rank-m reachability family
\[
\mathcal S_m(x)=\{S\in\binom{[n]}m:x\oplus S\in R(x)\}.
\]

**Theorem (maximal reachability lies in two principal filters).** If P is ANY monochromatic length-m geodesic starting at x, of color q and support S, then
\[
\boxed{I_q(x)\subseteq S.}
\]
Consequently
\[
\boxed{\mathcal S_m(x)\subseteq
\{S\in\binom{[n]}m:I_0(x)\subseteq S\}
\ \cup\
\{S\in\binom{[n]}m:I_1(x)\subseteq S\}.}
\]
This describes a constraint on the COLOR-FREE reachable-support family: there exists a partition [n]=A disjoint_union B such that every maximum-rank reachable support contains A or contains B. (The witness partition is the local edge-color split, although the definition and subsequent use of \(\mathcal S_m(x)\) need not encode colors.)

**Proof.** Suppose some i∈I_q(x) is absent from S. Traverse the q-colored edge x⊕e_i → x, then follow P from x to x⊕S. The resulting path uses direction i followed by the m distinct directions of S, so all m+1 coordinates are distinct. Every edge has color q, yielding a monochromatic geodesic of length m+1 and contradicting global maximality. This proves I_q(x)⊆S, and taking the union over the two possible witness colors proves the family inclusion. QED.

**Further consequences.**
1. A q-colored length-m geodesic can start at x only if |I_q(x)|≤m; in particular, if m<n/2, there can be terminal maximum-rank paths from x in AT MOST ONE color, necessarily a strictly minority incident-edge color.
2. For each color q represented by any maximum-rank geodesic from x, the entire family of q-witnessed rank-m supports has common intersection containing the nonempty star set I_q(x). This strengthens pairwise omitted-coordinate rigidity to a TOTAL intersection property.
3. Choose one direction i_q∈I_q(x) for each represented witness color q. Then \(\{i_0,i_1\}\) (omitting absent choices) intersects EVERY S∈\mathcal S_m(x). Thus the uncolored family \(\mathcal S_m(x)\) has transversal number at most TWO.
4. The size of \(\mathcal S_m(x)\) obeys
\[
|\mathcal S_m(x)|
\le \binom{n-|I_0(x)|}{m-|I_0(x)|}
+\binom{n-|I_1(x)|}{m-|I_1(x)|},
\]
with binomial coefficients of negative lower index defined as 0. A bound depending solely on n,m from the two-element transversal is
\[
|\mathcal S_m(x)|\le\binom nm-\binom{n-2}m
\]
when both colors occur; if only one witness color occurs, a one-element transversal gives the sharper bound \(\binom{n-1}{m-1}\). In particular there is no issue if one I_q(x) is empty, since no q-colored path of positive length can originate at x.
5. Under antipodal oddness, \(\mathcal S_m(\bar x)=\mathcal S_m(x)\) and \(I_q(\bar x)=I_{1-q}(x)\), giving the exact equivariance of this color-free filter structure.

**Topological program.** Rather than label roots with their entire exponentially large families \(\mathcal S_m(x)\), one may label each root with a minimal transversal of size 0,1,or2 of these supports, choosing it antipodally consistently. The missing step is to force an actual antipodal reachability overlap or an incompatible terminal-blocker incidence from this very small coordinate-label space. Abstract antipodal consistency of arbitrary two-element transversals is insufficient; the principal-filter and root-to-root extension constraints must be used.
