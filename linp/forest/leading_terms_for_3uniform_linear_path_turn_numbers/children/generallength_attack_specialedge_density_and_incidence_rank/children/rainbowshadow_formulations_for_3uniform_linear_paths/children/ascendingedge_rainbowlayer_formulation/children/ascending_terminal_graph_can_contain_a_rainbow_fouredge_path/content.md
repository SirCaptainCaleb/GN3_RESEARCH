# Ascending terminal graph can contain a rainbow four-edge path

## Statement

There is a finite linear 3-graph whose terminal-pair graph restricted to ascending edges, colored by the unique entrance vertex of each edge, contains a rainbow path of four edges. Thus the global ascending-edge bound cannot be reduced to forbidding rainbow four-edge paths in that terminal graph.

## Body

Take the nine edges E_0={2,3,9}, E_1={0,5,10}, E_2={0,2,4}, E_3={1,10,11}, E_4={4,7,8}, E_5={0,1,3}, E_6={5,6,7}, E_7={2,7,11}, E_8={1,4,6}. The system is linear. Direct inspection of the induced paths in its intersection graph gives φ(E_0)=φ(E_1)=φ(E_3)=φ(E_7)=5. Their unique entrance vertices are respectively 3,0,1,7, and φ(3)=φ(0)=φ(1)=φ(7)=4, so all four edges are ascending and nonspecial. Explicit longest induced paths ending with these edges are E_4,E_6,E_1,E_5,E_0 for E_0; E_1,E_5,E_8,E_4,E_7 for E_7; E_6,E_4,E_2,E_5,E_3 for E_3; and E_4,E_7,E_0,E_5,E_1 (also E_7,E_4,E_8,E_5,E_1) for E_1. In the ascending terminal graph these four hyperedges give the path 9-2-11-10-5. Its edge colors, namely the entrance vertices, are 3,7,1,0, which are distinct. Hence the path is rainbow.