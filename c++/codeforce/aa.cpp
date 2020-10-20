#include<bits/stdc++.h>
using namespace std;
int arr[1001];

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
        int a, n, k;
        cin >> n >> k;
        for (int i = 0; i <= n; i++)
        {
            cin >> arr[i];
        }
        sort(arr, arr + n);
        int min = arr[0];
        int f = 0;
        for (int i = 1; i < n; i++)
        {
            f += (k - arr[i]) / min;

        }
        cout << f << "\n";


    }
}
