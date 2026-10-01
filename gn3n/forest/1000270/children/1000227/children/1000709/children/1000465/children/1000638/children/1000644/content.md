# Trapped order-thirteen states force radius-three coupled escapes and alternating reconfiguration squares

## Statement

Let H be a minimum counterexample of order thirteen with mu=6, and let V(H)=R disjoint-union S be a minimum D=1 state with |R|=7, |S|=6, d(R)=1, d(S)=0, trapped for alternating single-vertex transfers. If G={r in R:H[R-{r}] is Hamiltonian}, then good R-deletions have the canonical cover (R-{r})|S, while every bad R-deletion and every S-deletion has only fully mixed exact 6|6 covers. Every S-deletion cover has, up to swapping components, support type (5R+1S)|(2R+4S) or (4R+2S)|(3R+3S); restoring the deleted S-vertex to the R-heavier component gives a new D=1 support at Johnson distance respectively 2 or 3 from R, and the six S-labels yield at least two distinct coupled escapes. Moreover, any crosswise exact-two-crossing endpoint cover in this shell yields a D=1 support at Johnson distance at most three; with the smaller endpoint block of size s in {1,2}, its two restored states and every canonical good-label transfer state form alternating radius-three/single-transfer four-cycles, and the far restored state is adjacent in Gamma to the entire good-label transfer clique.

## Body

# Trapped order-thirteen states force radius-three coupled escapes and alternating reconfiguration squares

Work in a minimum counterexample H of order thirteen with mu=6.

## 1. The deletion shell of a single-transfer trap

Let
V(H)=R disjoint-union S,
with |R|=7, |S|=6, d(R)=1, and d(S)=0, and suppose R|S is trapped for the alternating single-vertex-transfer dynamics. Thus S is Hamiltonian, R is non-Hamiltonian, and
D={r in R : H[R-{r}] is Hamiltonian}
is nonempty.

The universal order-thirteen shell gives component orders 6,6 for every exact deletion two-cover, and no seven-set is Hamiltonian. The trapping characterization says that for every r in D, the seven-set S union {r} has r as its unique Hamiltonian deletion; equivalently, for every s in S,
H[(S-{s}) union {r}]
is non-Hamiltonian.

For r in D, both R-{r} and S are Hamiltonian, so
(R-{r}) | S
is the canonical exact cover of H-r.

Now let r be in R-D and let H-r=A|B be any exact two-cover. If one component were contained in R-{r}, it would equal R-{r}, which is non-Hamiltonian. If one component were contained in S, it would equal S and force the other component to be R-{r}, again impossible. Hence both components meet both inherited sides.

Next fix s in S and let H-s=A|B be any exact two-cover. No component can lie in S-{s}, which has only five vertices. If a component lies in R, it must be R-{r} for some r in R. For r not in D this support is non-Hamiltonian. For r in D the complementary support is (S-{s}) union {r}, which is non-Hamiltonian by trapping. Thus every S-deletion cover is also fully mixed.

Write k=|A intersect R|. Since both components have order six,
|A intersect (S-{s})|=6-k,
|B intersect R|=7-k,
|B intersect (S-{s})|=k-1.
Full mixing gives 2<=k<=5, and swapping A,B replaces k by 7-k. Therefore, up to swapping the components, precisely two support types remain:
(5R+1S)|(2R+4S), called shallow, and
(4R+2S)|(3R+3S), called deep.

## 2. Every such trap has coupled exits within radius three

Fix s in S and an exact cover H-s=A|B, choosing A to be the R-heavier component. Since A is Hamiltonian, if A union {s} were Hamiltonian then a Hamilton path on A union {s} together with B would give a spanning two-path cover of H. Hence A union {s} is non-Hamiltonian. It contains the Hamiltonian six-set A, so its longest-path deficit is exactly one, while B remains Hamiltonian. Thus
(A union {s}) | B
is another D=1 state.

