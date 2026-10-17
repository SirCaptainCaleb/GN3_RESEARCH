# A five-cube disproves factorial-proportion red geodesic bounds

- Stable ID: note_nori_factorial_path_count_counterexample_q5_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction
- Labels: NORI1, counterexample, enumeration, product, counting-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11010_3
- Updated session: session_nori_r11010_3
- Disposition: none
- Successor: none

## Related references

- subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction

## Research note

**Counterexample and amplification.** The proposed universal bound \(N_R(c)\ge n!/2\) for the number \(N_R(c)\) of rooted red full antipodal geodesics of a legal antipodally odd edge coloring is false already in \(Q_5\). Index antipodal unordered-edge orbits by scanning edges \(\{u,u\oplus e_i\}\) with \(u<u\oplus e_i\), increasing \(u\), then \(i\), introducing an orbit on its first encounter. Give the first encountered edge of orbit \(j\) red color when bit \(j\) of \(\texttt{0xdb12893271}\) is one, and its antipodal mate blue; otherwise swap these colors. There are \(5\cdot2^3=40\) orbits. An integer subset-path recursion computes \(N_R(c)=32<5!/2=60\). Specifically, for each root \(x\) define \(D_x(\varnothing)=1\) and \(D_x(S)=\sum_{i\in S}[c_i(x\oplus\mathbf1_{S\setminus\{i\}})=0]D_x(S\setminus\{i\})\). Summing \(D_x([5])\) over the 32 roots gives 32. This is an integer calculation using 32 states per root, and the orbit rule makes legality immediate.

For independent Cartesian products of legal colorings \(c\) on \(Q_a\) and \(d\) on \(Q_b\), the rooted red full-path count satisfies
\[
N_R(c\boxtimes d)=\binom{a+b}{a}N_R(c)N_R(d).
\]
Indeed every product red full geodesic projects to red full geodesics in both factors, and the two sequences admit \(\binom{a+b}{a}\) interleavings; conversely every such interleaving is red. Therefore the \(k\)-fold product of the specified \(Q_5\) coloring has
\[
N_R(c^{\boxtimes k})=(5k)!\left(\frac4{15}\right)^k.
\]
In particular the fraction \(N_R(c)/n!\) has no positive dimension-uniform lower bound. This refutes factorial-proportion counting proposals while remaining compatible with the NORI1 assertion \(N_R(c)>0\). The value 32 was independently reproduced by a Python rooted subset dynamic program and by the optimized integer search program.
