# A Hamiltonian six-support has a good deletion outside any prescribed three-set

## Statement

Let H be a minimum counterexample, let U be a proper Hamiltonian six-vertex set, and suppose H-U is non-Hamiltonian with path-cover number two. For every set T subseteq U with |T| at most three, there exists d in U-T such that U-d is Hamiltonian and H-(U-d) is non-Hamiltonian with path-cover number two. In particular, any structure supported on at most three prescribed vertices of U can be retained while reducing the Hamiltonian six-support to a Hamiltonian five-support.

## Body

Put K=H-U and let D={d in U: U-d is Hamiltonian}. By ham6extensiongrid01, |D|>=4 and, for every d in D, K+d is non-Hamiltonian with path-cover number two. Since |T|<=3, D is not contained in T. Choose d in D-T. Then U-d is Hamiltonian and contains T, while H-(U-d)=K+d is non-Hamiltonian with path-cover number two, as required.