Its deficient support R'=A union {s} satisfies
|R intersect R'|=|R intersect A|.
Therefore
d_J(R,R')=7-|R intersect A|,
which is 2 in the shallow case and 3 in the deep case.

Choose one exact cover for each of the six labels s in S. Each resulting deficient support R'_s contains its label s and contains at most three vertices of S. Consequently one fixed support can occur for at most three labels, so the six labels produce at least two distinct deficient supports.

Thus a trap for alternating single-vertex transfers is never trapped for coupled D<=1 reconfiguration: it has at least two coupled exits at Johnson radius at most three. If no radius-two exit occurs through an S-deletion, then all S-deletion covers are deep, so the residual obstruction is exactly the all-deep radius-three shell.

## 3. Crosswise endpoint covers are explicit radius-three moves

Now let V(H)=X disjoint-union Q be any D=1 state in the same order-thirteen shell, with |X|=7, |Q|=6, X non-Hamiltonian with a Hamiltonian six-deletion, and Q Hamiltonian. Fix a Hamilton order Q=(q_0,...,q_5). Suppose an exact cover
H-q_0=C_1|C_2
has exactly two crossings across (Q-{q_0})|X and is in the crosswise four-block case.

Put B=Q-{q_0}. Cutting the two crossing edges gives nonempty B-blocks B_1,B_2 and nonempty X-blocks X_1,X_2, where C_i uses B_i union X_i. If |B_1|=r, then 1<=r<=4,
|B_2|=5-r,
|X_1|=6-r,
|X_2|=1+r.

Restoring q_0 to either component of an exact deletion two-cover gives a D=1 state. Hence the deficient supports
R_1=V(C_1) union {q_0},  R_2=V(C_2) union {q_0}
are valid D=1 supports. Since q_0 and the B-blocks lie outside X,
|R_1 intersect X|=6-r,
|R_2 intersect X|=1+r,
and therefore
d_J(R_1,X)=r+1,
d_J(R_2,X)=6-r.
For r=1,2,3,4 the smaller of these distances is respectively 2,3,3,2. Thus every crosswise exact-two-crossing endpoint cover yields a D=1 neighbor of X in Gamma at radius at most three; radius two occurs exactly for a 1+4 split of B, and otherwise the nearest restored state is at radius three.

## 4. Alternating squares and the good-label clique

Relabel the crosswise components so that the smaller B-block has size
s=min{r,5-r} in {1,2}.
Let C_- use that s-vertex B-block and C_+ the other block, and put
R_-=V(C_-) union {q_0},
R_+=V(C_+) union {q_0}.
The preceding calculation gives d_J(X,R_-)=s+1<=3, so X--R_- is an edge of Gamma.

The two marked D=1 states R_-|C_+ and C_-|R_+ come from the same exact deletion cover. Deleting q_0 from R_- leaves C_-, and transferring q_0 to the opposite Hamiltonian side C_+ produces R_+. Hence R_- and R_+ are joined by the legal single-transfer move labelled q_0.

Let
D_X={t in X : H[X-{t}] is Hamiltonian}.
For every t in D_X, the canonical deletion cover
H-t=(X-{t})|Q
gives the transfer state T_t=Q union {t}. Thus X and T_t are joined by the legal single-transfer move labelled t.

The Q-part of R_+ has order 6-s and its X-part, call it Y_+, has order 1+s. Hence
|R_+ intersect T_t|=(6-s)+1_{t in Y_+},
so
d_J(R_+,T_t)=1+s-1_{t in Y_+}.
This is s when t is in Y_+ and s+1 otherwise, always at most three. Therefore R_+--T_t is an edge of Gamma for every t in D_X.

Finally, for distinct t,u in D_X, the supports T_t and T_u intersect exactly in Q, so their Johnson distance is one. The transfer states {T_t:t in D_X} form a clique in Gamma, and R_+ is adjacent to every member of it. Consequently
{R_+} union {T_t:t in D_X}
is a clique in Gamma and deg_Gamma(R_+)>=|D_X|.

For every good label t this gives the alternating four-cycle
X --Gamma-- R_- --transfer(q_0)-- R_+ --Gamma-- T_t --transfer(t)-- X.

Thus the order-thirteen single-transfer trapping shell has a unified coupled geometry: the trap first forces mixed deletion covers, those covers yield multiple radius-at-most-three D=1 exits, and every crosswise endpoint two-crossing configuration supplies explicit alternating squares tied to the full good-label transfer clique.
