# Dimension-nine counterexample to the physical ordered-three-face NORI conjecture

# A dimension-nine counterexample to the physical NORI conjecture

## Theorem

There exists a binary coloring of **physical ordered three-faces** of \(Q_9\) obeying
\[
c(\bar F,(w,v,u))=1-c(F,(u,v,w))
\]
for which **every** full antipodal geodesic has at least two color changes in its seven ordered-three-face windows. Thus the unrestricted, unrooted NORI grand conjecture is false already in dimension nine.

The proof is an explicit construction with a finite certificate of only 2,016 cases (56 binary class words, nine sentinel positions, two sentinel start bits, and two possible middle-sentinel colors). The enumeration below checks both middle-sentinel colors adversarially, making its conclusion independent of the chosen tie-break ordering.

## The coloring

Partition the nine coordinate directions as \(V=A\sqcup B\sqcup\{s\}\), where \(|A|=3\), \(|B|=5\), and \(s\) is a distinguished sentinel direction. Fix an arbitrary strict total order \(<\) on the eight directions in \(D=A\sqcup B\). Give directions in \(A\) type \(0\) and directions in \(B\) type \(1\), and write \(\tau:D\to\{0,1\}\).

Define the reversal-even ternary rule
\[
h(a,b,c)=\mathbf1_{\{(a,b,c)=(0,0,0)\ \text{or}\ [b=1\ \text{and}\ (a=0\text{ or }c=0)]\}},
\qquad h(a,b,c)=h(c,b,a).
\tag{1}
\]
For each physical ordered three-face \((F,(u,v,w))\), set
\[
c(F,(u,v,w))=
\begin{cases}
z_s(F)\oplus h(\tau(u),\tau(v),\tau(w)),& u,v,w\in D,\\
1,&u=s,\\
0,&w=s,\\
\mathbf1_{\{u>w\}},&v=s.
\end{cases}
\tag{2}
\]
Here \(z_s(F)\) is the fixed \(s\)-coordinate when \(s\notin\{u,v,w\}\). In the last three cases \(s\) is one of the varying directions, so no \(s\)-bit is needed. These cases are mutually exclusive. The rule is independent of any traversal corner within \(F\).

**Lemma 1 (legality).** The coloring in (2) satisfies the physical ordered-face antipodal-reversal law.

*Proof.* For triples avoiding \(s\), complementation flips the fixed bit \(z_s(F)\), and reversal leaves \(h\) unchanged. For triples containing \(s\) at an endpoint, reversal interchanges the constant values \(1\) and \(0\). For triples containing \(s\) in the middle, reversal interchanges distinct outside directions \(u,w\), and \(\mathbf1_{\{u>w\}}\oplus\mathbf1_{\{w>u\}}=1\). These cases exhaust all faces. \(\square\)

## Finite forcing lemma

For a word \(q=(q_1,\ldots,q_8)\in\{0,1\}^8\) with exactly three zeros and five ones, insert the sentinel symbol \(s\) at any position \(k\in\{1,\ldots,9\}\). Regard the resulting nine-letter word as a direction order. Choose a starting \(s\)-bit \(z\in\{0,1\}\), and an arbitrary \(\varepsilon\in\{0,1\}\) for the unique length-three window in which \(s\) is middle (if that window exists).

Give a length-three window avoiding \(s\) color \(h\) of its three letters, XOR \(z\) before the \(s\)-step, and XOR \(1-z\) after the \(s\)-step. Give windows containing \(s\) color \(1\) if \(s\) is first, \(0\) if \(s\) is last, and \(\varepsilon\) if \(s\) is middle.

**Lemma 2 (2,016-case certificate).** Every such seven-bit window-color word has at least two changes. More precisely, taking the minimum over all 56 words \(q\), both \(z\), and both \(\varepsilon\), the minima by sentinel position \(k=1,\ldots,9\) are
\[
(3,2,2,2,2,2,2,2,3).
\tag{3}
\]

