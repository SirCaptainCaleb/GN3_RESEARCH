# Same two-end signature pairs force bidirectional five-path root advance — preserved pre-item development

## Composition

(none yet)

## Development

## Same two-end signature pairs give bidirectional five-path root advance

Let \(X\) be a minimum two-cover deletion set and fix
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t),
\]
with \(s,t\ge2\). For \(z\in X\), put
\[
\tau_I(z)=h(p_1,z,q_1),
\qquad
\tau_T(z)=h(p_s,z,q_t).
\]
Minimum-hole four-end synchronization gives, for every \(z\in X\),
\[
h(p_2,p_1,z)=h(q_2,q_1,z)=1,
\]
and
\[
h(z,p_s,p_{s-1})=h(z,q_t,q_{t-1})=1.
\]

Suppose distinct \(x,y\in X\) have the same two-end signature:
\[
\tau_I(x)=\tau_I(y),
\qquad
\tau_T(x)=\tau_T(y).
\]

### Initial boundary

If \(\tau_I(x)=\tau_I(y)=1\), then
\[
h(p_1,x,q_1)=h(p_1,y,q_1)=1.
\]
Exactly one of
\[
h(x,q_1,y),\qquad h(y,q_1,x)
\]
equals one. Hence for some ordering \((u,v)\) of \((x,y)\),
\[
(p_1,u,q_1,v)
\]
is a tight four-path. Since \(h(p_2,p_1,u)=1\),
\[
\boxed{(p_2,p_1,u,q_1,v)}
\]
is a tight five-path.

If instead \(\tau_I(x)=\tau_I(y)=0\), boundary antisymmetry gives
\[
h(q_1,x,p_1)=h(q_1,y,p_1)=1.
\]
The same argument, with \(P,Q\) exchanged, gives for some ordering \((u,v)\) of \((x,y)\)
\[
\boxed{(q_2,q_1,u,p_1,v)}
\]
tight.

Thus the same pair \(\{x,y\}\) admits one-step root advance at the initial boundary.

### Terminal boundary

If \(\tau_T(x)=\tau_T(y)=1\), then
\[
h(p_s,x,q_t)=h(p_s,y,q_t)=1.
\]
Exactly one of
\[
h(y,p_s,x),\qquad h(x,p_s,y)
\]
equals one. Hence for some ordering \((u,v)\) of \((x,y)\),
\[
(v,p_s,u,q_t)
\]
is a tight four-path. Since \(h(u,q_t,q_{t-1})=1\),
\[
\boxed{(v,p_s,u,q_t,q_{t-1})}
\]
is a tight five-path.

If \(\tau_T(x)=\tau_T(y)=0\), then
\[
h(q_t,x,p_s)=h(q_t,y,p_s)=1,
\]
and symmetrically for some ordering \((u,v)\) of \((x,y)\),
\[
\boxed{(v,q_t,u,p_s,p_{s-1})}
\]
is tight.

Therefore the same pair \(\{x,y\}\) admits one-step root advance at the terminal boundary as well.

### Induced two-deletion core

Put
\[
G_{x,y}=H-(X-\{x,y\}).
\]
Minimum-hole heredity gives
\[
\kappa_2(G_{x,y})=2.
\]
The initial five-path above, together with the untouched contiguous remainders of \(P\) and \(Q\), gives a spanning three-cover of \(G_{x,y}\); the terminal five-path gives a second spanning three-cover rooted at the opposite boundary. In the symmetric zero-root case
\[
|P|=|Q|=s+1,
\]
both have profile
\[
\boxed{5\mid(s-1)\mid s}
\]
up to exchanging the two long components.

Hence two hole vertices with the same initial and terminal endpoint signatures produce one genuine deletion-distance-two induced core in which the same restored pair supports root-advancing five-components from both opposite boundaries.

There are only four two-end signatures. Consequently, if \(|X|\ge5\), some pair \(x,y\in X\) has this property. More generally, every signature class contributes all of its vertex pairs, so minimum holes contain quadratically many such bidirectional pairs once a class is large.
