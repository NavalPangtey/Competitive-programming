#include<bits/stdc++.h>
using namespace std;

vector <int> v[100000];
vector <pair<int, int>> pai;
int visited[100001], in[100001], low[100001];
int timer;
bool flag = true;
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}



void solve()
{
	int x1, y1, x2, y2, ans = 0;
	cin >> x1 >> y1 >> x2 >> y2;

	if (x1 == x2)
	{
		if (y1 == y2)cout << 0 << "\n", return;
		else if (y2 > y1)
		{
			if (x1 > 0)
			{

				while (y1 != y2)
				{
					y1 = y1 + 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}
				cout << ans << "\n";
			}
			else {
				while (y1 != y2)
				{
					y1 = y1 - 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}
				cout << ans << "\n";

			}
		}
	}
	else if (x1 != x2)
	{
		while (y1 != 1)
		{
			if (x1)
			}
	}

}


int main()
{
	read();
	int t; cin >> t;
	while (t--)
	{
		solve();
	}
}
