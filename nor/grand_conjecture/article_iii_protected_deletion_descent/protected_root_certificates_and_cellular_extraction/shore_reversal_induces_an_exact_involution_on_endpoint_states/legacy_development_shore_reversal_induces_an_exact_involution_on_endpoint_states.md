# Shore reversal induces an exact involution on endpoint states — preserved pre-item development

## Shore reversal induces an exact involution on endpoint states

Use the switching-split endpoint state of §333. A shore order
\[
P=(v_1,\ldots,v_m)
\]
is made into a directed Hamiltonian path by switching bits
\[
\sigma(v_i)\in\{0,1\}.
\]
Its endpoint parities are
\[
\epsilon_L=\sigma(v_1)\oplus\sigma(v_2),\qquad
\epsilon_R=\sigma(v_{m-1})\oplus\sigma(v_m),
\]
and its internal ternary word is \(c(P)\).

### Reverse the path

In the switched tournament realizing \(P\) as a directed path, every consecutive edge points
\[
v_i\to v_{i+1}.
\]
To make the reversed order
\[
P^{\rm rev}=(v_m,\ldots,v_1)
\]
directed, toggle alternating vertices along the path. Equivalently define
\[
\sigma'(v_i)=\sigma(v_i)\oplus(i\bmod 2),
\]
up to one global complement of all switching bits.

Every consecutive edge has exactly one endpoint toggled, so every path edge reverses. Thus \(P^{\rm rev}\) is directed in the new switching representative.

For each adjacent pair,
\[
\sigma'(v_i)\oplus\sigma'(v_{i+1})
=
1-\bigl(\sigma(v_i)\oplus\sigma(v_{i+1})\bigr).
\]
Therefore the reversed endpoint parities are
\[
\boxed{
\epsilon_L(P^{\rm rev})=1-\epsilon_R(P),\qquad
\epsilon_R(P^{\rm rev})=1-\epsilon_L(P).
}
\]

### Ternary word

Switching preserves the ternary label \(\alpha\), while reversal is odd. Hence
\[
\boxed{
c(P^{\rm rev})=\overline{c(P)^{\rm rev}}.
}
\]

Thus the complete endpoint state has the involution
\[
\boxed{
(c,\epsilon_L,\epsilon_R)
\longmapsto
(\overline{c^{\rm rev}},\,1-\epsilon_R,\,1-\epsilon_L).
}
\]

Applying it twice returns the original state.

### One-change normalization

If
\[
c=0^p1^q,
\]
then
\[
\overline{c^{\rm rev}}=0^q1^p.
\]
So reversal preserves the direction of a normalized \(0\to1\) shore switch while exchanging the phase lengths and complementing/swapping the endpoint parity ports.

For a monochromatic word \(0^p\), reversal produces \(1^p\), and conversely.

### Consequence

Every recursively attainable shore state occurs together with its involutive partner above. Any finite-state reachability or least-unreachable proof for the switching-split composition law may quotient by this involution.

In particular the endpoint-state search does not require treating the four parity pairs independently for both path orientations; reversal pairs
\[
(0,0)\leftrightarrow(1,1),\qquad
(0,1)\leftrightarrow(0,1),\qquad
(1,0)\leftrightarrow(1,0)
\]
after the left/right swap prescribed above, together with the corresponding transformed ternary word.
