robot_id = [12, 25, 38, 47, 63, 90]
robot_id_2 = [38, 12, 63, 38, 50, 25, 99, 47]

robot_id = robot_id.sort()
robot_id_2 = robot_id_2.sort()

# target ber korar loop

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while(low <= high):
        mid = (low + high) / 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        return -1

ans = binary_search(robot_id, robot_id_2)

if ans == -1:
    print("All Clear")
else:
    print()

