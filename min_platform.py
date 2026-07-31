arr=[900,940,950,1100,1500,1800]
dep=[910,1120,1150,1200,1900,2000]
def minPlatforms (arr, dep):
    arr.sort()
    dep.sort()
    a=0
    d=0
    platform=0
    max_Platform=0
    while a<len(arr):
        if arr[a]<dep[d]:
            platform+=1
            a+=1
            if platform>max_Platform:
                max_Platform=platform

        else:
            platform-=1
            d+=1
    return max_Platform

print(minPlatforms(arr,dep))
