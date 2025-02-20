def cfreq(nums):
    if type(nums) is str:
        result_str = []
        nums_splitted = nums.split()
        unique_nums_str = set(nums_splitted)
        for num in nums_splitted:
            if num in unique_nums_str:
                num_frequency = nums_splitted.count(num)
                result_str.append((num, num_frequency))
        return result_str
    elif type(nums) is list:
        result_list = ''
        unique_nums_list = set(nums)
        for num in nums:
            if num in unique_nums_list:
                result_list += f'{num}:{nums.count(num)}'
        return result_list
            

        



    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cfreq)
