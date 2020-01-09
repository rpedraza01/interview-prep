# Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if
# prices = [1,2,3,4] and Mark has k=7 to spend, he can buy items [1,2,3] for 6 or [3,4] for 7 units of currency.
# He would choose the first group of 3 items

# function takes in the parameter of the number of different prices as an array and the amount of money Mark can spend, k an integer
def maximumToys(prices, k):
	# the array prices is then sorted
    prices.sort()
    # the varaible i is created and set to 0. This will serve as a counter for how many items Mark has bought
    i = 0
    # the while loop is saying that so long as Mark's money, k, is greater than 0 and the number of bought items, i, is less than the number of prices (continued on line 13)
    while k > 0 and i < len(prices):
    	# Mark's money, k, will be decreased by one of the item prices at a time
        k -= prices[i]
        # the number of bought items, i, will then add 1 for each item bought
        i += 1
    # the return statement subtracts 1 from the number of items bought, i
    return i - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
