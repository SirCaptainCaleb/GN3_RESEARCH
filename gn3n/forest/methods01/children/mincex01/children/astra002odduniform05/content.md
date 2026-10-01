# Odd balanced-cover failures force a linear uniform exchange-or-support-switch family

## Statement

Let H be a minimum-order counterexample to the balanced two-cover conjecture of odd order n=2k+1 with k>=4. Choose one balanced k|k deletion cover F_v of H-v for every vertex v. Then there is a label d and a set S of at least ceil(k/2) labels incompatible with F_d such that uniformly either (A) every F_t, t in S, is support-incompatible with F_d, or (B) every F_t is support-compatible but order-incompatible with F_d. In branch (B), writing F_d=P|Q, support compatibility and balance force for each t: if t in P then F_t has support partition (P-{t}) union {d} | Q, while if t in Q then it has support partition P | (Q-{t}) union {d}. Consequently one may further choose S' subseteq S of size at least ceil(|S|/2) whose labels all lie on one anchor side, so all covers in S' are one-for-one support exchanges against the same fixed opposite support, while still carrying relative-order disagreement with F_d on the common vertices.

## Body

# Proof

By astra002odddensity04, some chosen balanced deletion cover F_d is incompatible with at least k other chosen covers.

Every incompatible partner F_t falls into exactly one of two broad classes.

- The induced support partitions of F_d and F_t on H-{d,t} differ. Call this support-incompatible.
- The support partitions agree, but the full pair states do not. Then some pair of common vertices in one common support occurs in opposite relative orders. Call this support-compatible but order-incompatible.

By pigeonhole, at least ceil(k/2) incompatible partners have the same broad type. Let S be such a family. This proves the uniform alternatives (A) and (B).

Now assume branch (B), and write the balanced anchor cover as

F_d=P|Q,

with |P|=|Q|=k.

Fix t in S. Suppose first that t lies in P. Restrict F_d to H-{d,t}. Its support partition is

(P-{t}) | Q,

with class sizes k-1 and k.

Since F_t is support-compatible with F_d, its restriction to the same common vertex set has exactly this same unordered support partition.

The cover F_t itself is balanced on H-t, so its two supports both have order k. The omitted label d must therefore restore to the smaller class P-{t}; if d restored to Q, the two support sizes would be k-1 and k+1, not k and k.

Hence the support partition of F_t is

((P-{t}) union {d}) | Q.

The case t in Q is symmetric and gives

P | ((Q-{t}) union {d}).

Thus every support-compatible incompatible partner is, at the support level, a one-for-one exchange of d for t on the anchor side containing t, while the opposite anchor support is fixed.

Because F_t is not fully compatible with F_d, their common ordered support data disagree somewhere: some two common vertices belonging to one common support occur in different relative orders.

Finally partition S according to whether its labels lie in P or Q. One side contains at least ceil(|S|/2) labels. Calling that subfamily S' gives the claimed synchronized same-side exchange family with one fixed opposite support.

No crossing-number hypothesis is used. In particular this does not invoke the stronger reciprocal-one-crossing singleton-transfer theorem.
