# Equality-row supports alone do not synchronize connector incidences

**Workspace:** D17
**State:** limitation
**Key:** `singleton-cover-union-equality-support-fence`

**Summary:** The rigid equality-row support skeleton does not by itself force row-independent connector pairs or a common atom path. Abstractly, with separator labels a,b,c and four atoms 0,1,2,3, the three valid suppressed rows F_a=(0-b-1)|(2-c-3), F_b=(0-a-2)|(1-c-3), F_c=(0-a-3)|(1-b-2) satisfy every support-level equality-row condition, yet each connector label changes its atom pair between rows. This is a quotient combinatorial fence, not a realizable boundary-tournament counterexample. Any stronger equality-separator synchronization theorem must use tight orders, selected states, or antisymmetry beyond support incidence alone.

### Support-only synchronization fails abstractly
The equality theorem `singleton-cover-union-separator-row` says that when c(U-S)=|S|+1, every omitted-label row suppresses to two alternating paths on the common Hamilton atoms and the surviving separator labels. It is tempting to infer that a fixed separator label must join the same atom pair in every row, or that all rows arise from one common atom path with the omitted label removed. That inference is false from the support skeleton alone.

Take three separator labels

  S={a,b,c}

and four abstract atoms

  {0,1,2,3}.

Consider the three suppressed rows

  F_a = (0-b-1) | (2-c-3),
  F_b = (0-a-2) | (1-c-3),
  F_c = (0-a-3) | (1-b-2).

Each row has exactly two path components. Every atom occurs exactly once. Every surviving separator label is internal, has quotient degree two, and separates two atom blocks. No two separator labels are consecutive. Thus each row satisfies exactly the support-level conclusions forced by equality after the omitted label is removed.

Nevertheless connector incidences are not row-independent. For example a joins atoms 0 and 2 in F_b but atoms 0 and 3 in F_c; b joins 0 and 1 in F_a but 1 and 2 in F_c; c joins 2 and 3 in F_a but 1 and 3 in F_b. There is therefore no common atom path whose fixed labelled connector edges simply lose one label from row to row.

This is an abstract quotient counterexample only. It is not asserted to arise from a boundary tournament, from actual tight path orders, or from a selected-edge union U. Its purpose is a logical fence: any theorem synchronizing equality-separator rows must use information beyond the support quotient, such as literal tight orders, boundary antisymmetry, selected cross-fiber states, or a global extremal potential.

Status: exact support-combinatorial limitation; no realizability claim.
