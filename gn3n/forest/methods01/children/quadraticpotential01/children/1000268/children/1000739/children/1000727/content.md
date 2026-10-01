# Same-isolated unique-crossing endpoint probes force relative-order disagreement

## Statement

Let H be a minimum counterexample with an all-equal spanning three-cover A|B|C, where A=(a_1,...,a_r) and r>=4. Suppose deletion covers of H-a_1 and H-a_r each have exactly one crossing relative to the inherited partition, and both isolate the same opposite block B. Then the two corresponding near-merge Hamilton paths on (A-{a_1}) union C and (A-{a_r}) union C expose relative-order disagreement on their common vertices.

## Body

Let L_1 be the Hamilton path on (A-{a_1}) union C in the deletion cover of H-a_1, and L_r the Hamilton path on (A-{a_r}) union C in the deletion cover of H-a_r. Cutting the unique crossing in each gives one A-block and one C-block. If either L_1 or L_r already reorders one of its inherited displayed blocks, we are done. Assume both preserve the displayed relative order on A and C. Then L_1 has one of the block orders (A-{a_1}),C or C,(A-{a_1}). The first is impossible: since r>=4, prepending a_1 to the displayed initial block (a_2,...,a_r) preserves tightness at the new first triple (a_1,a_2,a_3), so a_1 followed by L_1 is a Hamilton path on A union C; together with the displayed path B this two-covers H. Hence L_1 has order C,(a_2,...,a_r). Similarly L_r cannot have block order C,(A-{a_r}), because appending a_r to the final displayed block (a_1,...,a_{r-1}) would Hamiltonize A union C and again two-cover H with B. Thus L_r has order (a_1,...,a_{r-1}),C. The common vertex set of L_1 and L_r contains C and the nonempty interior A^o={a_2,...,a_{r-1}}. Every c in C precedes every a in A^o in L_1, while every a in A^o precedes every c in C in L_r. Hence the two Hamilton orders disagree on every such pair.
