### Problem Statement :- 
```text
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
```
URL to Problem Statement :- 

`https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/`

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] nums2 = {-1, -1};
        for (int i = 0; i < nums.length; i++) {
            if(target == nums[i]){
                nums2[0] = i;
                break;
            }
        }
        for (int j = nums.length-1;j >= 0; j--) {
            if(target == nums[j]){
                nums2[1] = j;
                break;
            }
        }
        return nums2;
    }
}
```
