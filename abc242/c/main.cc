#include<bits/stdc++.h>
using namespace std;
int const N = 1e6 + 10;
int const mod = 998244353;
long long dp[N][10], n, ans;

int main(){
	cin >> n;
	for(int i = 1; i <= 9; i++) dp[1][i] = 1;
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= 9; j++){
      //その桁の数字はそれぞれ絶対値1の範囲での通りの合計できまるから前回結果を使いまわせる漸化式を作れる。
      //ちなみにこれはもらうdpね
			//dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1];
			dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1];
      //逆元ねココ
			dp[i + 1][j] %= mod;	
		}
	}
	
	for(int i = 1; i <= 9; i++) ans += dp[n][i];
	cout << ans % mod;
	return 0;
}
