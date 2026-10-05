# A protected good band forces thin face blocks

**Summary:** A common forbidden-pattern-free status interval cannot contain two disjoint three-position windows internal to face blocks; hence at most one block has protected width at least three, and that width is at most five.

## Statement

Let F be a permutahedron face and J an interval of status positions such that every chamber avoids 001, 011, and 0101 on J. Then no i<j in J with j-i>=3 can have both vertex windows i..i+2 and j..j+2 lying wholly inside face blocks. Consequently at most one block has protected width at least three, and no block has protected width at least six.

## Body

If two such internal windows existed, [[disjoint_status_windows_form_boolean_cubes]] would give a chamber with epsilon_i=0 and epsilon_j=1. Since j-i>=3, [[two_cover_words_avoid_three_local_patterns]] forces 001, 011, or 0101 between i and j, contradicting that J is protected. Two distinct blocks with internal protected triple windows would therefore be impossible. A single block with six protected vertex positions contains two disjoint internal triple windows, also impossible.

## Metadata

- ID: protected_good_band_forces_thin_face_blocks
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
