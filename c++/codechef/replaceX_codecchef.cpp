#include<bits/stdc++.h>
using namespace std;
long long arr[400001];
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
		int n, x, p, k;
		cin >> n >> x >> p >> k;
		for (int i = 1; i <= n; i++)cin >> arr[i];
		sort(arr + 1, arr + n + 1);
		if (n == 0)cout << -1 << "\n";
		else if (arr[p] == x)cout << 0 << "\n";
		else if (k < p)
		{
			if (arr[p] > x)cout << -1 << "\n";
			else {
				int ans = 0;
				for (int i = p; i <= n; i++)
				{
					if (arr[i] < x)ans++;
					if (arr[i] >= x)break;
				}
				cout << ans << "\n";
			}
		}
		else if (p == k)
		{
			if (arr[k] == x)cout << 0 << "\n";
			else {
				int ans = 0;
				if (arr[k] > x)
				{
					for (int i = 1; i <= k; i++)
						if (arr[i] > x)ans++;
					cout << ans << "\n";
				}
				else if (arr[k] < x)
				{	long long temp = arr[k];
					for (int i = k; i <= n; i++)
					{
						if (arr[i] < x)ans++;
						if (arr[i] >= x)break;
					}
					cout << ans << "\n";
				}

			}
		} else
		{
			if (arr[p] < x)cout << -1 << "\n";
			else if (arr[p] > x)
			{	int ans = 0;
				for (int i = 1; i <= p; i++)
				{
					if (arr[i] > x)ans++;
				}
				cout << ans << "\n";
				// else cout << -1 << "\n";
			}
		}
	}
}
