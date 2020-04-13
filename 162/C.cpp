#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
  if(a<b){
    int tmp=a;
    a=b;
    b=tmp;
  }
  int r = a%b;
  if(r==0){
    return b;
  }else{
    return gcd(b,r);
  }
}
    

int main(){
  int n;cin>>n;
  
  int sum=0;
  for(int i=1;i<=n;i++){
    for(int j=1;j<=n;j++){
       int g=gcd(i,j);
      for(int k=1;k<=n;k++){
       sum+=gcd(g,k);
      }
    }
  }
    
  cout<<sum;
  
  return 0;
}


