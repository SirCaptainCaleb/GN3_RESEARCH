# Unused terminal colors are repelled from both ends of a zero-slack witness

## Statement

In the zero-slack witness of f3a692e51efb, let y be a terminal port different from the entrance x and let d be an unused connector color. If the d-colored edge {y,d,w} has w in the first forest triple T_1, then nonspeciality forces w to be the port of T_1 used by C_1. Hence at most one unused-color y-edge meets T_1. Together with f3a692e51efb, at most two unused-color y-edges meet T_1∪T_{c-1}; therefore at least k/3-1 of the k/3+1 unused-color y-edges have X-contact in the interior triples T_2,...,T_{c-2}.

## Body

Let f={y,d,w} with d unused by the alternating witness and w in T_1.

Write p_out for the port of T_1 used by C_1. Suppose w!=p_out. Then w is either the other connector-free port or the other last vertex of T_1.

Orient the old precursor segment backward from T_{c-1} through C_{c-2},...,C_1,T_1, and then append f,e. Since w!=p_out, f is disjoint from C_1 and from every earlier connector, while the unused color d avoids all connector D-vertices.

This path uses the c-1 forest triples T_1,...,T_{c-1}, the c-2 connectors C_1,...,C_{c-2}, and f,e, for a total
(c-1)+(c-2)+2=2c-1
edges. It ends in e through y, contradicting nonspeciality.

Thus w=p_out, and simplicity of G allows at most one unused-color edge through y to hit that vertex.

By f3a692e51efb, at most one unused-color y-edge meets the penultimate triple T_{c-1}. Since the witness uses c-1 colors out of k, the number of unused colors is
k-(c-1)=k/3+1.
Therefore at least
(k/3+1)-2=k/3-1
unused-color y-edges have their X-contact in one of the interior triples T_2,...,T_{c-2}.