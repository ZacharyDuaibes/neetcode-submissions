# Thoughts

### 1. duplicate-integer
used `dict` in my solution: `{}`
- stores key-value pairs - `{key: value,...}`
- **NO DUPLICATES** = will overwrite `value`
- O(1) lookup/add

can use `set`: `set()`
- stores single values - `{value1, value2,...}`
- **NO DUPLICATES** = unique
- O(1) lookup/add

### 2. is-anagram
thought of `dict` right away - letter : frequency
- First should check if the two strings are of equal length, if not then they cannot contain the same letters
- Loop through string, add to `dict` (becomes **key**), set **value** to 1 if not seen before, else add 1 per match
- **Initial Approach:** create two `dicts`, add strings to each `dict` with count of letter and compare `values`.
- Initial approach is good but i can do it with 1 `dict` instead of 2
- **Refined Approach**: 
1. Loop through first string, store count of each letter in `dict`
2. Loop through second string, check if letter is in `dict`. If it is subtract 1 from frequency, if letter isnt in `dict`, strings dont match = return `false` 
3. Loop through `dict`, if any `keys` dont have a `value` of 0, strings dont match (regardless of order) = return `false`, esle return `true`
- O(n) time and space

Second submission reduced number of loops
**third submission** - solution posted by neetcode:
1. check for equal lengths
2. initialize 2 dicts/hashmaps
3. loop through length of one string, add to the `hashmap` 1 (saw the letter) + the current count if it was seen before (get(key, fallback) method - retrieves the values for the key and uses a fallback value incase not seen before)
- O(n) time and space

### 3. two-sum
Thought of sliding window technique = used to solve problems that involve subarray/substring
**Sliding window**: maintains a range throughout the data updating incrementally. The main idea is to use the results from the previous "window" to compute the next.
- ```[i for i in range(len())]``` # Generates [0, 1, 2]
- ```list(enumerate())``` # Generates (index, item)

- So i have come to find out sliding window isnt the right idea here. It should be used when i have a contiguous window/adjacent elements like "find the max sum for 3 **consecutive** elements". In the case of ***Two Sum***, the numbers can be anywhere.
