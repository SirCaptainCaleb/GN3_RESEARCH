# A block-count identity

Let \(A,B,C\) be disjoint vertex sets and let \(T\) be a two-cover of their union. Decompose the paths of \(T\) into maximal nonempty blocks contained in one of \(A,B,C\). If \(b_A,b_B,b_C\) are the corresponding block counts and \(t\) is the number of edges of the paths of \(T\) whose endpoints lie in different sets among \(A,B,C\), then
\[
t=b_A+b_B+b_C-2.
\]

Indeed, deleting those \(t\) edges from two paths produces \(t+2\) blocks. Hence \(t\ge1\). If \(t=1\), each displayed set occurs as one block. If \(t=2\), the block counts are \((2,1,1)\) in some order. If the two blocks of the split set lie in different paths of \(T\), an edge of any displayed Hamilton path on that set has endpoints in different paths of \(T\). If the two blocks lie in the same path of \(T\), a nonempty block from another displayed set lies between them.
