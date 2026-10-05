# Aligned two-camp polarity gives a two-cover

Solve the exact model suggested by the disconnected mediator-swap branch: both parity mediator families split into aligned T versus reverse(T) camps.

Let A=U union W and B=C union D with |U|=|C| and |W|=|D|. Assume there are tournaments T on A and S on B such that T_b[A]=T for b in C, T_b[A]=reverse(T) for b in D, T_a[B]=S for a in U, and T_a[B]=reverse(S) for a in W.

Choose directed Hamilton paths in T[U], reverse(T)[W], S[C], and reverse(S)[D] by Redei. Interleave the concatenated A-order U then W with the concatenated B-order C then D.

Every odd status strictly before the common block boundary is tight because its mediator lies in C and its A-edge is a T-edge; every odd status strictly after is tight because its mediator lies in D and its A-edge is a reverse(T)-edge. Only the odd status at the U/W boundary is undetermined.

Symmetrically every even status strictly before the boundary is tight and every even status strictly after is tight; only the even status at the C/D boundary is undetermined.

Thus the full status word has at most two consecutive undetermined/non-tight positions. Their defect intervals have a common cut position. By the defect-interval Helly criterion, the order yields a spanning two-cover.

Therefore aligned exact two-camp polarity on both parity systems implies pc(H)<=2.

This is the exact model approximated by the disconnected robust-swap branch, so that branch should be treated as a stability problem around a solved configuration.