*Proof.* The following self-contained Python 3 program exhausts all \(\binom83=56\) possible class words and all \(9\cdot2\cdot2\) insertion parameters. The first loop visits every possible triple of zero positions, the second loop every sentinel position, and the last two loops both binary choices. The window clauses implement exactly (1)--(2), so every relevant color comparison is evaluated. It computes the minima (3).

```python
from itertools import combinations

def h(a, b, c):
    return int((a == b == c == 0)
               or (b == 1 and (a == 0 or c == 0)))

minimum = [7] * 9
histogram = [0] * 7

for zeros in combinations(range(8), 3):
    q = [1] * 8
    for i in zeros:
        q[i] = 0
    for k in range(9):
        p = q[:k] + [2] + q[k:]   # sentinel = 2
        for z in (0, 1):
            for eps in (0, 1):
                colors = []
                for j in range(7):
                    a, b, c = p[j:j + 3]
                    if 2 not in (a, b, c):
                        colors.append(z ^ int(k < j) ^ h(a, b, c))
                    elif a == 2:
                        colors.append(1)
                    elif c == 2:
                        colors.append(0)
                    else:
                        colors.append(eps)
                switches = sum(colors[j] != colors[j + 1]
                               for j in range(6))
                minimum[k] = min(minimum[k], switches)
                histogram[switches] += 1

assert minimum == [3, 2, 2, 2, 2, 2, 2, 2, 3]
assert histogram == [0, 0, 112, 524, 812, 484, 84]
```

In particular no word with at most one switch occurs. The reported histogram independently specifies the entire 2,016-case distribution and provides an additional arithmetic check. \(\square\)

## From the finite lemma to every physical geodesic

Fix any starting vertex \(x\in Q_9\) and any ordering \(p\) of the nine distinct coordinate directions. Delete \(s\) from \(p\) and replace the eight remaining directions by their types; this gives a word \(q\) with three zeros and five ones. The position of \(s\) in \(p\) is \(k\), and its initial bit is \(z=x_s\).

For a window avoiding \(s\), its physical face has \(s\)-coordinate fixed at \(z\) before the \(s\)-move and \(1-z\) after that move. Therefore its color in (2) is precisely the color specified in Lemma 2. For a window containing \(s\), the first/last sentinel clauses of (2) likewise agree with Lemma 2. If \(s\) is middle, (2) selects one definite value \(\varepsilon\in\{0,1\}\) by comparing the two adjacent, distinct directions. Lemma 2 allows *either* value.

Consequently the actual seven-window color word of **every** rooted full antipodal geodesic appears among the finite words of Lemma 2 and has at least two changes. The starting vertex and full direction order were arbitrary, proving the theorem. \(\square\)

## Scope and relation to earlier constructions

This is an **unrooted counterexample in the exact active physical ordered-three-face model**. Its face color does not depend on traversal corner, and its legality uses antipodal reversal rather than ordinary reversal. The earlier \(Q_{15}\) three-class construction also provides a correct, independent finite certificate but is superseded as a dimension bound. Unconditional positive results in dimensions five and six remain true. This proof makes no minimal-dimension claim, and leaves dimensions seven and eight for separate consideration.

The structural obstruction is a reversal-even local direction-word rule shielded by one exterior sentinel bit; the sentinel-containing triples satisfy global oddness via order reversal, while the class-word switch constraints survive every possible sentinel insertion. This is a globally physical counterexample and removes the extraction premise of the proposed universal NORI theorem.

## Independent exhaustive physical-cube verification

Composition version 1 was independently audited in session session_nori_r4584_4. A separately written C++ implementation uses the literal triple truth table (1,0,1,1,0,0,1,0), labels A={0,1,2}, B={3,4,5,6,7}, s=8, and compares ordinary coordinate labels for the middle-sentinel clause. It checks all 32,256 ordered physical faces for antipodal-reversal oddness and all 258,048 choices of a face and traversal corner for corner independence. It then constructs the actual ten cube vertices of each of the 512 * 9! = 185,794,560 rooted full geodesics, derives each window's fixed-one mask by intersecting its four vertices, and evaluates its color directly. This enumeration uses no reduction to class words and no SAT solver.

