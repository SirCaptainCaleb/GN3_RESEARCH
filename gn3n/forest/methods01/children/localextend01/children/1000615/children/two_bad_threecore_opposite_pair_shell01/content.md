# Two bad extensions of a three-set force every opposite-pair four-set Hamiltonian

## Statement

Let H be a boundary tournament, let T be a three-vertex set, and let e,f be distinct vertices outside T. If T union {e} and T union {f} are both non-Hamiltonian, then for every two-element subset P of T the four-set P union {e,f} is Hamiltonian.

## Body

Fix P subset T with |P|=2 and write T=P union {a}. Apply the certified fixed-pair orientation-class theorem bd3c8d17ca06 to the fixed pair P. The exterior vertices split into two classes C_+,C_- such that any two distinct vertices in the same class complete P to a Hamiltonian four-set. Since T union {e}=P union {a,e} is non-Hamiltonian, a and e cannot lie in the same class; hence they lie in opposite classes. Similarly, non-Hamiltonicity of P union {a,f} forces a and f into opposite classes. Therefore e and f lie in the same class. The fixed-pair theorem now gives that P union {e,f} is Hamiltonian. As P was arbitrary among the three two-subsets of T, all three opposite-pair four-sets are Hamiltonian.
