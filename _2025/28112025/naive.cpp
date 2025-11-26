#include "common.h"

u128 modpow(u128 a, u128 b, u128 m)
{
    u128 result = 1;
    while (b-- > 0)
        result = (result * a) % m;
    return result;
}