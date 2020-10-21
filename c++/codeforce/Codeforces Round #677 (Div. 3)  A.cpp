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
        int x;
        cin >> x;
        int m = x % 10;
        int ans = 10 * (m - 1);
        int cont = 0;
        while (x > 0)
        {
            x = x / 10;
            cont++;
        }
        if (cont == 1)ans += 1;
        if (cont == 2)ans += 3;
        if (cont == 3)ans += 6;
        if (cont == 4)ans += 10;
        cout << ans << "\n";

    }
}
