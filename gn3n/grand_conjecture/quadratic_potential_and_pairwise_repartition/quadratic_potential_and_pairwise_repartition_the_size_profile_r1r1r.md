# The size profile \(\{r+1,r+1,r\}\)

**Lemma 4.** Suppose a minimum-\(\Phi\) level in one component of \(\mathcal R(H)\) has size multiset \(\{r+1,r+1,r\}\), \(r\ge3\). Assume that an equal-\(\Phi\) pairwise repartition never gives a two-cover, a strict decrease of \(\Phi\), an order disagreement, or a Hamiltonian support of order four or five whose complement has path-cover number two. Then there are disjoint tight paths \(A,B,C\), each of order \(r\), and distinct vertices \(x,y\) such that both \(x\) and \(y\) extend the same end of each of \(A,B,C\).

For every two-cover \(T\) of
\[
H-\{x,y\}=A\cup B\cup C,
\]
at least one of the following holds:
1. a path of \(T\) and one of \(A,B,C\) have an order disagreement;
2. \(T\) has at least three edges whose endpoints lie in different sets among \(A,B,C\);
3. an edge of one of \(A,B,C\) has endpoints in different paths of \(T\);
4. one path of \(T\) contains two nonempty blocks from one of \(A,B,C\) separated by a nonempty block from another.

**Proof.** At this size profile, an equal-\(\Phi\) repartition can only transfer one endpoint from a path of order \(r+1\) to the path of order \(r\). Under the hypotheses, both large paths admit such a transfer, and the transfers use the same end of the receiving path; opposite ends or different inherited orders give one of the excluded conclusions.

Write one state as
\[
(x,A)\mid B\mid(y,C),
\]
with all chosen transfers at the initial end. After one transfer, its reverse is one of the two available equal-\(\Phi\) moves, so choosing the other move forces
\[
x:A\to B,\quad y:C\to A,\quad x:B\to C,\quad
y:A\to B,\quad x:C\to A,\quad y:B\to C.
\]
After six moves the support partition returns to the initial state. The first three states and their unused reverse moves show that both \(x\) and \(y\) initial-extend each of \(A,B,C\). The terminal-end case is symmetric.

Now let \(T\) be a two-cover of \(A\cup B\cup C\). If there is an order disagreement, (1) holds. Otherwise let \(t\) be the number of edges of \(T\) joining different cores. If \(t=1\), the block-count identity gives one block in each core. One path of \(T\) is the concatenation of two whole cores and the other is the third core. Prepending \(x\) to the first path and \(y\) to the second gives a two-cover of \(H\), a contradiction. Thus \(t\ge2\). If \(t\ge3\), (2) holds. If \(t=2\), Section 3 gives (3) or (4). \(\square\)
