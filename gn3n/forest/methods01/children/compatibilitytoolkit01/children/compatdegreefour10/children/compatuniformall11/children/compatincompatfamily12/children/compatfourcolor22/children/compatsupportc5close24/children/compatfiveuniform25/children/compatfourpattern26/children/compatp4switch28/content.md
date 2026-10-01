# The exceptional P4 pattern has a two-switch support normal form

## Statement

Let F_1,F_2,F_3,F_4 be deletion covers for distinct labels a_1,a_2,a_3,a_4, with nonempty common core W=V(H)-{a_1,a_2,a_3,a_4}. Suppose the four covers are pairwise incompatible and their support-compatibility graph is the path 1-2-3-4. Then all four covers induce one common support partition R|S on W. Relative to this partition, a_1 has the same core class in F_2,F_3,F_4 and a_4 has the same core class in F_1,F_2,F_3; meanwhile a_2 lies in opposite core classes in F_1 versus F_3,F_4, and a_3 lies in opposite core classes in F_1,F_2 versus F_4. Consequently the support incompatibilities of F_1,F_3 and F_2,F_4 are forced respectively by switches of a_2 and a_3, while F_1,F_4 contains both switches simultaneously.

## Body

# Proof

Write the blue support-compatible path as
F_1 -- F_2 -- F_3 -- F_4.

Because support-compatible consecutive covers agree on their common domains, their restrictions to W agree. Hence all four covers induce one common support partition R|S on W.

Fix a reference vertex r in W and encode the core class of a surviving special label by whether it lies with r.

The label a_1 occurs in F_2,F_3,F_4. Since F_2,F_3 and F_3,F_4 are support-compatible, the class of a_1 is the same in all three covers.

Similarly a_4 occurs in F_1,F_2,F_3, and support compatibility along F_1--F_2--F_3 makes its class constant in those three covers.

Now consider the red pair F_1,F_3. Their common domain is W union {a_2,a_4}. The label a_4 has the same class in both covers, and the partition on W is the same. Since F_1,F_3 are support-incompatible, the only possible support disagreement is therefore a_2. Thus a_2 lies in opposite core classes in F_1 and F_3. Compatibility of F_3,F_4 then gives the same class for a_2 in F_3 and F_4. Hence a_2 switches exactly across the first gap: F_1 versus F_3,F_4.

Likewise the red pair F_2,F_4 has common domain W union {a_1,a_3}. The label a_1 is stable, so their support incompatibility must be caused by a_3. Therefore a_3 lies in opposite classes in F_2 and F_4. Compatibility of F_1,F_2 gives the same class for a_3 in F_1 and F_2. Hence a_3 switches exactly across the second gap: F_1,F_2 versus F_4.

Finally compare F_1,F_4. Their common domain contains W,a_2,a_3. Both a_2 and a_3 have switched between these covers, so their support incompatibility contains both changes simultaneously.

Thus the P_4 pattern has a rigid two-switch normal form: the two internal deletion labels a_2,a_3 are the unique forced switch coordinates associated with the two nonadjacent red pairs.
