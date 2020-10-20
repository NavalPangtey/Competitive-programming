#include<bits/stdc++.h>
using namespace std;
int arr[101];
int a[101], b[101], c[101];
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
		int n;
		cin >> n;
		for (int j = 0; j < 3; j++)
		{
			for (int i = 0; i < n; i++)
			{
				if (j == 0)cin >> a[i];
				else if (j == 1)cin >> b[i];
				else if (j == 2)cin >> c[i];
			}
		}
		int temp = a[0];
		arr[0] = a[0];
		for (int i = 1; i < n; i++)
		{
			if (a[i] != temp)arr[i] = a[i], temp = a[i];
			else if (b[i] != temp)arr[i] = b[i], temp = b[i];
			else if (c[i] != temp)arr[i] = c[i], temp = c[i];
		}

		if (arr[0] == arr[n - 1])
		{
			if (a[n - 1] != arr[0] && a[n - 1] != arr[n - 2]) arr[n - 1] = a[n - 1];
			if (b[n - 1] != arr[0] && b[n - 1] != arr[n - 2]) arr[n - 1] = b[n - 1];
			if (c[n - 1] != arr[0] && c[n - 1] != arr[n - 2]) arr[n - 1] = c[n - 1];
		}
		for (int i = 0; i < n; i++)
		{
			cout << arr[i] << " ";
		}
		cout << endl;
	}
}
