# Global flatness still permits exact perfect-blocker transfer — preserved pre-item development

## Composition

(none yet)

## Development


The codimension-two insertion strategy does not close merely from global coboundary flatness.

Take a one-change carrier O=(v_1,...,v_6) with alpha-word 0011. In a tournament representative switched so O is a directed Hamilton path, choose two exterior vertices x,y with scans

s^x = 00001,
s^y = 11100.

Choose the initial pair bit alpha(x,y,v_1) so that the flat switching-class relation

c_i xor c_{i+1} = s_i^x xor s_i^y

holds along O. These data are realizable by a tournament and therefore define a globally coboundary-flat alternating orientation.

The scan s^y=11100 is the unique perfect blocker scan for 0011. Vertex x is individually insertable: prepending x, inserting x after v_4, or appending x yields a one-change carrier.

After each of these successful insertions, the scan of y on the enlarged carrier is exactly the unique perfect blocker scan for the new one-change word:
- for the carriers with word 00011 it becomes 111100;
- for the carrier with word 00111 it becomes 111000.

Thus blocker status can transfer perfectly from a codimension-two carrier to every successful codimension-one extension. A two-vertex induction must rule out finite blocker-transfer cycles; it is not enough to know that two simultaneous perfect blockers cancel.
