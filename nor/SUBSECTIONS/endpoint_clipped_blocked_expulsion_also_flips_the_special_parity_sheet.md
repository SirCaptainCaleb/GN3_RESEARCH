# Endpoint-clipped blocked expulsion also flips the special parity sheet

## Metadata

- ID: endpoint_clipped_blocked_expulsion_also_flips_the_special_parity_sheet
- Parent Section: hartman_least_unreachable_connectors
- Position: 27
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For a realized equal-zero expulsion at a released boundary, the special vertex moves two positions and its path-normalizing switch bit flips, so the special parity flips. This excludes perfect alternation on the new sheet. It does not force a thick wall or provide an escape from every equal-one barrier.

## Development

Continue with the zero-polarity blocked x-cell
(p,a,x,b,c)
of the preceding subsection. In the old path-normalized switching,
p->a, a->x, x<-b, b->c
give
sigma_p=sigma_a=sigma_x,
sigma_b=sigma_c=1-sigma_x.

For the right-expelled zero order
(p,a,b,c,x),
fix the switching gauge on the preserved left collar by sigma'_p=sigma_p. The adjacent fixed-representative edges are
p->a,
b->a,
b->c,
c->x.
The path-normalizing recurrence yields
sigma'_a=sigma_x,
sigma'_b=sigma'_c=1-sigma_x,
sigma'_x=1-sigma_x.
Thus x moves two positions to the right while its switch bit flips. The special parity
chi=|i_z-i_x|+sigma_x+sigma_z
therefore flips.

For the left-expelled order
(x,p,a,b,c),
fix the gauge on the preserved right collar. The same recurrence gives sigma'_x=1-sigma_x, while x moves two positions left, so chi again flips.

The reversed-polarity and z versions are identical.

Hence every realized escape from a blocked special cell crosses the two special-parity sheets:
- a legal one-step A2 rotation flips chi by changing position parity;
- an endpoint-clipped blocked expulsion flips chi by changing the special switching bit.

Therefore the perfectly alternating blocker sheet cannot be isolated merely by trapping the special vertices. Once a trapped cell is brought to a released boundary, its exact expulsion crosses to the thick-wall sheet.
