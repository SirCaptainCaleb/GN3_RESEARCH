// NORI1 Q7 balanced coloring: full integer Gram-minor verification.
// Build: c++ -O2 -std=c++17 nori_q7_cubic_minor_obstruction.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
using namespace std;
constexpr int n=7,V=128,H=64;
constexpr array<uint32_t,n> tab={0x2b6ba977U,0xf01a3f0dU,0x9b855c4eU,
  0x203e3b1aU,0x53f7b024U,0xef3ceb49U,0xf2d0c593U};
int color(int x,int i){
  int ex=(x&((1<<i)-1))|((x>>(i+1))<<i);
  int u=ex<32?ex:(ex^63);
  return int((tab[i]>>u)&1U)^(ex>=32);
}
int main(){
  for(int x=0;x<V;++x){
    int degree=0;
    for(int i=0;i<n;++i){
      int a=color(x,i);degree+=a;
      assert(a==color(x^(1<<i),i));
      assert(a+color(x^127,i)==1);
    }
    assert(degree==3||degree==4);
  }
  array<int,n> pi={0,1,2,3,4,5,6};
  array<int64_t,8> histogram={};
  int64_t min_det=numeric_limits<int64_t>::max();
  int64_t min_2x2=numeric_limits<int64_t>::max();
  int64_t min_m=numeric_limits<int64_t>::max();
  int min_mu_num=10000,max_mu_num=0,orders=0,min_s=0,min_r=0;
  array<int,n> min_order={};
  do{
    ++orders;
    int f[H]={};
    for(int x=0;x<H;++x){
      int y=x,w[n];
      for(int t=0;t<n;++t){w[t]=color(y,pi[t]);y^=1<<pi[t];}
      int g=(w[n-1]==w[0]);
      for(int t=0;t<n-1;++t)g+=(w[t]!=w[t+1]);
      assert(g==1||g==3||g==5||g==7);
      ++histogram[g];f[x]=g;
    }
    for(int len=1;len<H;len*=2)
      for(int a=0;a<H;a+=2*len)
        for(int b=0;b<len;++b){
          int u=f[a+b],v=f[a+b+len];
          f[a+b]=u+v;f[a+b+len]=u-v;
        }
    int64_t m=int64_t(f[0])-3*H;
    min_m=min(min_m,m);
    min_mu_num=min(min_mu_num,f[0]);
    max_mu_num=max(max_mu_num,f[0]);
    for(int s=1;s<H;++s){
      int64_t a=f[s];
      min_2x2=min(min_2x2,m*m-a*a);
      for(int r=s+1;r<H;++r){
        int64_t b=f[r],d=f[s^r];
        int64_t D=m*m*m-m*(a*a+b*b+d*d)+2*a*b*d;
        if(D<min_det){min_det=D;min_order=pi;min_s=s;min_r=r;}
      }
    }
  }while(next_permutation(pi.begin(),pi.end()));
  assert(orders==5040);
  assert(histogram[1]==14728&&histogram[3]==143752&&
    histogram[5]==152152&&histogram[7]==11928);
  assert(min_m==48&&min_mu_num==240&&max_mu_num==272);
  assert(min_2x2==1392&&min_det==12800);
  cout<<"Verified all "<<orders<<" direction orders and 1953 three-character minors per order.\n";
  cout<<"Minimum mean-minus-three numerator: "<<min_m<<" / 64\n";
  cout<<"Minimum 2x2 determinant numerator: "<<min_2x2<<" / 4096\n";
  cout<<"Minimum 3x3 determinant numerator: "<<min_det<<" / 262144\n";
  cout<<"Minimum attained at order:";
  for(int i:min_order)cout<<' '<<i;
  cout<<" and Walsh labels "<<min_s<<','<<min_r<<"\n";
  cout<<"Projective-support grade histogram:";
  for(int g:{1,3,5,7})cout<<" G="<<g<<':'<<histogram[g]/14;
  cout<<"\nAll certificates passed.\n";
}
