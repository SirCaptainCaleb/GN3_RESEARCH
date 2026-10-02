# Small deletion sides generate synchronized omission families

## Statement

Let H be a minimum counterexample and H-x=P|Q an exact deletion two-cover with 3<=|P|<=5. Then C=V(P) union {x} has at least four Hamiltonian vertex deletions. These yield deletion covers with the same fixed Q and synchronized endpoint hooks; every three labels give Hamiltonian five-set fans at both ends of Q; and any four chosen deletion paths must contain a relative-order disagreement, hence a reversed edge, reversing tight triple, or tight cycle inside C. Thus a side can be frozen to one omission label only from order six onward.

## Body

# Small deletion sides generate synchronized omission families

Let H be a minimum counterexample and let

H-x = P | Q

be an exact two-path cover. Assume 3<=|P|<=5 and put

C = V(P) union {x}.

Let

G = { y in C : H[C-{y}] is Hamiltonian }.

Then:

1. H[C] is non-Hamiltonian.
2. x belongs to G.
3. |G|>=4.
4. For every y in G and every Hamilton path R_y on C-{y},

   H-y = R_y | Q

   is an exact two-path cover.
5. Writing Q=(q_0,...,q_s), every y in G satisfies the four synchronized endpoint hooks

   (q_1,q_0,y),
   (q_2,y,q_0),
   (y,q_s,q_{s-1}),
   (q_s,y,q_{s-2})

   tight.
6. For every three distinct a,b,c in G, both five-sets

   {q_0,q_2,a,b,c}
   and
   {q_{s-2},q_s,a,b,c}

   are Hamiltonian.
7. Choose any four distinct labels D subseteq G, and for each d in D choose any Hamilton path R_d on C-{d}. Then the four paths cannot be pairwise compatible on their common vertices. Hence some pair R_d,R_e has different relative order on common vertices. Consequently, inside C there is at least one of:
   - a reversed common ordered edge;
   - a tight triple reversing an ordered edge at an intersection;
   - a vertex-simple tight cycle.

Proof.

If C were Hamiltonian, a Hamilton path on C together with Q would be a spanning two-cover of H, impossible. Thus C is non-Hamiltonian. Since P itself is a Hamilton path on C-{x}, one has x in G.

It remains to bound |G|. There are three cases.

- If |P|=3, then |C|=4 and every three-vertex boundary tournament is Hamiltonian. Hence every vertex deletion of C is Hamiltonian, so |G|=4.
- If |P|=4, then |C|=5. The small-set theorem says that a non-Hamiltonian five-set has at most one non-Hamiltonian four-vertex deletion. Hence at least four deletions are Hamiltonian, so |G|>=4.
- If |P|=5, then |C|=6. The four-of-six theorem says that every six-set has at least four Hamiltonian five-subsets. Hence again |G|>=4.

Now fix y in G and a Hamilton path R_y on C-{y}. Since C and Q partition V(H), the two paths R_y and Q are disjoint and cover H-y. Thus H-y=R_y|Q is an exact two-path cover.

Every component of a deletion two-cover in a minimum counterexample has order at least three, so Q=(q_0,...,q_s) has s>=2. Apply endpoint-hook forcing to the fixed component Q in the cover H-y=R_y|Q, with omitted vertex y. This gives exactly

(q_1,q_0,y),
(q_2,y,q_0),
(y,q_s,q_{s-1}),
(q_s,y,q_{s-2})

tight, for every y in G.

Now take distinct a,b,c in G. The three triples

(q_2,a,q_0), (q_2,b,q_0), (q_2,c,q_0)

are tight. By the small-set theorem that three common-endpoint triples force a Hamilton five-path, {q_0,q_2,a,b,c} is Hamiltonian. Applying the same theorem to

(q_s,a,q_{s-2}), (q_s,b,q_{s-2}), (q_s,c,q_{s-2})

shows that {q_{s-2},q_s,a,b,c} is Hamiltonian.

Finally choose four distinct labels D subseteq G and Hamilton paths R_d on C-{d}. Suppose all four were pairwise compatible on their intersections. Apply the compatible-cover gluing theorem to the boundary tournament H[C], with q=1 and deletion-label set D. Since |D|=4=max(4,q+2), the four compatible one-path deletion covers would glue to a Hamilton path of C. This contradicts the already proved non-Hamiltonicity of C. Hence some pair R_d,R_e disagrees in relative order on common vertices. The reversed-order theorem for two tight paths then gives a reversed common ordered edge, a reversing tight triple, or a vertex-simple tight cycle inside C.

Therefore any deletion-cover component P of order at most five produces at least four distinct omission labels while the opposite component Q remains fixed. All labels carry the same four Q-end hook orientations; every triple of labels generates Hamiltonian five-sets at both ends of Q; and every choice of four deletion orders contains explicit order disagreement inside the small enlarged support.

Call the component P frozen at x if x is the only vertex y of C=P union {x} for which C-{y} is Hamiltonian. The theorem shows that a frozen component must have order at least six. Hence if both components P,Q of H-x=P|Q are frozen at x, then |P|,|Q|>=6 and therefore

|V(H)|=|P|+|Q|+1>=13.

For the one-defect reconfiguration route, orders three, four, and five therefore cannot be terminal merely because omission-label exchange runs out: they automatically carry a four-label fixed-complement family, dense Hamiltonian five-set fans at both ends of the complementary path, and unavoidable internal order-disagreement data.