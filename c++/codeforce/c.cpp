

#include<bits/stdc++.h>
using namespace std;
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int main()
{
	read();
	int t;
	cin >> t;
	while (t--)
	{
		int n, m;
		cin >> n ;
		int ans = 1e9;
		for (int i = 1; i * i <= n; i++)
		{
			ans = min(ans, (i - 1) + ((n - i) + i - 1) / i);

		}
		cout << ans << "\n";
	}
}
