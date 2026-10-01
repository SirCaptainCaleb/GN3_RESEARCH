# Near-minimal switching states require order at least 201 over 88 times the host rank

## Statement

Let H be a finite linear 3-graph on n vertices and let v be an active misaligned vertex with p=phi(v). Suppose eta_v=o(p) and the switching-family source-rank mass is within o(p^2) of the generic 185/512 p^2 floor. Then
  n >= (201/88-o(1))p.
Indeed, if U_v is the terminal-retained part of the switching family, then |U_v| >= (25/88-o(1))p and its distinct omitted entrances lie outside the chosen maximum p-edge host path.

## Body

By 28f6933b98de, near-minimal switching-source mass at a low-defect vertex of rank p forces
  k:=|U_v| >= (25/88-o(1))p.
Let P_v be the chosen maximum p-edge path. A linear 3-uniform p-edge path has exactly 2p+1 vertices. For every terminal-retained switcher e={x,v,u}, the unique entrance x is absent from P_v by definition. Distinct switchers through v have distinct entrances, since two distinct hyperedges already share v and linearity forbids a second common vertex. Hence
  n >= |V(P_v)|+k
    = 2p+1+k
    >= (2+25/88-o(1))p
    = (201/88-o(1))p.
Equivalently, for any fixed epsilon>0, if n <= (201/88-epsilon)p for all sufficiently large p, then a low-defect vertex of rank p cannot remain within o(p^2) of the generic 185/512 source-rank floor; it must pay a fixed positive quadratic source-rank gain, quantitatively by the gap statement in 28f6933b98de.
