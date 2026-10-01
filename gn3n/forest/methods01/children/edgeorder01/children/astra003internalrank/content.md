# A permanently internal vertex in a Hamiltonian edge-ordered K4 has one of two extreme rank forms

## Statement

Let K be an edge-ordered K4 on {v,a,b,c}. Suppose a-v-b-c is an increasing Hamilton path and v is not an endpoint of any increasing Hamilton path. Then exactly one of the following two rank patterns holds: max{ab,vc}<ac<av<vb<bc, or ac<av<vb<bc<min{ab,vc}. Conversely either pattern makes a-v-b-c increasing and forbids v from being an endpoint of any increasing Hamilton path.

## Body


Let the six edge ranks be denoted by

x=av, y=vb, z=vc,
A=ab, B=ac, C=bc.

The displayed increasing Hamilton path gives

x<y<C.

Assume v is not an endpoint of any increasing Hamilton path. Since reversing a vertex order reverses the edge-rank sequence, v is an endpoint of an increasing Hamilton path exactly when one of the six edge sequences obtained from a Hamilton path starting at v is monotone in either direction.

Consider first

v-a-b-c,

whose edge sequence is x,A,C. Since x<C, monotonicity would occur if x<A<C. Hence

A<x or A>C.                                            (1)

Similarly, the path

v-a-c-b

has edge sequence x,B,C, so

B<x or B>C.                                            (2)

Now use

v-b-c-a,

whose edge sequence is y,C,B. Since y<C, the alternative B>C would make

y<C<B

strictly increasing, impossible. Thus B<C, and (2) sharpens to

B<x.                                                   (3)

There are now two cases from (1).

Case I: A<x.

Since B<x<y, consider v-b-a-c, whose edge sequence is y,A,B. If B<A, then

y>A>B

is strictly decreasing, again giving v as an endpoint. Therefore

A<B.

Hence

A<B<x<y<C.

Finally consider v-c-a-b, with edge sequence z,B,A. Because A<B, if z>B then

z>B>A

is strictly decreasing. Thus z<B. Therefore

max{A,z}<B<x<y<C,

which is exactly

max{ab,vc}<ac<av<vb<bc.

Case II: A>C.

Together with (3) and x<y<C this gives

B<x<y<C<A.

Consider v-c-b-a, whose edge sequence is z,C,A. Since C<A, if z<C then

z<C<A

is strictly increasing. Hence z>C. Therefore

B<x<y<C<min{A,z},

which is exactly

ac<av<vb<bc<min{ab,vc}.

This proves necessity.

Conversely, inspect the six Hamilton paths starting at v. In the first pattern, every corresponding three-edge rank sequence has a strict peak or valley; none is monotone. The same direct check holds in the second pattern. Meanwhile av<vb<bc makes a-v-b-c increasing in both cases. Thus the two patterns are also sufficient.

In the eight-label Astra residue, astra003internaluv gives Hamiltonian four-sets P,Q with excluded vertices u,v permanently internal. The mutual bad-extension core 851be99bfc11 says, for example, Q+r is non-Hamiltonian for each of three exterior labels r. By the certified five-set theorem, any such Q+r is edge-orderable, and restricting its representing edge order to Q represents Q. Hence the classification applies to Q with distinguished vertex v, and symmetrically to P with distinguished vertex u.
