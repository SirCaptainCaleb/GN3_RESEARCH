# Double matching-block singleton residue forces an explicit Hamiltonian five-bridge

## Statement

Under the reciprocal-one-crossing first form, assume both endpoint four-sets X_L={b,x,m,y} and X_R={m,y,s,q} from astra003doublekernel are non-Hamiltonian. Then S={x,b,m,q,y} is Hamiltonian, with path order either (x,b,m,q,y) or (b,x,y,q,m). Moreover the Astra 003 repartition component containing the singleton-transfer states contains the spanning three-cover S|(B-b)|(Q-q), reached from C_m or C_y by two legal moves. Its component orders are 5,lambda-2,lambda-2. Hence the double-non-Hamiltonian singleton-transfer residue necessarily escapes the (lambda,lambda,1) equality plateau.

## Body

# The double-kernel residue creates a Hamiltonian five-bridge and escapes the equality plateau

Assume the first form

G_x=(m,B)|(Q,y),
G_y=(x,B)|(Q,m),
G_m=(x,B)|(Q,y),

with B=(b,r,...) and Q=(...,s,q), and assume both endpoint four-sets from astra003doublekernel are non-Hamiltonian.

The left four-set

X_L={b,x,m,y}

has the forced matching-block order

{bx,my} < {bm,xy} < {by,xm}.

In particular bx<bm, so

(x,b,m)

is tight.

The first-form theorem also gives

(b,m,q)

tight.

For the right four-set

X_R={m,y,s,q},

put

N_0={my,sq},
N_1={mq,ys},
N_2={ms,yq}.

Its bottom block is N_0, and there are two possible orders for the upper blocks.

## First right-kernel order

Suppose

N_0<N_1<N_2.

Then mq<yq, so

(m,q,y)

is tight. Therefore

S=(x,b,m,q,y)

is a tight Hamilton path on the five-set {x,b,m,q,y}.

Recall the spanning three-cover

C_m=(x,B)|(Q,y)|{m}.

Repartition the two components (x,B) and {m}. The tight three-path (x,b,m) and the tail

B^- = B-b = (r,...)

are disjoint and partition the same union. Thus one legal Astra 003 move gives

(x,b,m)|B^-|(Q,y).

Now repartition the components (x,b,m) and (Q,y). The Hamilton five-path S=(x,b,m,q,y) and the prefix

Q^- = Q-q

are disjoint and partition their union. Hence a second legal move gives

S|B^-|Q^-.

## Second right-kernel order

Suppose instead

N_0<N_2<N_1.

Then yq<mq, so

(y,q,m)

is tight.

Endpoint-hook forcing applied to G_y on (x,B) gives

(b,x,y)

tight, while endpoint-hook forcing applied to G_x on (Q,y) gives

(x,y,q)

tight. Hence

S=(b,x,y,q,m)

is a tight Hamilton path on the same five-set {x,b,m,q,y}.

Now start from

C_y=(x,B)|(Q,m)|{y}.

Repartition (x,B) and {y} into the tight three-path (b,x,y) and the same tail B^-=B-b. This is one legal move:

(b,x,y)|B^-|(Q,m).

Then repartition (b,x,y) and (Q,m) into the Hamilton five-path S=(b,x,y,q,m) and Q^-=Q-q. This gives, in a second legal move,

S|B^-|Q^-.

## Consequences

Thus in either right matching-block order the connected component of the Astra 003 move graph containing the singleton-transfer segment also contains the explicit three-cover

S | (B-b) | (Q-q),

where S is a Hamiltonian five-set and

|S|=5,
|B-b|=lambda-2,
|Q-q|=lambda-2.

Therefore the double-non-Hamiltonian singleton-transfer residue cannot be trapped on the equal-size (lambda,lambda,1) plateau: pairwise repartition necessarily reaches a state with different component sizes.

Since S is a proper Hamiltonian set in a minimum counterexample, H-S is non-Hamiltonian and has path-cover number exactly two. The explicit cover above supplies one particular two-path cover of H-S when B-b and Q-q happen to be the two components; regardless, the move-graph conclusion already gives a concrete plateau escape. The remaining task is to exploit the new 5|(lambda-2)|(lambda-2) geometry to force a merge or further monotone progress.
