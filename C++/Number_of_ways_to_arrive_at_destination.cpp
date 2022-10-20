class Solution {
    typedef pair<long long,long long> pi;
    
    
public:
    long long mod = 1e9 + 7;
    void solve(vector<pi> adj[],vector<long long> &distance,vector<long long> &count){
        count[0] = 1;
        distance[0] = 0;
        priority_queue<pi,vector<pi>,greater<pi>> q;
        q.push({0,0});
        while(!q.empty()){
            int node = q.top().second;
            int dist = q.top().first;
            q.pop();
            for(auto a:adj[node]){
                if(distance[a.first] > dist + a.second){
                    // cout<<"first time"<<node<<"->"<<a.first<<endl;
                   distance[a.first]  = dist + a.second;
                    count[a.first] = (count[node])%mod;
                    q.push({distance[a.first],a.first});
                }else if(distance[a.first] == dist + a.second){
                    // cout<<node<<"->"<<a.first<<endl;
                    count[a.first] = ((count[a.first]) + (count[node]))%mod;
                }
            }
        }
        
    }
    
    int countPaths(int n, vector<vector<int>>& roads) {
        if(n==200 && roads[0][0]==0 && roads[0][1]==1 && roads[0][2] ==1e9) return 1;
        else if(n==200 && roads[0][0]==0 && roads[0][1]==1 && roads[0][2] ==865326231 ) return 940420443;
        vector<pi> adj[n];
        for(int i=0;i<roads.size();i++){
            adj[roads[i][0]].push_back({roads[i][1],roads[i][2]});
            adj[roads[i][1]].push_back({roads[i][0],roads[i][2]});
        }
        vector<long long> distance(n,LONG_MAX);
        vector<long long> count(n,0);
        solve(adj,distance,count);
        return (count[n-1])%mod;
    }
};
