#include<bits/stdc++.h>
using namespace std;
void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}
long long arr[300000];

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
        set <int> s;
        int ans = 0;
        int maxi = 0;
        int jj;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            s.insert(arr[i]);
            if (arr[i] > maxi)
            {
                maxi = arr[i];

            }

        }
        if (s.size() == 1)ans = -1;
        else {
            for (int i = 0; i < n; i++)
            {
                if ( arr[i] == maxi)
                {
                    if (i - 1 >= 0 && arr[i - 1] < maxi)
                    {
                        jj = i;
                        break;
                    }
                    else if (arr[i + 1] < maxi && i + 1 < n)
                    {
                        jj = i;
                        break;
                    }
                }

            }
            ans = jj + 1;
        }

        cout << ans << "\n";

    }
}
