# Minimum endpoint cycles reduce pinned boundaries to one-bit pivot stops

## Metadata

- ID: minimum_endpoint_cycles_reduce_pinned_boundaries_to_one_bit_pivot_stops
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 117
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Minimal endpoint cycles reduce pinned boundaries to one-bit pivot stops

Assume the witness-preserving endpoint CORNER-LIFT property of Subsection 93. By Subsection 114, after minimizing partner changes and pushing every partner block backward, an unresolved endpoint-root cycle decomposes into exact constant-core arcs joined at pinned boundaries.

At a pinned boundary beginning at edge s,
a_s=x_{s-1},
and the endpoint witness omitting x_s has the form
O_{x_s}=(x_{s-1},b_s,x_{s+1},d_s,...)
with one-change deletion word.

Choose now, among all actual endpoint-root cycles obtainable from legal endpoint/deletion witnesses in the minimum-counterexample class, one of minimum length. Subject to that choice, normalize its partner word by the corner-lift procedure of §114.

### Apply the endpoint pivot theorem at a pinned boundary

Use the notation of Subsection 113:
x=x_s,
a=x_{s-1},
b=b_s,
c=x_{s+1},
d=d_s.

Put
lambda_0=alpha(a,c,d),
lambda_1=alpha(x,c,d).

Subsection 113 proves:

- if lambda_0=0, the endpoint pivot produces a legal one-change deletion witness omitting b with the same suffix beginning at c;
- if also lambda_1=0, a second pivot produces a legal witness omitting a;
- in the double-zero case the three endpoint witnesses realize the Johnson triangle
  {x,a}, {b,x}, {a,b},
  and, crucially, all three protected endpoint roots have the SAME target c:
  x->c, b->c, a->c.

Here a=x_{s-1} and c=x_{s+1}. Therefore the completed pivot triangle contains the actual protected endpoint root
x_{s-1} -> x_{s+1}.

### Shortcut lemma

The original physical root cycle contains the two consecutive roots
x_{s-1} -> x_s
and
x_s -> x_{s+1}.

If lambda_0=lambda_1=0, replace those two roots by the pivot root
x_{s-1} -> x_{s+1}.

Every other root of the cycle is unchanged. The result is again a directed physical endpoint-root cycle of actual protected roots, now with x_s removed from its cyclic support. Its length is one smaller.

This contradicts the choice of a minimum-length endpoint-root cycle.

Hence a pinned boundary of a minimum-length unresolved cycle CANNOT complete the pivot triangle.

### Theorem: every pinned boundary carries one explicit stopped bit

At every partner-change boundary of a minimum-length corner-lift-normalized endpoint cycle, at least one of
lambda_0=alpha(x_{s-1},x_{s+1},d_s),
lambda_1=alpha(x_s,x_{s+1},d_s)
equals 1 in the stopping order of §113.

More precisely, the local obstruction is one of:

1. first-stop type:
   lambda_0=1;

2. second-stop type:
   lambda_0=0 and lambda_1=1.

The double-zero type is excluded by physical-cycle shortening.

Thus, conditional on the corner-lift theorem, the arbitrary partner-defect circulation has been reduced to a cyclic sequence of exact constant-core arcs whose only junction data are one binary stop type at each pinned boundary.

### Face patterns at the two stop types

The pinned endpoint geometry already gives
alpha(x_{s-1},x_s,x_{s+1})=1.

Let
a=x_{s-1}, x=x_s, c=x_{s+1}, d=d_s.

Coboundary flatness on {a,x,c,d} gives the following useful local descriptions.

If lambda_0=0 and lambda_1=1 (second-stop type), then
alpha(a,x,c)=1,
alpha(a,c,d)=0,
alpha(x,c,d)=1,
and flatness forces
alpha(a,x,d)=0.

So the four face values in the ordered tetrahedron (a,x,c,d) are
1,0,0,1
in the natural face list
axc, axd, acd, xcd.

If lambda_0=1 (first-stop type), then flatness gives
alpha(a,x,d)=lambda_1.
Thus its remaining freedom is one bit lambda_1; the face pattern is
alpha(a,x,c)=1,
alpha(a,c,d)=1,
alpha(a,x,d)=alpha(x,c,d)=lambda_1.

These are the only local face packets that can occur at a pinned boundary of a minimum-length unresolved endpoint cycle.

### New closure target

The endpoint frontier is therefore no longer an arbitrary Johnson defect walk.

Under corner lifting and minimum physical-cycle choice it is:

- exact constant-core arcs, where cuts concatenate with zero defect;
- pinned arc junctions, each on three consecutive physical-cycle vertices;
- each junction has one of the two explicit stopped-pivot face packets above.

A closure proof may now attack the cyclic compatibility of these stop bits. Showing that one junction is double-zero shortens the cycle; showing that one stopped packet splices gives the full order.

## Frontier

- Development version when composed: None
- Development version now: 1
