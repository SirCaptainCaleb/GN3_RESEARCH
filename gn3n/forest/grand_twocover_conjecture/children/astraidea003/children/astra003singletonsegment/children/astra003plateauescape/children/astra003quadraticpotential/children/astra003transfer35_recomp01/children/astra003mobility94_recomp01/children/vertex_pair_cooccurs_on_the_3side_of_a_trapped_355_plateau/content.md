# Every vertex pair co-occurs on the 3-side of a trapped 3|5|5 plateau

## Statement

Let K be a connected Astra-003 component consisting of 3|5|5 states on thirteen vertices, and let D be its family of three-side supports. Then the two-shadow of D is the complete graph K_13: every pair of vertices occurs together in some reachable three-side. Since every occurring pair has D-codegree at least seven, |D|>=182.

## Body

# Every pair is reachable on the three-side

Let D be the family of three-side supports in a trapped order-thirteen 3|5|5 connected component of the Astra-003 move graph. By the full-label reachability theorem, every vertex occurs in some member of D.

Assume for contradiction that a pair {z,w} occurs in no member of D.

Choose a reachable state

X|P|Q

with z in X. Since {z,w} is absent from the two-shadow, w is not in X. After interchanging P,Q if necessary, assume w in P. Write

X={z,x_1,x_2}

and put

B=P-{w}.

For i=1,2, the five-set

B union {x_i}

must be non-Hamiltonian. Indeed, if it were Hamiltonian, then replacing X|P by

(X-{x_i}) union {w}  |  B union {x_i}

would be a legal 3|5 repartition whose new three-side contains both z and w, contrary to the assumed absence of {z,w} from the shadow.

We again split according to B.

## Case 1: B is Hamiltonian

Choose a Hamilton path

B=(a,b,c,d).

Both B union {x_1} and B union {x_2} are non-Hamiltonian. The repeated-bad-extension lemma therefore gives a Hamiltonian five-set

F={a,b,c,x_1,x_2}.

Its complement inside X union P is

{d,w,z},

which is a Hamiltonian three-set. Hence

F | {d,w,z}

is a legal repartition of X|P with a new three-side containing z,w, contradiction.

## Case 2: B is non-Hamiltonian

Choose any tight three-vertex path T on three vertices of B, and let b_0 be the fourth vertex.

In the bad-extension graph around T on exterior vertices {b_0,x_1,x_2}, both b_0x_1 and b_0x_2 are bad edges because

T union {b_0,x_i}=B union {x_i}

is non-Hamiltonian. The certified bad-extension graph is triangle-free. Therefore x_1x_2 is not bad, so

T union {x_1,x_2}

is Hamiltonian.

Its complement inside X union P is

{b_0,w,z},

again a Hamiltonian three-set. Thus this gives a legal repartition whose new three-side contains z,w, contradiction.

Therefore no pair is absent: the two-shadow G of D is K_13.

The Johnson-projection lemma gives D-codegree at least seven for every pair in the shadow. Since now all C(13,2)=78 pairs occur,

3|D| = sum_{uv} d_D(uv) >= 7*78=546.

Hence

|D|>=182.

Equivalently, at most 104 of the 286 triples can be absent, and every pair lies in at most four absent triples.