### Running Sum of 1d Array
```text
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
```

## Link to Problem :- 

```html
https://leetcode.com/problems/running-sum-of-1d-array/
```

```java
class Solution {
    public int[] runningSum(int[] nums) {
        int[] nums2 = new int[nums.length];
        for (int i = 1; i <= nums.length; i++) {
            int sum = 0;
            for (int j = 0; j < i; j++) {
                // System.out.println(sum);
                sum += nums[j];
            }
            //System.out.println(sum + " " + i);
            nums2[i-1] = sum;
        }
        return nums2;
    }
}
```
