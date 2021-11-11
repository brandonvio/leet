from typing import List, Dict

def test_myAtoi():
    """
    https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/
    """

    class Solution:
        def myAtoi(self, s: str) -> int:
            pass

    _solution = Solution()
    result = _solution.myAtoi(None)
    # print(result)
    assert result == None

    result = _solution.myAtoi(None)
    # print(result)
    assert result == None


def test_ipoOffering():
    """
    https://codereview.stackexchange.com/questions/247977/initial-public-offering-auction

    A company registers for an IPO. All shares are available on the website for bidding during a time frame called the bidding window. At the end of the bidding window an auction logic is used to decide how many available shares go to which bidder until all shares have been allocated, or all the bidders have received the shares they bid for, whichever comes first.

    The bids arrive from users in the form of [userid, # shares, bidding price, timestamp] until the bidding window is closed.

    The auction logic assigns shares as follows:

    The bidder with the highest price gets the # of shares they bid for

    If multiple bidders have bid at the same price, the bidders are assigned shares in the order in which they places their bids (earliest bids first)

    List the userids of all the users who didn't get even 1 share after all shares have been allocated.

    Input
    bids
    list of lists of ints representing [userid, # shares, $bid, timestamp]
    totalShares
    total # of shares to be distributed.
    Todo
    distribute shares amongst bidders and return userids of bidders that got 0 shares.

    Share distribution logic:

    bidder with highest offer gets all the shares they bid for, and then
    if there are ties in $ bid price, assign shares to earlier bidder.
    I feel like the solution I came up with is relatively simple. It seems to pass all edge cases I can think of.

    Question
    I have found a questionable situation:
    Bid price and times are the same and there aren't enough shares for all bidders ie: bids is [[0,2,10,0], [1,2,10,0]] and totalShares is 2. It's unclear if 1 share should be given to each, or if userid 0 just gets both.
    """
    class Solution:
        def ipoOffering(self, s: str) -> int:
            pass

    _solution = Solution()
    result = _solution.ipoOffering(None)
    # print(result)
    assert result == None

    result = _solution.ipoOffering(None)
    # print(result)
    assert result == None




def test_distinctSubstring():
    """
    https://www.geeksforgeeks.org/count-number-of-distinct-substring-in-a-string/
    https://www.datacamp.com/community/tutorials/scope-of-variables-python
    """
    counter = 0
    class Solution:
        def test_distinctSubstring(self, s):
            pass

    _solution = Solution()
    result = _solution.test_distinctSubstring("abcde")
    assert result == 15
    assert counter == 15


# Driver Code
if __name__ == '__main__':
    str = "aaaa";
    print(distinctSubstring(str));


def test_lastStoneWeight():
    """
    1046. Last Stone Weight
    https://www.youtube.com/watch?v=i67IAEG_jhU

    You are given an array of integers stones where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    At the end of the game, there is at most one stone left.

    Return the smallest possible weight of the left stone. If there are no stones left, return 0.

    Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation:
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

    Example 2:
    Input: stones = [1]
    Output: 1

    Constraints:

    1 <= stones.length <= 30
    1 <= stones[i] <= 1000

    Notes:
    https://www.youtube.com/watch?v=i67IAEG_jhU
    """

    class Solution:
        def lastStoneWeight(self, s: str) -> int:
            pass

    _solution = Solution()
    result = _solution.lastStoneWeight([2, 2])
    # print(result)
    assert result == 0

    result = _solution.lastStoneWeight([2, 7, 4, 1, 8, 1])
    # print(result)
    assert result == 1

    result = _solution.lastStoneWeight([1])
    # print(result)
    assert result == 1


def test_addStrings():
    """
    415. Add Strings

    Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

    You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

    Example 1:
    Input: num1 = "11", num2 = "123"
    Output: "134"

    Example 2:
    Input: num1 = "456", num2 = "77"
    Output: "533"

    Example 3:
    Input: num1 = "0", num2 = "0"
    Output: "0"

    Constraints:
    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.
    Accepted
    """

    class Solution:
        def addStrings(self, num1: str, num2: str) -> str:
            pass

    _solution = Solution()
    result = _solution.addStrings(num1="987", num2="665")
    print(result)
    assert result == "1652"

    result = _solution.addStrings(num1="11", num2="123")
    print(result)
    assert result == "134"

    result = _solution.addStrings(num1="456", num2="77")
    print(result)
    assert result == "533"

    result = _solution.addStrings(num1="0", num2="0")
    print(result)
    assert result == "0"


