# Five-cycle turn-density and six-resource marked intersection theorem

# Five-cycle turn-density and six-resource port intersections

Let \(b(a,v,c)\in\mathbb F_2\) be an arbitrary ordinary boundary 3-tournament on a vertex set \(V\) of size \(n\ge5\), with \(b(c,v,a)=1+b(a,v,c)\). Let \(\widetilde H_V\) have ordered-triple vertices \((a,v,c)\) and edges from \((a,v,c)\) to \((v,c,d)\) whenever all four symbols are distinct. Reversal \(J(a,v,c)=(c,v,a)\) gives a connected double cover of the quotient graph \(H_V\), whose turn cochain is
\[
d_b([\{t,t'\}])=b(t)+b(t')\in\mathbb F_2.
\tag{1}
\]
Its port cycle in the pointed binary matroid of the preceding Subsections is \(X_b=\operatorname{supp}(d_b)\cup\{p\}\).

**Theorem 1 (hereditary five-cycle turn-density bound).** For every \(n\ge5\),
\[
\boxed{|\operatorname{supp}(d_b)|\le \frac45|E(H_V)|=\frac25(n)_4.}
\tag{2}
\]
The same inequality holds on the graph induced by any subset of at least five original vertices.

*Proof.* For five pairwise distinct vertices \(a,b,c,d,e\), the five ordered-triple states
\[
(a,b,c),(b,c,d),(c,d,e),(d,e,a),(e,a,b)
\tag{3}
\]
form a closed five-cycle in the lifted state graph. The sum of its five turn labels in \(\mathbb F_2\) telescopes to zero. Thus the integer number of changed turns is even and at most four. Averaging over uniformly random ordered quintuples, every directed overlap of four distinct symbols appears equally frequently by the transitive action of the symmetric group, and reversal preserves the turn cochain. Consequently the expected fraction of changed turns in (3) is \(|\operatorname{supp}(d_b)|/|E(H_V)|\le4/5\). Since \(|E(H_V)|=(n)_4/2\), (2) follows. Restricting the argument to any vertex subset proves hereditariness. \(\square\)

For an injective six-vertex word \(v=(v_1,\ldots,v_6)\), the boundary twisted-closure lemma constructs the following state sequence, ending at the reversal of the first state:
\[
\begin{split}
&(v_1,v_2,v_3),(v_2,v_3,v_4),(v_3,v_4,v_5),
(v_4,v_5,v_6),\\
&(v_5,v_6,v_3),(v_6,v_3,v_2),(v_3,v_2,v_1).
\end{split}
\tag{4}
\]
Its projection \(C_v\) is a simple monodromy-one six-cycle. Therefore \(Y_v=C_v\cup\{p\}\) is a *resource-simple marked port cocircuit of size seven*, whether or not it has minimum size in the unrestricted pointed matroid.

**Theorem 2 (all-dimensional six-resource intersection with abundance).** In every ordinary boundary tournament on \(n\ge6\) vertices, for every six-element subset \(S\subseteq V\), at least **36** of the \(6!=720\) permutations \(v\) of \(S\) yield
\[
\boxed{|X_b\cap Y_v|\le4,\qquad |Y_v|=7.}
\tag{5}
\]

*Proof.* Fix \(S\), and choose a permutation \(v\) uniformly. Each of the six turn positions in (4) is individually uniform among the edges of \(H_S\): all involve four distinct original vertices, and the \(S_6\)-action is transitive on their reversal-orbits. Write
\(w(v)=|X_b\cap Y_v|-1=\sum_{t\in C_v}d_b(t)\)
with the sum taken as an integer. By Theorem 1,
\[
\boxed{\mathbb E_v\,w(v)
=6\frac{|\operatorname{supp}(d_b|_{H_S})|}{|E(H_S)|}
\le\frac{24}{5}<5.}
\tag{6}
\]
Odd covering monodromy makes \(w(v)\) odd; six turns restrict \(w(v)\) to \(\{1,3,5\}\). Therefore some \(v\) has \(w(v)\le3\), giving (5). In fact, the total deficit is
\[
\sum_{v\in\mathfrak S(S)}(5-w(v))
\ge720(5-24/5)=144.
\]
Every word with \(w(v)\le3\) contributes at most four to this deficit, and every other contributes zero. Hence there are at least \(144/4=36\) marked four-intersection witnesses. \(\square\)

**Corollary 3 (a uniform finite-range consequence).** The canonical boundary case \(q=3\) of the seam-controlled resource-gallery conjecture, requiring a marked port cocircuit with intersection at most four and \(m\ge\max\{6,\lceil\sqrt n\rceil\}\) distinct original vertices, holds whenever
\[
\boxed{6\le n\le36.}
\tag{7}
\]
Indeed, any six-subset supplies \(m=6\) and Theorem 2 gives the intersection bound.

**Proposition 4 (sharpness of five-cycle averaging).** Take \(V=\{0,1,2,3,4\}\). Index the 30 reversal-orbits of ordered triples by increasing middle entry followed by lexicographically increasing outer pair \(a<c\). Set the color on each representative equal to the corresponding bit of
\[
\boxed{M=\mathrm{0x3ed25058},}
\tag{8}
\]
and color its reversal by the complementary bit. On all \(5!=120\) cyclic five-vertex words, the five-state turn count is four; the density in (2) is therefore \(4/5\). No full five-vertex tight word is monochromatic.

*Proof (complete finite certificate).* The following standard-library program enumerates all 120 words and checks the cyclic switch histogram \(4:120\) and ordinary three-triple-color switch histogram \(1:48,\,2:72\).

    from itertools import permutations, combinations
    V=range(5)
    reps=[(a,b,c) for b in V
          for a,c in combinations([u for u in V if u!=b],2)]
    assert len(reps)==30
    idx={t:i for i,t in enumerate(reps)}
    M=0x3ed25058
    def b(a,v,c):
        t=(a,v,c) if a<c else (c,v,a)
        return ((M>>idx[t])&1)^int(a>c)
    cyclic={0:0,2:0,4:0}
    ordinary={0:0,1:0,2:0}
    for v in permutations(V):
        z=[b(v[i],v[(i+1)%5],v[(i+2)%5]) for i in range(5)]
        cyclic[sum(z[i]!=z[(i+1)%5] for i in range(5))]+=1
        ordinary[sum(z[i]!=z[i+1] for i in range(2))]+=1
    assert cyclic=={0:0,2:0,4:120}
    assert ordinary=={0:0,1:48,2:72}

This example shows that a stronger all-order density bound cannot follow from parity on isolated five-cycles alone. \(\square\)

**Seam-control limitation.** These theorems control the total number of changes around a six-turn twisted cycle, not their placement. At port intersection four, the seam identity
\[
|X_b\cap Y_v|-1=s(v)+h(v)=3
\]
allows \((s,h)=(3,0),(2,1),(1,2),(0,3)\), where \(s\) is the number of original internal turns and \(h\) counts the three closing seams. The following Subsection proves that tail reflection preserves the marked cocircuit and, on six resources, interchanges the internal and seam switch counts. Consequently the present density theorem **does** yield a one-turn path on every induced six-set after this reflection is applied. For longer galleries, the reflection leaves a central-defect interval requiring additional resource-preserving exchange.
