# Signed turn adjacency spectrum and global cycle density

# Signed turn adjacency and a dimension-independent disagreement bound

Let \(n\ge6\), and put \(T_n=\{(a,b,c)\in[n]^3:a,b,c\text{ pairwise distinct}\}\). The oriented legal-turn graph has transitions \((a,b,c)\to(b,c,d)\) whenever \(a,b,c,d\) are pairwise distinct. Its reversal involution is \(R(a,b,c)=(c,b,a)\). Write
\[
V_n=\{f:T_n\to\mathbb R:f(Rt)=-f(t)\},\qquad
N_n=\dim V_n=n\binom{n-1}{2}.
\]
Define the operator
\[
(A_nf)(a,b,c)=\sum_{d\notin\{a,b,c\}}
\bigl(f(b,c,d)+f(d,a,b)\bigr).\tag{1}
\]
The two summands enumerate forward and backward legal turns. Reversal exchanges these summands with opposite signs, so \(A_nV_n\subseteq V_n\). Moreover, \(A_n\) is self-adjoint: every forward transition is the backward transition at its other endpoint. Choosing one ordered triple from every reversal pair makes \(A_n\) the signed adjacency matrix of the reversal quotient, of order \(N_n\) and signed degree \(2(n-3)\).

**Theorem 1 (signed-turn spectral identity).** For every \(n\ge6\),
\[
\boxed{A_n(A_n-I)(A_n+2I)\bigl(A_n^2-(n-2)^2I\bigr)=0.}\tag{2}
\]
Consequently,
\[
\boxed{\operatorname{spec}(A_n)\subseteq\{-(n-2),-2,0,1,n-2\},
\qquad A_n\succeq-(n-2)I.}\tag{3}
\]

*Proof.* Fix the initial oriented reversal orbit represented by \(t_0=(1,0,2)\), and let \(e_0\) be its coordinate basis vector in \(V_n\). The action of the symmetric group on the labels commutes with \(A_n\) and acts transitively on oriented reversal-orbit basis vectors up to sign. It therefore suffices to prove that the operator in (2) annihilates \(e_0\).

For any fixed target triple \(t\) whose letters belong to \(\{0,1,2,3,4,5\}\), the coefficient of \(e_t\) in \(A_n^ke_0\), for \(n\ge6\), is a polynomial in \(n\) of degree at most \(k\). Indeed, a contributing walk of length \(k\) introduces at most \(k\) letters outside the three initial labels. Partition its intermediate letters according to equality and according to any equalities with the fixed initial and terminal letters. Each admissible equality pattern contributes \(\pm(n-r)_j\) choices of unused letters, for some fixed integer \(r\) and \(j\le k\), where \((z)_j=z(z-1)\cdots(z-j+1)\). Summing finitely many such patterns gives the claimed polynomial degree bound. The reversal sign of a terminal coordinate depends only on the fixed letters and is independent of \(n\).

The polynomial in the operator on the left of (2) expands to
\[
P_n(A_n)=A_n^5+A_n^4-\bigl((n-2)^2+2\bigr)A_n^3
-(n-2)^2A_n^2+2(n-2)^2A_n.\tag{4}
\]
Every coordinate of \(P_n(A_n)e_0\) thus has degree at most five in \(n\). Since any ordered target triple can, by permuting the labels outside \(\{0,1,2\}\), be represented using at most three further labels, it suffices to check target triples among those six labels. Integer-arithmetic evaluation gives \(P_n(A_n)e_0=0\) for the six values \(n=6,7,8,9,10,11\). A self-contained certificate follows; all entries and operations are integers.

~~~python
from itertools import combinations

def check(n):
    reps = [(a,b,c) for b in range(n)
            for a,c in combinations([v for v in range(n) if v != b], 2)]
    where = {t:i for i,t in enumerate(reps)}
    adjacency = []
    for a,b,c in reps:
        row = []
        for d in range(n):
            if d in (a,b,c):
                continue
            for u,v,w in ((b,c,d),(d,a,b)):
                key = (u,v,w) if u < w else (w,v,u)
                row.append((where[key], 1 if u < w else -1))
        adjacency.append(row)
    def act(x):
        return [sum(s*x[j] for j,s in row) for row in adjacency]
    basis = [0]*len(reps)
    basis[0] = 1  # reps[0] = (1,0,2)
    powers = [basis]
    for _ in range(5):
        powers.append(act(powers[-1]))
    q = (n-2)**2
    return all(powers[5][i] + powers[4][i]
               - (q+2)*powers[3][i] - q*powers[2][i]
               + 2*q*powers[1][i] == 0 for i in range(len(reps)))

assert all(check(n) for n in range(6,12))
~~~

The degree-five polynomial coordinate vanishes at six distinct values, hence vanishes identically. Relabeling proves (2) on the entire space \(V_n\). Self-adjointness then places the spectrum among the roots of \(P_n\), proving (3). \(\square\)

**Theorem 2 (turn-disagreement density).** Let \(b:T_n\to\{0,1\}\) be any reversal-odd coloring, so \(b(c,b,a)=1-b(a,b,c)\). Its legal-turn cochain is
\[
d_b\bigl([(a,b,c)\to(b,c,d)]\bigr)=b(a,b,c)+b(b,c,d)\pmod2.
\]
The reversal quotient has \(E_n=(n)_4/2=N_n(n-3)\) edges. For every \(n\ge6\),
\[
\boxed{\quad
|\operatorname{supp}d_b|\le
\frac{3n-8}{4(n-3)}E_n,
\qquad
\frac{|\operatorname{supp}d_b|}{E_n}\le
\frac34+\frac{1}{4(n-3)}.\quad}\tag{5}
\]
The same statement holds on every restriction to a subset of \(m\ge6\) labels, with \(n\) replaced by \(m\). In particular, (5) improves the five-label parity-cycle bound \(4E_n/5\) when \(n\ge9\), and gives asymptotic disagreement density at most \(3/4\).

*Proof.* Choose one orientation of every reversal pair, and let \(x\in\{\pm1\}^{N_n}\) record \((-1)^{b(t)}\) there. For every quotient turn, its signed-adjacency contribution is \((-1)^{d_b}\). Thus
\[
\frac12x^\top A_nx=\sum_{e\in E(H_n)}(-1)^{d_b(e)}
=E_n-2|\operatorname{supp}d_b|.
\]
By (3), \(x^\top A_nx\ge-(n-2)\|x\|^2=-(n-2)N_n\), giving
\[
|\operatorname{supp}d_b|\le\frac12E_n+\frac14(n-2)N_n
=\frac{3n-8}{4(n-3)}E_n.
\]
Restriction to a subset retains reversal oddness and the legal-turn rule, proving the hereditary assertion. \(\square\)

**Pointed-matroid corollary.** In the cycle--cocycle model of legal turns with added port \(p\), the coloring cycle \(X_b=\operatorname{supp}d_b\cup\{p\}\) obeys
\[
|X_b\setminus\{p\}|\le\frac{3n-8}{4(n-3)}|E(H_n)|.
\]
Equivalently, at least \(\frac{n-4}{4(n-3)}|E(H_n)|\) admissible turns avoid the coloring cycle. This is a global quantitative restriction on the port-cycle sector of the canonical binary covering matroid; the estimate uses neither an edge ordering of the underlying tournament nor a small distinguished class of colorings.
