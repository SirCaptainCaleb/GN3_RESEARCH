# The residual endpoint type itself yields a four-shore-vertex monochromatic connector

## Metadata

- ID: the_residual_endpoint_type_itself_yields_a_four_shore_vertex_monochromatic_connector
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 366
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Residual endpoint type (0,1) supplies a compatible six-coordinate zero seed on four shore vertices. When the shore is larger this is a local seed, not a spanning connector. Article IV's collective collar is the relevant enlargement interface.

## Development

Let O=(a_1,...,a_k) be a NOR-good order of the minimum shore A in the switching-normalized split B -> z -> A -> x. Suppose its endpoint tournament-edge state is the reversal-stable residual type
e_1=0, e_{k-1}=1,
so a_2 -> a_1 and a_{k-1} -> a_k.

Then the six-coordinate order
(a_2,a_1,x,z,a_{k-1},a_k)
is monochromatic zero.

Indeed,
alpha(a_2,a_1,x)=0
because a_2 -> a_1 -> x while x does not dominate a_2;
alpha(a_1,x,z)=0
because alpha(x,z,a_1)=0 on the shore;
alpha(x,z,a_{k-1})=0
for the same reason;
and
alpha(z,a_{k-1},a_k)=0
because z dominates A and a_{k-1} -> a_k.

Hence the persistent endpoint obstruction itself produces a zero connector containing x,z and four shore vertices.

This strictly strengthens the three-shore-vertex directed-triangle seed for the residual endpoint class. Any proof by maximal connector support may therefore start from support size four on A whenever the good-order component is trapped in type (0,1).
