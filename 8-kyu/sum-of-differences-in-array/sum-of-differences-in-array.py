def sum_of_differences(arr):
    arr.sort(reverse=True)
    sum=0
    for i in range(len(arr)-1):
        value=arr[i]-arr[i+1]
        sum=sum+value
    return sum