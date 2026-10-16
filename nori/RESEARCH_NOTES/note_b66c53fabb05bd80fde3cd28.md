# Sharp half-dimensional face barrier and complementary one-detour caps

- Stable ID: note_b66c53fabb05bd80fde3cd28
- Author: unspecified; session provenance retained
- Primary home: subsection:zero_turn_contraction_pointed_odd_girth_and_the_cube_geodesic_distance_defect
- Labels: method-limitation, shortest-antipodal-paths, face-shortcut, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_3
- Updated session: session_nori_r10487_3
- Disposition: none
- Successor: none

## Related references

- subsection:zero_turn_contraction_pointed_odd_girth_and_the_cube_geodesic_distance_defect, exact version 12

## Research note

# Half-dimensional barrier for face-shortcut arguments

Fix \(n\ge5\), put \(K=\lfloor(n-3)/2\rfloor\), \(a=K\), and \(d=n-3-a\), so \(a,d\ge K\). In \(Q_n\), consider the direction word
\[
\boxed{W=(1,\ldots,a,\ n,\ a+1,\ n,\ a+2,\ n,\ a+3,\ldots,n-1).}
\tag{1}
\]
It specifies an antipodal path \(P=(v_0,\ldots,v_L)\) from \(v_0=0^n\), of length \(L=n+2\).

**Theorem (half-dimensional shortcut barrier).** The path \(P\) is vertex-simple. For every \(0\le s<t\le L\), put \(k=n-d_H(v_s,v_t)=d_H(v_s,\bar v_t)\). Then
\[
\boxed{(t-s)+k<L\implies k\ge\lfloor(n-3)/2\rfloor+1.}
\tag{2}
\]
Thus a positive-detour antipodal path need not have any pair of vertices to which the cross-antipodal face-shortcut obstruction applies for face dimensions at most \(\lfloor(n-3)/2\rfloor\).

*Proof.* All directions other than \(n\) occur once in (1), while \(n\) occurs three times. Thus the final vertex is antipodal to the initial vertex. Any nonempty contiguous subword with a non-\(n\) direction has nonzero XOR, since that direction occurs only once. A contiguous subword consisting solely of \(n\) has one step because occurrences of \(n\) are separated by other directions. Thus the path is vertex-simple.

Fix \(s<t\), let \(r\in\{0,1,2,3\}\) be the number of direction-\(n\) steps outside the subword \(W[s+1:t]\), and let \(m\) count the omitted steps in all other directions. The subword has Hamming displacement \(n-m-(r\bmod2)\), hence
\[
k=m+(r\bmod2),\qquad L-(t-s)=m+r.
\]
Therefore \((t-s)+k<L\) holds precisely when \(r\ge2\). If two omitted direction-\(n\) steps are both in the prefix, the prefix necessarily contains the \(a\) leading directions and direction \(a+1\), giving \(m\ge a+1\ge K+1\). If two are in the suffix, that suffix contains direction \(a+2\) and the \(d\) trailing directions, giving \(m\ge d+1\ge K+1\). Otherwise the prefix and suffix each contain an omitted \(n\)-step, and together contain all \(a+d=n-3\) exterior directions, so \(m\ge n-3\ge K+1\). In all cases \(k\ge K+1\), proving (2). \(\square\)

**Scope.** The construction is geometric, with no prescribed edge coloring. It establishes a method limitation, not a counterexample to NORI1. The conditions from the cross-antipodal face-shortcut theorem in Article XI can be vacuous for every face of dimension as high as \(\lfloor(n-3)/2\rfloor\) even for the minimum positive detour \(L-n=2\). Thus eliminating detours using that theorem requires additional coloring constraints or larger-dimensional face information.

Finite enumeration of the specified direction words in dimensions 5 through 16 independently confirms the minimum eligible face dimension is \(K+1\); the proof covers all \(n\ge5\).

## Sharpness and the complementary-face obstruction

For an antipodal path \(P=(v_0,\ldots,v_L)\), let
\[
\kappa(P)=\min\{n-d_H(v_s,v_t):\,0\le s<t\le L,\ 
(t-s)+n-d_H(v_s,v_t)<L\}.
\]
The minimum is nonempty when \(L=n+2\).

**Theorem (optimal face dimension at one detour).** For every \(n\ge5\),
\[
\boxed{\max_{P:\,L=n+2}\kappa(P)=\lfloor(n-1)/2\rfloor,}
\tag{3}
\]
where the maximum ranges over antipodal cube walks and is attained by a vertex-simple path.

*Proof.* Since all direction multiplicities of an antipodal walk are positive and odd, one direction \(i\) appears three times in an \(n+2\)-edge word, while every other direction appears once. Let \(q\) be the position of the middle \(i\)-step. The pair \(v_q,v_L\) is shortcut-eligible with face dimension \(k_1=q-2\), since \((L-q)+k_1=L-2<L\). Likewise \(v_0,v_{q-1}\) is shortcut-eligible with face dimension \(k_2=L-q-1\), since \((q-1)+k_2=L-2<L\). Their sum is \(k_1+k_2=L-3=n-1\), so one has dimension at most \(\lfloor(n-1)/2\rfloor\). The construction (1) and its proved bound (2) attain \(\kappa(P)\ge K+1=\lfloor(n-1)/2\rfloor\), giving equality. \(\square\)

**Corollary (opposite-color complementary detours).** Suppose \(c\) is antipodally odd and a globally shortest color-zero antipodal path \(P\) has length \(n+2\). Put \(x=v_0\), let \(A\) be the directions other than \(i\) occurring before the middle \(i\)-step, and let \(B=[n]\setminus(A\cup\{i\})\). Then \(|A|+|B|=n-1\), and both faces
\[
F_A=[x,x\oplus\mathbf1_A],\qquad F_B=[x,x\oplus\mathbf1_B]
\tag{4}
\]
lie in the same \(i\)-fixed facet and have no monochromatic geodesic between their displayed opposite corners. Furthermore a red walk joins \(x\) to \(x\oplus\mathbf1_A\) in \(|A|+2\) steps, and a blue walk joins \(x\) to \(x\oplus\mathbf1_B\) in \(|B|+2\) steps. Each of these detours traverses direction \(i\) twice and each member of its own direction set once.

*Proof.* The prefix through the middle \(i\)-step is the asserted red detour: its direction word has two occurrences of \(i\), and one of each direction in \(A\). The suffix beginning immediately before that middle step is red, runs from \(v_{q-1}\) to \(\bar x\), and contains two occurrences of \(i\) and one of each direction in \(B\). Antipodally translate and reverse the suffix to obtain the blue detour from \(x\) to \(\bar v_{q-1}=x\oplus\mathbf1_B\). Theorem 26 of the linked Article XI Subsection applies to the two eligible vertex pairs in the preceding proof and excludes monochromatic full geodesics between the indicated face corners. \(\square\)

The sharp threshold in (3) demonstrates the limitation of geometric face-shortcut arguments. The opposite-color, complementary rooted detours in (4) supply additional coloring constraints in the minimal positive-detour case; whether these can be turned into an unrestricted descent remains open.
