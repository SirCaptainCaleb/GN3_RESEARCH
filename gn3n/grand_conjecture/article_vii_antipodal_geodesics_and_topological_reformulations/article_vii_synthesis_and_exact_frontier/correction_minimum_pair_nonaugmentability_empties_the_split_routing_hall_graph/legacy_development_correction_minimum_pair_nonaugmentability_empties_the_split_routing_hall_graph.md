# Correction: minimum-pair nonaugmentability empties the split-routing Hall graph — preserved pre-item development

## Development

## Correction/elevation: the split-attachment Hall graph is empty for a minimum pair

Retain the setup of [[two_tail_split_routing_is_an_exact_hall_problem]] with minimum deletion pair
\[
X=\{x,y\},\qquad H-X=P\mid Q.
\]

For \(z\in\{x,y\}\), any P-attachment makes \(P^- , z , b\) a Hamilton path on \(V(P)\cup\{z\}\). Together with the untouched Hamilton path \(Q\), this gives a two-cover after deleting only the other hole label, contradicting minimality of \(X\). The same argument excludes every Q-attachment.

Therefore, in a genuine two-deletion state, the entire \(2\times2\) split-attachment graph is empty.

Equivalently, for each hole \(z\),
\[
h(u,a,z)=0\ \text{or}\ h(a,z,b)=0,
\]
and
\[
h(v,d,z)=0\ \text{or}\ h(d,z,c)=0.
\]
Thus every hole has at least one explicit reverse junction on each tail.

The split-routing theorem remains a valid sufficient criterion for a general two-label residue, but its perfect-matching branch cannot occur once \(\{x,y\}\) is known to be a minimum deletion pair.

The live finite problem is therefore coupled two-hole routing: a successful path segment must use both \(x,y\) together, even though neither is individually insertable. Same-signature root-advance paths and the local two-bad-extension/parallel-middle lemmas are precisely of this coupled form.
