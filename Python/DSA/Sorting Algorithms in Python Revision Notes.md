# Sorting Algorithms in Python: Revision Notes

*Bubble, Selection, Insertion, Merge and Quick sort, with step-by-step visual traces*

## 1. Quick comparison

| Algorithm | Best | Average | Worst | Extra space | Stable | In-place |
| --- | --- | --- | --- | --- | --- | --- |
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |

**Stable** means equal elements keep their original relative order. **In-place** means the sort needs only O(1) (or tiny) extra memory beyond the input.

All traces below use the same input: `[5, 2, 9, 1, 6]`. A `|` marks the boundary of the sorted part.

## 2. Bubble sort

**Idea:** repeatedly compare neighbours and swap if out of order. After each pass the largest remaining element bubbles to the end.

```python
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

arr = [100, 2, 55, 78, 4]
bubbleSort(arr)
print(arr)
```

**Trace:**

```
Start:   5 2 9 1 6

Pass 1:  (5 2) swap  -> 2 5 9 1 6
         (5 9) ok    -> 2 5 9 1 6
         (9 1) swap  -> 2 5 1 9 6
         (9 6) swap  -> 2 5 1 6 | 9

Pass 2:  (2 5) ok    -> 2 5 1 6 | 9
         (5 1) swap  -> 2 1 5 6 | 9
         (5 6) ok    -> 2 1 5 | 6 9

Pass 3:  (2 1) swap  -> 1 2 5 | 6 9
         (2 5) ok    -> 1 2 | 5 6 9

Pass 4:  (1 2) ok, no swaps -> stop early

Result:  1 2 5 6 9
```

**Remember:** the `swapped` flag gives the O(n) best case. Simple but slow; mainly for teaching.

## 3. Selection sort

**Idea:** find the minimum of the unsorted part and swap it to the front. Grows a sorted prefix one element at a time.

```python
def selection_sort(a):
    n = len(a)

    for i in range(n):
        min = i

        for j in range(i, n):
            if a[min] > a[j]:
                min = j

            a[i] , a[min] = a[min] , a[i] 

lst = [64, 25, 32, 20, 40, 15]
selection_sort(lst)
print(lst)
```

**Trace:**

```
Start:   5 2 9 1 6

i=0: min of [5 2 9 1 6] is 1 (index 3) -> swap with index 0
     1 | 2 9 5 6

i=1: min of [2 9 5 6] is 2 (already in place)
     1 2 | 9 5 6

i=2: min of [9 5 6] is 5 (index 3) -> swap with index 2
     1 2 5 | 9 6

i=3: min of [9 6] is 6 (index 4) -> swap with index 3
     1 2 5 6 | 9

Result:  1 2 5 6 9
```

**Remember:** always O(n²) comparisons, but at most n - 1 swaps. Not stable because the long-distance swap can jump an element past its equals.

## 4. Insertion sort

**Idea:** like sorting playing cards in your hand. Take the next element (the key) and shift larger sorted elements right to make room.

```python
def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i-1

        while(j >= 0 and key < a[j]):
            a[j+1] = a[j]
            j = j-1

        a[j+1] = key


arr = [100, 2, 55, 78, 4]
insertion_sort(arr)
print(arr)
```

**Trace:**

```
Start:        5 | 2 9 1 6

key=2: shift 5          -> 2 5 | 9 1 6
key=9: no shift         -> 2 5 9 | 1 6
key=1: shift 9, 5, 2    -> 1 2 5 9 | 6
key=6: shift 9          -> 1 2 5 6 9 |

Result:       1 2 5 6 9
```

**Remember:** excellent on small or nearly sorted data (best case O(n)). Stable and in-place. Real-world hybrids such as Timsort use it for small runs.

## 5. Merge sort

**Idea:** divide and conquer. Split the list in half, sort each half recursively, then merge the two sorted halves.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # <= keeps it stable
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Trace (split down, then merge up):**

```
                 [5 2 9 1 6]
               /             \
          [5 2]              [9 1 6]
         /     \             /     \
       [5]     [2]         [9]    [1 6]
                                  /   \
                                [1]   [6]

Merging back up:
  merge [5]   + [2]     -> [2 5]
  merge [1]   + [6]     -> [1 6]
  merge [9]   + [1 6]   -> [1 6 9]
  merge [2 5] + [1 6 9] -> [1 2 5 6 9]
```

**Remember:** guaranteed O(n log n) and stable, but needs O(n) extra space. Great for linked lists and external (disk) sorting.

## 6. Quick sort

**Idea:** pick a pivot, partition so smaller elements go left and larger go right, putting the pivot in its final position. Then recurse on both sides. This version uses the Lomuto partition with the last element as pivot.

```python
def quick_sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort(arr, lo, p - 1)
        quick_sort(arr, p + 1, hi)
    return arr

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1                      # end of the 'smaller' zone
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]   # pivot to its place
    return i + 1
```

**Trace:**

```
Call 1: [5 2 9 1 6], pivot = 6
  j=0: 5 <= 6 -> grow smaller zone      5 2 9 1 6
  j=1: 2 <= 6 -> grow smaller zone      5 2 9 1 6
  j=2: 9 > 6  -> skip                   5 2 9 1 6
  j=3: 1 <= 6 -> swap 9 and 1           5 2 1 9 6
  place pivot: swap 9 and 6             5 2 1 [6] 9
  pivot 6 is now final (index 3)

Call 2 (left): [5 2 1], pivot = 1
  no element <= 1, so place pivot at front:  [1] 2 5
  pivot 1 is final (index 0)

Call 3 (right of 1): [2 5], pivot = 5
  2 <= 5 -> stays; pivot already in place:   2 [5]

Right of 6: [9] -> single element, done

Result:  1 2 5 6 9
```

**Remember:** average O(n log n) and usually the fastest in practice (cache friendly, in-place). Worst case O(n²) happens when the pivot is always the min or max, for example a sorted list with a last-element pivot. Fix with a random or median-of-three pivot.

## 7. Which one to use?

- **Tiny or nearly sorted data:** insertion sort.
- **Need guaranteed O(n log n) or stability:** merge sort.
- **General purpose, memory tight:** quick sort (with a random pivot).
- **Minimising swaps (expensive writes):** selection sort.
- **Teaching only:** bubble sort.
- **In real Python code:** use `sorted()` or `list.sort()`, which run Timsort (a stable merge and insertion hybrid, O(n log n) worst case, O(n) on sorted data).

## 8. Exam checklist

1. State the idea in one sentence and name the technique (comparison swap, select min, insert into sorted part, divide and conquer).
2. Know the complexity table by heart, especially quick sort's O(n²) worst case.
3. Know stability: bubble, insertion and merge are stable; selection and quick are not.
4. Be able to trace each algorithm on a small list, pass by pass.
5. Edge cases: empty list, one element, duplicates, already sorted, reverse sorted.
6. Merge sort's merge step and quick sort's partition are the two functions most often asked to write from memory.
