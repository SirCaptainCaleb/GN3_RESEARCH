# A minimum shortcut-free signature shore is a protected clique — preserved pre-item development

## Composition

(none yet)

## Development

## A minimum shortcut-free signature shore is a protected clique

Continue with a minimum shortcut-free pair \(x,z\) and its minimum nonempty signature shore
\[
A=\{u:\alpha(x,z,u)=0\},
\]
with opposite shore \(B\). Use the switching-normalized form of §332:
\[
B\to z\to A\to x,
\]
and every \(B\)-vertex dominates every \(A\)-vertex.

Section §334 already shows that every \(u\in A\) is protectively adjacent to both \(x\) and \(z\).

We now show that every pair inside \(A\) is also protected.

### Outside \(A\), every internal pair has constant signature

Fix distinct \(u,v\in A\). Let
\[
h(w)=\alpha(u,v,w),
\qquad w\notin\{u,v\}.
\]
Write
\[
e=t(u,v)\in\{0,1\}
\]
in the switching-normalized tournament representative.

If \(w\in B\cup\{z\}\), then \(w\) dominates both \(u\) and \(v\). Hence
\[
t(v,w)=0,\qquad t(w,u)=1,
\]
and therefore
\[
h(w)=e\oplus1.
\]

If \(w=x\), then both \(u\) and \(v\) dominate \(x\). Hence
\[
t(v,x)=1,\qquad t(x,u)=0,
\]
so again
\[
h(x)=e\oplus1.
\]

Thus
\[
\boxed{h(w)=e\oplus1\quad\text{for every }w\notin A.}
\]

### Minimality forces a protected shortcut

Suppose the ordered pair \(u,v\) had no protected shortcut.

If \(h\) were constant on all of \(V\setminus\{u,v\}\), then \(u,v\) would be a clone pair and the clone-contraction theorem would close NOR.

Hence \(h\) is nonconstant. Since every vertex outside \(A\) has value \(e\oplus1\), the opposite signature shore
\[
\{w:h(w)=e\}
\]
is a nonempty subset of
\[
A\setminus\{u,v\}.
\]
Its size is at most
\[
|A|-2<|A|.
\]

But then \(u,v\) would be a shortcut-free pair with a strictly smaller nonempty signature shore, contradicting the minimal choice of \(A\).

Therefore \(u,v\) has an actual protected shortcut cell.

Reversal of a fully-curved transition carrier realizes the opposite root on the same four-set, so the protected adjacency is bidirectional.

### Theorem

For a minimum shortcut-free pair \(x,z\),
\[
\boxed{\text{every two distinct vertices of }A\text{ are protectively adjacent}.}
\]

Combining with §334,
\[
A\cup\{x,z\}
\]
has protected shortcut cells for every unordered pair except possibly the original missing pair \(\{x,z\}\).

Thus a minimum unresolved switching split contains a **protected almost-clique**
\[
K_{|A|+2}-xz.
\]

### Closure target

The remaining obstruction is no longer a sparse protected-root circulation. It is one missing protected edge inside an otherwise complete protected graph, together with the universal flat \(x,z\) connector.

A natural next theorem is therefore a local completion principle:

> If \(x,z\) are joined through two or more common vertices that are pairwise protectively adjacent, then the missing protected edge \(x,z\) is forced, or a spanning NOR order exists.

Since §337 gives \(|A|\ge2\), every minimum unresolved split already supplies at least two such common protected neighbors.
