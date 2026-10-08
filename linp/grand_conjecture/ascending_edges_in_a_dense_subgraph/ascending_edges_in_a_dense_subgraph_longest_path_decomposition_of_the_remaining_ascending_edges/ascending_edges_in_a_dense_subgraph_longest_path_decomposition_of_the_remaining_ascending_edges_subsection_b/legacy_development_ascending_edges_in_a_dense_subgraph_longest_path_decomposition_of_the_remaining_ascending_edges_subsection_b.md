# Lemma 7 — preserved pre-item development

Fix \(\varepsilon>0\). Among the edges in class \(X\) assigned to a fixed vertex \(v\), only \(O_\varepsilon(1)\) can satisfy
\[
\phi(e)\le (1-\varepsilon)\phi(v). \tag{7}
\]

#### Proof
For an edge in class \(X\), the intersection of \(e\) with \(P_v\) is exactly \(\{x,v\}\). Order such intersections along \(P_v\). If two unique entrances occur far enough apart, the two corresponding edges can replace an interval of \(P_v\), producing a path that ends at one entrance and is too long for its vertex rank. Quantitatively, if the later edge has edge-rank deficit
\[
D=\phi(v)-\phi(e),
\]
then successive admissible entrance positions must be separated by at least \(D+1\), up to an absolute boundary term. Hence only
\[
O\!\left(\frac{\phi(v)}{D+1}+1\right)
\]
such edges can occur. Under (7), \(D\ge\varepsilon\phi(v)\), which gives \(O_\varepsilon(1)\). ∎

Thus a leading-order class \(X\) family must have edge rank \((1-o(1))\phi(v)\).

The class \(U\) creates many alternative last vertices by rotation.
