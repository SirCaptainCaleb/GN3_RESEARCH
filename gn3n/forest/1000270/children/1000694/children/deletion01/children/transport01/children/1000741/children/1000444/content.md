# A minimum-side endpoint deletion has only direct crossing, support-compatible restoration, or one rigid two-crossing block configuration

## Statement

Let H be a minimum counterexample, and let mu be the minimum smaller-component order among all two-covers of one-vertex deletions. Let H-y=R|Q be a deletion two-cover with |R|=mu<=|Q|, and let z be an endpoint of the displayed path R. Put A=V(R)-{z}. Choose any two-cover T of H-z.

Then at least one of the following holds.

(1) Direct crossing: T contains an ordinary path edge joining A to V(Q).

(2) Support-compatible restoration: T has support partition (A union {y}) | V(Q), with A union {y} Hamiltonian. If the Hamilton order on its A-vertices disagrees with the inherited order R-z, explicit order disagreement is present. Otherwise either y is an endpoint, giving a clean same-order omission swap replacing omitted label y by z, or y is internal and deleting y splits the varying component into exactly two inherited-order A-blocks.

(3) Rigid two-crossing block configuration: T has exactly two crossing edges across the partition A | V(Q) | {y}; both are incident with y; A occurs as one intact T-block; V(Q) splits into exactly two T-blocks, one of which is an entire T-component and the other of which is joined through y to A. Thus, up to reversing the mixed component, T has block form
Q_1 | (Q_2, y, A)
or
Q_1 | (A, y, Q_2),
where Q_1,Q_2 are nonempty Q-blocks. If the displayed orders within these blocks disagree with the inherited R,Q orders, explicit order disagreement is already present.

In particular, probing an endpoint of a globally minimum deletion side cannot produce an arbitrary support-incompatible cover: absent direct crossing/order disagreement it is either a support-compatible endpoint/internal restoration or one rigid two-crossing block configuration with the entire (mu-1)-vertex remainder of the minimum side kept intact.

## Body

Let Pi={A,V(Q),{y}} and let t be the number of ordinary edges of T joining different Pi-classes.

The three classes are nonempty Hamiltonian sets: A is the inherited endpoint truncation of R, Q is the displayed path, and {y} is a singleton. By coversurg01 Section 6, since T has two components,
t >= 1+1+1-2 = 1.

By the definition of mu, every component of every deletion two-cover has order at least mu. Hence A, of order mu-1, cannot itself be a component of T; the singleton {y} cannot be a component either.

If T contains an A-Q edge, outcome (1) holds. Assume henceforth that there is no A-Q edge. Then every cross-class edge is incident with y, so t<=deg_T(y)<=2. Thus t is 1 or 2.

Suppose t=1. Cutting the unique crossing edge produces exactly three monochromatic blocks, hence one block in each Pi-class. Contracting the blocks gives one edge and one isolated vertex. The isolated class cannot be A, since |A|=mu-1, and cannot be {y}. Therefore Q is an entire T-component and the other component is a Hamilton path on A union {y}. Since there is only one cross edge, y is an endpoint of that component and A is one T-block. This is the endpoint subcase of outcome (2), with order disagreement recorded if the A-order differs from the inherited order.

Now suppose t=2. Cutting the two crossing edges produces four monochromatic blocks. Since {y} contributes one block, the block counts of A and Q sum to three, so exactly one of A,Q splits into two blocks. Both crossing edges are incident with y.

If y is adjacent to two A-blocks, then A has exactly two blocks and Q one; the mixed component is A_1-y-A_2, hence Hamiltonian on A union {y}, while Q is the other component. This is the internal-restoration subcase of outcome (2). If the A-vertices do not retain their inherited relative order, order disagreement is already present.

If y is adjacent to two Q-blocks, then Q has two blocks and A one, leaving A as the other entire T-component. This is impossible because |A|=mu-1.

It remains that y is adjacent to one A-block and one Q-block. If A were the split class, its second block would be an entire T-component of order strictly less than mu, impossible. Therefore A is one intact block and Q is the split class. The Q-block not incident with y is one T-component; the other Q-block, y, and A form the mixed component. This is exactly outcome (3).
