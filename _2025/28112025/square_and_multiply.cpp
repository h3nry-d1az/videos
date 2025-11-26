#include "common.h"
#include <cmath>

u128 modpow(u128 a, u128 b, u128 m)
{
    uint max = (uint)ceil(log2(b));
    u128 result = 1, current = a;

    for (uint i = 0; i <= max; i++)
    {
        if ((b & (1 << i)) >> i)
            result = result*current % m;
        current = (current*current) % m;
    }

    return result;
}