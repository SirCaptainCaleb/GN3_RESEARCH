# A one-exception fan yields an exceptional-coordinate deletion witness with an adjacent clone pair — preserved pre-item development

## Composition

(none yet)

## Development

## Fan-to-deletion handoff

Assume a one-exception fan
alpha(a,b,c)=1-eta,
alpha(b,c,x)=eta for every x outside {a,b,c}.

Then b and c are exact ternary clones in every context avoiding a.

### Construct a one-change witness omitting the exceptional coordinate

Delete both a and b. By minimum-counterexamplehood, the smaller instance on
V minus {a,b}
has a one-change spanning order O containing c.

Insert b adjacent to c. Since a is absent, the exceptional-coordinate obstruction from the clone-insertion theorem disappears completely.

If c is internal in O, write
...,x,y,c,z,w,...
and put B=alpha(y,c,z).

- If B=eta, insert b immediately before c.
- If B=1-eta, insert b immediately after c.

The exact clone-insertion calculation shows that the new status word is precisely the old one with the single bit B duplicated. Hence it is still one-change. Endpoint occurrences are easier.

Therefore there exists a genuine one-change deletion witness on
V minus {a}
in which b and c are consecutive.

### Reinserting the exceptional coordinate certifies a controlled transition

Suppose for definiteness the witness contains
...,y,b,c,z,...
with
alpha(y,b,c)=alpha(b,c,z)=eta.
Insert a immediately before b:
...,y,a,b,c,z,...

The consecutive windows
(a,b,c), (b,c,z)
have colors
1-eta, eta.
Thus the reinsertion packet contains a certified transition on the tetrahedron {a,b,c,z}.

The two off-faces are alpha(a,b,z) and alpha(a,c,z). Because exactly one context coordinate is the exception a, the clone identity says these values are opposite. Hence this certified transition is in the standard coboundary-flat dichotomy:
- flat, with the corresponding endpoint repair available; or
- fully curved, carrying its protected slide root.

### Scope qualification

Reinserting a can also change the outer windows involving the coordinate(s) immediately to the left of the insertion site. Therefore the preceding paragraph does NOT claim that the resulting full spanning order has only this one defect, nor that the flat/full transition already closes NOR.

The valid handoff is narrower: the fan produces a genuine one-change deletion witness omitting its exceptional coordinate, with adjacent clones, and reinsertion next to that pair produces a certified flat-or-full transition with tightly localized additional splice data.

### Consequence

A one-exception fan is not an unconstrained global geometry. It reduces to the existing Article III deletion/reinsertion interface with unusually rigid provenance:
1. the omitted coordinate is exactly the fan exception a;
2. the clone pair b,c is adjacent in a genuine one-change deletion witness;
3. reinsertion of a beside that pair exposes a certified flat/full transition on {a,b,c,z}.

The remaining obligation is the bounded outer-window reconnection, i.e. the same provenance-sensitive barrier frontier already active elsewhere in Article III.
