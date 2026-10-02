# A first-type failed-insertion window is Hamiltonian or the universal cyclic four-kernel

## Statement

Let B=(b_1,...,b_m) be a tight path in a boundary tournament and let x lie outside B. Suppose the failed-insertion normal form of insert01 has alternative 1 at an internal index t. Put a=b_{t-1}, b=b_t, c=b_{t+1}, and X={a,b,c,x}. Then either H[X] is Hamiltonian, or X is exactly the cyclic non-Hamiltonian four-vertex configuration from smallset01. In the latter case X union {d} is Hamiltonian for every d outside X. No deletion-cover hypothesis is required.

## Body

Alternative 1 of insert01 is the comparison cycle f_t -> e_{t-1} -> e_t -> f_t. Translating back to tight triples gives (x,b,a), (a,b,c), and (c,b,x) tight. If H[X] is Hamiltonian there is nothing to prove. Assume it is non-Hamiltonian. The proof in transport01, Section 'First-type insertion obstructions are Hamiltonian four-windows or universal cyclic four-kernels', uses only these three tight triples, boundary antisymmetry, and non-Hamiltonicity of X to force the remaining reversal classes. It obtains precisely the cyclic non-Hamiltonian four-vertex orientation of smallset01. The cyclic-kernel extension theorem in smallset01 then says X union {d} is Hamiltonian for every exterior vertex d. None of these steps uses the ambient deletion-cover hypothesis appearing in the transport01 application, so the classification holds in the stated local setting.