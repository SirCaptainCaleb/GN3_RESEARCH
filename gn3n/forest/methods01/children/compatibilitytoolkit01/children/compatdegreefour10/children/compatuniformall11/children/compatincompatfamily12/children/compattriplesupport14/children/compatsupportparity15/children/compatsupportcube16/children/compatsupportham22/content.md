# The two support-switch parity types force explicit Hamiltonian core enlargements

## Statement

In the common-core support-switch branch with W=R disjoint-union S and special labels a,b,c, the two parity types of compatsupportparity15 have the following Hamiltonian-support normal forms after relabeling R,S and a,b,c. (I) If all three deletion covers are split, then each of R union {a}, R union {b}, R union {c}, S union {a}, S union {b}, S union {c} is Hamiltonian. (II) If exactly one deletion cover is split, then one may label so that R, S, R union {a}, S union {b}, R union {b,c}, and S union {a,c} are Hamiltonian. These conclusions use only the three deletion-cover support partitions and do not assert anything about the two missing cube corners.

## Body

# Proof

Use the bit convention of compatsupportcube16: bit 0 means the corresponding special label lies with R and bit 1 means it lies with S.

Each coordinate edge of the cube comes from one deletion cover F_x. Along that edge the omitted label x is absent, while the fixed positions of the other two labels specify the two Hamiltonian path supports of F_x. Therefore the two supports obtained from the fixed coordinates, before restoring x anywhere, are Hamiltonian.

## All-three-split type

After relabeling, the three deletion-cover edges are

(*,0,1), (1,*,0), (0,1,*).

For F_a, the fixed labels place b with R and c with S, so

R union {b}  and  S union {c}

are Hamiltonian.

For F_b, the fixed labels place c with R and a with S, so

R union {c}  and  S union {a}

are Hamiltonian.

For F_c, the fixed labels place a with R and b with S, so

R union {a}  and  S union {b}

are Hamiltonian.

This gives all six one-label core enlargements.

## Exactly-one-split type

After relabeling, the three edges are

(*,0,0), (1,*,1), (0,1,*).

For F_a, both b,c lie with R, so its two Hamiltonian supports are

R union {b,c}  and  S.

For F_b, both a,c lie with S, so its supports are

R  and  S union {a,c}.

For F_c, a lies with R and b with S, so its supports are

R union {a}  and  S union {b}.

These are exactly the six Hamiltonian sets listed in (II).

No claim about longest-path deficit under adding or deleting a vertex is used.