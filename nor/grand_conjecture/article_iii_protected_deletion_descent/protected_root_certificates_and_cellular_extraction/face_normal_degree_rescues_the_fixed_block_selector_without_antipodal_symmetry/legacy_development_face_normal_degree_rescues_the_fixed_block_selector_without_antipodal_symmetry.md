# Face-normal degree rescues the fixed block selector without antipodal symmetry — preserved pre-item development

## Composition

(none yet)

## Development

## Face-normal degree rescues the fixed block selector without antipodal symmetry

Root §169 correctly observes that the global fixed block-order selector of §§163-167 is not generally reversal-equivariant. However this does NOT invalidate its use in the proper-face Brouwer/Sperner degree argument.

The boundary degree theorem of roots §§146,155 uses a stronger local face-normal property which does not require antipodality.

### Fixed-selector face labels

Fix one NOR-good order g(S) for every proper nonempty coordinate subset S. For a proper ordered-partition face

F=B_1|...|B_s,

put

pi_F=g(B_1)...g(B_s)

and label its barycenter by the consecutive-change defect

L(F)=C(pi_F).

Because each block order is NOR-good, root §155 proves that every consecutive-change macro root occurring in C(pi_F) strictly crosses F-blocks. Therefore for the block-rank functional beta_F,

beta_F(L(F))<0.

### Boundary flags remain strictly separated

Consider a barycentric boundary simplex

F_0<...<F_k=G.

Every pi_{F_i} refines the largest face G. Hence every macro root occurring in L(F_i) is weakly forward in the G-block order, so

beta_G(L(F_i))<=0

for all i.

For i=k, the largest-face label is strict:

beta_G(L(G))<0.

At every point of the relative interior of this flag simplex, the barycentric coefficient of G is positive. Consequently the affine boundary carrier R satisfies

beta_G(R(x))<0.

Thus R has no boundary zero.

### Degree does not require oddness

Choose the standard outward/inward radial-normal PL carrier N on the barycentric subdivision, assigning to each face barycenter a vector in the corresponding strict normal cone with the same beta_F sign.

The straight homotopy

(1-t)R+tN

remains zero-free on every boundary flag by exactly the same largest-face functional beta_G: all terms are weakly one-sided and the largest-face contribution is strict.

Therefore R/||R|| has the same nonzero boundary degree as the radial normal map.

No relation between L(-F) and -L(F) is needed.

### Corrected status of §§163-167

Hence the fixed-selector construction is valid as a NON-EQUIVARIANT witnessed Sperner/Brouwer boundary carrier of nonzero degree. Its advantages remain available:

- codimension-one face witnesses are block-local (§163);
- defect-label increments are local transition-root sums (§164);
- a zero relation decomposes into positive merge increments (§165);
- each merge has bounded interface complexity (§166);
- witness gluing reduces to disjoint merge squares and three-block associativity diamonds (§167).

What §169 still correctly forbids is calling this fixed-selector carrier antipodally odd or using Borsuk-Ulam/Tucker conclusions that require equivariance.

The topology now has two distinct legitimate implementations:

1. the honest antipodal switch-prism lift for equivariant degree/side-balance;
2. the fixed-selector proper-face Sperner carrier for ordinary nonzero boundary degree plus block-local gluing.

They should not be conflated.
