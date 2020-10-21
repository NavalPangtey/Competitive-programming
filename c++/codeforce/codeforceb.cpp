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
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	read();
	int t;
	cin >> t;
	while (t--)
	{
		int n, m;
		cin >> n >> m;
		bool flag = false;
		for (int i = 0 ; i < n; i++)
		{
			int a, b, c, d;
			cin >> a >> b >> c >> d;
			if (b == c)
			{
				flag = true;
			}

		}
		if ((flag == true) && (m % 2 == 0))
		{
			cout << "YES" << "\n";
		}
		else {
			cout << "NO" << "\n";
		}
	}
}
