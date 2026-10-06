# Same-signature rerooting reduces to two explicit reverse junctions

## Metadata

- ID: same_signature_rerooting_reduces_to_two_explicit_reverse_junctions
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 44
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Same-signature central supports reduce rerooting to two reverse junctions

Let \(X=\{x,y\}\) be a minimum deletion pair and
\[
H-X=P\mid Q,
\]
with terminal pieces
\[
(\ldots,u,a,b)=P,\qquad (\ldots,v,d,c)=Q.
\]
Thus minimum-hole four-end synchronization gives, for each \(z\in\{x,y\}\),
\[
h(z,b,a)=1,\qquad h(z,c,d)=1.
\]

Assume first that the common terminal signature is
\[
h(b,x,c)=h(b,y,c)=1.
\]
Exactly one of
\[
h(x,b,y),\qquad h(y,b,x)
\]
is tight. Choose the ordering \((\gamma,\delta)\) of \((x,y)\) so that
\[
h(\gamma,b,\delta)=1.
\]
Then
\[
(\gamma,b,\delta,c,d)
\]
is a tight five-path, since
\[
h(b,\delta,c)=1,\qquad h(\delta,c,d)=1.
\]

If both
\[
h(u,a,\gamma)=1
\quad\text{and}\quad
h(a,\gamma,b)=1,
\]
then
\[
(p_1,\ldots,u,a,\gamma,b,\delta,c,d)
\]
is a tight path. Together with the untouched path
\[
(q_1,\ldots,v)
\]
it is a spanning two-cover of \(H\). Therefore a genuine obstruction must satisfy at least one of
\[
h(u,a,\gamma)=0,\qquad h(a,\gamma,b)=0.
\]
By boundary antisymmetry these are respectively equivalent to the reverse junctions
\[
\boxed{h(\gamma,a,u)=1}
\qquad\text{or}\qquad
\boxed{h(b,\gamma,a)=1}.
\]

If instead the common terminal signature is zero, boundary antisymmetry gives
\[
h(c,x,b)=h(c,y,b)=1,
\]
and the same argument with \(P,Q\) exchanged produces a distinguished ordering \((\gamma,\delta)\) for which
\[
(\gamma,c,\delta,b,a)
\]
is tight. Unless this already extends through the inherited \(Q\)-prefix to a two-cover, one of the corresponding two reverse junctions at \(d,v\) is forced.

Hence:

> **Two-junction rerooting dichotomy.** At either boundary of a same-signature minimum deletion pair, the Hamiltonian central four-support is not an unstructured routing problem. It either splices directly to the inherited complementary path and yields a two-cover, or a uniquely selected leading hole label \(\gamma\) witnesses one of two explicit reverse junctions across the next two anchor layers.

Applying the theorem independently at the two opposite boundaries leaves only four binary rerooting types. The next closure step can therefore compare those reverse junctions with the cross-end five-path tests and the local bad-extension calculus, rather than ranging over Hamilton orders of the whole central support.

## Frontier

- Development version when composed: None
- Development version now: 1
