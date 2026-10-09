# Six reversal-odd coordinate directions force a monochromatic five-direction facet

Let V be a set of at least six coordinate directions and let h(a,b,c) be a binary label of ordered triples of distinct directions, satisfying h(c,b,a)=1-h(a,b,c). A five-direction order a b c d e is monochromatic when h(a,b,c)=h(b,c,d)=h(c,d,e).

**Theorem.** Every such labeling contains a monochromatic five-direction order. In particular, every coordinate-only antipodal-reversal-odd coloring of Q_6 has a monochromatic geodesic in some five-dimensional facet and hence a full antipodal geodesic with at most one change.

The following proof is finite rearrangement, with no exhaustive-search premise. It suffices to use six directions. Suppose that no five-direction order is monochromatic. Write h(abc) for h(a,b,c). Our forcing rule is: on five distinct directions, two equal labels among h(abc), h(bcd), h(cde) force the third label to be their complement.

**Four-direction rearrangement lemma.** Under this supposition, if h(abc)=h(bcd)=q, then h(adc)=h(bad)=q.

Proof. Complement all labels to make q=0, and let e,f be the two remaining directions. For each z in {e,f}, the orders abcdz, dcbaz, and bazdc force, respectively,
h(cdz)=1, h(baz)=0, h(azd)=1.
Assume h(adc)=1. For each z in {e,f}, the orders adcbz, bcdaz, and cbzad then force, respectively,
h(cbz)=0, h(daz)=1, h(bza)=1.
Thus h(azb)=0. In the order beafd the first and third labels are h(bea)=1 and h(afd)=1, so h(eaf)=0. But the order bfaed has labels h(bfa)=1, h(fae)=1, h(aed)=1, a contradiction. Therefore h(adc)=0.

Apply the implication just proved to the reversed order dcba, whose two labels equal 1. It gives h(dab)=1, and reversal gives h(bad)=0. This establishes the lemma for either q.

**Proof of the theorem.** An equal adjacent pair of triple labels exists. Indeed, take any cyclic order of five distinct directions and label its five consecutive cyclic triples. Adjacent labels cannot all differ around this odd cycle. The corresponding four-direction order may therefore be named abcd, and complementing all labels makes h(abc)=h(bcd)=0.

The rearrangement lemma gives h(adc)=h(bad)=0. Let e,f denote the remaining directions. For z in {e,f}, the five-direction orders in the following table force the indicated labels:
| order | forced label |
|---|---|
| abcdz | h(cdz)=1 |
| dcbaz | h(baz)=0 |
| badcz | h(dcz)=1 |
| cdabz | h(abz)=0 |
| abzcd | h(bzc)=1 |
| bazcd | h(azc)=1 |

For example, in cdabz the first two labels are h(cda)=1 and h(dab)=1, by reversal of adc and bad. All table rows follow from the forcing rule and reversal.

There are two cases.

If h(aeb)=0, the order beafc forces h(eaf)=0, since its first and third labels equal 1. The order bfaec then forces h(bfa)=0, so h(afb)=1. In the four-direction order ceaf, the two consecutive labels h(cea) and h(eaf) equal 0. The rearrangement lemma forces h(ecf)=0. In ecfb, the labels h(ecf)=0 and h(cfb)=0 force h(ebf)=0 by the same lemma. Finally fbea has h(fbe)=h(bea)=1, so the lemma forces h(bfa)=1, contradicting h(bfa)=0.

If h(aeb)=1, the order aebfc forces h(ebf)=0. The order afbec forces h(afb)=0. The order bfaec now forces h(fae)=0. In cebf the consecutive labels h(ceb)=0 and h(ebf)=0 force h(ecf)=0 by the rearrangement lemma. In cfae, the consecutive labels h(cfa)=0 and h(fae)=0 force h(fce)=0, contradicting reversal of h(ecf)=0. Both cases contradict the supposition. QED.

**Facet-lifting corollary.** In Q_6, take the five directions of the monochromatic order and let g be the omitted direction. Choose either g-facet and traverse the five directions there. Prepending g produces a full six-direction word b,q,q,q, where b is arbitrary and q is the monochromatic facet color. It has at most one change.

**Applicability and frontier.** This confirms a precise cross-facet mechanism: a reversal-odd coordinate-only labeling on five directions may lack a monochromatic spanning order, whereas extension to six directions forces a monochromatic order on some five-direction subset. The omitted direction may change. The result supplies monochromatic paths of length five inside every six-direction restriction of a larger coordinate-only coloring. It does not yet produce a monochromatic path of length n-1 or a good spanning order in arbitrary dimension. In face-dependent NORI, the rearranged triples occur at different exterior bit assignments; the proof above requires position independence. A general extension must replace those comparisons with compatible face assignments or a justified transport argument.

**Verification.** Every displayed forcing row and each use of the rearrangement lemma was checked symbolically using only the five-direction nonmonochromaticity rule and reversal. The proof itself supplies all deductions.
