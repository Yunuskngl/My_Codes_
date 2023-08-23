class Solution { // Bu soru yarıda kaldı.
public:
    string longestCommonPrefix(vector<string>& strs) {
    unordered_map<char,int>mp;
    string s;
    int i,j;
    for(i=0;i<strs.size();i++){
        for(j=0;j<strs[i].size();j++){
            mp[strs[i][j]]++;
        }
    }
    for(auto it=mp.begin();it!=mp.end();it++){
        if(it->second==strs.size()){
            s+=it->first;
        }
    }
    return s;
    }
};