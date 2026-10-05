# The switch and common endpoint normalize to r

## Metadata

- ID: auxiliary_vertex_exactification_subsection_b
- Parent Section: auxiliary_vertex_exactification
- Position: 2
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

The extension does more than create a correspondence: it normalizes the geometry.

For nonempty \(P,Q\), let \(p=|P|\) and
\[
\epsilon=h(\operatorname{last}(P),r,\operatorname{last}(Q)).
\]
In the order \((P,r,Q^{\rm rev})\), the number of initial tight triple positions is
\[
a=p-1+\epsilon.
\]
Thus the ordinary edge straddling the change contains \(r\). The switch location is forced by the extension.

Likewise, every tight path containing \(r\) has at most one vertex after \(r\), because any triple beginning at \(r\) is non-tight. Therefore any pair of tight paths sharing an oppositely directed terminal edge and covering \(V\cup\{r\}\) must share an edge containing \(r\). Under the endpoint-moving involution, exactly one of its two common-terminal states ends at \(r\). Removing \(r\) from that normalized state gives a two-cover of \(H\).

So neither the switch position nor the common endpoint needs to be found by a separate search once the extension is made.

## Development

The extension does more than create a correspondence: it normalizes the geometry.

For nonempty \(P,Q\), let \(p=|P|\) and
\[
\epsilon=h(\operatorname{last}(P),r,\operatorname{last}(Q)).
\]
In the order \((P,r,Q^{\rm rev})\), the number of initial tight triple positions is
\[
a=p-1+\epsilon.
\]
Thus the ordinary edge straddling the change contains \(r\). The switch location is forced by the extension.

Likewise, every tight path containing \(r\) has at most one vertex after \(r\), because any triple beginning at \(r\) is non-tight. Therefore any pair of tight paths sharing an oppositely directed terminal edge and covering \(V\cup\{r\}\) must share an edge containing \(r\). Under the endpoint-moving involution, exactly one of its two common-terminal states ends at \(r\). Removing \(r\) from that normalized state gives a two-cover of \(H\).

So neither the switch position nor the common endpoint needs to be found by a separate search once the extension is made.
