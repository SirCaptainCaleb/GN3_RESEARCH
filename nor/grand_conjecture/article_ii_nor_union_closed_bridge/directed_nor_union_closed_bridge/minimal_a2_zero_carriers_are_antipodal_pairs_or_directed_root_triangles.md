# Minimal A2 zero carriers are antipodal pairs or directed root triangles

## Composition

(none yet)

## Development

## Minimal A2 zero carriers are antipodal pairs or directed root triangles

Consider the switch-prism Borsuk--Ulam construction in ternary arity (r=3). Let a zero of the odd root map have a minimal Coxeter carrier whose unique nontrivial tied block is
[
B={a,b,c}.
]

On the corresponding permutohedral face, the block-rank functional used in the localization theorem is nonpositive on every selected root
[
e_x-e_y,
]
and is strictly negative whenever (x,y) lie in different ordered blocks. A convex combination of selected roots can equal zero only if every root receiving positive mass has block-rank value zero. Hence both endpoints of every active root lie in the same tied block (B).

Therefore every active label belongs to the (A_2) root set
[
Phi_B=
{pm(e_a-e_b), pm(e_b-e_c), pm(e_c-e_a)}.
]

### Proposition

Every inclusion-minimal positive dependence among roots in (Phi_B) is of one of two types:

1. an antipodal pair
   [
   r+(-r)=0;
   ]
2. a directed triangle
   [
   (e_a-e_b)+(e_b-e_c)+(e_c-e_a)=0,
   ]
   or its reverse.

### Proof

Associate to a root (e_x-e_y) the directed edge (y	o x) on the three vertices (B). A positive linear dependence
[
sum lambda_{xy}(e_x-e_y)=0,
qquad lambda_{xy}>0,
]
is exactly a nonzero circulation on this directed graph: at every vertex total incoming weight equals total outgoing weight.

A support-minimal nonzero circulation is a directed cycle. On three vertices the only directed cycles are:
- a two-cycle using opposite directed edges between one pair;
- a directed three-cycle through all three vertices.

These give precisely the two displayed dependence types. (square)

### Interpretation

The first possible topological obstruction in the switch prism is therefore not an arbitrary convex cancellation. On an (A_2) braid hexagon it is forced into one of two local combinatorial species:

- **pair reversal:** two selected violating windows have opposite ordered endpoints on the same coordinate pair;
- **triangle circulation:** three selected violating windows form a directed cycle on the three tied coordinates.

The triangle-circulation branch is the root-system shadow of the centered directed triangles and three-element circuit geometry already isolated in Article II.

A closure proof via the switch prism can now focus on eliminating the antipodal-pair carrier and identifying the triangle-circulation carrier with a local surgery configuration.
