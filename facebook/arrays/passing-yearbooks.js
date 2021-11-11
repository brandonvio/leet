/*
Passing Yearbooks
There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.
Signature
int[] findSignatureCounts(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
Output
Return a list of n integers output, as described above.
Example 1
n = 2
arr = [2, 1]
output = [2, 2]
 */
// Add any extra import statements you may need here


// Add any helper functions you may need here


function findSignatureCounts(arr) {
    // Write your code here

}


// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom.
function printintegerArray(array) {
    var size = array.length;
    var res = '';
    res += '[';
    var i = 0;
    for (i = 0; i < size; i++) {
        if (i !== 0) {
            res += ', ';
        }
        res += array[i];
    }
    res += ']';
    return res;
}

var test_case_number = 1;

function check(expected, output) {
    var expected_size = expected.length;
    var output_size = output.length;
    var result = true;
    if (expected_size != output_size) {
        result = false;
    }
    for (var i = 0; i < Math.min(expected_size, output_size); i++) {
        result &= (output[i] == expected[i]);
    }
    var rightTick = "\u2713";
    var wrongTick = "\u2717";
    if (result) {
        var out = rightTick + ' Test #' + test_case_number;
        console.log(out);
    } else {
        var out = '';
        out += wrongTick + ' Test #' + test_case_number + ': Expected ';
        out += printintegerArray(expected);
        out += ' Your output: ';
        out += printintegerArray(output);
        console.log(out);
    }
    test_case_number++;
}

var arr_1 = [2, 1];
var expected_1 = [2, 2];
var output_1 = findSignatureCounts(arr_1);
check(expected_1, output_1);

var arr_2 = [1, 2];
var expected_2 = [1, 1];
var output_2 = findSignatureCounts(arr_2);
check(expected_2, output_2);

// Add your own test cases here
