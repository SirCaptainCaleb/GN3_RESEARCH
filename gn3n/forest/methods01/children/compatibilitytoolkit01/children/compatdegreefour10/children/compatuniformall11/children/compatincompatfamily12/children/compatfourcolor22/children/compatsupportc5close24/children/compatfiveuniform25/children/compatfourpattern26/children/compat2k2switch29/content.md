# The exceptional 2K2 pattern has a core-disagreement or paired-switch normal form

## Statement

Let F_1,F_2,F_3,F_4 be deletion covers for distinct labels a_1,a_2,a_3,a_4, with nonempty common core W=V(H)-{a_1,a_2,a_3,a_4}. Suppose the four covers are pairwise incompatible and their support-compatibility graph is exactly the matching {12,34}. Then either the support partitions induced by F_1,F_2 on W differ from the common support partition induced by F_3,F_4 on W, or all four covers induce one common partition R|S on W and at least one of the following holds: (i) both a_1 and a_2 switch core class between the {F_1,F_2} side where they occur and the pair F_3,F_4; (ii) both a_3 and a_4 switch core class between the pair F_1,F_2 and the {F_3,F_4} side where they occur.

## Body

# Proof

The blue edges are F_1F_2 and F_3F_4. Thus F_1,F_2 induce one common support partition on W, and F_3,F_4 induce one common support partition on W.

If these two W-partitions differ, the first alternative holds. Assume they agree, and denote the common partition by R|S. Fix r in W and encode every surviving special label by its class relative to r.

Because F_1,F_2 are support-compatible, the labels a_3 and a_4, which survive in both, have fixed classes across F_1,F_2. Because F_3,F_4 are support-compatible, the labels a_1 and a_2 have fixed classes across F_3,F_4.

Define four switch indicators:
A=1 if a_1 has different classes in F_2 and F_3,F_4;
B=1 if a_2 has different classes in F_1 and F_3,F_4;
C=1 if a_3 has different classes in F_1,F_2 and F_4;
D=1 if a_4 has different classes in F_1,F_2 and F_3.

Every cross pair is support-incompatible. Inspecting the labels surviving in each common domain gives:
F_1,F_3: B or D;
F_1,F_4: B or C;
F_2,F_3: A or D;
F_2,F_4: A or C.

Hence
(B or D)(B or C)(A or D)(A or C)
must hold. The first two factors equal B or (C and D), while the last two equal A or (C and D). Their conjunction is therefore
(A and B) or (C and D).

Thus either A=B=1, meaning both a_1,a_2 switch across the matching, or C=D=1, meaning both a_3,a_4 switch across it; both may occur.

So the 2K_2 exception has only two sources: disagreement already present on the common core, or a paired two-label support switch across one side of the matching.
