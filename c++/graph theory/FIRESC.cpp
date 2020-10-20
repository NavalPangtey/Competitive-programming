#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
vector<int> v[100001];
int vis[100001];

void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}
long long r;
void dfs(int node)
{
    r++;
    vis[node] = 1;
    for (int i = 0 ; i < v[node].size(); i++)
    {
        int child = v[node][i];
        if (vis[child] == 0)
            dfs(child);
    }


}


int main()
{

    read();
    int t ; cin >> t;
    while (t--)
    {
        int a , b, n, m;
        cin >> n >> m;
        for (int i = 0 ; i <= n; i++)
        {
            vis[i] = 0;
            v[i].clear();
        }

        for (int i = 0 ; i < m; i++)
        {
            cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        long long count = 0, permu = 1;
        for (int i = 1; i <= n; i++)
        {
            if (vis[i] == 0)
            {   r = 0;
                dfs(i);
                count++;
                permu = (permu * r) % mod;

            }
        }
        cout << count << " " << permu << "\n";
    }
}
