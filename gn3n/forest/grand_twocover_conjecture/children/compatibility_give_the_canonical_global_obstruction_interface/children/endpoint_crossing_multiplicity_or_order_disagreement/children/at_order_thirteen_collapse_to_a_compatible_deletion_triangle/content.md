# Minimal direct endpoint crossings at order thirteen collapse to a compatible deletion triangle

## Statement

Work in the order-thirteen mu=6 shell with V(H)=X disjoint-union Q, |X|=7, |Q|=6, X non-Hamiltonian, Q Hamiltonian, and t in X such that F_t=(X-{t})|Q is canonical. Suppose chosen covers at both endpoints y of Q are support-incompatible with F_t, and each has exactly two cross-class edges relative to (X-{t}) | (Q-{y}) | {t}, including a direct edge between the two nonsingleton classes. Then each endpoint cover is necessarily a one-vertex exchange (Q-{y}+{a_y}) | (X-{a_y}). If the two exchange labels coincide, explicit order disagreement follows from two-sided endpoint replacement. If they are distinct, then unless explicit order disagreement already occurs, the canonical deletion covers for t and the two exchange labels are pairwise compatible and form a common-gap deletion triangle whose common base inside X has order four. For transitive precedence the gap is exactly the middle 2|2 cut.

## Body

# Minimal direct endpoint crossings at order thirteen collapse to a compatible deletion triangle

Work in the order-thirteen mu=6 shell. Let

V(H)=X disjoint-union Q,

with |X|=7, |Q|=6, X non-Hamiltonian and Q=(q_0,...,q_5) Hamiltonian. Let t in X be a Hamiltonian deletion label of X and put

A=X-{t}.

Fix a Hamilton path on A and the canonical deletion state

F_t=A|Q

of H-t.

For y in {q_0,q_5}, put B_y=Q-{y}. Let G_y be an exact two-cover of H-y that is support-incompatible with F_t on H-{t,y}. Assume that G_y has exactly two ordinary edges joining different classes of

A | B_y | {t},

and that at least one of these two edges directly joins A to B_y.

We first classify one endpoint.

## 1. Exact two-crossing direct mixing is a singleton exchange

Cut the two cross-class edges of G_y. By the transition identity, the total number of resulting nonempty blocks is

2+2=4.

The singleton class {t} contributes one block. Hence exactly one of A,B_y is split into two blocks and the other remains one block.

Every exact one-vertex deletion cover in the mu=6 order-thirteen shell has two components of order six.

Suppose B_y were split and A were one block. Because a direct A--B_y crossing exists, the six-vertex A-block and a nonempty B_y-block would lie in the same cover component, giving that component more than six vertices. Impossible.

Therefore A is split into two blocks and B_y is one block. Let A_1 be the A-block joined directly to B_y. Since |B_y|=5 and their common cover component has order six, A_1 is a singleton, say A_1={a_y}. That component has support

B_y union {a_y}.

The singleton t cannot belong to it, since that would give seven vertices. Hence the second component has support

(A-{a_y}) union {t}=X-{a_y}.

Both supports are Hamiltonian because they are the supports of the two path components of G_y. Thus

G_y = (Q-{y}+{a_y}) | (X-{a_y})

at the support level, with a_y in A, and both displayed supports Hamiltonian.

So every minimal direct endpoint crossing is exactly a one-vertex exchange.

## 2. The same exchange label at both ends forces order disagreement

Apply the preceding classification at y=q_0 and y=q_5, obtaining labels a_0,a_5 in A.

Suppose a_0=a_5=a.

Then X-{a} is Hamiltonian. Also both endpoint replacements

(Q-{q_0}) union {a},
(Q-{q_5}) union {a}

are Hamiltonian, using their path orders from G_{q_0},G_{q_5}.

The seven-set Q union {a} is non-Hamiltonian. Otherwise a Hamilton path on Q union {a}, together with a Hamilton path on X-{a}, would be a spanning two-cover of H.

Apply the two-sided endpoint-replacement theorem insert01 to the Hamilton path Q and exterior vertex a. Since Q union {a} is non-Hamiltonian while both endpoint replacements are Hamiltonian, one of Q and the two replacement paths disagrees in relative order with another. Hence pathcalc01 yields explicit order disagreement.

Thus, absent explicit order disagreement,

a_0 != a_5.

## 3. Distinct exchange labels give a compatible deletion triangle

Assume now that a_0,a_5,t are distinct.

For i in {0,5}, the exchange classification gives a Hamilton path on X-{a_i}. Pair that path with the fixed Hamilton order Q to obtain a canonical exact deletion cover

F_{a_i}=(X-{a_i})|Q

of H-a_i.

Consider the three covers

F_t, F_{a_0}, F_{a_5}.

Their support partitions are pairwise compatible: after deleting any two labels, the common supports are the surviving vertices of X and the unchanged support Q.

If any pair of the three X-side Hamilton paths disagrees in relative order on common vertices, pathcalc01 already gives explicit order disagreement. Otherwise all three covers are pairwise compatible as ordered deletion covers.

The common-gap theorem gapgeom01 then applies. All three labels t,a_0,a_5 lie in one common insertion gap of the common X-side path, while Q is the fixed second path.

After deleting the three labels from X, the common base has order

|X|-3=4.

Hence the minimal direct synchronized-crossing residue is a compatible deletion triangle on a four-vertex base.

If its precedence tournament is transitive, the two-deep-gap theorem in gapgeom01 forces at least two base vertices on each side of the common gap. Since the base has exactly four vertices, the gap is exactly the middle 2|2 cut.

If the common gap is an endpoint, transitive precedence is impossible; the precedence is therefore cyclic, placing the state in the certified endpoint-compatible-triangle / cyclic-kernel frontier.

Thus two minimal direct endpoint crossings do not leave an arbitrary mixed-support configuration: they produce explicit order disagreement, or a four-base compatible deletion triangle, with the transitive case rigidly centered. ∎