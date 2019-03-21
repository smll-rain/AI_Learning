from tqdm import tqdm, trange

# # Wrap tqdm() around any iterable
# for i in tqdm(range(10000)):
#     pass
#
# # trange(i) is a special optimised instance of tqdm(range(i))
# for i in trange(10000):
#     pass
#
# # Manual control on tqdm() updates by using a with statement
# with tqdm(total=10000) as pbar:
#     for i in range(100):
#         pbar.update(100)
#
# pbar = tqdm(total=10000)
# for i in range(100):
#     pbar.update(100)
# pbar.close()
#
# # Perhaps the most wonderful use of tqdm is in a script or on the command line.
# # Simply inserting tqdm (or python -m tqdm) between pipes will pass through all stdin to stdout while printing progress to stderr.
# # time find . -name '*.py' -exec cat \{} \; | tqdm | wc -l
#
# # Custom information can be displayed and updated dynamically on tqdm bars with the desc and postfix arguments
# from random import random, randint
# from time import sleep
#
# t = trange(100)
# for i in t:
#     # Description will be displayed on the left
#     t.set_description('GEN %i' % i)
#     # Postfix will be displayed on the right, and will format automatically
#     # based on argument's datatype
#     t.set_postfix(loss=random(), gen=randint(1,999), str='h', lst=[1, 2])
#     sleep(0.1)
#
# # tqdm supports nested progress bars. Here’s an example
# from time import sleep
#
# for i in trange(10, desc='1st loop'):
#     for j in trange(5, desc='2nd loop', leave=False):
#         for k in trange(100, desc='3nd loop'):
#             sleep(0.01)

# # Due to popular demand we’ve added support for pandas
# # here’s an example for DataFrame.progress_apply and DataFrameGroupBy.progress_apply
# import pandas as pd
# import numpy as np
# from tqdm import tqdm
#
# df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
#
# # Register `pandas.progress_apply` and `pandas.Series.map_apply` with `tqdm`
# # (can use `tqdm_gui`, `tqdm_notebook`, optional kwargs, etc.)
# tqdm.pandas(desc="my bar!")
#
# # Now you can use `progress_apply` instead of `apply`
# # and `progress_map` instead of `map`
# df.progress_apply(lambda x: x**2)
# # can also groupby:
# # df.groupby(0).progress_apply(lambda x: x**2)

# IPython/Jupyter is supported via the tqdm_notebook submodule
from tqdm import tnrange, tqdm_notebook
from time import sleep

for i in tnrange(10, desc='1st loop'):
    for j in tqdm_notebook(range(100), desc='2nd loop'):
        sleep(0.01)