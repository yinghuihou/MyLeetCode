# Definition for singly-linked list.

def main():
    a = [1,2]
    b = [3,4]

    print(findMedianSortedArrays(a, b))


def findMedianSortedArrays(nums1, nums2):
    x = len(nums1)
    y = len(nums2)

    i = int((x + y) / 2)
    k = 0

    m = 0
    n = 0
    res1 = 0
    res2 = 0

    while k <= i:
        res1 = res2
        if m < x and n < y:
            if nums1[m] <= nums2[n]:
                res2 = nums1[m]
                m += 1
            else:
                res2 = nums2[n]
                n += 1
        elif m >= x and n < y:
            res2 = nums2[n]
            n += 1
        elif m < x and n >= y:
            res2 = nums1[m]
            m += 1
        k += 1

    if (x+y) % 2 == 0:
        return (res1 + res2)/2
    else:
        return res2


if __name__ == '__main__':
    main()
