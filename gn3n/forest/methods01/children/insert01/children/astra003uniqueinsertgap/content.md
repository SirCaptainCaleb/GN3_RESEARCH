# The neutral two-label insertion residue has unique equal-or-adjacent insertion gaps

## Statement

Let B be a displayed tight path and x,y two exterior vertices that are each insertable into B. If either x or y has two distinct successful insertion positions, then the two corresponding Hamilton paths on the same enlarged support have relative-order disagreement. Hence, in any branch with no relative-order disagreement and no simultaneous separated insertion, each label has a unique successful insertion position. By astra003twoinsertlocal the two unique positions differ by at most one. Thus the fully order-neutral residue consists only of two labels with either the same unique insertion gap or two adjacent unique insertion gaps.

## Body

Suppose x has two distinct successful insertion positions i<j. Let P_i and P_j be the tight Hamilton paths on V(B) union {x} obtained by inserting x into the displayed order of B at positions i and j. Choose any old vertex b lying strictly after position i and at or before position j; such a vertex exists because i<j. In P_i the vertex x occurs before b, while in P_j it occurs after b. Thus P_i and P_j order the common pair {x,b} differently, which is relative-order disagreement. The same argument applies to y. Therefore absence of relative-order disagreement forces each insertion set I_x,I_y to be a singleton. If there is also no simultaneous separated insertion, astra003twoinsertlocal says every cross-distance between the insertion sets is at most one; for singleton sets this says their unique positions are equal or adjacent.