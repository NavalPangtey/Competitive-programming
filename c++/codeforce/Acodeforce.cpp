#include<bits/stdc++.h>
using namespace std;



int arr[50000];

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
		int a, n;
		cin >> n;
		bool flag = false;
		for (int i = 0; i < n; i++)
		{
			cin >> a;
			arr[i] = a;
			if (i >= 1)
			{
				if (arr[i - 1] <= arr[i])
					flag = true;
			}
		}

		if (flag == true)
		{
			cout << "Yes" << "\n";
		}
		else
		{
			cout << "NO" << "\n";
		}

	}
}
