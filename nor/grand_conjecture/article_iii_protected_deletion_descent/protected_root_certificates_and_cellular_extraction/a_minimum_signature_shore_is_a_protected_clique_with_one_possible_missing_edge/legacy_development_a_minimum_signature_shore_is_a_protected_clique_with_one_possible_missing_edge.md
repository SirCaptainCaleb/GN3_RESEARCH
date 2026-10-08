# A minimum signature shore is a protected clique with one possible missing edge — preserved pre-item development

## Composition

(none yet)

## Development

## A minimum signature shore is a protected clique, leaving only the connector edge missing

Continue with the minimum shortcut-free signature shore
A={u:alpha(x,z,u)=0},
B={u:alpha(x,z,u)=1}.

Section 334 gives protected shortcut cells between each u in A and each of x,z.

Now fix distinct u,v in A and put
h(y)=alpha(u,v,y)
for y outside {u,v}.

Let
s=alpha(x,u,v).

For any y in B, flatness on {x,u,v,y} gives
alpha(u,v,y)
=alpha(x,u,v) xor alpha(x,u,y) xor alpha(x,v,y)
=s xor 1 xor 1
=s,
because the universal connector gives alpha(x,u,y)=alpha(x,v,y)=1.

The same calculation with y=z uses
alpha(x,u,z)=alpha(x,v,z)=1
and gives
alpha(u,v,z)=s.

Finally
alpha(u,v,x)=alpha(x,u,v)=s
by cyclic invariance.

Thus the pair signature h is CONSTANT with value s on every vertex outside A.

Suppose u,v had no protected shortcut. If h were globally constant, u,v would be a clone pair and minimum counterexamplehood would fail. Hence h would be nonconstant, and its opposite-value shore would be a nonempty subset of
A\{u,v},
strictly smaller than A.

That contradicts minimality of A among shortcut-free pair-signature shores.

Therefore every pair u,v in A has a protected fully-curved shortcut cell.

Combining with §334, every unordered pair in
K=A union {x,z}
is protected except possibly the original connector pair {x,z}.

Equivalently the minimum unresolved split is an almost-complete protected clique:
the protected-root compatibility graph on K is K_|K| minus at most the single edge xz.

This is a major sharpening of the frontier. Any closure theorem showing that an almost-complete protected clique cannot have one shortcut-free missing edge would eliminate switching splits entirely.
