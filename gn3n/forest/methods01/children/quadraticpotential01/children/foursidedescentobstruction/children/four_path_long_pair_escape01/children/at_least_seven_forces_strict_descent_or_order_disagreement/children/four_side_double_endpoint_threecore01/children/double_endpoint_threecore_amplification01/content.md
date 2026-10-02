# Two common endpoint three-cores amplify to five-windows or multiple endpoint-pair four-windows

## Statement

Let H be a boundary tournament, let X be a Hamiltonian four-vertex set, and let a,b be distinct vertices outside X. Suppose X union {a} and X union {b} are non-Hamiltonian. Then there exist distinct x,y in X such that for each z in {x,y}, with C=X-{z}, either C union {a,b} is Hamiltonian, or at least two of the three four-sets (C-{c}) union {a,b}, c in C, are Hamiltonian.

## Body

By four_side_double_endpoint_threecore01, choose distinct x,y in X such that for each z in {x,y}, both C union {a} and C union {b} are Hamiltonian, where C=X-{z}. Fix such z and put S=C union {a,b}. If S is Hamiltonian, the first alternative holds. Otherwise S is a non-Hamiltonian five-set. By the certified five-vertex small-set theorem in smallset01, at most one of its five four-subsets is non-Hamiltonian. The deletions S-a=C union {b} and S-b=C union {a} are already Hamiltonian, so among the three remaining deletions S-c=(C-{c}) union {a,b}, c in C, at least two are Hamiltonian. Apply this independently for z=x and z=y.