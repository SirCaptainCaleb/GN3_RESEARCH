# Every vertex occurs as a three-side label in a trapped 3|5|5 plateau

## Statement

Let K be a connected Astra-003 component consisting of 3|5|5 states on thirteen vertices, and let D be the family of three-vertex component supports occurring in K. Then every vertex of H belongs to some member of D. Consequently the two-shadow of D uses all thirteen vertices. Combined with the coordinate-wise six-exchange property, |D|>=122.

## Body

# No vertex can remain permanently excluded from the three-side

Let K be a connected Astra-003 component consisting entirely of 3|5|5 states on a thirteen-vertex boundary tournament H. Let D be the family of three-vertex supports occurring in K.

Assume for contradiction that some vertex z belongs to no member of D.

Choose any state

X|P|Q

in K with z in P. Write

X={x_1,x_2,x_3},

and put

B=P-{z}.

For each i, the five-set

B union {x_i}

must be non-Hamiltonian. Indeed, if it were Hamiltonian, then replacing X|P by

(X-{x_i}) union {z}  |  B union {x_i}

would be a legal 3|5 repartition whose new three-side contains z, contradicting the choice of z.

We now split according to whether B is Hamiltonian.

## Case 1: B is Hamiltonian

Choose a Hamilton path

B=(a,b,c,d).

The five-sets B union {x_1} and B union {x_2} are both non-Hamiltonian. By the certified repeated-bad-extension lemma, the five-set

F={a,b,c,x_1,x_2}

is Hamiltonian. Its complement inside X union P is

{d,z,x_3},

which has order three and hence is Hamiltonian. Thus

F | {d,z,x_3}

is a legal repartition of X|P whose new three-side contains z, contradiction.

## Case 2: B is non-Hamiltonian

Choose any three vertices of B and order them as a tight three-vertex path T; let b_0 be the fourth vertex of B.

Consider the bad-extension graph around T on the four exterior vertices

{b_0,x_1,x_2,x_3},

where two exterior vertices are adjacent exactly when adjoining them to T gives a non-Hamiltonian five-set.

For each i,

T union {b_0,x_i}=B union {x_i}

is non-Hamiltonian, so b_0x_i is an edge of this bad-extension graph for i=1,2,3.

The certified bad-extension theorem says this graph is triangle-free. Hence no pair x_ix_j can also be bad: otherwise b_0,x_i,x_j would span a triangle. Therefore, for every distinct i,j,

T union {x_i,x_j}

is Hamiltonian.

Take i=1,j=2. Its complement inside X union P is

{b_0,z,x_3},

again a Hamiltonian three-set. Thus

T union {x_1,x_2}  |  {b_0,z,x_3}

is a legal repartition of X|P whose new three-side contains z, contradiction.

Both cases are impossible. Therefore every vertex of H occurs in some reachable three-side support.

The Johnson-projection lemma gives the coordinate-wise exchange condition, and its shadow-count proof gives

|D| >= (28/3)m,

where m is the number of vertices appearing in the two-shadow. Here m=13, so

|D| >= ceil(364/3)=122.

Thus any trapped order-thirteen 3|5|5 plateau component reaches at least 122 distinct three-side supports and uses all thirteen vertex labels.