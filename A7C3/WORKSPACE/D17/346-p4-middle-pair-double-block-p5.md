# A double-blocked same-middle reentry of a P4 is necessarily Hamiltonian on its five vertices

**Workspace:** D17
**State:** established
**Key:** `p4-middle-pair-double-block-p5`

**Summary:** Let K=(x,p,q,y) be a tight P4 and let J=(p,b,q) be a tight turn on its middle pair, with b outside K. Test the two natural extension seams alpha=(x,p,b), beta=(b,q,y). If both are tight then (x,p,b,q,y) is a literal P5. The new content is the double-blocked cell alpha,beta both bad. R3 gives (b,p,x) and (y,q,b). If the induced five-set X={x,p,q,y,b} were non-Hamiltonian, accepted R902 makes it edge-orderable. The certified turns force the edge-label chain bp<xp<pq<qy<bq. This chain alone forces an increasing Hamilton path by a four-case split on by versus qy and xy versus qy,xp: x-p-q-y-b, b-p-q-y-x, y-x-p-q-b, or p-x-y-q-b. Contradiction. Thus the double-blocked cell is a Hamilton P5 support. Mixed seam cells are explicitly not claimed Hamiltonian; exact edge-order realizations show they can be non-Hamiltonian. Hence the genuine five-vertex replay residue is exactly one-pass/one-fail.

### 1. P4 middle-pair replay cell
Let H be a hypothetical smallest Strong Level-(1) counterexample and retain a proper tight P4

  K=(x,p,q,y).                                            (DB.1)

Thus

  (x,p,q), (p,q,y)

are tight. Let b be a fifth vertex outside K and suppose the same physical middle pair supports a later tight turn

  J=(p,b,q).                                              (DB.2)

Test the two literal extension seams

  alpha=(x,p,b),
  beta =(b,q,y).                                          (DB.3)

If both are tight, then

  (x,p,b,q,y)                                             (DB.4)

is immediately a tight P5. We analyze the opposite extreme in which both seams are bad.

### 2. Double blocking gives two exact reverse turns
Assume

  alpha, beta are both bad.                               (DB.5)

Boundary antisymmetry R3 gives their complete reversals

  (b,p,x) tight,
  (y,q,b) tight.                                          (DB.6)

Put

  X={x,p,q,y,b}.                                          (DB.7)

We claim H[X] is Hamiltonian.

### 3. Suppose the five-set is non-Hamiltonian
Assume for contradiction that H[X] has no tight Hamilton P5. Accepted R902 applies to this exact five-vertex induced boundary tournament: H[X] is edge-orderable. Let < be a strict total order on the ten ordinary edges of K_X which realizes tight turns as increasing consecutive-edge comparisons, as in accepted R887.

Write an ordinary edge by concatenating its endpoint names. From the four certified turns

  (b,p,x),
  (x,p,q),
  (p,q,y),
  (y,q,b)

we obtain respectively

  bp < px,
  px < pq,
  pq < qy,
  qy < qb.                                                (DB.8)

Hence

  bp < px < pq < qy < qb.                                (DB.9)

Notice that the later turn J=(p,b,q) is compatible with this chain, but the argument below needs no additional comparison beyond (DB.9).

### 4. The chain forces an increasing Hamilton order
Only the positions of the two edges by and xy relative to the displayed chain matter. Since < is a strict total order, exactly one of the following cases occurs.

**Case 1: qy < by.**
Then

  px < pq < qy < by,

so the vertex order

  (x,p,q,y,b)                                             (DB.10)

has strictly increasing consecutive edge labels. By R887 it is a tight Hamilton P5.

**Case 2: by < qy and qy < xy.**
Then

  bp < pq < qy < xy,

using bp<px<pq from (DB.9). Hence

  (b,p,q,y,x)                                             (DB.11)

is a tight Hamilton P5.

**Case 3: by < qy, xy < qy, and xy < px.**
Then

  xy < px < pq < qb,

so

  (y,x,p,q,b)                                             (DB.12)

is a tight Hamilton P5.

**Case 4: by < qy, xy < qy, and px < xy.**
Then

  px < xy < yq < qb,

so

  (p,x,y,q,b)                                             (DB.13)

is a tight Hamilton P5.

The four cases are exhaustive and each contradicts the assumption that H[X] is non-Hamiltonian. Therefore H[X] is Hamiltonian.

### 5. Exact local conclusion
For a P4 K=(x,p,q,y) and a later same-middle turn J=(p,b,q):

- if both natural extension seams pass, (x,p,b,q,y) is a literal P5;
- if both natural extension seams fail, the five-set {x,p,q,y,b} nevertheless has a tight Hamilton P5 by Sections 2--4.

Thus the two equal-parity seam patterns are Hamiltonian. The only five-vertex patterns not consumed by this theorem are the two MIXED cells in which exactly one of alpha,beta is tight.

### 6. Scope fence and genuine mixed residue
No claim is made that a mixed cell is Hamiltonian. This is not merely caution: exact edge-order realizations exist satisfying the P4, J, and one-pass/one-fail seam inequalities while avoiding every increasing Hamilton order on the five-set. Therefore the mixed branch is a genuine local residue and must be consumed by additional family information rather than by R902 alone.

The theorem also does not call a P5 born at phase zero numerical Morse progress. Its use in G26 is structural: in the P4 middle-pair transport system, any replay avoiding Hamilton five-vertex growth must flip exactly one of the two boundary seam bits.