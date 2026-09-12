# Correction: endpoint-perfect residual is a matching, not two triangles

**Workspace:** D17
**State:** limitation
**Key:** `three-petal-endpoint-prism-correction`

**Summary:** The Type-II/two-triangle classification in DR17.109 was false. Endpoint-perfect data alone says only that the three pair-union endpoint pairs form a perfect matching on the six solo endpoints, with each edge lying in the allowed union of two petal color classes. Many matchings exist, including the displayed example of DR17.109, whose combined incidence with solo-petal endpoint pairs is actually one 6-cycle, not two 3-cycles. Therefore DR17.110-112 endpoint-prism role/triangle deductions are withdrawn unless rederived from additional hypotheses.

### Correction
Retain the setup of `three-petal-cover-row-endpoint-dichotomy`: solo endpoint pairs

  E_L={l_0,l_1}, E_B={b_0,b_1}, E_Z={z_0,z_1}

and pair-union endpoint pairs F_Z for L+B, F_B for L+Z, F_L for B+Z. In the endpoint-perfect branch every one of the six solo endpoints occurs exactly once among F_Z,F_B,F_L.

The only unconditional combinatorial conclusion is therefore:

  {F_Z,F_B,F_L} is a PERFECT MATCHING on the six solo endpoints,

with the support restrictions

  F_Z subset E_L union E_B,
  F_B subset E_L union E_Z,
  F_L subset E_B union E_Z.

No two-triangle dichotomy follows.

The concrete assignment displayed previously,

  F_Z={l_0,b_0},
  F_B={l_1,z_1},
  F_L={b_1,z_0},

when combined with the solo-petal pairs E_L,E_B,E_Z, forms the single 6-cycle

  l_0 - b_0 - b_1 - z_0 - z_1 - l_1 - l_0,

not two disjoint triangles. Thus the claimed Type-II incidence interpretation was incorrect.

### Consequences
The downstream sections `three-petal-endpoint-triangle-roles`, `three-petal-endpoint-prism-splice`, and `directed-triangle-prism-absorption` relied on the false two-triangle premise and are not usable as deductions from endpoint-perfect data. They remain historical working attempts only.

The valid branch point is now simply ENDPOINT-PERFECT MATCHING. A correct next analysis must classify the allowed perfect matchings modulo petal symmetries and use actual endpoint roles/path orders directly, without inventing triangle components in the incidence graph.

Status: correction/limitation. This section explicitly withdraws the Type-II/two-triangle claims of DR17.109-112 from current reasoning.
