# Relative-order gauges force common face blocks

**Summary:** Balanced relative-order gauges force their endpoint labels into common permutahedron face blocks.

## Statement

On a permutahedron face, if the relative-order sign g_ab takes both signs among chambers of a positive balanced carrier, then a and b lie in the same face block. Consequently pair-order gauges along a connected graph force every connected component into one face block.

## Body


For distinct labels \(a,b\), define on permutation chambers
\[
g_{ab}(\pi)=
\begin{cases}
+1,&a\text{ precedes }b,\\
-1,&b\text{ precedes }a.
\end{cases}
\]

Let \(F=B_1|\cdots|B_r\) be a permutahedron face and suppose positive chamber weights on \(F\) satisfy
\[
\sum_\pi \lambda_\pi g_{ab}(\pi)=0,
\qquad
\lambda_\pi>0.
\]

If \(a,b\) lay in different blocks of \(F\), their relative order would be fixed in every chamber of \(F\), so \(g_{ab}\) would be constant and could not have weighted average zero. Hence \(a,b\) lie in the same block.

More generally, if such zero-average gauges are imposed for every edge of a graph \(G\) on the labels, then every connected component of \(G\) lies in one block of \(F\).

This lets spare antipodal target dimensions be converted into geometric control of carrier faces.


## Metadata

- ID: relative_order_gauges_force_common_face_blocks
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
