# 

## Composition

Fix \(v\), put \(p=\phi(v)\), and let \(F\subseteq H_v\) contain \(k\) edges that meet the chosen maximum \(p\)-edge path \(P\) in exactly one off-\(v\) vertex.

Separate \(F\) into \(U\) and \(X\), where an edge belongs to \(U\) if that intersection is its opposite terminal and belongs to \(X\) if that intersection is its unique entrance.

For \(e\in X\), let \(a(e)\) be the first edge of \(P\) containing its unique entrance and put
\[
\sigma(e)=\phi(x_e)-a(e).
\]
The path-splice recurrence for ordered entrance intersections gives, for every integer \(s\ge0\),
\[
k
\le
|U|+
|\{e\in X:\sigma(e)>s\}|+
4s+O(\log p). \tag{38}
\]

Take \(s=\lfloor k/16\rfloor\). If \(|U|\ge k/2\), at least half of the family meets \(P\) at its opposite terminal. Otherwise
\[
|\{e\in X:\sigma(e)>s\}|
\ge
k/4-O(\log p). \tag{39}
\]
Linearity places these edges in at least
\[
k/8-O(\log p)
\]
distinct interior pairs. By Lemma 8, at least half of those pairs either are doubly occupied and therefore determine a \(3\)-edge linear cycle, or have a distinct output edge contained in \(V_{\ge p}\).

We have proved:

## Development

Fix \(v\), put \(p=\phi(v)\), and let \(F\subseteq H_v\) contain \(k\) edges that meet the chosen maximum \(p\)-edge path \(P\) in exactly one off-\(v\) vertex.

Separate \(F\) into \(U\) and \(X\), where an edge belongs to \(U\) if that intersection is its opposite terminal and belongs to \(X\) if that intersection is its unique entrance.

For \(e\in X\), let \(a(e)\) be the first edge of \(P\) containing its unique entrance and put
\[
\sigma(e)=\phi(x_e)-a(e).
\]
The path-splice recurrence for ordered entrance intersections gives, for every integer \(s\ge0\),
\[
k
\le
|U|+
|\{e\in X:\sigma(e)>s\}|+
4s+O(\log p). \tag{38}
\]

Take \(s=\lfloor k/16\rfloor\). If \(|U|\ge k/2\), at least half of the family meets \(P\) at its opposite terminal. Otherwise
\[
|\{e\in X:\sigma(e)>s\}|
\ge
k/4-O(\log p). \tag{39}
\]
Linearity places these edges in at least
\[
k/8-O(\log p)
\]
distinct interior pairs. By Lemma 8, at least half of those pairs either are doubly occupied and therefore determine a \(3\)-edge linear cycle, or have a distinct output edge contained in \(V_{\ge p}\).

We have proved:
