import sys,random,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir) # add parent_dir to sys.path

from ezr import the, DATA, csv, dot
import stats

def guess(N, data):
    # Pick N rows at random
    some = random.sample(data.rows, N)
    
    # Clone the data and add the picked rows, then sort on Chebyshev distance
    sorted_rows = data.clone(some).chebyshevs().rows

    # Return the sorted rows
    return sorted_rows




if __name__ == '__main__':

    data_list = [arg for arg in sys.argv if arg[-4:] == ".csv"]
    
    for data in data_list:
        #data_name = os.path.basename(data)

        d = DATA().adds(csv(data))
        
        #baseline
        b4 = [d.chebyshev(row) for row in d.rows]
        somes = [stats.SOME(b4, f"asIs,{len(d.rows)}")]

        for N in [20,30,40,50]:
            #result_dumb  = stats.SOME(txt=f"{data_name[:-4]}_dumb_{N}")
            #result_smart  = stats.SOME(txt=f"{data_name[:-4]}_smart_{N}")
            result_dumb  = stats.SOME(txt=f"dumb_{N}")
            result_smart  = stats.SOME(txt=f"smart_{N}")
            somes += [result_dumb]
            somes += [result_smart]

            dumb = guess(N,d)
            # print(dumb)
            dumb = [d.chebyshev( lst ) for lst in dumb]
            #result_dumb.add(dumb)
            
            for result in dumb:
                result_dumb.add(result)

            # smart
            the.Last = N
            smart = [d.shuffle().activeLearning()[0] for _ in range(20) ]
            # print('!!!!!!!!!!!!!!!')
            # print(smart)
            # assert 0
            smart = [d.chebyshev( lst ) for lst in smart]
            for result in smart:
                result_smart.add(result)

    stats.report(somes, 0.01)        













