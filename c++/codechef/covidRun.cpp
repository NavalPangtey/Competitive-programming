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
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t; cin >> t;

	while (t--)
	{
		int n , k, x, y;
		bool flag = false;
		cin >> n >> k >> x >> y;
		int b = 1000;
		while (b--) {
			x = (x + k) % n;
			if (x == y) {
				flag == true;
				break;
			}
		}
		if (flag == true) cout << "YES" << "\n";
		else cout << "NO" << "\n";

	}
}
