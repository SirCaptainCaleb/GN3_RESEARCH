# The outermost-change root is invariant under deep-core galleries

## Composition

For a bad order with first/last change positions p<q and D=e_{v_p}-e_{v_{q+3}}, any adjacent swap at positions r,r+1 with p+4<=r<=q-2 preserves the exact outermost root. Such a swap changes only window ranks r-2,...,r+1, strictly inside the outermost-change collars, and fixes both root endpoints. Hence the deep core may be gallery-normalized freely while keeping D and badness fixed; only bounded endpoint collars can obstruct realization.

## Development

## The outermost-change root is invariant under deep-core galleries

Let
\[
\pi=(v_1,\ldots,v_n)
\]
be a bad ternary order. Write \(c_i=\alpha(v_i,v_{i+1},v_{i+2})\), let \(p\) be the first change position and \(q\) the last change position, and let
\[
D(\pi)=e_{v_p}-e_{v_{q+3}}.
\]

Consider one adjacent transposition of positions \(r,r+1\).

An adjacent swap can change only the four ternary windows whose starting ranks are
\[
r-2,r-1,r,r+1.
\]
Therefore, if
\[
p+4\le r\le q-2,
\]
every changed window rank lies strictly between the two status pairs defining the outermost changes:
\[
\{r-2,r-1,r,r+1\}\subseteq\{p+2,\ldots,q-1\}.
\]

Hence the statuses \(c_p,c_{p+1},c_q,c_{q+1}\) are unchanged. The change at \(p\) remains a change, the change at \(q\) remains a change, no window outside \([p,q+1]\) changes, and so no new change can appear before \(p\) or after \(q\).

The swapped positions are also disjoint from positions \(p\) and \(q+3\). Thus the physical source and target coordinates of the outermost root are unchanged.

Consequently
\[
\boxed{D(\pi s_r)=D(\pi)}
\]
for every adjacent swap with \(p+4\le r\le q-2\).

### Gallery form

Any adjacent-swap gallery all of whose swaps remain in this deep-core range preserves the exact outermost root at every state. Since the changes at \(p\) and \(q\) persist, every gallery state remains bad.

In particular, the coordinates occupying positions
\[
p+4,\ldots,q-1
\]
may be permuted arbitrarily by adjacent swaps without changing \(D\), provided the endpoint collars are held fixed.

### Closure relevance

An outermost-root witness may therefore be normalized freely through its long interior. Its genuinely rigid data are confined to bounded collars around the first and last changes together with the two root endpoints.

For a flag-compatible root chain
\[
x_0\to x_1\to\cdots,
\]
long interiors of the individual witnesses cannot be the source of a realization obstruction: each can be gallery-normalized independently while retaining the same physical root. The remaining compatibility problem is an endpoint-collar problem at the shared vertex \(x_i\).

This supplies a direct bridge between the root-valued degree carrier of §243 and the width-two/three-coordinate collar program of §238: after deep-core normalization, only bounded endpoint collars can obstruct relative splicing.
