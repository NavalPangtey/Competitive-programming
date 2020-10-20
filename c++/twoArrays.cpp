#include<bits/stdc++.h>
using namespace std;
int arr[100001];

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
		int n, k;
		cin >> n >> k;
		int ans[n];
		for (int i = 0; i < n; i++) cin >> arr[i];
		int count = 1;
		for (int i = 0; i < n; i++)
		{
			if (arr[i] == k / 2 && k % 2 == 0)
			{
				if (count % 2 == 0)
					ans[i] = 0;
				else
					ans[i] = 1;
				count++;

			}
			else if (arr[i] * 2 < k) ans[i] = 1;
			else ans[i] = 0;

		}

		for (int i = 0; i < n; i++) cout << ans[i] << " ";
		cout << "\n";


	}
}
