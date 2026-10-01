# Asymmetric interior pivot cross-swaps force order disagreement or two endpoint bridges

## Statement

Let H be a minimum counterexample and H-x=P|Q an exact deletion two-cover, with second-type failed-insertion pivots at interior gaps p_i|p_{i+1} and q_j|q_{j+1}. Suppose the two central cross-join reversal pairs are asymmetric: exactly one of (p_i,x,q_{j+1}) and (q_j,x,p_{i+1}) is tight. Then either P or Q admits a Hamilton order different from its displayed order, hence an explicit relative-order-disagreement witness, or both endpoint bridge paths (p_1,p_0,p_m,p_{m-1}) and (q_1,q_0,q_s,q_{s-1}) are tight. Thus the asymmetric pivot-pivot residue cannot remain a generic nine-vertex cross-swap obstruction: absent order disagreement it simultaneously reverses the two end pairs of both deletion-cover components.

## Body

# Asymmetric interior pivot cross-swaps force order disagreement or two endpoint bridges

Let H be a minimum counterexample and let

H-x=P|Q,

where
P=(p_0,...,p_m),  Q=(q_0,...,q_s).

Assume the failed-insertion obstruction supplied by the second-type normal form occurs at interior gaps
p_i|p_{i+1} and q_j|q_{j+1},
so
1<=i<=m-2,  1<=j<=s-2.

Put
P_L=(p_0,...,p_i),  P_R=(p_{i+1},...,p_m),
Q_L=(q_0,...,q_j),  Q_R=(q_{j+1},...,q_s).

The pivot normal form gives the four tight paths

(P_L,x), (x,P_R), (Q_L,x), (x,Q_R).

Consider the two central cross-join reversal pairs

(p_i,x,q_{j+1})  versus  (q_{j+1},x,p_i),

(q_j,x,p_{i+1})  versus  (p_{i+1},x,q_j).

Assume they are asymmetric: exactly one of the two forward cross-joins
(p_i,x,q_{j+1}) and (q_j,x,p_{i+1})
is tight.

We prove that either P or Q has a second Hamilton order, or both endpoint bridge four-paths

(p_1,p_0,p_m,p_{m-1}),
(q_1,q_0,q_s,q_{s-1})

are tight.

## 1. The asymmetric pivot produces a spanning three-cover

By symmetry interchange P and Q if necessary, so

(q_j,x,p_{i+1})

is tight while

(p_i,x,q_{j+1})

is non-tight. Boundary antisymmetry gives

(q_{j+1},x,p_i)

tight.

The first of these central triples, together with the pivot paths (Q_L,x) and (x,P_R), shows that

K=(Q_L,x,P_R)

is a tight path.

Hence

K | P_L | Q_R

is a spanning three-path cover of H. All three components are nonempty, and P_L,Q_R are nontrivial because the pivot gaps are interior.

Since pc(H)>2, no ordered concatenation of two of these three displayed components can be a tight path: any such concatenation, together with the untouched third component, would be a spanning two-cover.

## 2. The P-end wrap

Consider concatenating K followed by P_L.

The path K ends with (...,p_{m-1},p_m), while P_L begins (p_0,p_1,...). The only new consecutive triples are

beta_P=(p_{m-1},p_m,p_0),
alpha_P=(p_m,p_0,p_1).

They cannot both be tight.

The cyclic-rotation lemma for the tight path P says:

- alpha_P tight iff (p_m,p_0,p_1,...,p_{m-1}) is a Hamilton tight path on V(P);
- beta_P tight iff (p_1,...,p_m,p_0) is a Hamilton tight path on V(P);
- if neither is tight, then, since m>=3,
  (p_1,p_0,p_m,p_{m-1})
  is a tight four-vertex path.

Because alpha_P,beta_P cannot both be tight, there are only two possibilities.

If exactly one is tight, P has a Hamilton order different from its displayed order. The path-intersection calculus therefore supplies an explicit relative-order-disagreement witness: a reversed common ordered edge, a reversing tight triple, or a vertex-simple tight cycle.

If neither is tight, the endpoint bridge
(p_1,p_0,p_m,p_{m-1})
is tight.

Thus, absent order disagreement on P, its two endpoint pairs are joined by the displayed reversed four-path.

## 3. The Q-end wrap

Now concatenate Q_R followed by K.

The path Q_R ends with (...,q_{s-1},q_s), while K begins (q_0,q_1,...). The only new consecutive triples are

beta_Q=(q_{s-1},q_s,q_0),
alpha_Q=(q_s,q_0,q_1).

Again they cannot both be tight, since otherwise Q_R K | P_L would be a spanning two-cover.

Apply the same cyclic-rotation lemma to Q. If exactly one of alpha_Q,beta_Q is tight, Q has a second Hamilton order and hence yields explicit relative-order disagreement. If neither is tight, then

(q_1,q_0,q_s,q_{s-1})

is a tight four-vertex path.

Therefore, if neither P nor Q exposes relative-order disagreement, both endpoint bridges are simultaneously tight:

(p_1,p_0,p_m,p_{m-1}),
(q_1,q_0,q_s,q_{s-1}).

The opposite asymmetric orientation is identical after interchanging P and Q.

Thus the asymmetric interior pivot-pivot branch reduces to explicit order disagreement or a synchronized pair of endpoint-to-endpoint tight four-paths. ∎
