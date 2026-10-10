# Bounded NORI2 switches from finite exterior-coordinate support

# Bounded NORI2 switches from finite exterior-coordinate support

## Theorem

Let \(V\) be the \(n\) coordinate directions of \(Q_n\), let \(S\subseteq V\) have \(t\) elements, and put \(D=V\setminus S\). Suppose a binary coloring \(c(F,(u,v))\) is defined on **physical ordered squares** and has the following exterior-support property:

**(ES)** For every two ordered distinct directions \(u,v\in D\), the value \(c(F,(u,v))\) depends only on the ordered pair \((u,v)\) and on the \(t\) fixed bits \(z_S(F)\) of \(F\) in directions in \(S\). In particular it is independent of all other exterior fixed bits. There is no condition whatsoever on colors of squares meeting \(S\).

**Theorem (finite-support NORI2 bound).** Under (ES), there exists a full antipodal geodesic whose ordered-square color word has at most
\[
\boxed{t+1}
\]
switches. This holds for every \(n\) and every such physical coloring, with **no antipodal-reversal hypothesis needed**. Consequently it holds for legal NORI2 colorings satisfying (ES).

In particular:
- One distinguished exterior direction, allowing *arbitrary directed* pair rules and arbitrary colors of squares containing that direction, guarantees at most two changes.
- Two distinguished exterior directions, allowing arbitrary nonlinear interactions of their exterior bits and arbitrary square colors meeting either direction, guarantee at most three changes.
- Every family with an exterior dependence support of fixed size \(t\) has a switch budget bounded independently of ambient dimension.

The sharp previously established one-switch theorem for a **symmetric pair rule with one sentinel** is stronger under its additional hypotheses. The present bound is intentionally independent of reversal symmetry of the ordinary pair function.

## Raynaud's directed two-color Hamiltonian path theorem

**Lemma (Raynaud, 1973; Hamilton path consequence).** Let \(D\) be a finite set, and arbitrarily color each **ordered pair** \((u,v)\), \(u\ne v\), red or blue. There is a Hamiltonian vertex order \((q_1,\dots,q_m)\) in which the consecutive arc-color word
\[
h(q_1,q_2),\dots,h(q_{m-1},q_m)
\]
has at most one change.

**Proof from Raynaud's theorem.** Raynaud's directed result says that every red/blue arc coloring of a complete symmetric digraph has a directed Hamiltonian cycle expressible as one red directed path and one blue directed path (monochromatic cases permitted). The edge colors therefore form at most two monochromatic runs cyclically. Delete one arc at a transition between those runs. The remaining directed Hamiltonian path has at most one switch. If the cycle is monochromatic, delete any arc. For \(m\le2\), the claim is immediate.

This directed lemma allows \(h(u,v)\) and \(h(v,u)\) to be completely unrelated; the undirected Gerencsér–Gyárfás path-partition lemma only covers symmetric \(h\). Raynaud's theorem is a published external input. One source explicitly stating it is A. Gyárfás, *Vertex covers by monochromatic pieces — a survey*, Theorem 2, which attributes the directed Hamiltonian-cycle result to Raynaud (1973). The same result appears as Theorem 2.1 in Ben-Eliezer et al., *The size Ramsey number of a directed path*, Journal of Combinatorial Theory, Series B **102** (2012).

## Proof of the NORI2 theorem

Let \(S=(s_1,\dots,s_t)\) be any order of the special directions. Fix any initial cube vertex \(x\). After traversing each member of \(S\) once, the fixed \(S\)-bit vector on subsequent ordinary squares is
\[
 \beta = \bigl(1-x_{s_1},\dots,1-x_{s_t}\bigr).
\]
By (ES), for each ordered pair \(u,v\in D\) the color of **every physical square** with ordered free directions \((u,v)\) and fixed \(S\)-bits \(\beta\) is a well-defined bit
\[
 h_\beta(u,v)\in\{0,1\}. \tag{1}
\]
No symmetry is assumed between \(h_\beta(u,v)\) and \(h_\beta(v,u)\).

Apply Raynaud's lemma to this 2-coloring of all directed arcs on \(D\). Obtain an order \(q=(q_1,\dots,q_m)\) of the \(m=n-t\) ordinary coordinates for which the adjacent-pair color word
\[
 H=(h_\beta(q_1,q_2),\dots,h_\beta(q_{m-1},q_m))
 \tag{2}
\]
has at most one change.

Traverse the complete direction permutation
\[
 p=(s_1,\dots,s_t,q_1,\dots,q_m)
 \tag{3}
\]
from the chosen cube root \(x\). For every consecutive ordered-square window entirely inside the ordinary \(q\)-block, its physical fixed \(S\)-bits are exactly \(\beta\); therefore its color equals the corresponding entry of \(H\) in (2), regardless of exterior bits on the other ordinary directions, by (ES). The suffix of the actual full square-color word thus contributes at most one internal switch.

When \(t\ge1\), precisely the first \(t\) consecutive ordered-square windows in (3) meet \(S\): their free direction pairs are
\[
 (s_1,s_2),\dots,(s_{t-1},s_t),(s_t,q_1).
 \tag{4}
\]
For \(t=1\), only \((s_1,q_1)\) occurs. The colors of these \(t\) windows can be *arbitrary*, contributing at most \(t-1\) internal switches. The transition from the last window in (4) to the first ordinary window contributes at most one further switch. Therefore
\[
 \sigma(c(P)) \le (t-1)+1+1=t+1. \tag{5}
\]
For \(t=0\), the complete word is \(H\) and has at most one switch. If \(D\) has zero or one coordinate, the full word is too short to violate the claimed bound. This covers all cases.

Crucially, the argument evaluates each window as an actual **physical square with its correct fixed exterior bits**; the prefix of special directions is a genuine cube geodesic, and the ordinary suffix is a genuine simple Hamilton order of distinct directions. There is no root or coordinate-interleaving assumption. \(\square\)

## Implications for the NORI hierarchy

The multilevel NORI3 amplification uses a constant number of sentinel directions but a *ternary* local-minimum statistic, whose mandatory changes grow unboundedly with the number of direction classes. The present theorem proves a qualitatively different phenomenon for **square** colorings: the same finite-support architecture has a uniform switch bound, even if the ordinary ordered-pair rule is asymmetric and the colors of special-direction squares are otherwise unconstrained.

Therefore a putative NORI2 coloring forcing an **unbounded** number of switches must have unbounded minimal exterior-coordinate support (in the precise sense (ES)) as \(n\to\infty\). A coloring forcing **two** switches might already exist with one or two exterior directions; (5) does not decide this. The sharp symmetric-pair one-sentinel result rules out a two-switch obstruction in that restricted subfamily. Nor does (5) settle unrestricted NORI2, where ordinary squares can depend on arbitrarily many exterior coordinate bits.

## References

A. Gyárfás, *Vertex covers by monochromatic pieces — a survey*, Theorem 2 (Raynaud's 1973 directed two-color Hamiltonian-cycle theorem), accessible at https://www.renyi.hu/~gyarfas/Cikkek/172_krakowrev3.pdf.

The directed statement is also quoted as Theorem 2.1 in *The size Ramsey number of a directed path*, Journal of Combinatorial Theory, Series B **102** (2012), 743–755.
