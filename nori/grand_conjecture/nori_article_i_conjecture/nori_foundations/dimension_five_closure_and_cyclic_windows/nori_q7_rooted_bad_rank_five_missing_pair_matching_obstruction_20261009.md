# Q7 rooted bad five-supports form a matching-two graph; ten good supports at every root

# A sharp matching obstruction for rooted rank-five failures in \(Q_7\)

Let \(V\) be a seven-element coordinate set and let \(c(F,\pi)\in\mathbb F_2\) color the **physical** ordered three-faces of \(Q_7\), with
\(c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi)\).
For a root \(x\), call a five-coordinate support \(B\) *bad at \(x\)* when **every** five-step \(B\)-geodesic from \(x\) has alternating three-window word \(010\) or \(101\). Define the simple graph
\[
 G_x=(V,E_x),\quad E_x=\{D\in\binom V2:V\setminus D\text{ is bad at }x\}.
\]
We identify the edge \(D\) with the **two directions omitted** by its bad support.

**Lemma 1 (disjoint-complement bridge).** Suppose \(D,P\in E_x\) are disjoint, and write \(T=V\setminus(D\cup P)\), so \(|T|=3\). For distinct \(a,b\in P\), distinct \(d,e\in D\), and **any** \(t,v\in T\) (including \(t=v\)),
\[
 h_x(a,b,t)+h_x(d,e,v)=1,\qquad
 h_x(a,b,t):=c(F_x(a,b,t),(a,b,t)),
\]
where \(F_x(a,b,t)\) is the ordered face with these three free coordinates and all remaining bits inherited from \(x\).

*Proof.* First take \(t\ne v\) and let \(u\) be the third member of \(T\). The five-order \((a,b,t,u,v)\) uses precisely \(V\setminus D=P\cup T\). As it is bad at \(x\), its first and third window colors agree:
\[
 h_x(a,b,t)=c(F_{x\oplus e_a\oplus e_b}(t,u,v),(t,u,v)).
\]
Complementing this physical last face and reversing its free order gives
\[
 c(F_{x\oplus e_a\oplus e_b}(t,u,v),(t,u,v))
 =1+c(F_{x\oplus e_d\oplus e_e}(v,u,t),(v,u,t)).
\]
The last face on the right is *exactly* the third window of the five-order \((d,e,v,u,t)\) from the same root \(x\): outside \(\{t,u,v\}\), its fixed bits on \(P\) are the original bits of \(x\), and its fixed bits on \(D\) are their complements. That order uses precisely \(V\setminus P=D\cup T\) and is also bad. Its first and third window colors therefore agree, yielding
\(h_x(a,b,t)=1+h_x(d,e,v)\).
For any two distinct \(t,t'\in T\), choose \(v\in T\setminus\{t,t'\}\); applying the established relation twice shows \(h_x(a,b,t)=h_x(a,b,t')\). Likewise \(h_x(d,e,v)\) is constant over \(T\). Consequently the relation holds when \(t=v\) too. The argument applies independently to either ordering of the two pairs. \(\square\)

**Theorem 2 (rooted matching obstruction).** \(G_x\) contains no matching of size three.

*Proof.* If \(A,B,C\) were three pairwise disjoint edges, there would be exactly one remaining direction \(g\in V\setminus(A\cup B\cup C)\). Fix an orientation of each of the pairs and abbreviate its first-window color \(h_x(A,g)\), \(h_x(B,g)\), \(h_x(C,g)\). Lemma 1 applied successively to the pairs \(A,B\), \(B,C\), and \(C,A\), with \(t=v=g\), gives
\[
 h_x(A,g)+h_x(B,g)
 =h_x(B,g)+h_x(C,g)
 =h_x(C,g)+h_x(A,g)=1.
\]
Adding the three equalities over \(\mathbb F_2\) yields \(0=1\). \(\square\)

**Corollary 3 (ten simultaneously good supports at every root).**
\[
 |E_x|\le 11.
\]
Consequently, for **every** root \(x\in Q_7\), at least ten of the 21 five-coordinate supports admit a genuine one-change five-step geodesic from that *same physical root*. If equality \(|E_x|=11\) holds, there is a distinguished pair \(S\subset V\) such that
\[
 E_x=\{D\in\binom V2:D\cap S\ne\varnothing\};
\]
in other words, all eleven failures omit at least one of two fixed hub directions.

*Proof.* Theorem 2 gives matching number \(\nu(G_x)\le2\). The Tutte–Berge matching identity supplies a set \(S\) with \(o(G_x-S)-|S|\ge7-2\nu(G_x)\ge3\). Thus \(|S|\le2\). If \(|S|=0\), at least three components are odd, and their total internal edge count is at most \(\binom52=10\). If \(|S|=1\), at least four odd components remain on six vertices, so internal edges total at most \(\binom32=3\), and at most six further edges meet \(S\), giving nine. If \(|S|=2\), all five vertices outside \(S\) are isolated in \(G_x-S\); there are at most \(2\cdot5+\binom22=11\) edges. Equality in the last count forces precisely every edge meeting \(S\). \(\square\)

**Sharpness: all eleven failures are simultaneously feasible in a legal coloring.**
The following self-contained finite parity certificate realizes the equality graph at root \(0\). Vertices of its constraint graph are **all 3360 actual ordered physical three-faces** of \(Q_7\). Join antipodal-reversed faces by an inequality edge; for each of the eleven supports \(B=V\setminus D\) with \(D\cap\{0,1\}\ne\varnothing\), join each pair of successive windows in each of its 120 five-orders rooted at \(0\) by an inequality edge. The certificate verifies that this entire constraint graph is bipartite. Taking its bipartition as the colors yields an actual reversal-odd coloring with all eleven supports bad at \(0\). Every face variable is physical, and the certificate checks all antipodal and rank-five equations.

~~~python
from itertools import permutations, combinations
from collections import deque
V = set(range(7))
FULL = (1 << 7) - 1
mask = lambda T: sum(1 << i for i in T)
states = [(t,s) for t in permutations(range(7),3)
          for s in range(1 << 7) if not (s & mask(t))]
idx = {w:i for i,w in enumerate(states)}
adj = [[] for _ in states]
def opposite(a,b):
    a,b=idx[a],idx[b]
    adj[a].append(b); adj[b].append(a)
for t,s in states:
    opposite((t,s),(t[::-1],(FULL ^ mask(t)) ^ s))
for D in combinations(range(7),2):
    if not (set(D) & {0,1}): continue
    B = sorted(V-set(D))
    for p in permutations(B):
        w=[];prefix=0
        for j in range(3):
            t=p[j:j+3]
            w.append((t,prefix & (FULL ^ mask(t))))
            prefix ^= 1 << p[j]
        opposite(w[0],w[1]); opposite(w[1],w[2])
colors=[-1]*len(states)
for seed in range(len(states)):
    if colors[seed] != -1: continue
    colors[seed]=0; todo=deque([seed])
    while todo:
        a=todo.popleft()
        for b in adj[a]:
            if colors[b] == -1:
                colors[b]=1-colors[a];todo.append(b)
            else:
                assert colors[b] != colors[a]
assert len(states)==3360
~~~

The code is a finite proof of consistency and a constructive definition of a legal coloring; no optimization solver or external data are used.

**Scope and next extraction obligation.** The theorem concerns *rooted five-support witnesses*, not the switch count of a full seven-direction geodesic. It is a new physically exact cross-support restriction, but the missing seven-dimensional closure requires matching terminal direction pairs, window colors, and actual two new seam windows. The rootwise counting alone does not force this alignment.
