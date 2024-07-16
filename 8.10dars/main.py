#    https://www.codewars.com/kata/56b4bae128644b5613000037/train/python


def repeat_sum(lists):
    num_count = {}
    for sublist in lists:
        seen_numbers = set()
        for num in sublist:
            if num in seen_numbers:
                continue
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
            seen_numbers.add(num)

    result_sum = 0
    for num, count in num_count.items():
        if count >= 2:
            result_sum += num

    return result_sum
