notes on how to install and run your code, all the rq.sh results, a walk thought the table results summarizing what the tables are all about and what they are saying for this experiment, and a last paragraph that is a conclusion section of the form
“Since we observed XXXX, we confirm/ doubt/ refine the JJR1/ JJR2 hypothesis as follows…” (and the “as follows” section is only needed if you want to refine the hypothesis).
Include in your code tests cases that checks at least the items mentioned above (and you might want to check more).

# This is the repo for hw3 of Hua Yang

## Setting Up
    cd /workspaces/ezr/hw3

## running code tests
    pytest /workspaces/ezr/hw3/fuc_test.py

## make the bash file for all experiment
    make Act=dumb_vs_smart > /workspaces/ezr/hw3/tmp/dumb_vs_smart.sh

## summarizes with the rq.sh script:
    cd /workspaces/ezr/hw3/tmp/dumb_vs_smart 
    bash /workspaces/ezr/hw3/tmp/rq.sh

## results

RANK                  0            1             2            3             4             5           6           7           8           9
smart_50_high_dim    61            6             2                                                                                         
smart_40_high_dim    55           10             4                                                                                         
dumb_50_high_dim     41           20             8                                                                                         
smart_30_high_dim    35           24            10                                                                                         
dumb_40_high_dim     33           29             8                                                                                         
dumb_30_high_dim     27           22            18            2                                                                            
smart_20_high_dim    24           22            20            2                                                                            
smart_50_low_dim     24            6                                                                                                       
dumb_20_high_dim     22           22            16            8                                                                            
smart_40_low_dim     22            6                          2                                                                            
dumb_50_low_dim      18            8             4                                                                                         
smart_20_low_dim     14            2            12                          2                                                              
smart_30_low_dim     14            4             8            4                                                                            
dumb_40_low_dim      12           10             8                                                                                         
dumb_30_low_dim      10           10            10                                                                                         
dumb_20_low_dim      10            6             8            4             2                                                              
asIs                  2           29            16           37            12             4                                                
                                                                                                                                        100

## conclusion



