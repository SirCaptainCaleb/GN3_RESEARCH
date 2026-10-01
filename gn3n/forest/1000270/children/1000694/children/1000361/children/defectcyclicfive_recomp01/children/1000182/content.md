# The full C5 cyclic defect certificate cannot occur in a minimum counterexample

## Statement

Let H be a minimum counterexample and let pi be a minimum-defect-span ordering. Then its cyclic defect graph Gamma is proper; in particular the full-cycle exception Gamma=C5 cannot occur. Combined with ba50a9a99fd3, the only remaining cyclic defect-run multisets are {1,1,1}, {2,1,1}, {3,1}, and {3,2}.

## Body

The cyclic defect graph in 52f5b958156e has one vertex for each cyclic cut position of the spanning ordering, hence |V(Gamma)|=|V(H)|=n. The only full-cycle exception surviving the span-three classification 0d475452037a is Gamma=C5, which forces n=5. But the minimum-counterexample calculus mincex01 gives n>10. Thus Gamma cannot be the full-cycle exception and must be proper. The proper classification in 0d475452037a leaves the five run multisets {1,1,1}, {2,1,1}, {3,1}, {3,2}, {5}; ba50a9a99fd3 eliminates {5}.
