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
		int n, k;
		cin >> n >> k;

		if ( n <= 2)
			cout << 1 << endl;
		else
		{
			n -= 2;
			int c = (n) / k;
			if (n % k != 0)
				c++;
			cout << c + 1 << endl;
		}


	}
}
