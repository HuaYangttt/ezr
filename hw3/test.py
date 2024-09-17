import sys,random,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir) # add parent_dir to sys.path

from ezr import the, DATA, csv, dot
from part1 import guess
import stats

def test_guess(test_data):
    
    # randomly set N = 3
    N = 3
    result = guess(N, test_data)

    # print output
    print(f"Selected and sorted rows based on Chebyshev distance: {result}")
    
    # check the length
    assert len(result) == N, f"Expected {N} rows, but got {len(result)}"

    # check the order
    assert result == sorted(test_data.clone(result).rows, key=lambda r: test_data.chebyshev(r)), "Rows are not correctly sorted by Chebyshev distance"
    
    print("Test passed.")

# run the test case
if __name__ == "__main__":

    # using a real dataset as test_data
    test_data = DATA().adds(csv('/workspaces/ezr/data/optimize/misc/auto93.csv'))

    test_guess(test_data)