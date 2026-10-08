# Compatible connectors are switchable directed square-paths — preserved pre-item development

## Composition

(none yet)

## Development

Work in the fixed switching-normalized tournament on U=A union {x,z}. Let C=(c_1,...,c_m) be any order of U; x and z are not required to be adjacent. Choose switching bits sigma_i along C so that every consecutive edge is forward after switching. This choice is unique up to complementing all sigma_i. Switching preserves alpha. In the switched tournament, for every i, alpha(c_i,c_{i+1},c_{i+2}) equals t(c_{i+2},c_i), because both consecutive edges are forward. Hence alpha is zero exactly when c_i also dominates c_{i+2}. Therefore C is a monochromatic-zero connector iff, after its path-normalizing switch, every distance-one and distance-two edge points forward. In other words C is a directed square-path in a switching-equivalent tournament. The endpoint pair (c_1,c_2) is forward in the original fixed representative iff sigma_1=sigma_2, and similarly the final pair is forward iff sigma_{m-1}=sigma_m. Thus compatibility is exactly zero switching parity on the first and last path edges. This characterization allows x and z to move independently anywhere in C. The earlier representation P,x,z,Q is only the adjacent-xz subfamily supplied by the seed; it is not the full repair state space.
