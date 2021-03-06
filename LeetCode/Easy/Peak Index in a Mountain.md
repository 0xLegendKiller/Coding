### Peak Index in a Mountain Array
```text
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
```

### Problem Link :- 
```html
https://leetcode.com/problems/peak-index-in-a-mountain-array/
```

### Solution :- 

Method 1 - Binary Search

```java
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while(start < end){
            int mid = start + ( end - start ) / 2;
            if(arr[mid] > arr[mid+1]){
                end  = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }
}
```

Method 2 - Linear Search

```java
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int max = 0;
        int index = 0;
        for (int i = 0; i < arr.length; i++) {
            if(max < arr[i]){
                max = arr[i]; 
                index = i;
            }
        }
        // System.out.println(arr[index]);
        return index;
    }
}
```
