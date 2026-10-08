# Every protected barrier root has a flag-compatible opposite cut crossing — preserved pre-item development

## Development

## Every protected barrier root has a flag-compatible opposite cut crossing

Assume the root-valued proper-face boundary carrier D of §243. Let
rho=e_s-e_t
be any actual protected root with certified cut C, so
s in C and t notin C.

Use rho as the label of an interior cone vertex over the barycentric subdivision of the permutahedron boundary, while retaining the canonical proper-face labels D(pi_F) on the boundary.

The boundary map is zero-free and has nonzero degree. Therefore its affine cone extension must vanish in some cone simplex. Hence there is a positive dependence
lambda rho + sum_i lambda_i D(pi_{F_i})=0,
lambda>0,
where the faces F_i form one nested proper-face flag.

Take a support-minimal positive subdependence containing rho. Since all labels are type-A roots, it is a simple directed physical cycle. Thus
s -> t=x_0 -> x_1 -> ... -> x_m=s,
where the first edge is rho and every return edge is an outermost-change root of a canonical proper-face witness from the same flag.

Now pair the cycle with the cut indicator 1_C. The apex edge contributes
<1_C,rho>=1.
The return path begins at t outside C and ends at s inside C. Therefore at least one return edge
eta=e_y-e_z
satisfies
y notin C, z in C,
so
<1_C,eta>=-1.
Choose the first such edge along the return path. Every earlier return-path vertex lies outside C.

Thus every protected barrier root has a flag-compatible boundary witness whose outermost root crosses the SAME certified cut in the opposite direction.

### Two-shore localization

Writing
V=C disjoint-union C^c,
the forced cycle contains:
- the protected edge s->t from C to C^c;
- a canonical proper-face outermost edge y->z from C^c to C;
- a flag-compatible root path entirely in C^c from t to y before the first return crossing;
- a remaining flag-compatible path from z back to s.

The first opposite crossing is canonical and needs no global search or circuit minimization.

### Closure target

The Article III realization problem can therefore be reduced around one certified cut:

Given an actual protected barrier root s->t across C and a canonical proper-face outermost root y->z crossing C oppositely, together with a flag-compatible path inside C^c from t to y, produce a spanning NOR-good order or a strict admissible improvement.

If y=t and z=s this is an opposite-root two-term cell. Otherwise the path in C^c supplies a strictly smaller-shore return problem on the proper subset C^c. This is the natural induction parameter suggested by the protected cut provenance.
