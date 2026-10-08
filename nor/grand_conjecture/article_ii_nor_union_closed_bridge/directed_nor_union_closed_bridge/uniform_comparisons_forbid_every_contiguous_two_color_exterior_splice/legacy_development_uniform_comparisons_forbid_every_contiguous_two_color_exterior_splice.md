# Uniform comparisons forbid every contiguous two-color exterior splice — preserved pre-item development

## Uniform comparisons exclude every contiguous cycle-path splice

Let C be a color-0 monochromatic tight cycle of length at least three, and let Q be an exterior spanning order whose ternary color word w has exactly one change, with both color runs nonempty. Suppose C and the support E of Q satisfy one of the two uniform-comparison configurations from the cycle-absorption theorem.

A contiguous splice means: cut C at any vertex, choose either cyclic direction, choose either orientation of Q, and concatenate the two resulting vertex blocks in either order. No vertex is deleted or repeated.

### Proposition
Every such contiguous splice has at least two color changes. Thus the two-color exterior case cannot be closed by choosing better cuts or orientations within this entire class of splices.

More precisely:
- in configuration (I), if w runs 0 to 1, the minimum over these splices is two changes; if w runs 1 to 0, it is three;
- in configuration (II), the corresponding minima are three and two.

These statements concern the specified path Q and its reversal, not arbitrary reorderings or interleavings of E.

### Proof
For any orientation of Q and either direction of the cut cycle, each block has at least three vertices. Hence their concatenation has two crossing windows.

In configuration (I), a cycle followed by Q has crossing colors (1,0). At the cycle endpoint the exterior vertex precedes both cyclic neighbors, so either incoming cycle neighbor gives color 1. At the first Q vertex every cycle vertex precedes every other exterior vertex, giving color 0. If Q precedes the cycle, the crossing colors are again (1,0), by the same two uniform comparisons at the two other endpoints.

A forward cut of C has constant word 0; a reverse cut has constant word 1. Thus the four possible block/orientation types have words
0^a,1,0,w;
1^a,1,0,w;
w,1,0,0^a;
w,1,0,1^a,
where a=|C|-2>=1.

If w goes 0 to 1, their change counts are respectively 3,2,2,3.
If w goes 1 to 0, their counts are respectively 4,3,3,4.
Reversing Q reverses and complements its word, preserving the direction of its unique change, so this does not introduce another case.

In configuration (II), both crossing colors are instead (0,1). The four words are
0^a,0,1,w;
1^a,0,1,w;
w,0,1,0^a;
w,0,1,1^a.
For w going 0 to 1 their counts are 3,4,4,3.
For w going 1 to 0 their counts are 2,3,3,2.
This proves the assertions.

### Closure obligation
If E has a monochromatic spanning order, the earlier uniform-comparison corollary closes NOR on C union E. If all available exterior certificates have two nonempty color runs, the present proposition rules out an exhaustive family of contiguous joins. A successful continuation must change the exterior order more substantially, interleave vertices of C and E, or first derive a stronger exterior certificate.

The proof is only a limitation of this splice family. It does not produce a counterexample to NOR, and it does not show that the uniform configurations violate the conjecture.
