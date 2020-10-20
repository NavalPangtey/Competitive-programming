#include<bits/stdc++.h>
using namespace std;


int mat[1000][1000];

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
		long long n, ans = 0;
		cin >> n;
		long long maxi = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> mat[i][j];
			}
		}
		for (int j = 0; j < n; j++)
		{	int u = 0;
			int v = j;
			while (u < n && v < n)
			{
				ans = ans + mat[u][v];

				u = u + 1;
				v = v + 1;
			}
			maxi = max(maxi, ans);
			ans = 0;
		}
		for (int j = 0; j < n; j++)
		{	int u = j;
			int v = 0;
			while (u < n && v < n)
			{
				ans = ans + mat[u][v];
				u = u + 1;
				v = v + 1;
			}
			maxi = max(maxi, ans);
			ans = 0;
		}

		cout << "Case #" << tt << ": " << maxi << endl;
		tt++;

	}
	return 0;

}
