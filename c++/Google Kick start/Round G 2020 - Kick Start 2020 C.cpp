#include<bits/stdc++.h>
using namespace std;


long long arr[1000000];

void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	read();
	int t; cin >> t;
	int tt = 1;
	while (t--)
	{
		long long w, n, ans = 0;
		cin >> w >> n;

		long long mini = 10000000;
		for (int i = 0; i < w; i++)cin >> arr[i];
		for (int i = 1; i <= n; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if ((abs(arr[j] - n) + i) < abs(arr[j] - i))
				{
					ans = ans + abs(arr[j] - n) + i;
				}
				else {
					ans = ans + abs(arr[j] - i);
				}
			}
			cout << ans << endl;
			mini = min(ans, mini);
			ans = 0;

		}
		cout << "Case #" << tt << ": " << mini << endl;
		tt++;

	}
	return 0;

}
