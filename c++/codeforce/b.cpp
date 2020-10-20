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

int msb(int n)
{
	int k = (int)(log2(n));
	return k;
}

int main()
{
	read();
	int t;
	cin >> t;
	while (t--)
	{
		int a, n;
		cin >> n;
		unordered_map<int, vector<int>> mp;
		for (int i = 1; i <= n; i++)
		{
			cin >> a;
			int msb_b = msb(a);
			mp[msb_b].push_back(i);
		}
		long long sum = 0;
		for (auto p : mp)
		{
			long long size = p.second.size();
			sum = sum + (size * (size - 1)) / 2;
		}

		cout << sum << "\n";

	}
}
