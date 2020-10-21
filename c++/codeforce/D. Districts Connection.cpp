#include<bits/stdc++.h>
using namespace std;
void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}
long long arr[5001];
int vis[5001];

vector<int> v[5001];
vector <pair<int, int>> p;
void dfs(int node)
{
    vis[node] = 1;
    // cout << node << " ";
    for (int i = 0 ; i < v[node].size(); i++)
    {
        int child = v[node][i];
        if (vis[child] == 0)
        {   p.push_back({node, child});
            dfs(child);
        }
    }
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
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++)
        {
            cin >> arr[i];
            vis[i] = 0;
            v[i].clear();

        }
        for (int j = 1; j < n; j++)
        {
            for (int i = j + 1; i <= n; i++)
            {
                if (arr[j] != arr[i])
                {   v[i].push_back(j);
                    v[j].push_back(i);
                }
            }
        }
        dfs(1);
        if (p.size() == n - 1)
        {
            cout << "YES" << "\n";
            for (int i = 0; i < p.size(); i++)
            {

                cout << p[i].first << " " << p[i].second << "\n";
            }
        }
        else {
            cout << "NO" << "\n";
        }


        p.clear();


    }
}
