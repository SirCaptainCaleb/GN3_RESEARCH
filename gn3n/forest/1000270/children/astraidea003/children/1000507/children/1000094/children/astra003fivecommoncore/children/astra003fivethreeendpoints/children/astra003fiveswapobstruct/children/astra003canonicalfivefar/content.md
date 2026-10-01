# Canonical five-vertex central components synchronize the two far endpoints

## Statement

Let H-x=P|Q be an exact deletion two-cover with P=(p_0,...,p_m), Q=(q_0,...,q_s), and suppose its canonical five-vertex central-component state A|C|B is Phi-minimal in a trapped pairwise-repartition component, where A=(p_0,...,p_{m-2}), C=(q_1,q_0,x,p_m,p_{m-1}), and B=(q_2,...,q_s). Assume |A|,|B|>=7. Then either (i) C-{p_{m-1}}+{p_0} is Hamiltonian and C|A has an equal-Phi repartition that replaces A by (p_1,...,p_{m-1}); or (ii) C-{q_1}+{q_s} is Hamiltonian and C|B has an equal-Phi repartition that replaces B by (q_1,...,q_{s-1}); or (iii) there is z in {q_0,x,p_m} such that both C-{z}+{p_0} and C-{z}+{q_s} are Hamiltonian. In case (iii), for each of the two far endpoints independently, either exchanging z with that endpoint gives an equal-Phi repartition, or z has a bounded failed-insertion obstruction on the corresponding inherited far-end truncation. Hence if neither far endpoint admits any equal-Phi exchange, one middle vertex z has bounded failed-insertion obstructions on both outer paths.

## Body

# Proof

Write
A=(p_0,...,p_{m-2}),\qquad C=(q_1,q_0,x,p_m,p_{m-1}),\qquad B=(q_2,...,q_s).
The displayed order makes C a Hamilton tight path.

Because the state A|C|B is Phi-minimal and |A|>=7>|C|, the endpoint-transfer inequality with t=1 implies that C union {p_0} is non-Hamiltonian: otherwise moving p_0 from A to C would replace the size pair (5,|A|) by (6,|A|-1) and strictly decrease Phi. The same argument shows that C union {q_s} is non-Hamiltonian.

For e in {p_0,q_s}, let
I_e={z in V(C): H[(V(C)-{z}) union {e}] is Hamiltonian}.
Apply the four-of-six theorem to the non-Hamiltonian six-set V(C) union {e}. At least four of its five-vertex deletions are Hamiltonian. Deleting e leaves C itself, which is Hamiltonian, so at least three deletions z in C are also Hamiltonian. Thus |I_{p_0}|>=3 and |I_{q_s}|>=3.

If p_{m-1} belongs to I_{p_0}, then C-{p_{m-1}}+{p_0} is Hamiltonian, while
(A-{p_0}) union {p_{m-1}}
has the inherited tight order (p_1,...,p_{m-1}). These two Hamilton paths partition V(A) union V(C), have orders 5 and |A|, and therefore give an equal-Phi legal repartition. This is conclusion (i). Similarly, if q_1 belongs to I_{q_s}, then C-{q_1}+{q_s} is Hamiltonian and
(B-{q_s}) union {q_1}
has the inherited tight order (q_1,...,q_{s-1}), giving conclusion (ii).

Assume neither (i) nor (ii). Then p_{m-1} is not in I_{p_0} and q_1 is not in I_{q_s}. Since both sets have size at least three in the five-element set V(C),
|I_{p_0} intersect I_{q_s}| >= 3+3-5 = 1.
Choose z in the intersection. It cannot equal p_{m-1}, because that vertex is absent from I_{p_0}, and it cannot equal q_1, because that vertex is absent from I_{q_s}. Hence z belongs to {q_0,x,p_m}. By construction both C-{z}+{p_0} and C-{z}+{q_s} are Hamiltonian, proving the first assertion of (iii).

Now fix e=p_0 or e=q_s and let R be the corresponding outer path A or B. The five-set C-{z}+{e} is Hamiltonian. If (R-{e}) union {z} is Hamiltonian, the two Hamilton paths form an exact two-path cover of V(C) union V(R) with the same component orders 5 and |R|, hence an equal-Phi repartition exchanging z and e. If (R-{e}) union {z} is non-Hamiltonian, then z cannot be inserted anywhere into the inherited tight-path order R-e, since a successful insertion would itself give a Hamilton path on that support. The failed-insertion theorem therefore gives a bounded local obstruction involving z and at most four consecutive vertices of R-e.

Applying this independently on A-p_0 and B-q_s proves the final assertion. In particular, if no equal-Phi exchange exists at either far endpoint, the same middle vertex z has bounded failed-insertion obstructions on both inherited outer paths. ∎