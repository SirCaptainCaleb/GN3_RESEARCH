# Two selected contacts from one interior pair force a superlevel rotation output

## Statement


Let P=(g_1,...,g_p) be the chosen maximum p-edge path ending at v. For an interior index i, let
  C_i={b_i,z_i}
be the two possible contact vertices used in the D+Y selection of c8d14f7306ab, and let
  h_i=g_{i+2}
be the corresponding standard rotation output.

Suppose two distinct selected center-edge incidences at v have their unique off-v contacts equal to b_i and z_i, respectively. Then every vertex of h_i has vertex rank at least p:
  V(h_i) subseteq {w: phi(w)>=p}.

Equivalently, if h_i has a vertex of rank at most p-1, at most one selected incidence can have its unique off-v contact in C_i.


## Body


The selection rule of c8d14f7306ab injects the D+Y units cell by cell into distinct center-edge incidences. A doubly occupied interior cell always contributes one D-unit. It contributes a second unit exactly when it is also counted by Y; in that case its two occupants are both selected. If it is not counted by Y, it contributes only the single D-unit, so at most one of its two occupants is selected.

Therefore two selected incidences with contacts b_i and z_i force C_i to be counted by Y. By 39d0d99258db, an occupied interior cell is counted by Y exactly when its rotation output h_i=g_{i+2} is contained in the vertex-rank superlevel
  V_p={w:phi(w)>=p}.
This proves the claim.
