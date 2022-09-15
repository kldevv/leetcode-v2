class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        auto n = edges.size();
        vector<uint> cnt(n+2, 0u);
        
        for (auto edge : edges) {
            auto u = edge[0];
            auto v = edge[1];
            if (++cnt[u] == n) {
                return u;
            }
            if (++cnt[v] == n) {
                return v;   
            }
        }
        return -1;
    }
};

