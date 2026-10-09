# Globally longest good cube geodesics have exactly one switch and forced opposite-phase blockers at both ends

# Global LONGEST ≤1-switch geodesics have two-sided antipodal snake blockers

Let n>=5 and c be arbitrary active NORI coloring of actual ordered 3-faces with c(bar F,reverse pi)=1-c(F,pi). Define a GOOD direction-distinct cube geodesic as one whose ordered three-face window color word has at most ONE change; no antipodality/ full dimension requirement for shorter paths. Assume the unrestricted GRAND conjecture fails. Choose P to have globally MAXIMUM edge length k among all GOOD geodesics in the whole Q_n (all roots, supports, direction orders). Then 4<=k<=n−1. Write
 P: x -- (p_1,...,p_k) --> y,
its ordered-three-face window colors as q repeated s times followed by r repeated t times, with s,t>=1 and q≠r, s+t=k−2. Let a=p_(k−1), b=p_k, initial α=p_1, β=p_2 and T=[n]\{p_1,...,p_k}, m=n−k>=1.

**THEOREM (TWO-SIDED GOOD-SNAKE BLOCKER LAW).** P NECESSARILY has EXACTLY ONE color switch. For every missing direction d∈T, the physical three-face windows at the two ends are FORCED:
   c(F_y({a,b,d});(a,b,d)) = q = 1−r;
   c(F_x({d,α,β});(d,α,β)) = r = 1−q.
Consequently the genuine full-direction-distinct (k+1)-edge geodesics
   P followed by d (root x) have color word q^s r^t q;
   d followed by P (root x xor d) have color word r q^s r^t.
Both have EXACTLY TWO switches, with the same ACTUAL interior P window colors. Their new root locations are distinct because prepending d begins at x xor d, and both paths are actual cubes, not abstract words. Under active antipodal reversal these blocked caps give the dual certified incoming and outgoing three-face fans:
   c(F_bar_y({a,b,d});(d,b,a))=r;
   c(F_bar_x({d,α,β});(β,α,d))=q.
The terminal r-colored opposite-corner incoming snake of P lies in a Boolean T-root cube, and the initial r-colored prepend 3-face fan is at the OTHER endpoint.

**PROOF.** If the maximal good P were MONOCHROMATIC, any unused direction d could be appended; it creates exactly one new window, so the resulting (k+1)-edge path would still have at most one switch, contradicting maximality. Hence P is genuinely q^s r^t with q≠r. Appending d creates exactly one new physical window (a,b,d). If this were color r, the longer path would still be good, contradiction. Therefore its color is 1−r=q. Prepending d from root x xor d creates exactly one new physical window (d,α,β) and leaves the original P window sequence on the SAME physical faces (because the new first step d ends at x); if it were q, the longer path would remain good, contradiction. Therefore its color is 1−q=r. Reversing at antipodal physical faces gives the dual colors. The proof uses neither any claimed long mono path nor a freely reorderable tail. QED.

**NEAR-FULL n−1 CASE.** If k=n−1 then T={d} and bar y=x xor d (since y=x xor ([n]\{d})). Thus the prepended full path d+P starts EXACTLY AT bar y, while the appended full path P+d begins at x. Their color words are forced r q^s r^t and q^s r^t q, respectively, with two switches. Meanwhile the global antipodal reversal ΘP starts at bar y and has complementary reversed window word q^t r^s. This gives a concrete *two-by-two antipodal rectangle of full/near-full cube paths* where the two end-caps are opposite phases. The geometry does NOT by itself imply a good full path, because the cap free-coordinate triples at two ends differ and their colors can be independently assigned consistently with the oddness axiom when all directions of P are distinct.

**EXACT LIMITATION.** A longest good path P gives an opposite-corner fan in its LAST phase r, whereas its FIRST phase q differs. In contrast to the monochromatic maximal-path fan, splicing a fan branch through P_s would generally make TWO switches, not one. Thus neither the maximal-q rank bound nor its top-rank extraction transfers automatically to globally maximal *good* paths. To find a genuine descent, use a new defect measure that tracks both phases and both endpoint ordered pairs.

**GLOBAL STRATEGIC VALUE.** This is the proper maximal-defect analogue of the Devine–Milans snake method, directly about the target property rather than only about monochromatic paths: a hypothetical counterexample produces mandatory, bidirectional, oppositely colored extension walls at BOTH ends of a globally longest good partial cube geodesic. Progress requires constructing an extension or root exchange that breaks one wall while preserving one-switch coloring. The theorem does not solve unrestricted grand closure.
