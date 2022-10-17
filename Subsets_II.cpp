#include<bits/stdc++.h>
using namespace std;
void generate(vector<int>& nums,int i,vector<int>&subset,vector<vector<int>>&res)
    {
        
        if(i==nums.size())
        {
            res.push_back(subset);
            return;
        }
        else
        {
            
            
            subset.push_back(nums[i]);
            generate(nums,i+1,subset,res);
            subset.pop_back();
            while(i+1<nums.size() && nums[i]==nums[i+1])
            {
                i++;
            }
            generate(nums,i+1,subset,res);
        }
    }
vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> subset;
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        
        generate(nums,0,subset,res);
        return res;
        
 }
int main(){

    vector<int> nums={1,2,2};

    vector<vector<int>> ans = subsetsWithDup(nums);

    for(int i=0;i<ans.size();i++)
    {
        cout<<"[";
        for(int j=0;j<ans[i].size();j++)
        {
            if(j!=ans[i].size()-1)
            {cout<<ans[i][j]<<",";}
            else
            {
                cout<<ans[i][j];
            }
        }
        cout<<"]"<<endl;
    }
}