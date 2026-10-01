# Minty-type potential on the directed graph obtained from nonspecial edges

## Statement

Let R be the digraph on V(H) obtained by replacing every nonspecial edge e={x,y,z}, with unique entrance x, by the arcs x→y and x→z. For an arc x→y arising from e, put q=φ(e). Assign score log(1+1/φ(x)) if e is ascending; assign -log 2 if e is nonascending and φ(x)<=2(q-1); otherwise assign -log 3. Then every directed closed walk in R has total score at most zero.

## Body

If e is ascending, then φ(x)=q-1, while y is a snake vertex of e and hence φ(y)>=q. Therefore log(φ(y)/φ(x))>=log(q/(q-1))=log(1+1/φ(x)). If e is nonascending and φ(x)<=2(q-1), then φ(y)>=q gives φ(x)<2φ(y), so log(φ(y)/φ(x))>-log2. In the remaining case, the corrected entrance-value distortion lemma gives φ(x)<=3(q-1)<3φ(y), so log(φ(y)/φ(x))>-log3. Thus each assigned arc score is at most log(φ(y)/φ(x)). Summing along a directed closed walk telescopes the logarithmic φ-ratios to zero. Hence every closed walk has nonpositive score. On each strongly connected component, fixing a root and taking the maximum score of a directed walk from the root to a vertex gives a finite potential satisfying the corresponding step inequalities.