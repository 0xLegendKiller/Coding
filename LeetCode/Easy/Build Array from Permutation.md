### Build Array from Permutation
```text
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
```

## Link to Problem :- 

```html
https://leetcode.com/problems/build-array-from-permutation/
```

```java
class Solution {
    public int[] buildArray(int[] nums) {
        int num2[] = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            num2[i] = nums[nums[i]];
        }
        return num2;
    }
}
```
