# A non-Hamiltonian five-set forces an almost-complete path-cover-two cube on its complement

## Statement

Let H be a minimum counterexample and let F be a non-Hamiltonian five-vertex set. Put K=H-F and D={d in F : F-{d} is Hamiltonian}. Then |D|>=4. For every nonempty S subseteq F with 2<=|S|<=4, K union S is non-Hamiltonian with path-cover number two. In addition, K union {d} is non-Hamiltonian with path-cover number two for every d in D. Thus among the 31 proper extension states K union S, S proper nonempty subset of F, every state of extension-size two, three, or four is path-cover-two and non-Hamiltonian, and at least four of the five singleton states are as well; only the base K and at most one singleton extension remain uncontrolled.

## Body

By the five-vertex small-set theorem, at most one four-subset of F is non-Hamiltonian, so |D|>=4. For d in D, F-{d} is Hamiltonian. If K+d were Hamiltonian, these two Hamilton paths would form a spanning two-cover of H; hence K+d is non-Hamiltonian and, being proper, has path-cover number two by minimum-counterexample calculus. Now let S subseteq F with 2<=|S|<=4. The complementary set F-S has order between one and three, hence is Hamiltonian. If K union S were Hamiltonian, a Hamilton path on K union S together with one on F-S would two-cover H. Therefore K union S is non-Hamiltonian; it is proper because S is a proper subset of F, so minimum-counterexample calculus gives path-cover number two. This proves all claimed cube layers.