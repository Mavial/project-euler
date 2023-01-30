def collatz_seq_len(start_n: int) -> int:
    chain_lenght = 1
    n = start_n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        chain_lenght += 1
    return chain_lenght


max_chain = (0, 0)
for start_n in range(1, 1000000):
    n_chain_len = collatz_seq_len(start_n)
    if n_chain_len > max_chain[1]:
        max_chain = (start_n, n_chain_len)

print(max_chain[0])