from typing import List
import numpy as np

def get_pct_change(array: List[float]):

    pct_change = []
    for i in range(1, len(array)):

        pct_change.append((array[i] - array[i-1]) / array[i-1])

    return pct_change


def get_beta_covariance_model(security_pricing, benchmark_pricing):
    """
    Follows covariance beta model of cov(benchmark, security)/var(benchmark)
    Or known as cov(x,y)/var(x)
    """

    security_pct_change = get_pct_change(security_pricing)
    benchmark_pct_change = get_pct_change(benchmark_pricing)

    covariance = np.cov(
            benchmark_pct_change, 
            security_pct_change
        )[0][1]
    variance = np.var(benchmark_pct_change)

    return (covariance / variance)
 