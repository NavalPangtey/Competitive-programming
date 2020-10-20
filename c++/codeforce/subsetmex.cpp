
#include <bits/stdc++.h>
using namespace std;
int calculateMex(unordered_set<int> Set)
{
    int Mex = 0;

    while (Set.find(Mex) != Set.end())
        Mex++;

    return (Mex);
}
void solve()
{

    int n, v;
    unordered_set<int> Set;
    unordered_set<int> Set2;
    cin >> n;
    for ( int i = 0; i < n; i++ )
    {
        cin >> v;

        if (Set.count(v) == 1)
        {
            Set2.insert(v);
        }
        Set.insert(v);

    }

    cout << calculateMex(Set) + calculateMex(Set2) << "\n";

}

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
        solve();
    }

}
