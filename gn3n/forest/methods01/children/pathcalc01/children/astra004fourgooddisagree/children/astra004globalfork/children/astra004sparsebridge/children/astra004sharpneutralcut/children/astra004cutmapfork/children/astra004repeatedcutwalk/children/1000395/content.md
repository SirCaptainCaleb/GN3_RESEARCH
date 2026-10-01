# A clean repeated cut ends in a Hamiltonian-or-matching-block four-kernel

## Statement

Keep the support-compatible repeated-cut setup of astra004repeatedcutwalk, and suppose the resulting fixed-support odd two-walk lies in the clean branch of astra004twowalk. Consider the case in which the varying supports have a common tight path K followed by the exchanged terminal labels: P_u=(K,v) in the exact cover of H-u and P_v=(K,u) in the exact cover of H-v. Write the last two vertices of K as t,z. Then on F={t,z,u,v} the four ordered triples (t,z,u), (t,z,v), (u,v,z), and (v,u,z) are tight. Consequently either H[F] is Hamiltonian, or H[F] is a non-Hamiltonian edge-orderable matching-block K4 whose unique bottom matching is {tz,uv}; equivalently its matching blocks have one of the two orders {tz,uv} < {tu,zv} < {tv,zu} or {tz,uv} < {tv,zu} < {tu,zv}. The initial-end version is symmetric after reversing the displayed role of the common path.

## Body

By cleanliness of the length-two odd walk, the two varying Hamilton paths differ only by replacing one endpoint at the same end. In the terminal case write them as P_u=(K,v) and P_v=(K,u), with the same inherited order on K. The common endpoint-extension lemma inside astra004twowalk gives |K|>=2, so let t,z be the final two vertices of K. Tightness of P_u and P_v gives (t,z,v) and (t,z,u) tight.

Now use the standard deleted-vertex endpoint barriers. In the exact cover C_u of H-u, the vertex v is the terminal endpoint of P_u with path neighbor z, so (u,v,z) is tight. Symmetrically, in C_v the terminal endpoint u has neighbor z, so (v,u,z) is tight. These two triples are not a reversal pair; they are simply two additional tight triples on F.

If H[F] is Hamiltonian, the first alternative holds. Assume H[F] is non-Hamiltonian. The certified four-vertex classification in smallset01 applies to the two common-first-pair tight triples (t,z,u) and (t,z,v). It rules out the cyclic non-Hamiltonian K4 and forces the edge-orderable matching-block form with {tz,uv} as the unique bottom matching. The remaining two perfect matchings {tu,zv} and {tv,zu} may occur in either order. Both orders are consistent with the already known triples (u,v,z) and (v,u,z), so no further contradiction follows from antisymmetry alone. This proves the stated normal form. The initial-end case is the left-right symmetric version. ∎