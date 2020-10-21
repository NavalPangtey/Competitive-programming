#include<bits/stdc++.h>
using namespace std;
void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}
int arr[50];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    read();
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int gg;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            if (arr[i] == 1)gg = i;
        }
        int ans = 0;
        bool flag = false;
        for (int i = 0; i <= gg; i++)
        {
            if (arr[i] == 1)flag = true;

            if (flag == true)
            {
                if (arr[i] == 0)ans++;
            }
        }
        cout << ans << "\n";

    }
}
