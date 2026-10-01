# The longest path cannot have order seven in an order-eleven minimum counterexample

## Statement

A hypothetical order-eleven minimum counterexample cannot have maximum tight-path order seven. The balanced 4|4 endpoint-kernel branch is excluded by astra003lambda7case1, and the remaining 6|2 branch of codim4_01 Proposition 5.1 reverses and splices with the inherited middle 3-path to give a spanning 9|2 two-cover.

## Body

Assume for contradiction that H is a hypothetical order-eleven minimum counterexample with a globally longest tight path

Y=(L,u,x_2,x_3,x_4,v,R)

of order seven. Let

S=V(H)-V(Y),

so |S|=4, and put

N=(x_2,x_3,x_4).

The codimension-four theorem codim4_01 Proposition 5.1 gives an exact two-cover of the eight-vertex induced subtournament on

S union {L,u,v,R}

in one of two forms.

The first, 4|4 form is impossible by astra003lambda7case1.

Hence only Proposition 5.1 case 2 could remain. In that case, writing the outgoing middle-matching edge as

O={o_0,o_1}

and the complementary middle-matching edge as I, the proposition gives the tight six-path

A=(u,L,o_0,o_1,R,v)

and the complementary two-vertex path I.

Reverse A. Reversal preserves tight paths, so

A^rev=(v,R,o_1,o_0,L,u)

is a tight six-path.

Now append the inherited middle path N. The nine-vertex order

(v,R,o_1,o_0,L,u,x_2,x_3,x_4)

is tight.

Indeed, all consecutive triples through

(v,R,o_1,o_0,L,u)

belong to the reversed tight path A^rev. The only new junction triple is

(L,u,x_2),

which is a consecutive triple of the original tight path Y. The following triples

(u,x_2,x_3)
and
(x_2,x_3,x_4)

are also consecutive triples of Y.

Thus A union N is a Hamiltonian nine-set. Its complementary vertex set is exactly I, and every two-vertex set is a tight path. Therefore

(A union N) | I

is a spanning two-path cover of H, contradiction.

Hence the 6|2 endpoint-kernel case is impossible as well. Together with astra003lambda7case1, this eliminates the entire lambda=7 branch.

Consequently every hypothetical order-eleven minimum counterexample has maximum tight-path order at most six. Combined with the half-order lower bound, only lambda=5 or lambda=6 remain.
