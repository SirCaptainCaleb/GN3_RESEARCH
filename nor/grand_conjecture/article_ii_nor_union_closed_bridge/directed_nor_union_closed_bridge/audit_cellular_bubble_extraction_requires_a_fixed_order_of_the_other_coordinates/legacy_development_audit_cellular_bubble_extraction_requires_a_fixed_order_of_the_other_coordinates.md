# Audit cellular bubble extraction requires a fixed order of the other coordinates — preserved pre-item development

This audits the extraction step in §§143,150,154 while preserving the cellular degree obstruction of §§141,150,168 and the local repair identities of §§118,144,156,161.

The missing premise. A path connecting arbitrary permutations pi and sigma cannot in general move only b while keeping the relative order of all other coordinates fixed. Removing b from every vertex on such a path gives the SAME order. Thus such a path exists only if pi without b equals sigma without b. Membership in one permutohedron face does not impose that condition. Even a single block face contains vertices with arbitrary different relative orders of its other coordinates.

For example pi=(a,b,c,d) and sigma=(c,d,b,a) belong to the full four-coordinate face, but deleting b gives (a,c,d) and (c,d,a). A b-only bubble path cannot join them. This is a structural example, not a computational cutoff argument.

Correct restricted lemma. If the two carrier witnesses have the same order after deleting b, their positions lie in the same allowable block, and b remains a middle coordinate throughout the relevant path, one may bubble b monotonically. If b stays violating across the cut crossing, §118 applies. If the violation predicate changes on a b-moving same-side edge, §§143-144 apply. This is a valid fiberwise extraction statement.

What an arbitrary face path additionally permits:
(1) swapping a neighbor of b with another coordinate while b itself stays fixed, thereby changing its centered window;
(2) loss or acquisition of a centered window when b reaches a global endpoint;
(3) in a product path, changing the threshold assigned to b's window by a cut move.
A predicate toggle caused by (1) is not the two-central-window packet of §144, so its energy inequality and moment potential cannot be invoked without a separate calculation.

The cellular Tucker theorem supplies a complementary PRODUCT CELL, not a complementary fiber and not a complementary edge. It therefore does not yet imply the unconditional legal-bubble-edge conclusion in §143 or §154. Acyclicity of a class of edges cannot establish that a required carrier contains an edge of that class.

Repair obligation: prove a same-deleted-order localization theorem, or give boundary-preserving surgery for the additional neighbor-replacement and endpoint events. The topological conclusion remains valid; carrier-to-path extraction remains open. Do not assume a minimal complementary carrier has dimension two: two-cells are the first possible non-edge residues, but higher-dimensional minimal residues have not been excluded.
