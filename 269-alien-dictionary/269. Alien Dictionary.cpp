class Solution {
public:
    bool topo(int n,vector<vector<int>> &adj, vector<int> &vis, vector<int> &dfsVis, stack<int> &s){
        vis[n] = 1;
        dfsVis[n] = 1;
        
        for(auto it: adj[n]){
            if(!vis[it]){
                if(!topo(it, adj, vis, dfsVis, s))
                    return false;
            }
            else if(dfsVis[it] == 1)
                return false;
        }
        
        dfsVis[n] = 0;
        s.push(n);
        return true;
    }
    string alienOrder(vector<string>& words) {
        // words are already sorted lexicographically
        int i, j;
        // vector<vector<int>> adj(n, 0);
        string res = "";
        set<int> st;
        vector<vector<int>> adj(26, vector<int>({}));
        for(i=0; i<words.size(); i++){
            for(j=0; j<words[i].size(); j++){
                st.insert(words[i][j] - 'a');
            }
        }
        
        string w1, w2;
        int f = 0;
        for(i=0; i<words.size()-1; i++){
             w1 = words[i];
             w2 = words[i+1];
             f = 0;
             for(j=0; j<min(words[i].length(), words[i+1].length()); j++){
                 if(w1[j] != w2[j]){
                     cout<<i<<" "<<w1[j]<<" "<<w2[j]<<endl;
                     adj[w1[j] - 'a'].push_back(w2[j]-'a');
                     f = 1; 
                     cout<<"F is: "<<f << endl;
                     break; // IMP!!!!! put a break
                 }
             }
              if(f==0 && w1.size() > w2.size()) // important condition
                     return "";
        }
        
        vector<int> vis(26, 0);
        vector<int> dfsVis(26, 0);
        stack<int> s;
        
        for(auto it=st.begin(); it!=st.end(); it++){
            cout<<"Running loop for: "<<char(*it+'a')<<endl;
            if(!vis[*it]){
                if(!(topo(*it, adj, vis, dfsVis, s)))
                {cout<<"False condition hit"<<endl; return "";}
            }
        }
        // cout<<"Done loop"<<endl;
        // cout<<s.size()<<endl;
        while(!s.empty()){
            // cout
            // cout<<char(s.top() + 'a');
            res += char(s.top() + 'a');
            s.pop();
        }
        
        return res;
        
        
        
    }
};