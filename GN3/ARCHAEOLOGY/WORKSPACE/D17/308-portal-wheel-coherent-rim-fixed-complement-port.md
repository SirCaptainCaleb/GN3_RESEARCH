# Every support-coherent rim cycle of length three to five lies inside one fixed-complement puncture port

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-coherent-rim-fixed-complement-port`

**Summary:** Let d_0->...->d_{r-1}->d_0, 3<=r<=5, be a root-capture rim from SV60333, with chosen singleton rows T_{d_i}. If every consecutive pair of rows has compatible support partitions on the common pair deletion, then accepted R926 forces all rim labels to be incident with one common rail-incidence port: the alternative spanning odd compatibility cycle is impossible because |H|>10 while r<=5, and in the forest-root alternative any line-graph cycle lies in one star clique. Hence there is one nonempty proper universe Omega containing all rim labels and one fixed Hamilton complement B=V-Omega such that every rim row has support partition (Omega-d_i)|B. Counterexamplehood makes Omega non-Hamiltonian. Moreover each selected root-capture crossing d_{i+1}e_i lies inside the Omega-d_i rail, so its exterior endpoint e_i belongs to Omega-K. Thus the entire coherent rim recurrence is internal puncture dynamics of one fixed-complement block, not a generic wheel. At r=5 all five K-punctures are Hamiltonian with the same complement. This is a coherent-wheel compression, not yet absorption of the resulting partial critical block.


### 1. Setup: compatibility along a root-capture rim

Retain the G23 root-capture circuit of SV60333 on the Hamilton P5 \(K\). Let

\[
 d_0\to d_1\to\cdots\to d_{r-1}\to d_0,\qquad 3\le r\le5,
\]

be one simple directed rim cycle, indices modulo \(r\). For every root \(d_i\), retain the actual exact singleton-deletion row used to generate its outgoing capture edge:

\[
 T_i=T_{d_i}=P_i\mid Q_i\quad\text{on }H-d_i.
\]

Every exact singleton-deletion row in a smallest counterexample has two nonempty rails of order at least two. Indeed, if one rail were the singleton \((z)\), the other rail would Hamiltonize \(H-\{d_i,z\}\); the automatic dimer \((d_i,z)\) would then give a spanning two-cover of \(H\).

Let \(\sigma_i\) be the unordered support partition of \(T_i\). Assume the rim is SUPPORT-COHERENT in the literal R926 sense:

\[
 \sigma_i|_{V-\{d_i,d_{i+1}\}}
   =\sigma_{i+1}|_{V-\{d_i,d_{i+1}\}}
 \qquad\text{for every }i. \tag{CW.1}
\]

Equivalently, every consecutive pair \(d_i d_{i+1}\) is an edge of the singleton compatibility graph for the chosen family \(\{T_v\}\), after extending the rows outside the rim arbitrarily by exact singleton covers.

### 2. R926 rules out a short non-star compatibility cycle

Apply accepted R926 to the complete chosen singleton-cover family. It supplies a simple triangle-free rail-incidence root \(R\) with compatibility graph

\[
 G=L(R),
\]

and says that \(R\) is either a forest or one odd cycle containing every physical edge of \(H\). In the latter case \(G\) itself is the same spanning odd cycle.

The vertices

\[
 d_0,d_1,\ldots,d_{r-1}
\]

are distinct and (CW.1) makes them a simple cycle in \(G\) of length \(3\le r\le5\). The spanning-odd-cycle alternative is impossible: accepted R533 gives \(|V(H)|>10\), while a cycle graph has no proper smaller simple cycle. Hence \(R\) is a forest.

Now use the elementary line-graph structure of a forest. Every simple cycle in \(L(R)\) is contained in the clique of edges incident with one root vertex. One direct proof is as follows. Write \(e_i\) for the root edge representing physical label \(d_i\), and let \(v_i=e_i\cap e_{i+1}\). If two consecutive intersection vertices \(v_i,v_{i+1}\) were distinct, then \(e_{i+1}\) would be the root edge joining them. Traversing the cyclic sequence and suppressing maximal runs with one common intersection would produce a closed walk in the forest with no immediate edge repetition; deleting backtracking pairs yields a root cycle, impossible. Therefore all intersections are one root vertex \(P\), so every \(e_i\) is incident with \(P\).

Thus all rim labels use one common R926 port:

\[
 d_i\text{ is incident with }P\quad\text{for every }i. \tag{CW.2}
\]

### 3. One fixed port universe and one literal complement support

Let

\[
 \Omega=\Omega_P
\]

be the R926 support universe of the common port. For any physical edge \(d_i=P R_i\), accepted R926 gives

\[
 \Omega_P\cup\Omega_{R_i}=V(H),\qquad
 \Omega_P\cap\Omega_{R_i}=\{d_i\}. \tag{CW.3}
\]

The two rail supports of \(T_i\) are exactly

\[
 \Omega_P-\{d_i\},\qquad \Omega_{R_i}-\{d_i\}.
\]

By (CW.3), the second support is independent of \(i\):

\[
 B:=V(H)-\Omega,
\qquad
 T_i:\ (\Omega-\{d_i\})\mid B. \tag{CW.4}
\]

Both displayed supports are nonempty, and both carry literal Hamilton tight paths because \(T_i\) is an exact two-cover. In particular:

- every rim label \(d_i\in\Omega\);
- \(B\) is a nonempty Hamiltonian support, with the same physical support in every rim row;
- \(\Omega-\{d_i\}\) is Hamiltonian for every rim label \(d_i\).

The active universe \(\Omega\) itself is non-Hamiltonian. Otherwise a Hamilton path on \(\Omega\) together with any retained Hamilton path on \(B\) would be a spanning two-cover of \(H\).

Thus a support-coherent rim is already a PARTIAL DELETION-HAMILTONIAN FIXED-COMPLEMENT BLOCK.

### 4. Every root-capture crossing stays inside the active block

Retain the actual selected crossing that generated the outgoing root-capture edge

\[
 d_i\to d_{i+1}.
\]

By SV60333 it has physical endpoints

\[
 \{d_{i+1},e_i\},
 \qquad d_{i+1}\in K-\{d_i\},
 \qquad e_i\in V(H)-V(K). \tag{CW.5}
\]

Because \(d_{i+1}\in\Omega-\{d_i\}\), it lies on the active \(\Omega-d_i\) rail of \(T_i\). A selected adjacency of a path cannot cross between the two rail supports in (CW.4). Therefore its mate \(e_i\) lies on the same active rail:

\[
 e_i\in\Omega-\{d_i\}. \tag{CW.6}
\]

Combining (CW.5)-(CW.6),

\[
 e_i\in\Omega-V(K). \tag{CW.7}
\]

So the apparent \(K\mid(H-K)\) portal crossing is, after coherent support synchronization, entirely INTERNAL to the one active fixed-complement universe \(\Omega\): it crosses from \(K-d_i\) into \(\Omega-K\), never into the fixed complement \(B\).

In particular \(\Omega-K\ne\varnothing\), so the coherent block is strictly larger than the original P5 support.

### 5. Consequences by rim length

For every \(3\le r\le5\), the whole coherent rim is now localized to puncture dynamics inside one non-Hamiltonian universe \(\Omega\) with one fixed Hamilton complement \(B\).

If \(r=5\), the rim uses every vertex of the original P5 \(K\). Hence

\[
 \Omega-d\text{ is Hamiltonian for every }d\in K, \tag{CW.8}
\]

with the same complement support \(B\), and every chosen root-capture marker joins \(K-d\) to \(\Omega-K\). This is a five-root partial critical block.

For \(r=3,4\), the same conclusion holds for the rim-root subset; the noncycle K-roots are not asserted compatible with this port.

### 6. G23 interpretation and scope

Therefore a support-coherent short rim is not a generic rank-flat return cycle. Its entire support geometry collapses to

\[
 V(H)=\Omega\sqcup B,
\]

where \(B\) is Hamiltonian, \(\Omega\) is non-Hamiltonian, every rim-root puncture \(\Omega-d_i\) is Hamiltonian, and every actual rim capture crossing stays inside \(\Omega\).

This is precisely the coherent-wheel side of G23 in compressed form: the next theorem need only absorb a bounded partial critical block with fixed complement, or prove that one of the remaining K-roots / active exterior vertices extends the puncture family and forces a strict compatibility or disagreement consequence.

No Hamilton-order synchronization between different \(\Omega-d_i\) paths is claimed. No assertion is made that every vertex of \(\Omega\) is Hamilton-deletable, so accepted R945/R961 cannot yet be invoked as a full critical-block theorem. The result is support-level compression, not closure.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R533"
    },
    {
        "relation": "dependency",
        "revision_id": "R926"
    }
]
```