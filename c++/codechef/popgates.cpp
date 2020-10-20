#include<iostream>

using namespace std;


int main()
{
    int K ,N,T;
    
    cin >> T;
    while(T>0)
    {
         	cin >> N;
        	char coin[N];
        	cin >> K;
        	
            		for(int i=0;i<N;i++)
            		{
                
                		cin>> coin[i];

            		}
					int temp=N-1;
            	while(K>0)
        	{
            	
            	while(temp>0)
            	{
               		if(coin[temp]==H)
                	{
                		for(i=temp;i>0;i--)
                   		{
                       			if(coin[i]==H)
                      			{
                          			coin[i]=T;
                          
                       			}
                      			else
                      			{
                           			coin[i]=H;
                        		} 
            				
            			}
            
                	}
    


                   temp--;
    		}
    	         K--;
    		}
    		int count=0;
    		for(int i=0;i<N;i++)
    		{ 
    		   if(coin[i]==H)
    		   count++;
    		 }
    		 cout<<count  ;
     T--;    
    }
 return 0;
}
    


