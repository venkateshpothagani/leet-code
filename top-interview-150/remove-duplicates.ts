function removeDuplicates(nums: Array<number>) {
    let pointer = 0;
    let index = 1;
    const length = nums.length;

    while(index < length) {
        if(nums[pointer] === nums[index] || nums[pointer] >= nums[index]) {
            index += 1;
        } else {
            pointer += 1;
            nums[pointer] = nums[index];
            index = pointer + 1;
        }
    }

    return pointer + 1
};