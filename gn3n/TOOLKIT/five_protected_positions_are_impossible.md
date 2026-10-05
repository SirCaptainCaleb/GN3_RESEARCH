# Five protected positions are impossible inside one face block

**Summary:** If every chamber of a permutahedron face avoids the two-cover forbidden patterns on a common interval, no face block can contain five consecutive protected vertex positions.

## Statement

Let five consecutive vertex positions lie in one block of a permutahedron face, and suppose every chamber avoids 001, 011, and 0101 on the corresponding protected status interval. Then contradiction. Hence the protected width of any face block is at most four.

## Body

Write h(u,v,w)=1 when (u,v,w) is tight. Five vertices inside one face block may be placed in every order. Protection forbids epsilon_1=0 and epsilon_3=1 simultaneously, so every ordering (a,b,c,d,e) satisfies h(c,d,e)=1 => h(a,b,c)=1. Together with boundary antisymmetry, the seven orderings (20134),(02431),(13024),(03142),(14203),(14302),(20143) give the implication chain h(102)=1 => h(134)=0 => h(024)=1 => h(031)=0 => h(142)=0 => h(203)=0 => h(143)=1 => h(102)=0. Thus h(102)=0. The seven orderings (10234),(01432),(23014),(03241),(24103),(10342),(10243) similarly give h(102)=0 => h(234)=0 => h(014)=1 => h(032)=0 => h(142)=1 => h(103)=0 => h(243)=1 => h(102)=1, contradiction. Therefore five protected positions cannot lie in one block.

## Metadata

- ID: five_protected_positions_are_impossible
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
