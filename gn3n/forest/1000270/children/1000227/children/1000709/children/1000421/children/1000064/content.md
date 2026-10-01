# Minimal endpoint exchanges force a coupled square-triangle configuration

## Statement

In the order-thirteen mu=6 shell, the minimal synchronized two-end direct-crossing branch either yields explicit relative-order disagreement or simultaneously produces (i) a pairwise-compatible three-label deletion triangle on a four-vertex X-core, (ii) a Johnson four-cycle of Hamiltonian six-supports obtained by commuting the two endpoint exchanges, and (iii) the corresponding radius-three deficient-support triangle with its two hybrid transfer triangles.

## Body

# Minimal synchronized endpoint exchanges force a coupled square-triangle configuration

Work in the order-thirteen mu=6 shell. Let

V(H)=X disjoint-union Q, with |X|=7 and |Q|=6,

where X is non-Hamiltonian and Q=(q_0,...,q_5) is a Hamilton tight path. Let t in X be a Hamiltonian deletion label of X, and put F_t=(X-{t})|Q.

Assume the two endpoint deletion covers are in the minimal direct-crossing branch of b27f4c1a9e63. Thus for y=q_0,q_5 the chosen exact cover of H-y is support-incompatible with F_t, has exactly two three-part crossings relative to

(X-{t}) | (Q-{y}) | {t},

and contains a direct edge between the two nonsingleton classes.

Then either there is explicit relative-order disagreement, or the following configuration exists.

There are distinct vertices a,c in X-{t} such that

H-q_0=(Q-{q_0}+{a}) | (X-{a}),

H-q_5=(Q-{q_5}+{c}) | (X-{c}),

at the support level, with all four displayed six-sets Hamiltonian.

Moreover:

1. The canonical deletion covers for t,a,c,
   (X-{t})|Q, (X-{a})|Q, (X-{c})|Q,
   are pairwise compatible; hence t,a,c occupy one common insertion gap of the four-vertex base
   B=X-{t,a,c}.

2. The four Hamiltonian six-supports
   Q,
   Q_0=Q-{q_0}+{a},
   Q_5=Q-{q_5}+{c},
   Q_05=Q-{q_0,q_5}+{a,c}
   form a four-cycle in the Johnson graph J(13,6):
   Q--Q_0--Q_05--Q_5--Q,
   with every cycle edge a one-for-one exchange and the two diagonals at Johnson distance two.

3. Put
   N_a=(X-{a}) union {q_0},  N_c=(X-{c}) union {q_5}.
   Then X,N_a,N_c are deficient seven-supports forming a triangle in the radius-three deficient-support graph Gamma. In addition, N_a and N_c lie in the two certified hybrid single-transfer triangles attached to X.

If the compatible triangle on t,a,c has transitive precedence, its common gap is exactly the middle 2|2 gap of B; if its gap is an endpoint, the precedence is cyclic and the state enters the endpoint-compatible-triangle four-kernel frontier.

## Proof

By b27f4c1a9e63, either explicit relative-order disagreement already occurs, or the two endpoint covers are singleton exchanges with distinct exchange labels a,c, and the canonical X-side deletion covers for t,a,c are pairwise compatible. The common-gap theorem then gives conclusion 1 and the stated transitive/cyclic alternatives.

Let L be the Hamilton path on Q_0 coming from the q_0-deletion cover and let R be the Hamilton path on Q_5 coming from the q_5-deletion cover.

If L orders two common Q-vertices differently from Q, or R does, the path-intersection calculus gives explicit relative-order disagreement. Thus in the remaining branch both L and R preserve the inherited relative order of their common Q-vertices.

The opposite-endpoint splice theorem 70fa2fdc777c now applies to Q,L,R with exterior labels a,c. It gives a Hamilton tight path on
Q_05=Q-{q_0,q_5}+{a,c}.
Hence all four supports in conclusion 2 are Hamiltonian. Their set differences show that consecutive supports differ by exactly one exchange, while opposite corners differ by two exchanges. Thus they form the displayed Johnson four-cycle.

Finally 7ba4686e7ab5, applied to the same two singleton endpoint-exchange covers, gives the deficient supports N_a,N_c, the distances
d_J(X,N_a)=d_J(X,N_c)=1 and d_J(N_a,N_c)=2,
and the two attached hybrid transfer triangles. This is conclusion 3.
