#include <bits/stdc++.h>
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    long long t, n, count, x, i, m;
    cin >> t;
    while (t > 0)
    {   count = 0;
        i = 1;
        cin >> n;
        while (n > 0)
        {
            x = pow(2, i) - 1;
            m = (x * (x + 1)) / 2;
            n = n - m;
            if (n < 0)
            {
                break;
            }
            count++;
            i++;
        }
        cout << count << "\n";

        t--;
    }


}
