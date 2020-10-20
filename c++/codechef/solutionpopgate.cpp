#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n, k, h=0, t=0, c=0;
	    cin>>n>>k;
	    char coins[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>coins[i];
	
	    }
	    /*int newn=n-k;
	    for(int i=n-1;i>=k;i--)
	    {
	        if(coins[i]=='H')
	            c++;
	    }
	    for(int i=0;i<newn;i++)
	    {
	        if(coins[i]=='H')
	            h++;
	        else if(coins[i]=='T')
	            t++;
	    }
	    if(c%2==0)
	    {
	        cout<<t<<endl;
	    }
	    else if(c%2!=0)
	    {
	        cout<<h<<endl;
	    }*/
	    int l=n-1;
	    for(int i=0;i<k;i++)
	    {
	        if(coins[l]=='H')
	        {
	            for(int j=0;j<l;j++)
	            {
	                if(coins[j]=='H')
	                    coins[j]='T';
	               else if(coins[j]=='T')
	                    coins[j]='H';
	            }
	        }
	        l--;
	    }
	    for(int i=0;i<n-k;i++)
	    {
	        if(coins[i]=='H')
	            h++;
	    }
	    cout<<h<<endl;
	}
	return 0;
}
