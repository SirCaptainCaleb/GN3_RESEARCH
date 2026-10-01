# Schrijver rainbow paths give a one-third ceiling for full transversal designs

## Statement

Let T_q be any transversal design TD(3,q), equivalently the lift of a proper q-edge-coloring of K_{q,q} using q colors. Then T_q contains a linear path of length q-o(q) as q tends to infinity. Consequently, if ell(T_q) is one plus the maximum linear-path length of T_q, then (|E(T_q)|/|V(T_q)|)/ell(T_q) <= 1/3+o(1); in particular full transversal designs cannot yield an asymptotic lower-bound coefficient strictly larger than 1/3.

## Body

Bucic, Frederickson, Muyesser, Pokrovskiy and Yepremyan, 'Towards Graham's rearrangement conjecture via rainbow paths', Advances in Mathematics 492 (2026), Article 110892, prove asymptotically a question of Schrijver: every d-regular graph properly edge-colored with d colors contains a rainbow path of length d-o(d). A Latin square of order q is exactly a proper q-edge-coloring of K_{q,q}; its associated TD(3,q) has one hyperedge {r,c,s} for each colored graph edge rc of color s. Every rainbow graph path lifts to a linear hypergraph path, because consecutive graph edges share their graph endpoint while nonconsecutive graph edges have disjoint graph endpoints and distinct colors. Therefore every TD(3,q) contains P_{q-o(q)}. Since TD(3,q) has 3q vertices and q^2 edges, its edge density is q/3. At its first forbidden path length ell(T_q)>=q-o(q), the normalized density is at most (q/3)/(q-o(q))=1/3+o(1). This turns the q=4,5,6 exact calibrations into an asymptotic fence for the whole full-Latin-square family.
