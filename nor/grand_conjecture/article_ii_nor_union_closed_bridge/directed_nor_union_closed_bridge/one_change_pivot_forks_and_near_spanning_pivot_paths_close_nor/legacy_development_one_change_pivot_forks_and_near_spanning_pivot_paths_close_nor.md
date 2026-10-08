# One-change pivot forks and near-spanning pivot paths close NOR — preserved pre-item development

## Development

Let h be reversal odd in ternary coordinate arity and assume its center tournaments are transitive. Fix o and use the pivot graph G_o of Subsection 43: a->b if h(o,a,b)=h(a,b,o)=0. Regard each underlying edge as carrying color 0 in its directed orientation and color 1 in the reverse orientation.

Theorem. If the underlying graph of G_o has a Hamilton vertex order (u1,...,um) whose oriented edge colors e1,...,e_{m-1} change at most once, then (o,u1,...,um) is a spanning NOR order. For an edge of color e_i, both h(o,ui,ui+1) and h(ui,ui+1,o) equal e_i, including color 1 by reversal. Whenever e_i=e_{i+1}=sigma, transitivity of the color-sigma center tournament at ui+1 forces h(ui,ui+1,ui+2)=sigma. If there is one edge-color switch, only its straddling triple is not forced. Its binary color can be either adjacent run color, so it introduces at most one change. The first window equals e1. Short orders satisfy the statement directly.

Graph interpretation. Such an edge order is a spanning pair of directed paths meeting at a common terminal vertex, or meeting at a common initial vertex; one path may be trivial. The order reads one arm toward the meeting vertex and the other arm backward. This is a sufficient certificate, not a claimed existence theorem for every pivot graph.

A separate near-spanning certificate needs even less: if G_o has a directed path containing all but at most one vertex of V minus {o}, then o followed by that path is monochromatic. Prepending the one omitted vertex adds only one new window, and therefore gives a spanning one-change order. Consequently a locally transitive counterexample must, for every pivot o, lack both a spanning converging/diverging fork and a directed path on at least |V|-2 vertices of G_o.

This strengthens the defect obstruction: off-pivot defects must obstruct these graph certificates, not merely produce some missing edges. The gap toward closure is a theorem guaranteeing one of the certificates for some pivot, or a proof using orders that cross missing pairs. No such existence theorem is asserted.
