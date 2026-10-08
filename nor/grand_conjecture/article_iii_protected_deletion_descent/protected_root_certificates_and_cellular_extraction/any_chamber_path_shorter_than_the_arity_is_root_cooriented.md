# Any chamber path shorter than the arity is root-cooriented

## Composition

(none yet)

## Development

## Any chamber path shorter than the arity is root-cooriented

Let the ordered-window arity be r>=2. Let

pi_0, pi_1, ..., pi_l

be a path in the permutahedral chamber graph, each step an adjacent transposition, with l<r.

For a physical coordinate v write p_t(v)=pos_{pi_t}(v), and define the averaged rank

bar p(v)=(1/(l+1)) sum_{s=0}^l p_s(v).

Use the linear functional
Phi(e_v)=-bar p(v)
on the type-A root space.

Take any actual window-slide root from any chamber pi_t,

rho=e_a-e_c,

where a is the dropped coordinate and c the entering coordinate of two consecutive r-windows. Then

p_t(c)-p_t(a)=r.

Along one adjacent-transposition step, the position of any fixed coordinate changes by at most one. Hence

|p_s(v)-p_t(v)| <= |s-t|.

Therefore

bar p(c)-bar p(a)
>= r - (2/(l+1)) sum_{s=0}^l |s-t|.

The sum is maximized when t is an endpoint of the path and equals l(l+1)/2. Thus

bar p(c)-bar p(a) >= r-l >0.

Consequently
Phi(rho)>0
for every actual window-slide root carried by every chamber of the path.

### Theorem

The union of all actual window-slide roots carried by any permutahedral chamber path of length strictly less than r lies in one strict open halfspace. In particular it supports no positive root dependence.

For ternary arity r=3, no positive protected-root Radon obstruction can be carried on one, two, or three consecutive chambers: a connected carrier path must span at least three chamber walls, hence at least four chambers.

### Relevance to cut-changing extraction

A cut-changing wall is necessary for a genuine positive obstruction, but after the first such wall the obstruction cannot terminate locally. In ternary arity it must propagate through enough chamber geometry to achieve wall-distance at least three from some chamber in its support.

This matches the natural radius of the audited ternary repair packets (two- and three-position moves). A prospective extraction theorem may therefore use a shortest carrier path of wall-diameter three as the first genuinely non-cooriented local model; everything of smaller diameter is automatically zero-free by the averaged-rank functional.
