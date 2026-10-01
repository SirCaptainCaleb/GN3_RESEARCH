# Minty-type potential on the transfer digraph of nonspecial edges

## Statement

Define a digraph M on the nonspecial edges of H by e→f when e∩f={v}, φ(e,v)=φ(e), and v is the unique entrance of f. For e→f put p=φ(e), q=φ(f). If f is ascending, assign score log(1+1/p); if f is nonascending and φ(v)<=2(q-1), assign score -log 2; otherwise assign score -log 3. Every directed closed walk in M has total score at most zero.

## Body

For e→f through v, p<=φ(v). If f is ascending, then q=φ(v)+1>=p+1, so log(q/p)>=log(1+1/p). If f is nonascending and φ(v)<=2(q-1), then p<2q, so log(q/p)>-log2. In the remaining case, the corrected distortion lemma gives φ(v)<=3(q-1)<3q, hence p<3q and log(q/p)>-log3. Thus every assigned step score is at most log(q/p). Around a directed closed walk, the logarithms telescope to zero. Consequently, on each strongly connected component, fixing a root and taking the maximum score of a directed walk from the root to a given vertex produces a finite potential satisfying the corresponding step inequalities.
