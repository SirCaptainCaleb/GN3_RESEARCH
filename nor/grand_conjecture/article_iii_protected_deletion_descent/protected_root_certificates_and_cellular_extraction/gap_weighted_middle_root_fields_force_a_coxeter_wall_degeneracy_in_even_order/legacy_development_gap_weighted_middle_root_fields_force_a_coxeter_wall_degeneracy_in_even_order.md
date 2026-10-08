# Gap weighted middle root fields force a Coxeter wall degeneracy in even order — preserved pre-item development

## Development

**Audit qualification (root §30).** The field formulas and characteristic-class calculation below are valid, but both fields already vanish independently of the coloring on the universal gap-weight zero locus. Minimum-codimension examples use only disjoint doubleton ties, where physical window-slide roots remain strictly cooriented. Therefore this construction does not by itself force a coloring-sensitive physical root obstruction. Root §32 gives a continuous carrier of actual slide roots without these weight zeros; global zero forcing and protected-witness compatibility remain open.

## Gap-weighted middle-root fields force a Coxeter-wall degeneracy in even order

This gives a free-antipodal continuous formulation of the middle-root bivector in ternary arity.

Let
[
W={xinmathbb R^V:sum_v x_v=0},
qquad
S(W)cong S^{n-2}.
]
The braid arrangement cuts (S(W)) into permutation chambers.

For a point (x) in the open chamber
[
x_{v_1}<x_{v_2}<cdots<x_{v_n},
]
write
[
delta_j=x_{v_{j+1}}-x_{v_j}>0.
]
Let (w_1,ldots,w_{n-2}) be the ternary status word of the corresponding coordinate order.

For each transition position (i=1,ldots,n-3), put
[
eta_i=e_{v_{i+1}}-e_{v_{i+2}}.
]
Choose the local wall-vanishing weight
[
omega_i(x)=
prod_{j=max(1,i-1)}^{min(n-1,i+3)}delta_j.
]
Define
[
F_{10}(x)=sum_{i:w_iw_{i+1}=10}omega_i(x)eta_i,
]
[
F_{01}(x)=sum_{i:w_iw_{i+1}=01}omega_i(x)eta_i.
]

### Continuity across Coxeter walls

Cross a codimension-one wall where the coordinates at adjacent ranks (s,s+1) become equal and swap.

A transition term at index (i) can change its physical four-coordinate packet, its status type, or its middle root only if
[
sin{i-1,i,i+1,i+2,i+3}.
]
But then (delta_s) is a factor of (omega_i), so that term tends to zero on the wall from both adjacent chambers.

Every transition term with (s) outside this range has the same physical packet, status type, middle root, and limiting weight on both sides.

Therefore (F_{10}) and (F_{01}) glue continuously across every braid wall, hence define continuous maps on all of (S(W)).

### Oddness

Under (xmapsto -x), the coordinate order reverses. The ternary word becomes complement-reverse, so 10 transitions remain 10 transitions and 01 transitions remain 01 transitions. The corresponding local gap products are preserved under index reversal, while each ordered middle pair reverses:
[
e_b-e_cmapsto e_c-e_b.
]
Hence
[
F_{10}(-x)=-F_{10}(x),
qquad
F_{01}(-x)=-F_{01}(x).
]

### Independence in every open chamber of a counterexample

Inside a chamber all (omega_i>0). The roots (eta_i) are distinct simple roots of the chamber order.

If the status word has at least two changes, it contains at least one 10 and at least one 01 transition. Thus both fields are nonzero. Their simple-root supports are disjoint, so they are linearly independent.

Therefore in a ternary NOR counterexample the pair
[
(F_{10},F_{01})
]
is a pointwise 2-frame on the union of open chambers.

### Even-n topological obstruction

Assume, for contradiction, that the two fields remain linearly independent everywhere on (S(W)).

Put (d=n-2). Since both fields are odd, after quotienting by the antipodal action they define two pointwise independent sections of
[
E=(d+1)gamma
]
over (mathbb{RP}^{d}), where (gamma) is the tautological real line bundle.

Two independent sections would split
[
Econg arepsilon^2oplus E'
]
with (operatorname{rank}E'=d-1). Hence the degree-d Stiefel--Whitney class would vanish:
[
w_d(E)=0.
]

But
[
w(E)=(1+a)^{d+1},
]
so
[
w_d(E)=inom{d+1}{d}a^d=(d+1)a^d.
]
When (n) is even, (d=n-2) is even, so (d+1) is odd and
[
w_d(E)=a^d
e0.
]
Contradiction.

Thus for every even (n) ternary counterexample candidate there is a point on a Coxeter wall where
[
F_{10},F_{01}
]
are linearly dependent.

### Wall localization

At a wall point, every surviving transition root is still a simple root belonging to a strict-order segment separated from the tied gaps. The surviving supports of (F_{10}) and (F_{01}) remain disjoint. Hence if both fields are nonzero they are still linearly independent.

Therefore the forced dependence has the sharper form
[
oxed{F_{10}=0quad	ext{or}quad F_{01}=0}
]
at a Coxeter-wall point.

Equivalently, every transition of one orientation in every nearby chamber is localized to the bounded neighborhoods of the tied blocks whose gap factors vanish.

### Status

This is not yet an even-n proof of NOR: a vanishing weighted field on a wall does not immediately give a good chamber order. It does give a genuine free-antipodal carrier theorem with no arbitrary triangulation and no fixed-center zero. The next extraction problem is to refine/reorder the tied blocks so that the localized transitions of the vanished orientation are eliminated rather than merely hidden by zero gap weights.

For odd n the two-section top Stiefel--Whitney obstruction vanishes, so an additional field or a different characteristic-class argument would be needed.
