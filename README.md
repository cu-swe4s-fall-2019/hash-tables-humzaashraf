# Hash tables

# pngs of scatters saved = the hashed value versus the hashed index
# y axis: hashed value from random words in a dictionary
# x axis: parallel array of values corresponding to hashed indices  
# Each png file also has the run time for the program in the name

# The ascii method is less uniformally distributed with random data 
# and more memory allocation did not improve performance

# The Rolling method was much more uniformally distributed and 
# looked more uniform given more memory allocation

# Based on random data, the chained hash collision may be slightly 
# less sensitive to pre-allocated memory

# Larger N meant less time to run (this makes sense, since
# linear search time is reduced)

# Chained hash is much faster than linear probing 