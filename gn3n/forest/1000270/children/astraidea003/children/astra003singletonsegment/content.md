# Singleton-transfer endpoint residue is a two-step Astra repartition segment

## Statement

In the reciprocal-one-crossing first form of f6cdd6346980, the three associated exact deletion covers induce spanning three-covers C_x,C_m,C_y with component-size vector (lambda,lambda,1) such that C_x and C_m differ by one legal pairwise repartition move and C_m and C_y differ by one legal pairwise repartition move. Hence the singleton-transfer residue lies on a length-two path in the move graph of Astra idea 003, with the middle state having at least two distinct repartition neighbors.

## Body

# Singleton transfer as an Astra repartition segment

Assume the first form of f6cdd6346980. Thus H is a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, there are distinct vertices x,y,m and tight paths B,Q of order lambda-1 such that

G_x=(m,B)|(Q,y)

is an exact two-cover of H-x,

G_y=(x,B)|(Q,m)

is an exact two-cover of H-y, and

G_m=(x,B)|(Q,y)

is an exact two-cover of H-m.

Adjoin each omitted vertex as a singleton component and write

C_x=(m,B)|(Q,y)|{x},

C_m=(x,B)|(Q,y)|{m},

C_y=(x,B)|(Q,m)|{y}.

These are spanning three-path covers of H.

From C_x, repartition the pair of components (m,B) and {x}. Their union is V(B) union {m,x}. The two tight paths (x,B) and {m} partition exactly this same union. Therefore replacing

(m,B)|{x}

by

(x,B)|{m}

is one legal move of Astra idea 003, and the resulting cover is C_m.

Likewise, from C_m repartition the pair (Q,y) and {m}. Their union is V(Q) union {y,m}, and the two tight paths (Q,m) and {y} partition the same union. Hence replacing

(Q,y)|{m}

by

(Q,m)|{y}

is one legal move, producing C_y.

Thus C_x--C_m--C_y is a length-two path in the pairwise-repartition move graph. The three covers are distinct because x,y,m are distinct. Each nonsingleton component has order lambda, so all three covers have the same decreasing component-size vector (lambda,lambda,1).

Consequently the reciprocal-one-crossing singleton-transfer residue is not an isolated reconfiguration state. Rather, it is an equality plateau for any component-size lexicographic potential: size alone cannot distinguish progress along this segment. Any proof of Astra idea 003 that consumes this residue must use additional path-order or endpoint-hook information to escape the plateau or merge two components.
