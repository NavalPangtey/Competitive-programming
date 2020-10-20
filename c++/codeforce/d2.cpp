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
	int n, k, p;
	cin >> n;
	int arr[n];
	for (int i = 0; i < n; i++)
	{
		cin >> k; arr[i] = k;
	}

	sort(arr, arr + n);
	p = n / 2;
	int arr2[n], x = 0, y = p;
	for (int i = 0 ; i < n; i++)
	{
		if (i & 1 == 1)
		{
			arr2[i] = arr[x];
			x++;
		}
		else
		{
			arr2[i] = arr[y];
			y++;
		}

	}
	int count = 0;
	for (int i = 1; i < n - 1; i++)
	{
		if (arr2[i] < arr2[i - 1] && arr2[i] < arr2[i + 1])
		{
			count++;
		}
	}
	cout << count << "\n";
	for (int i = 0; i < n; i++)
	{
		cout << arr2[i] << " ";
	}



}
