#include <bits/stdc++.h>
using namespace std;

int main() {
  long N;
  cin >> N;
  vector<long> ans;


  for (long i = 1; i <= N; i++) {
    if (i % 3 == 0 && i % 5 == 0)  // iが3の倍数かつ5の倍数
      ans.push_back(0);
    else if (i % 3 == 0)  // iが3の倍数(かつ、5の倍数でない)
      ans.push_back(-1);
    else if (i % 5 == 0)  // iが5の倍数(かつ、3の倍数でない)
      ans.push_back(-1);
    else  // iが3の倍数でも5の倍数でもない
      ans.push_back(i);
  }

  long sum = 0;
  long cnt = 0;

  for (long i = 0; i <= N; i++){
    if (ans[i] == 0) {
      cnt += 1;
      if (cnt == N){
        break;
      }
    }else if(ans[i] == -1) {
      continue;
    }else {
      sum += ans[i];
    }
  }
  cout << sum << endl;
  return 0;
}
