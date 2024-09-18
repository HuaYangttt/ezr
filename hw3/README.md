
# This is the repo for hw3 of Hua Yang

## setting up
    cd /workspaces/ezr/hw3

## running code tests
    pytest /workspaces/ezr/hw3/fuc_test.py

## make the bash file for all experiment
    make Act=dumb_vs_smart > /workspaces/ezr/hw3/tmp/dumb_vs_smart.sh

## summarizes with the rq.sh script:
    cd /workspaces/ezr/hw3/tmp/dumb_vs_smart 
    bash /workspaces/ezr/hw3/tmp/rq.sh

## results

| RANK               | 0  | 1  | 2  | 3  | 4  | 5  |
|--------------------|----|----|----|----|----|----|
| smart_50_high_dim   | 61 | 6  | 2  |    |    |    |
| smart_40_high_dim   | 55 | 10 | 4  |    |    |    |
| dumb_50_high_dim    | 41 | 20 | 8  |    |    |    |
| smart_30_high_dim   | 35 | 24 | 10 |    |    |    |
| dumb_40_high_dim    | 33 | 29 | 8  |    |    |    |
| dumb_30_high_dim    | 27 | 22 | 18 | 2  |    |    |
| smart_20_high_dim   | 24 | 22 | 20 | 2  |    |    |
| smart_50_low_dim    | 24 | 6  |    |    |    |    |
| dumb_20_high_dim    | 22 | 22 | 16 | 8  |    |    |
| smart_40_low_dim    | 22 | 6  |    | 2  |    |    |
| dumb_50_low_dim     | 18 | 8  | 4  |    |    |    |
| smart_20_low_dim    | 14 | 2  | 12 |    | 2  |    |
| smart_30_low_dim    | 14 | 4  | 8  | 4  |    |    |
| dumb_40_low_dim     | 12 | 10 | 8  |    |    |    |
| dumb_30_low_dim     | 10 | 10 | 10 |    |    |    |
| dumb_20_low_dim     | 10 | 6  | 8  | 4  | 2  |    |
| asIs                | 2  | 29 | 16 | 37 | 12 | 4  |
                                            
## anlysis

Because there are two hypotheses:
1. **JJR1**: Nothing works better than 50 random guessed for **low dimensional** problems (less than 6 x attributes).
2. **JJR2**: But such random guessing is rubbish for **higher dimensional** data. 
So we divided the results into two different tables, i.e., **low-dimensional one (< 6 attributes)** and **higher-dimensional one (≥ 6 attributes)**.

In each table, we use the following notations:
- We use **smart** to denote results from active learning and **dumb** to denote results from random guessing.
- We use **asIs** to denote the baseline result against which everything else is compared.
- We have compiled the ranking results of each method's performance in **RANK**, where smaller values indicate better results for the method.

We also converted the original numbers into percentages for clarity.

### JJR1: in low dimensional data, random guessing (50 random guessed) works better than active learning.
| RANK               | 0  | 1  | 2  | 3  | 4  | 5  |total number of datasets|
|-------------------|--------|-------|-------|-------|-------|-------|----------|
| smart_50_low_dim   | 80.00% | 20.00% | 0.00%  | 0.00%  | 0.00%  | 0.00%  | 30  |
| smart_40_low_dim   | 73.33% | 20.00% | 0.00%  | 6.67%  | 0.00%  | 0.00%  | 30  |
| dumb_50_low_dim    | 60.00% | 26.67% | 13.33% | 0.00%  | 0.00%  | 0.00%  | 30  |
| smart_20_low_dim   | 46.67% | 6.67%  | 40.00% | 0.00%  | 6.67%  | 0.00%  | 30  |
| smart_30_low_dim   | 46.67% | 13.33% | 26.67% | 13.33% | 0.00%  | 0.00%  | 30  |
| dumb_40_low_dim    | 40.00% | 33.33% | 26.67% | 0.00%  | 0.00%  | 0.00%  | 30  |
| dumb_30_low_dim    | 33.33% | 33.33% | 33.33% | 0.00%  | 0.00%  | 0.00%  | 30  |
| dumb_20_low_dim    | 33.33% | 20.00% | 26.67% | 13.33% | 6.67%  | 0.00%  | 30  |
| asIs              | 2.00%  | 29.00% | 16.00% | 37.00% | 12.00% | 4.00%  | 100 |

***Point 1***: As you can see form the table above, **smart_50_low_dim** achieves best performance (80.00%) while **the best random guessing (dumb_50_low_dim)** could only achieve 60.00% in RANK 0. 

***Point 2***: The average of **smart** is 61.67% while the average of **dumb** is 41.67%. 

### JJR2: in higher dimensional data, random guessing works worse than active learning.
| RANK               | 0  | 1  | 2  | 3  | 4  | 5  |total number of datasets|
|-------------------|--------|-------|-------|-------|-------|-------|----------|
| smart_50_high_dim  | 88.41% | 8.70% | 2.90% | 0.00% | 0.00% | 0.00% | 69  |
| smart_40_high_dim  | 79.71% | 14.49%| 5.80% | 0.00% | 0.00% | 0.00% | 69  |
| dumb_50_high_dim   | 59.42% | 28.99%| 11.59%| 0.00% | 0.00% | 0.00% | 69  |
| smart_30_high_dim  | 50.72% | 34.78%| 14.49%| 0.00% | 0.00% | 0.00% | 69  |
| dumb_40_high_dim   | 47.14% | 41.43%| 11.43%| 0.00% | 0.00% | 0.00% | 70  |
| dumb_30_high_dim   | 39.13% | 31.88%| 26.09%| 2.90% | 0.00% | 0.00% | 69  |
| smart_20_high_dim  | 35.29% | 32.35%| 29.41%| 2.94% | 0.00% | 0.00% | 68  |
| dumb_20_high_dim   | 32.35% | 32.35%| 23.53%| 11.76%| 0.00% | 0.00% | 68  |
| asIs              | 2.00%  | 29.00%| 16.00%| 37.00%| 12.00%| 4.00% | 100 |

***Point 3***: As you can see form the table above, **smart_50_high_dim** achieves best performance (88.41%) while **the best random guessing (dumb_50_high_dim)** could only achieve 59.42% in RANK 0. 

***Point 4***: The average of **smart** is 63.53% while the average of **dumb** is 44.51%. 

## conclusion

Since we observed ***Point 1*** and ***Point 2***, we doubt the JJR1 hypothesis.

Since we observed ***Point 3*** and ***Point 4***, we confirm the JJR2 hypothesis.

