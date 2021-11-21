function fib(n, memo){
    if (n < 2){
        return n
    }
    if (memo === undefined){
        memo = {}
    }
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
}

const result = fib(11)
console.log(result)