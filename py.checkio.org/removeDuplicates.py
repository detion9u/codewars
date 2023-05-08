#remove the duplicates
def removeDuplicates(nums):
    lis1 = list(set(nums))
    lis1.sort()
    print(lis1)
    print(len(lis1))
      
    return lis1
if __name__ == '__main__':
    print("Hello Python!")
    removeDuplicates([1,1,2])