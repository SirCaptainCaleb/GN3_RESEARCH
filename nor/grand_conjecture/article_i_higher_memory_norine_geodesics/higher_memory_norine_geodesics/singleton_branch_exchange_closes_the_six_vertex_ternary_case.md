# Audit: singleton-branch exchange does not contradict splice forcing

## Composition

(none yet)

## Development

## Failed singleton-branch contradiction: color flip makes the two constraints agree

Work in coordinate arity \(r=3\), the directed translation-invariant sector of \(N_4\).

A tempting argument tried to combine blocked-front recentering with outer-splice forcing to rule out a singleton branch in a minimum counterexample. The argument fails because recentering flips the fork color.

Normalize the original deletion fork to color \(0\):
\[
P=A,(u,v),\qquad Q=(b,v,u),
\]
with omitted vertex \(x\) and singleton second branch \(B=(b)\). Endpoint blocking gives
\[
h(x,b,v)=1. \tag{1}
\]

Recenter through the opposite branch \(P\). The exchange lemma produces a color-\(1\) fork on \(V\setminus\{b\}\):
\[
P'=(x,F_P),\qquad Q'=P^{\rm rev}.
\]
Its first outer branch is the singleton \(x\), and the first outer vertex of the other branch is \(v\).

For a general fork color \(\sigma\), the ternary outer-splice rule is:

- if the first branch is a singleton, the cross triple has color \(\sigma\);
- if the second branch is a singleton, the cross triple has color \(1-\sigma\).

Therefore the exchanged color-\(1\) fork forces
\[
h(x,b,v)=1, \tag{2}
\]
which is exactly the original endpoint-blocking identity (1), not a contradiction.

### Conclusion

Blocked-front recentering and the current outer-splice forcing lemma are perfectly sign-compatible on singleton branches. They do not by themselves exclude a singleton branch or close the six-vertex ternary case.

This failed route is worth retaining because the apparent contradiction is extremely easy to generate if one silently renormalizes the exchanged fork to color \(0\) without also complementing the cross bit. Any future exchange argument must track the fork color through recentering.
