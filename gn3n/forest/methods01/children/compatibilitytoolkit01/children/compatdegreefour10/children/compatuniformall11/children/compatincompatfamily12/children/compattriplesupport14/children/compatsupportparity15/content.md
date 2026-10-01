# The three-label support-switch configuration has an odd split parity

## Statement

Assume the second branch of compattriplesupport14: the common core W has a fixed support partition R|S, and each of a,b,c switches core class between the two deletion covers that contain it. For x in {a,b,c}, call F_x split when its two surviving special labels lie in different core classes. Then the number of split covers among F_a,F_b,F_c is odd. Hence, up to interchanging R,S and relabeling a,b,c, exactly one of two patterns occurs: (i) all three covers are split, so each cover places one surviving special label with R and the other with S; or (ii) exactly one cover is split, while the other two place their two surviving special labels together, one pair with R and the other pair with S.

## Body

# Proof

Encode membership in the two fixed core classes R,S by bits 0,1.

Let
A be the class of b in F_a,
B the class of c in F_a,
C the class of a in F_b.

Because each special label switches class between the two covers that contain it, we then have

class of b in F_c = 1-A,
class of c in F_b = 1-B,
class of a in F_c = 1-C.

Let s_a,s_b,s_c be the split indicators of F_a,F_b,F_c, where s_x=1 exactly when the two surviving special labels lie in different classes.

Then over F_2,

s_a = A+B,
s_b = C+(1-B) = 1+B+C,
s_c = (1-C)+(1-A) = A+C.

Therefore

s_a+s_b+s_c = 1 mod 2.

So an odd number of the three covers are split: either exactly one or all three.

If all three are split, each deletion cover places its two surviving special labels on opposite sides of R|S; this is the cyclic split pattern.

If exactly one is split, say F_c after relabeling, then F_a places b,c together in one core class. Since c switches class from F_a to F_b and a switches between F_b,F_c while b switches between F_a,F_c, the nonsplit pair in F_b necessarily lies together in the opposite core class. Interchanging R and S if needed gives the stated canonical pattern.

Thus the three-label support-switch residue has only two parity types.
