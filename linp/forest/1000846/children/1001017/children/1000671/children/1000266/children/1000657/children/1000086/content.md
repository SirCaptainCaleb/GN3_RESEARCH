# Unblocked shared-last-vertex extension raises φ by two

## Statement

Let e and f be distinct nonspecial edges of a linear 3-graph sharing a vertex v. Assume φ(e,v)=φ(e) and φ(f,v)=φ(f), and that v is not the unique entrance vertex of either edge. Let P be a longest path with last edge e and last vertex v. If f meets P only at v, then φ(f)>=φ(e)+2.

## Body

Proof. Append f to P. Because f meets P only at v and v is the last vertex of P, the resulting sequence is a linear path of length φ(e)+1 with last edge f, entering f through v. Since f is nonspecial and v is not its unique entrance vertex, no longest path with last edge f can enter f through v. Therefore the appended path has length at most φ(f)-1. Hence φ(e)+1<=φ(f)-1, so φ(f)>=φ(e)+2.
