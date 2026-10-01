# Every eight-vertex boundary tournament has adjacent Hamiltonian four-windows

## Statement

Every boundary tournament on eight vertices contains two distinct Hamiltonian four-vertex sets whose intersection has order three.

## Body

By balanced8_structural01 and its multiplicity strengthening balanced8_multiplicity7_01, choose seven distinct Hamiltonian 4|4 partitions. Their fourteen sides are distinct and complement-paired. If two chosen sides meet in three vertices, we are done. Otherwise their 56 triples are all distinct, so they form a complement-paired 3-(8,4,1) block family. Under the no-overlap assumption these fourteen are all Hamiltonian four-sets, since any additional Hamiltonian four-set would share one of its triples with the unique selected block containing that triple. Now fix a vertex pair {u,v}. The 14-block family has exactly three blocks through {u,v}. But bd3c8d17ca06 partitions the other six vertices into two fixed-pair orientation classes, and every same-class pair completes {u,v} to a Hamiltonian four-set. If the class sizes are s and 6-s, the number of such Hamiltonian four-sets is C(s,2)+C(6-s,2)>=6, contradiction. Therefore two Hamiltonian four-sets meet in three vertices.