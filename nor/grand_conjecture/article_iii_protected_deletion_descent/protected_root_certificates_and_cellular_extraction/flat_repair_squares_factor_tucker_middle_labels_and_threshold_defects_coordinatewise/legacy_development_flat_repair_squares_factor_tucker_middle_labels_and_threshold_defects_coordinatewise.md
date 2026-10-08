# Flat repair squares factor Tucker middle labels and threshold defects coordinatewise — preserved pre-item development

## Flat repair squares factor Tucker middle labels and threshold defects coordinatewise

Continue with the flat repair square on consecutive coordinates (a,b,c,d). Let

L in {0,1}

record whether the left endpoint swap a<->b is applied, and let

R in {0,1}

record whether the right endpoint swap c<->d is applied.

The four orders are

L=0,R=0: (a,b,c,d),
L=0,R=1: (a,b,d,c),
L=1,R=0: (b,a,c,d),
L=1,R=1: (b,a,d,c).

Assume the original flat transition has local word

(x,1-x).

### Exact status factorization

The first local ternary window has color

s_1(L,R)=x xor L.

The second has color

s_2(L,R)=(1-x) xor R.

Thus the two status coordinates depend on the two repair directions independently.

### Exact middle-coordinate factorization

The middle coordinate of the first local window is

m_1(L,R)=
b if L=0,
a if L=1.

The middle coordinate of the second local window is

m_2(L,R)=
c if R=0,
d if R=1.

Hence the square is literally the Cartesian product

{b,a} x {c,d}

at the level of Tucker middle-coordinate choices.

No tie-breaking is hidden: each repair direction changes exactly one of the two central middle labels.

### Threshold defect energy is Hamming distance

Fix arbitrary target bits t_1,t_2 for the two central window ranks. Define

d_1=s_1 xor t_1,
d_2=s_2 xor t_2.

Then d_1 depends only on L and d_2 only on R. There is therefore a unique corner (L*,R*) with

d_1=d_2=0.

Moreover

E_central(L,R)=d_1+d_2

is exactly the Hamming distance from (L,R) to (L*,R*).

Consequently every nonoptimal corner has an incident repair edge that strictly decreases the central defect count, and no equality cycle exists inside the repair square.

### Relation to cellular Tucker extraction

This is the local product structure sought by the signed-middle Tucker program.

A complementary signed-middle event confined to one flat repair square cannot be terminal through central-window equality transport: the two middle-label coordinates and the two defect coordinates separate. Any unresolved equality event must therefore escape through one of the OUTER windows affected by the corresponding endpoint swap.

Thus the only obstruction to turning a flat-square Tucker event into a strict repair is boundary provenance outside the central two-window packet.

This matches the arbitrary-cell repair theorem: its same-side and neighbor equality cases are precisely transports to outer windows. The present factorization proves that such equality is not generated internally by the two central defects.

### Topological significance

The realized repair square carries simultaneously:

1. a degree-one Boolean status chart;
2. a Cartesian product chart for the two possible central Tucker middle labels;
3. a strictly convex discrete central defect potential, namely Hamming distance to the unique target corner.

Therefore any global equivariant carrier assembled from these squares may treat the square interiors as already solved. The topological obstruction must live on gluing/boundary data between squares or in overlapping braid cells, not in the flat 2-cell itself.