def test_validWordAbbreviation():
    """
    408. Valid Word Abbreviation
    https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/408-valid-word-abbreviation.html

    A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

    For example, a string such as "substitution" could be abbreviated as (but not limited to):

    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (no substrings replaced)
    The following are not valid abbreviations:

    "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
    "s010n" (has leading zeros)
    "s0ubstitution" (replaces an empty substring)
    Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

    A substring is a contiguous non-empty sequence of characters within a string.

    Example 1:
    Input: word = "internationalization", abbr = "i12iz4n"
    Output: true
    Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

    Example 2:
    Input: word = "apple", abbr = "a2e"
    Output: false
    Explanation: The word "apple" cannot be abbreviated as "a2e".

    Constraints:

    1 <= word.length <= 20
    word consists of only lowercase English letters.
    1 <= abbr.length <= 10
    abbr consists of lowercase English letters and digits.
    All the integers in abbr will fit in a 32-bit integer.
    """

    class Solution:
        def validWordAbbreviation(self, word: str, abbr: str) -> bool:
            pass

    _solution = Solution()
    result = _solution.validWordAbbreviation("internationalization", "i12iz4n")
    # print(result)
    assert result is True

    result = _solution.validWordAbbreviation("apple", "a2e")
    # print(result)
    assert result is False


def test_isPalindrome():
    """
    125. Valid Palindrome

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

    Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
    """

    class Solution:
        def isPalindrome(self, s: str) -> bool:
            pass

    _solution = Solution()
    result = _solution.isPalindrome("A man, a plan, a canal: Panama")
    # print(result)
    assert result == True

    result = _solution.isPalindrome("race a car")
    # print(result)
    assert result == False

    result = _solution.isPalindrome("race a car xxx")
    # print(result)
    assert result == False


def test_maxProfit():
    """
    122. Best Time to Buy and Sell Stock II

    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.

    Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Total profit is 4.

    Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

    Constraints:
    1 <= prices.length <= 3 * 104
    0 <= prices[i] <= 104
    """

    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            pass

    _solution = Solution()
    result = _solution.maxProfit([7, 1, 5, 3, 6, 4])
    # print(result)
    assert result == 7

    result = _solution.maxProfit([1, 2, 3, 4, 5])
    # print(result)
    assert result == 4

    result = _solution.maxProfit([7, 6, 4, 3, 1])
    # print(result)
    assert result == 0

    result = _solution.maxProfit([1, 2, 2, 6, 9])
    # print("maxProfit:", result)
    # assert result == 0


def test_countBinarySubstrings():
    """
    # 696. Count Binary Substrings
    Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

    Substrings that occur multiple times are counted the number of times they occur.

    Example 1:
    Input: s = "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

    Example 2:
    Input: s = "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
    https://www.youtube.com/watch?v=OJWKzff4Ivg
    """

    class Solution:
        def countBinarySubstrings(self, s: str) -> int:
            pass

    _solution = Solution()
    result = _solution.countBinarySubstrings("00110011")
    # print(result)
    assert result == 6

    result = _solution.countBinarySubstrings("10101")
    # print(result)
    assert result == 4


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
            pass

    _solution = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    result = _solution.reorderLogFiles(logs)
    # print(result)
    assert result == ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    result = _solution.reorderLogFiles(logs)
    # print(result)
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
            pass

        def addCar(self, carType: int) -> bool:
            pass

    # Your ParkingSystem object will be instantiated and called as such:
    # obj = ParkingSystem(big, medium, small)
    # param_1 = obj.addCar(carType)
    parkingSystem = ParkingSystem(1, 1, 0)
    # assert parkingSystem.addCar(1)  # return true because there is 1 available slot for a big car
    # assert parkingSystem.addCar(2)  # return true because there is 1 available slot for a medium car
    # assert not parkingSystem.addCar(3)  # return false because there is no available slot for a small car
    # assert not parkingSystem.addCar(1)  # return false because there is no available slot for a big car. It is already occupied.


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
            pass

    _solution = Solution()
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    result = _solution.maximumUnits(boxTypes, truckSize)
    # print(result)
    # assert result == 8

    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    result = _solution.maximumUnits(boxTypes, truckSize)
    # print(result)
    # assert result == 91


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
        pass

    nums = [3, 2, 4]
    target = 6
    result = twoSum(nums, target)
    # print(result)
    # assert result == [1, 2] or result == [2, 1]

    nums = [3, 3]
    target = 6
    result = twoSum(nums, target)
    # print(result)
    # assert result == [0, 1] or result == [1, 0]
