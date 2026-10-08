# A minimum signature shore is joined protectively to both connector vertices — preserved pre-item development

## Composition

(none yet)

## Development

## A minimum signature shore is joined protectively to both connector vertices

Assume shortcut-free pairs exist. Among all ordered pairs x,z with no protected shortcut and nonconstant pair signature, choose one for which the smaller signature shore has minimum size. Reverse x,z if necessary and write
A={u:alpha(x,z,u)=0},
B={u:alpha(x,z,u)=1},
with |A| minimal.

By the universal-connector theorem, for every u in A and v in B,
alpha(x,u,v)=1,
alpha(z,u,v)=0.

Fix u in A.

### The pair x,u

Let
f(y)=alpha(x,u,y)
for y outside {x,u}.

For y=z,
f(z)=alpha(x,u,z)=1
because alpha(x,z,u)=0 and swapping u,z complements.

For every y in B, the universal connector gives
f(y)=1.

Hence every vertex outside A belongs to the f=1 shore.

Suppose the pair x,u had no protected shortcut. If f were constant, x,u would be a clone pair and NOR would close. Therefore f is nonconstant. Its f=0 shore is then a nonempty subset of A\{u}, of size strictly smaller than |A|. This contradicts the minimal choice of A.

Therefore x,u has a protected fully-curved shortcut cell.

### The pair z,u

Put
g(y)=alpha(z,u,y).

For y=x,
g(x)=alpha(z,u,x)=alpha(x,z,u)=0
by cyclic invariance.

For every y in B,
g(y)=0
by the universal connector.

If z,u had no protected shortcut, nonconstancy would force its g=1 shore to be a nonempty subset of A\{u}, again contradicting minimality. The constant case is clone-contractible.

Thus z,u also has a protected shortcut cell.

Since reversing a fully-curved transition packet gives the opposite protected root on the same four-set, the protected relation is symmetric in orientation. Consequently every u in A is joined in both protected directions to both x and z.

### Consequence

A minimum unresolved switching split contains a protected complete bipartite exchange pattern
{x,z} <-> A.

Thus the split frontier has only two forms:
- |A|=1, a singleton shore with two protected connector pairs;
- |A|>=2, a nontrivial shore every vertex of which is protectively adjacent to both connector vertices.

This supplies a new finite/local target for the common-A3 machinery: exploit the dense protected join forced around a minimal signature shore, rather than an arbitrary protected circulation.
