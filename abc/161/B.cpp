#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  int sumAll;
  for(int i=0; i<n; i++){
    cin >> a[i];
    sumAll = sumAll + a[i];
  }
  sort(a.begin(), a.end(), greater<int>());

  int count;

  for(int i=0; i<n; i++){
    if(a[i] >= sumAll/(4.0*m)){
      count++;
    }
  }

  if(count >= m) {
    cout <<"Yes"<< endl;
  }else{
    cout <<"No"<< endl;
  }
  return 0;
}

