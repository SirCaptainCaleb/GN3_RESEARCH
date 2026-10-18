// NORI1 Q5: exhaustive two-direction parity-diamond census.
// g++ -O3 -std=c++17 -fopenmp nori_q5_parity_census.cpp -o census
// OMP_NUM_THREADS=5 ./census
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <tuple>
#include <vector>
#include <omp.h>

struct Pattern {
    uint32_t test,want;
    uint8_t a,p,b,q;
    bool operator<(const Pattern& z)const{
        return std::tie(test,want,a,p,b,q)<std::tie(z.test,z.want,z.a,z.p,z.b,z.q);
    }
    bool operator==(const Pattern& z)const{
        return std::tie(test,want,a,p,b,q)==std::tie(z.test,z.want,z.a,z.p,z.b,z.q);
    }
};
std::vector<Pattern> generate(){
    int index[5][32],sign[5][32],lookup[160];
    std::fill(lookup,lookup+160,-1);
    int num=0;
    for(int d=0;d<5;d++)for(int x=0;x<32;x++){
        int lo=x&~(1<<d),hi=(x^31)&~(1<<d),rep=std::min(lo,hi);
        int key=d*32+rep;
        if(lookup[key]<0)lookup[key]=num++;
        index[d][x]=lookup[key];
        sign[d][x]=(lo!=rep);
    }
    if(num!=40)std::abort();
    std::vector<Pattern> out;
    for(int x=0;x<16;x++){
        std::array<int,5> p={0,1,2,3,4};
        do{
            int y=x,ids[5],sg[5];
            for(int d:p){
                ids[d]=index[d][y];sg[d]=sign[d][y];y^=1<<d;
            }
            uint32_t test=0;
            for(int d=2;d<5;d++)test|=1u<<(ids[d]-16);
            for(int t=0;t<2;t++){
                uint32_t want=0;
                for(int d=2;d<5;d++)want|=uint32_t(t^sg[d])<<(ids[d]-16);
                out.push_back({test,want,(uint8_t)ids[0],(uint8_t)(t^sg[0]),
                               (uint8_t)(ids[1]-8),(uint8_t)(t^sg[1])});
            }
        }while(std::next_permutation(p.begin(),p.end()));
    }
    std::sort(out.begin(),out.end());
    out.erase(std::unique(out.begin(),out.end()),out.end());
    if(out.size()!=1920)std::abort();
    return out;
}
int diamonds(uint32_t mask,const std::vector<Pattern>& data){
    uint16_t C[8][2]={};
    for(const auto& d:data)if((mask&d.test)==d.want)
        C[d.a][d.p]|=uint16_t(1u<<(2*d.b+d.q));
    uint8_t R[8][8]={};
    for(int a=0;a<8;a++){
        uint16_t x=C[a][0],y=C[a][1];
        if(!x||!y)continue;
        for(int b=0;b<8;b++){
            unsigned xb=(x>>(2*b))&3,yb=(y>>(2*b))&3;
            if(!(xb|yb))continue;
            for(int c=b+1;c<8;c++){
                unsigned u=(y>>(2*c))&3,v=(x>>(2*c))&3,h=R[b][c];
                if(xb&1){if(u&1)h|=1;if(u&2)h|=2;}
                if(xb&2){if(u&1)h|=4;if(u&2)h|=8;}
                if(yb&1){if(v&1)h|=1;if(v&2)h|=2;}
                if(yb&2){if(v&1)h|=4;if(v&2)h|=8;}
                R[b][c]=uint8_t(h);
            }
        }
    }
    int total=0;
    for(int b=0;b<8;b++)for(int c=b+1;c<8;c++)total+=(R[b][c]==15);
    return total;
}
int main(){
    auto data=generate();
    std::array<uint64_t,29> hist={};
    std::vector<uint32_t> minimizers;
    constexpr int M=1<<24;
    #pragma omp parallel
    {
        std::array<uint64_t,29> local={};
        std::vector<uint32_t> minimal;
        #pragma omp for schedule(static)
        for(int m=0;m<M;m++){
            int d=diamonds(uint32_t(m),data);
            local[d]++;
            if(d<=4)minimal.push_back(uint32_t(m));
        }
        #pragma omp critical
        {
            for(int k=0;k<29;k++)hist[k]+=local[k];
            minimizers.insert(minimizers.end(),minimal.begin(),minimal.end());
        }
    }
    uint64_t sum=0;
    for(int k=0;k<29;k++){
        if(hist[k])std::printf("diamonds %d: %llu\n",k,(unsigned long long)hist[k]);
        sum+=hist[k];
    }
    if(sum!=M||hist[0]||hist[1]||hist[2]||hist[3]||hist[4]!=104){
        std::fprintf(stderr,"census mismatch\n");return 1;
    }
    std::sort(minimizers.begin(),minimizers.end());
    std::printf("TOTAL=%llu MIN=4 COUNT=%zu\n",(unsigned long long)sum,minimizers.size());
    std::printf("MIN_MASKS=");
    for(uint32_t m:minimizers)std::printf("%06x,",m);
    std::printf("\n");
}