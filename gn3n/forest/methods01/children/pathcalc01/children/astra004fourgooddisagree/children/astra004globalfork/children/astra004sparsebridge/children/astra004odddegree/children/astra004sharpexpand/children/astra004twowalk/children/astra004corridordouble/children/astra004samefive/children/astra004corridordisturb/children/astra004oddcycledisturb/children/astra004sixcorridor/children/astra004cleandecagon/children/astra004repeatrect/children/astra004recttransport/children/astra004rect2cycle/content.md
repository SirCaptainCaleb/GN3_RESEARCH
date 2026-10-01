# Rectangle transport is an involution and produces a common-middle four-corner square

## Statement

In the setting of astra004recttransport, put K=N union {a} and write the chosen Hamilton order on N from its far endpoint d toward the common attachment end of b,c as (d,R). Then N_prime=(N-{d}) union {a} has inherited order (a,R). Hence applying the same transport to the d-rectangle sends d back to a: rectangle transport closes after two steps. Moreover the four paths (a,R,b), (a,R,c), (d,R,b), (d,R,c) are all tight. Thus the all-clean repeated-label residue is a two-cycle of omitted labels a,d around one fixed non-Hamiltonian support K, together with a common-middle four-corner square on endpoints {a,d} and {b,c}.

## Body

Astra004recttransport gives N_prime=(N-{d})+{a}, says its Hamilton order is obtained from the order on N by replacing the far endpoint d with a at that same end, and says b,c attach at the same opposite end as before. Orienting from the far end therefore writes N=(d,R) and N_prime=(a,R), while the four transported supports are exactly (d,R,b),(d,R,c),(a,R,b),(a,R,c). In the transported rectangle the fixed missing support is N_prime+d=N+a=K. The endpoint opposite the common b,c attachment in the inherited order on N_prime is a. Reapplying the transport construction with omitted label d therefore replaces far endpoint a by d and recovers N=K-a. Thus the transport map interchanges a and d and is involutive. The four displayed paths are tight by the original and transported rectangle supports.