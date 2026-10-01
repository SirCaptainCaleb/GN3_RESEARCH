# The extremal critical-core color graph has minimum degree k minus two

## Statement

In the |D|=k critical-core normal form, let G on X=V(H)\D consist of all DXX edges, colored by their D-vertex. Then G is properly edge-colored, every forest-private vertex has color-degree k, and every forest joint has degree k, k-1, or k-2. Hence delta(G)>=k-2. Degree k-2 occurs only when a joint of total degree k+1 lies in exactly one DDX edge; otherwise a joint misses at most one D-color.

## Body


Assume |D|=k and put X=V(H)\D, with forest F=H[X]. By ee2c9575cf8f every x in X has degree k+1 or k+2, and F has no isolated vertices.

Fix x in X. Let t=d_F(x), so t is 1 or 2. The number of cross-edges through x meeting D is
  c_x=d_H(x)-t.
Distinct cross-edges through x use pairwise disjoint subsets of D, by linearity: if two such edges shared d in D they would both contain the pair {x,d}. Since |D|=k, the total number of D-incidences among these c_x edges is at most k.

If t=1, then d_H(x)=k+1 by ee2c9575cf8f, so c_x=k. Hence each cross-edge contains exactly one D-vertex and the k cross-edges use all k colors once.

Now let t=2. Then d_H(x) is k+1 or k+2.

If d_H(x)=k+2, then c_x=k, and again every cross-edge contains exactly one D-vertex and all k colors occur once.

If d_H(x)=k+1, then c_x=k-1. Since the D-subsets of these cross-edges are disjoint and nonempty, exactly one of two possibilities occurs:
(A) all k-1 cross-edges contain exactly one D-vertex, so exactly one color of D is absent;
(B) one cross-edge contains two D-vertices and the other k-2 contain one each, so all k colors occur and there is exactly one DDX edge.

Let G be the simple graph on X formed from the DXX edges, colored by their unique D-vertex. Linearity makes G properly edge-colored.

The preceding classification gives:
- every forest-private vertex has d_G(x)=k;
- every forest joint has d_G(x) in {k,k-1,k-2};
- hence delta(G)>=k-2.

Moreover d_G(x)=k-2 occurs only at a forest joint of total degree k+1 that lies in one DDX edge; d_G(x)=k-1 occurs only when exactly one D-color is missing at that joint.
