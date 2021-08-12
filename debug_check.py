def snakefill(n):
    area = n*n - 1
    count = 0
    snake_len = 0
    for i in range(area):
        snake_len += 2**i
        if snake_len < area :
            count += 1
    return count
        
snakefill(5)