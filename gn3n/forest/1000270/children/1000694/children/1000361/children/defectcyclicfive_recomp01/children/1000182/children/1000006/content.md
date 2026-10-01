# Minimum defect span three has no three-isolated-defect geometry

## Statement

Let H be a minimum counterexample and let pi be any spanning ordering attaining minimum defect span three. Then the cyclic defect graph of pi cannot have run type {1,1,1}. Consequently every minimum-span cyclic defect certificate is nonmatching and admits a double-wrap rotation.

## Body

Let pi=(v_1,...,v_n) attain minimum defect span three. By defectspanisdeletion, if i is its leftmost defect center and x=v_{i+1}, then pi is exactly the canonical concatenation P,x,Q for the deletion cover H-x=P|Q.

Apply 8ededbb50716 to this same deletion state. Its cyclic concatenation P|{x}|Q uses precisely the cyclic vertex order underlying pi, and it proves that the resulting cyclic defect graph is a proper nonmatching minimum-span certificate and cannot have run type {1,1,1}. Hence the three-isolated-defect case is impossible for pi.

Apply 687bbaa431c3 to this proper nonmatching certificate. It supplies a cut of the same cyclic order whose corresponding linear rotation has the double-wrap form. Therefore every minimum-span cyclic defect certificate admits a double-wrap rotation.
