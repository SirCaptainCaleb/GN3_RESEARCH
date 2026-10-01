# Unsupported: proposed 4/7 minimum-degree floor for ascending edge rank

## Statement

Unsupported. The displayed 4/7 rank floor was derived using 47c17993cf60, which is false by the explicit counterexample 2712f65b5d5e. No independent proof of this 4/7 bound is currently supplied.

## Body

The derivation bounded the number of private-slot single blockers by treating their occupied cells as an independent set. Counterexample 2712f65b5d5e refutes exactly that premise. Therefore the inequality 2(δ-t)<=ceil(3(t-1)/2) and its consequence 7t>=4δ+2 are not established by this argument. Retain this object only as a historical fence until an independent proof or counterexample to the numerical bound itself is found.
