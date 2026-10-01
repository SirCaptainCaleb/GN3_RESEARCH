# Reciprocal singleton-transfer states always escape the Astra equality plateau

## Statement

In the reciprocal-one-crossing first form of f6cdd6346980, let C_x,C_m,C_y be the three singleton-transfer covers of astra003singletonsegment. Their Astra-003 move component always contains a spanning three-cover whose component-size multiset differs from {lambda,lambda,1}. More precisely, if X_L={b,x,m,y} is Hamiltonian it contains a cover of orders {lambda-1,lambda-2,4}; if X_L is non-Hamiltonian but X_R={m,y,s,q} is Hamiltonian it contains one of orders {lambda,lambda-3,4}; and if both are non-Hamiltonian it contains the five-bridge cover of orders {lambda-2,lambda-2,5}. Thus the reciprocal singleton-transfer residue is never trapped by the component-size equality plateau.

## Body


# Reciprocal singleton transfers cannot trap the Astra move graph at equality

Assume the reciprocal-one-crossing first form

G_x=(m,B)|(Q,y),
G_y=(x,B)|(Q,m),
G_m=(x,B)|(Q,y),

where B=(b,r,...) and Q=(...,s,q) have order lambda-1. Let

C_m=(x,B)|(Q,y)|{m}

and use the connected singleton-transfer segment from astra003singletonsegment.

Put

X_L={b,x,m,y},
X_R={m,y,s,q}.

By astra003doublekernel, each of X_L and X_R is either Hamiltonian or a rigid non-Hamiltonian matching-block four-set. We treat the three exhaustive branches.

## 1. The left endpoint window is Hamiltonian

Endpoint-hook forcing for G_m gives (b,x,m) tight.

Starting from C_m, repartition the pair (x,B),{m} into

(b,x,m) | (B-b).

This is legal because the two displayed paths are disjoint and partition V(x,B) union {m}. Thus we reach

(b,x,m)|(B-b)|(Q,y).

Let L be any Hamilton path on X_L. Repartition the pair (b,x,m),(Q,y) into

L | Q.

Their union is exactly X_L disjoint-union V(Q), and L,Q are disjoint tight paths. Hence the move graph contains

L | (B-b) | Q,

whose component orders are 4, lambda-2, lambda-1.

## 2. The left window is non-Hamiltonian and the right endpoint window is Hamiltonian

The first-form theorem gives (m,y,q) tight.

From C_m, repartition (Q,y),{m} into

(m,y,q) | (Q-q).

This gives

(x,B)|(m,y,q)|(Q-q).

Let R be any Hamilton path on X_R. Repartition (m,y,q) and Q-q into

R | (Q-{s,q}).

Their union is the same: X_R together with the remaining vertices of Q. Thus the move graph contains

(x,B) | R | (Q-{s,q}),

with component orders lambda, 4, lambda-3.

## 3. Both endpoint windows are non-Hamiltonian

This is exactly the double-kernel branch treated in astra003fivebridge. There the move component contains

S | (B-b) | (Q-q),

where S is an explicit Hamiltonian five-path on {x,b,m,q,y}. Its component orders are 5, lambda-2, lambda-2.

## Conclusion

The three branches are exhaustive. In each case the connected component of the Astra pairwise-repartition graph containing the reciprocal singleton-transfer states contains a three-cover whose component-size multiset is different from {lambda,lambda,1}.

Therefore reciprocal-one-crossing singleton transfer cannot be a terminal equality plateau for Astra idea 003. Any genuine trapped component must fail for a deeper reason after this explicit local escape, rather than because the singleton transfer merely shuttles the omitted label among equal-size deletion states.
