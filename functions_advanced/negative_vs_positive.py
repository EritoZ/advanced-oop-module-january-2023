def negative_vs_positive(nums):
    nums = list(map(int, nums.split()))

    def negatives_sum():
        filtered_negatives = [n for n in nums if n < 0]

        return sum(filtered_negatives)

    def positives_sum():
        filtered_positives = [n for n in nums if n > 0]

        return sum(filtered_positives)

    negatives_sum_total = negatives_sum()
    positives_sum_total = positives_sum()

    print(negatives_sum_total)
    print(positives_sum_total)

    if abs(negatives_sum_total) > positives_sum_total:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = input()
negative_vs_positive(numbers)
