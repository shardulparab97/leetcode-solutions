class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i1 = -1, i2 = -1, n = nums.size();
        
        int i = n-2;
        while(i >= 0){
            if(nums[i] < nums[i+1]){
                i1 = i;
                break;
            }
            i--;
        }
        
        if(i1 != -1){
            i = n-1;
            while(i > i1){
                if(nums[i] > nums[i1]){
                    i2 = i;
                    break;
                }
                i--;
            }
            
            cout<<"i1: "<<i1<<" i2: "<<i2<<endl;
            swap(nums[i1], nums[i2]);
            // for(i=0; i<n; i++){
            //     cout<<nums[i]<<" ";
            // }
            reverse(nums.begin()+i1+1, nums.end());
            
        }
        
        else
            reverse(nums.begin(), nums.end());
    }
};