from typing import List, Dict


def test_reorderLogFiles():
    """
    You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

    There are two types of logs:

    Letter-logs: All words (except the identifier) consist of lowercase English letters.
    Digit-logs: All words (except the identifier) consist of digits.

    Reorder these logs so that:
    The letter-logs come before all digit-logs.
    The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
    The digit-logs maintain their relative ordering.
    Return the final order of the logs.

    Example 1:
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    Explanation:
    The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
    The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

    Example 2:
    Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    """

    class Solution:
        def reorderLogFiles(self, logs: List[str]) -> List[str]:
            logs_letter = []
            logs_digit = []

            for log in logs:
                if log.split()[1][0].isdigit():
                    logs_digit.append(log)
                else:
                    logs_letter.append(log)

            logs_letter.sort(key=self.sort_letter_logs)

            return logs_letter + logs_digit

        def sort_letter_logs(self, log):
            split_log = log.split()
            return (split_log[1:], split_log[0])

    _solution = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    result = _solution.reorderLogFiles(logs)
    print(result)
    assert result == ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    result = _solution.reorderLogFiles(logs)
    print(result)
    assert result == ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]


def test_parking_system():
    """
    Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.
    Implement the ParkingSystem class:
    ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
    bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

    Example 1:
    Input
    ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    [[1, 1, 0], [1], [2], [3], [1]]
    Output
    [null, true, true, false, false]

    Explanation
    ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
    parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
    parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
    parkingSystem.addCar(3); // return false because there is no available slot for a small car
    parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

    Constraints:
    0 <= big, medium, small <= 1000
    carType is 1, 2, or 3
    At most 1000 calls will be made to addCar
    """

    class ParkingSystem:

        def __init__(self, big: int, medium: int, small: int):
            self.parking_spaces: Dict[int, int] = {}
            self.parking_spaces[1] = big
            self.parking_spaces[2] = medium
            self.parking_spaces[3] = small

        def addCar(self, carType: int) -> bool:
            if self.parking_spaces[carType] == 0:
                return False
            else:
                self.parking_spaces[carType] -= 1
                return True

    # Your ParkingSystem object will be instantiated and called as such:
    # obj = ParkingSystem(big, medium, small)
    # param_1 = obj.addCar(carType)
    parkingSystem = ParkingSystem(1, 1, 0)
    assert parkingSystem.addCar(1)  # return true because there is 1 available slot for a big car
    assert parkingSystem.addCar(2)  # return true because there is 1 available slot for a medium car
    assert not parkingSystem.addCar(3)  # return false because there is no available slot for a small car
    assert not parkingSystem.addCar(
        1)  # return false because there is no available slot for a big car. It is already occupied.


def test_maximumUnits():
    """
    You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.
    You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
    Return the maximum total number of units that can be put on the truck.

    Example 1:
    Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    Output: 8
    Explanation: There are:
    - 1 box of the first type that contains 3 units.
    - 2 boxes of the second type that contain 2 units each.
    - 3 boxes of the third type that contain 1 unit each.
    You can take all the boxes of the first and second types, and one box of the third type.
    The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

    Example 2:
    Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
    Output: 91


    Constraints:
    1 <= boxTypes.length <= 1000
    1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
    1 <= truckSize <= 106
    """
    import math

    class Solution:
        def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
            # sort items in terms of boxes that can carry the most items.
            # start with the boxes that contain the most items.
            # get all of the boxes that have the most items first and then proceed to the next items.
            # until there is no more room left.
            boxTypes.sort(key=lambda x: -x[1])
            capacity = 0

            for box_count, box_quantity_of_items in boxTypes:
                if truckSize > box_count:
                    truckSize -= box_count
                    capacity += box_count * box_quantity_of_items
                else:
                    capacity += truckSize * box_quantity_of_items
                    # truck is full at this point.
                    break

            return capacity

    _solution = Solution()
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    result = _solution.maximumUnits(boxTypes, truckSize)
    # print(result)
    assert result == 8

    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    result = _solution.maximumUnits(boxTypes, truckSize)
    # print(result)
    assert result == 91


def test_two_sum():
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]

    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
    #two-sum #1
    """

    def twoSum(nums: List[int], target: int) -> List[int]:
        tracker = {}
        # loop over nums list.
        # subtract num from the target
        # check if result has been seen
        # if not store the current number and the current index
        # if has been seen return the stored index and the current index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in tracker:
                return [index, tracker[diff]]
            else:
                tracker[num] = index

        return None

    nums = [3, 2, 4]
    target = 6
    result = twoSum(nums, target)
    # print(result)
    assert result == [1, 2] or result == [2, 1]

    nums = [3, 3]
    target = 6
    result = twoSum(nums, target)
    # print(result)
    assert result == [0, 1] or result == [1, 0]