The exact numbers of full rooted geodesics with 0 through 6 switches are respectively (0, 0, 10137600, 48476160, 75018240, 44421120, 7741440). The minima by sentinel position are (3,2,2,2,2,2,2,2,3). A minimum witness starts at the all-zero vertex with order (0,1,2,3,8,4,5,6,7) and color word 1000111. Independently reimplementing the reduced class-word check also reproduced the stated 2,016-case histogram. Thus the construction satisfies the exact physical-face hypotheses and excludes good full paths at every root.

Reproducible independent verifier (C++17; compile with optimization):

```cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
using namespace std;
// Physical face is encoded by its free-coordinate mask and fixed-one mask.
int color(int a,int b,int c,int fixed){
 if(a==8) return 1;
 if(c==8) return 0;
 if(b==8) return a>c;
 int A=a<3?0:1,B=b<3?0:1,C=c<3?0:1;
 // Explicit truth table indexed by the three class bits.
 const int table[8]={1,0,1,1,0,0,1,0};
 return ((fixed>>8)&1)^table[4*A+2*B+C];
}
int main(){
 long long faces=0,corners=0;
 for(int a=0;a<9;a++)for(int b=0;b<9;b++)for(int c=0;c<9;c++){
  if(a==b||a==c||b==c) continue;
  int free=(1<<a)|(1<<b)|(1<<c),outside=511^free;
  for(int fixed=0;fixed<512;fixed++)if((fixed&free)==0){
   int value=color(a,b,c,fixed);
   assert(value==0||value==1);
   assert(color(c,b,a,fixed^outside)==1-value);
   faces++;
   for(int bits=free;;bits=(bits-1)&free){
    int root=fixed|bits;
    assert(color(a,b,c,root&outside)==value);corners++;
    if(bits==0)break;
   }
  }
 }
 array<int,9> p={0,1,2,3,4,5,6,7,8};
 array<long long,7> hist={};array<int,9> mins;mins.fill(7);
 long long paths=0;int witnessRoot=-1;array<int,9>witness;array<int,7>wcolors;
 do{
  int slot=find(p.begin(),p.end(),8)-p.begin();
  for(int root=0;root<512;root++){
   // Traverse actual cube vertices. Derive each face from its four vertices.
   array<int,10> v;v[0]=root;
   for(int j=0;j<9;j++)v[j+1]=v[j]^(1<<p[j]);
   assert(v[9]==(root^511));
   array<int,7> colors;
   for(int j=0;j<7;j++){
    int free=v[j]^v[j+3];
    int fixed=v[j]&v[j+1]&v[j+2]&v[j+3];
    assert((fixed&free)==0);
    colors[j]=color(p[j],p[j+1],p[j+2],fixed);
   }
   int changes=0;for(int j=1;j<7;j++)changes+=(colors[j]!=colors[j-1]);
   assert(changes>=2);hist[changes]++;paths++;mins[slot]=min(mins[slot],changes);
   if(changes==2&&witnessRoot<0){witnessRoot=root;witness=p;wcolors=colors;}
  }
 }while(next_permutation(p.begin(),p.end()));
 cout<<"ordered physical faces "<<faces<<"; corner checks "<<corners<<"; full rooted paths "<<paths<<"\n";
 cout<<"histogram ";for(auto x:hist)cout<<x<<' ';cout<<"\nminima ";for(auto x:mins)cout<<x<<' ';
 cout<<"\nwitness root "<<witnessRoot<<" order ";for(auto x:witness)cout<<x<<' ';cout<<" colors ";for(auto x:wcolors)cout<<x;cout<<'\n';
}

```
