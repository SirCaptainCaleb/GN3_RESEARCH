# Brouwer gives a protected-root circuit or an exposed global shore potential — preserved pre-item development

## Development

Let V be any finite family of realized protected p-cuts, regarded as vertices z_C of the centered hypersimplex, and let P=conv(V). For each C in V choose an actual canonical protected root rho_C=e_a-e_c crossing C and write its forced Johnson successor C^+=(C-{a}) union {c}. Put d_C=z_{C^+}-z_C=-rho_C.

There is a convex-topological dichotomy.

Assume first that d_C belongs to the tangent cone T_P(z_C) for every C in V. Because P is a polytope, for every vertex C there is eta_C>0 such that y_C=z_C+eta_C d_C lies in P. Choose any triangulation of P using only its vertices. Define a map F:P->P on vertices by F(z_C)=y_C and extend affinely over every simplex. This is a continuous self-map of the compact convex polytope P. Brouwer gives x with F(x)=x.

Let x lie in a simplex with vertices z_{C_1},...,z_{C_m} and barycentric coefficients lambda_i>=0 summing to one. Then
0=F(x)-x=sum_i lambda_i eta_{C_i} d_{C_i}.
After discarding zero coefficients this is a positive dependence of the actual canonical protected roots rho_{C_i}. Thus tangent-cone closure of all canonical Johnson directions forces a protected-root Radon circuit supported on realized extremal cuts.

Contrapositively, if no positive dependence of the chosen canonical protected roots exists, some realized cut C has d_C outside T_P(z_C). By polyhedral separation there is a linear functional w on cut space such that
w(d_C)>0
while
w(y-z_C)<=0
for every y in P.
Equivalently C maximizes w over the entire realized family V, but its forced successor satisfies
w(C^+)>w(C).

Hence every zero-free canonical protected-root system has an exposed escape edge from the convex hull of realized cuts.

Apply this to the minimum-short-phase state space of root 61. Complement-reversal fixes the short shore S, and the shore-oriented canonical root gives the same directed Johnson edge on both sheets. Let V be the set of realized minimum short shores. Then either:

1. the canonical protected roots contain a positive dependence, to which the hypersimplex/root-cycle extraction machinery applies; or
2. there is a minimum short shore S and a linear potential w, globally maximized on all realized minimum shores at S, whose canonical successor S^+ has strictly larger w-value and is therefore unrealized.

This provides a canonical global potential rather than a guessed local rank. A closure proof may choose an exposed extremal state and run threshold-band repairs while retaining the witness w. If every legal repair remains within the realized minimum-shore polytope, it cannot increase w; the canonical root points in the unique forbidden improving direction. The remaining theorem is to show that a fully-curved barrier at such a w-exposed maximal-band state either realizes the improving Johnson shore after all or creates a positive protected-root circuit.

The theorem is purely finite-dimensional convexity plus Brouwer; it does not require web/literature input or a full hypersimplex realization.
