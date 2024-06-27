#include <bits/stdc++.h>
using namespace std;

int main(){
  string N;
  cin >> N;
  char seven = '7';

  for (int i = 0; i < 3; i++) {
    if (N[i] == seven){
      cout << "Yes" << endl;
      return 0;
    }
	}
  cout << "No" << endl;
  return 0;
}
