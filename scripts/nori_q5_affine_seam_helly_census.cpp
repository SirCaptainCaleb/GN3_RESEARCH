// Exhaustive Q5 affine seam-root Helly census. Compile: g++ -O3 -std=c++17 file.cpp
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
struct Path {
 uint32_t fixedmask, need[2];
 uint8_t root, a[2], b[2];
};
vector<Path> paths;
int id[5][32],sg[5][32];
void setup(){
 int slot[5][32];fill(&slot[0][0],&slot[0][0]+160,-1);
 int total=0;
 for(int d=0;d<5;d++)for(int x=0;x<32;x++){
  int a=x&~(1<<d),b=(a^31)&~(1<<d),p=min(a,b);
  if(slot[d][p]<0)slot[d][p]=total++;
  id[d][x]=slot[d][p];sg[d][x]=(a!=p);
 }
 if(total!=40)abort();
 for(int root=0;root<16;root++){
  array<int,5> pi={0,1,2,3,4};
  do{
   int x=root,r=-1,ei[2],es[2];
   uint32_t fm=0,req=0;
   for(int d:pi){
    if(d==4)r=min(x&15,(x&15)^15);
    if(d<2){ei[d]=id[d][x];es[d]=sg[d][x];}
    else{int k=id[d][x]-16;fm|=1u<<k;req|=uint32_t(sg[d][x])<<k;}
    x^=1<<d;
   }
   paths.push_back({fm,{req,req^fm},(uint8_t)r,
     {(uint8_t)(2*ei[0]+es[0]),(uint8_t)(2*ei[0]+1-es[0])},
     {(uint8_t)(2*ei[1]+es[1]),(uint8_t)(2*ei[1]+1-es[1])}});
  }while(next_permutation(pi.begin(),pi.end()));
 }
 if(paths.size()!=1920)abort();
}
struct Imp {uint32_t arcs[32];};
void formula(uint32_t fixed,Imp out[8]){
 for(int r=0;r<8;r++)fill(out[r].arcs,out[r].arcs+32,0);
 for(auto const& p:paths)for(int t=0;t<2;t++)
  if((fixed&p.fixedmask)==p.need[t]){
   int a=p.a[t],b=p.b[t];
   out[p.root].arcs[a]|=1u<<(b^1);
   out[p.root].arcs[b]|=1u<<(a^1);
  }
}
bool contradiction(const Imp g[8],int x,int y,int z=-1){
 uint32_t reach[32];
 for(int v=0;v<32;v++)
  reach[v]=g[x].arcs[v]|g[y].arcs[v]|
    (z<0?0:g[z].arcs[v])|(1u<<v);
 for(int k=0;k<32;k++)for(int v=0;v<32;v++)
  if(reach[v]&(1u<<k))reach[v]|=reach[k];
 for(int v=0;v<16;v++)if((reach[2*v]&(1u<<(2*v+1)))&&
    (reach[2*v+1]&(1u<<(2*v))))return true;
 return false;
}
int main(){
 setup();int count0=0,tworoot=0,threeroot=0;
 for(int q2=0;q2<16;q2++)for(int q3=0;q3<16;q3++)
 for(int q4=0;q4<16;q4++){
  int q[3]={q2,q3,q4},coeff[3]={},constant[3]={};
  uint32_t mask=0;
  for(int d=2;d<5;d++){
   int bits=q[d-2]/2,par=0,k=0;
   constant[d-2]=q[d-2]&1;
   for(int j=0;j<5;j++)if(j!=d){
    int v=(k<3)?((bits>>k)&1):(par^1);
    coeff[d-2]|=v<<j;par^=v;k++;
   }
   for(int x=0;x<32;x++)if(!(x&(1<<d))){
    int lo=x&~(1<<d),hi=(lo^31)&~(1<<d);
    if(lo>hi)continue;
    int color=constant[d-2]^(__builtin_popcount((unsigned)(x&coeff[d-2]))&1);
    mask|=uint32_t(color)<<(id[d][x]-16);
   }
  }
  Imp g[8];formula(mask,g);
  int pairs=0;
  for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)
   pairs+=contradiction(g,i,j);
  bool exceptional=false;
  for(int u=0;u<2;u++){
   bool f2=coeff[0]==(1<<u),f3=coeff[1]==(1<<(1-u));
   bool f4=(coeff[2]==coeff[0]&&(constant[2]^constant[0])==1)||
           (coeff[2]==coeff[1]&&(constant[2]^constant[1])==1);
   exceptional|=f2&&f3&&f4;
  }
  if((pairs==0)!=exceptional){
   printf("ERROR: %06x pairs=%d predicted=%d\n",mask,pairs,exceptional);return 1;
  }
  if(pairs){tworoot++;continue;}
  count0++;bool triple=false;
  for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)
   for(int k=j+1;k<8;k++)triple|=contradiction(g,i,j,k);
  if(!triple){printf("UNRESOLVED %06x\n",mask);return 1;}
  threeroot++;
 }
 if(count0!=16||tworoot!=4080||threeroot!=16)return 1;
 printf("PASS: 4096 affine Q5 partial colorings; 4080 have forcing root pair; 16 require three roots.\n");
}