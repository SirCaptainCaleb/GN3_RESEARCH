# A three-label support-switch triple occupies six vertices of the one-defect cube

## Statement

Let H be a minimum counterexample and assume the common-core support-switch branch of compattriplesupport14 with fixed core partition R|S and special labels a,b,c. For each deletion cover F_x, restore the omitted label x once to each of its two path supports. The resulting six bipartitions are D=1 states. Identifying a full bipartition with the bit vector in {0,1}^3 that records whether each of a,b,c lies with R or with S, these six states are six distinct vertices of the 3-cube, and the two missing vertices are antipodal. In the all-three-split parity type, the missing pair is 000 and 111 after choosing the class labels suitably. In the exactly-one-split type, the missing antipodal pair has Hamming weights 1 and 2.

## Body

# Proof

By d8dce2799f24, every deletion cover gives two D=1 states by restoring its omitted label to either path support. Thus F_a,F_b,F_c produce six D=1 bipartitions.

Encode membership with R by 0 and with S by 1 for the special labels a,b,c. As in compatsupportparity15, write

A = class of b in F_a,
B = class of c in F_a,
C = class of a in F_b.

The switching condition gives

class of b in F_c = 1-A,
class of c in F_b = 1-B,
class of a in F_c = 1-C.

Therefore the two restorations of F_a are the cube edge

(*,A,B),

the two restorations of F_b are the edge

(C,*,1-B),

and the two restorations of F_c are the edge

(1-C,1-A,*).

We claim these three coordinate edges are pairwise vertex-disjoint. If an endpoint of the first and second edges coincided, then its fixed c-coordinate would require B=1-B, impossible. Similarly, an intersection of the first and third would require A=1-A, and an intersection of the second and third would require C=1-C. Thus the three edges contain six distinct cube vertices.

A 3-cube has eight vertices, so exactly two are missing. Since each of the three coordinate directions occurs in exactly one selected edge, every coordinate has three selected vertices with bit 0 and three with bit 1. Hence among the two missing vertices, each coordinate occurs once as 0 and once as 1. The missing vertices are therefore antipodal.

It remains to identify their form in the two parity types.

If all three deletion covers are split, relabel R,S and a,b,c so that F_a has b with R and c with S. The odd-split relations then give the three edges

(*,0,1), (1,*,0), (0,1,*),

whose six endpoints are all cube vertices except 000 and 111.

If exactly one deletion cover is split, choose labels so that F_c is split and interchange R,S if necessary so F_a places b,c with R. Then the three edges are

(*,0,0), (1,*,1), (0,1,*),

whose missing vertices are 001 and 110, an antipodal pair of Hamming weights 1 and 2. Any other labeling is equivalent by cube-coordinate permutation and global bit complement.

Thus every common-core support-switch triple determines three disjoint coordinate edges in the one-defect cube and leaves precisely one antipodal pair of D=1 states unrealized by the three deletion covers.