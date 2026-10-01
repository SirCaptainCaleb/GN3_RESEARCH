# Every minimum span-three ordering is a deletion-cover ordering in disguise

## Statement

Let H be a minimum counterexample and let pi=(v_1,...,v_n) be any spanning ordering with defect span three. If i is the leftmost defect center, put x=v_{i+1}, P=(v_1,...,v_i), and Q=(v_{i+2},...,v_n). Then P and Q are tight paths, so H-x=P|Q is a deletion cover. The ordering pi is precisely the canonical concatenation P,x,Q. Its two outer join centers i and i+2 are defective; the middle center i+1 is tight or defective according as the associated bounded central bridge has order three or five. Thus the minimum-defect-span interface and the deletion-cover central-bridge interface are the same state space, not two independent routes.

## Body

Because the defect span is three with leftmost center i and rightmost center i+2, there are no defect centers before i or after i+2. Deleting x=v_{i+1} leaves the prefix P=(v_1,...,v_i), all of whose internal consecutive triples have centers at most i-1 and hence are tight, and the suffix Q=(v_{i+2},...,v_n), all of whose internal consecutive triples have centers at least i+3 and hence are tight. Therefore P|Q covers H-x. Re-inserting x between P and Q recovers pi. In a counterexample the centers i and i+2 must be defective, since otherwise x could be absorbed into P or Q and yield a spanning two-cover. If the middle triple (v_i,x,v_{i+2}) is tight, the join window gives the order-three central path from defectspan35direct; if it is defective, boundary antisymmetry gives the reversed order-five central path. Hence the two interfaces coincide.