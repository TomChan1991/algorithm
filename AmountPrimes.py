import collections


def amountPrimes(maxV:int):
    """
    计算 [0, maxV]之间的素数
    :param maxV: 计算 [0, maxV]之间的素数
    :return [amount, list(prime)]: 返回由两个元素组成的列表, 第一个元素是素数的个数, 第二个元素是所有素数组成的列表
    """
    isPrime = [True] * (maxV + 1)
    cnt, pL = 0, collections.deque()
    for i in range(2, maxV+1):
        if isPrime[i]:
            cnt += 1
            pL.append(i)
            for j in range(2, maxV // i + 1):
                isPrime[i * j] = False
    return cnt, list(pL)

if __name__ == '__main__': #测试1000000以内素数的个数为78498
    cnt, pL = amountPrimes(10 ** 6)
    assert cnt == 78498
    print(cnt)
