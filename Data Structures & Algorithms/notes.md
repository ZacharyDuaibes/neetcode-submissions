# Thoughts

### 1. duplicate-int
used `dict` in my solution: `{}`
- stores key-value pairs - `{key: value,...}`
- **NO DUPLICATES** = will overwrite `value`
- O(1) lookup/add

can use `set`: `set()`
- stores single values - `{value1, value2,...}`
- **NO DUPLICATES** = unique
- O(1) lookup/add

### 2. Valid Anagram
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
