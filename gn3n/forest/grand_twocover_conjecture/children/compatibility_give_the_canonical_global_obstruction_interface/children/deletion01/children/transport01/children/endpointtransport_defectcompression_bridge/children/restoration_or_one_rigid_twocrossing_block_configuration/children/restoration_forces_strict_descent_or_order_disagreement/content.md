# Minimum-side internal restoration forces strict descent or order disagreement

## Statement

Let H be a minimum counterexample, let H-y=R|Q be a deletion cover whose smaller component R has globally minimum order mu, and let z be a displayed endpoint of R. Put A=V(R)-{z}. Suppose H-z has a deletion cover with support partition (A union {y}) | V(Q), the component on A union {y} is Hamiltonian, y is internal in its displayed Hamilton order, and deleting y splits that order into exactly two A-blocks whose vertices retain their inherited order from R-z. Then either explicit order disagreement occurs among tight paths on a bounded support, or the singleton lift R|Q|{y} has a legal pairwise repartition to a spanning three-cover with strictly smaller quadratic potential.

## Body

If 3<=mu<=5, apply the small-deletion-side theorem 6f72075b0b54 directly to the original cover H-y=R|Q. It produces at least four Hamiltonian deletions of V(R) union {y}, and any four chosen deletion paths contain explicit order disagreement. Hence assume mu>=6. Use the kernel classification 28d51346a6be. Write the terminal-end case as R=(P,b,a,z), with restored path ending (P,b,y,a), and put X={b,a,y,z}. Since mu>=6, P has order mu-3>=3; let c be its terminal vertex and write P=P',c, so |P'|=mu-4>=2. The initial-end case is symmetric.

If X is Hamiltonian, repartition the pair R|{y} as P|X, leaving Q unchanged. The potential change on this pair is (mu-3)^2+4^2-(mu^2+1)=24-6mu<0, so strict descent occurs.

Suppose X is the exceptional cyclic non-Hamiltonian four-kernel. By the fifth-vertex extension theorem in smallset01, X union {c} is Hamiltonian. Repartition R|{y} as P' | (X union {c}). The component orders change from mu,1 to mu-4,5, so the potential change is (mu-4)^2+5^2-(mu^2+1)=40-8mu<0.

It remains that X is edge-orderable with the forced matching-block order M0={ab,yz}<M1={az,by}<M2={ay,bz}. In particular ab<ay, so (b,a,y) is tight. The original path supplies (c,b,a) and (b,a,z). Apply the local extension lemma 69c0240a434e to p=c,x=b,y=a,q=z,u=y. Either S=X union {c} is Hamiltonian or S is non-Hamiltonian and both (y,z,a) and (z,y,a) are tight. In the Hamiltonian case the same repartition P'|S gives strict potential decrease 40-8mu<0. In the non-Hamiltonian case, X=S-{c} is a non-Hamiltonian four-subset of S. The five-vertex classification in smallset01 says a non-Hamiltonian five-set has at most one non-Hamiltonian four-vertex deletion. Therefore every other vertex deletion of S is Hamiltonian, so S has at least four Hamiltonian vertex deletions. Apply astra004fourgooddisagree: Hamiltonian paths on four such deletions cannot all induce the same relative order, and explicit order disagreement follows.

The three kernel alternatives are exhaustive. Therefore internal restoration at a globally minimum deletion-side endpoint always produces strict quadratic descent or order disagreement.