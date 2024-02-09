def snoom(d, c, n):
    schedule = [-1 for i in range(n)]
    serial = -1
    cloud = -1
    index = -1
    s_total = 0
    total = 0

    for i in range(n):
        cloud = -1
        for j in range(n):
            if c[j] > cloud and schedule[j] == -1:
                serial = d[j]
                cloud = c[j]
                index = j
        s_total += serial
        total = max(total, s_total + cloud)
        schedule[index] = i
    print(schedule)
    return total, schedule


def alt_snoom(d, c, n):
    max_cloud_serial = -1
    max_cloud = -1
    min_cloud = 999999999
    total_serial = 0

    for i in range(n):
        total_serial += d[i]
        if c[i] > max_cloud:
            max_cloud_serial = d[i]
            max_cloud = c[i]
        if c[i] < min_cloud:
            min_cloud = c[i]
    return max(max_cloud + max_cloud_serial, total_serial + min_cloud) 



if __name__ == '__main__':
    d = [9, 8, 3, 2, 4, 5, 1, 7, 6]
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    n = len(d)

    result = snoom(d, c, n)
    print(result)
    print("Test 1 passed?: " + str(result[0] == 46))

    result = alt_snoom(d, c, n)
    print(result)
    print("Test 1 passed?: " + str(result == 46))


    d = [10, 5, 23, 4, 17, 8, 12, 1, 6, 11, 7, 9, 3, 2, 14, 18, 20, 15, 1, 9, 19, 1, 13, 2, 5] # sum = 235
    c = [7, 6, 15, 4, 11, 10, 18, 3, 1, 9, 22, 13, 16, 23, 2, 8, 5, 12, 6, 14, 19, 3, 8, 11, 20]

    n = len(d)

    
    result = snoom(d, c, n)
    print(result)
    print("Test 2 passed?: " + str(result[0] == 236))

    result = alt_snoom(d, c, n)
    print(result)
    print("Test 2 passed?: " + str(result == 236))
