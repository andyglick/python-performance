import sys
import zarr

from zarr import blosc

sys.path.insert(0, '../shared')

from utilities import PLINK_PREF
from ch3 import conv_chrom

MAX_POSITIONS = 100000
BLOCK_SIZE = int(sys.argv[1])

blosc.set_nthreads(1)
root = zarr.open('ignore.zarr', mode='w')
conv_chrom(f'{PLINK_PREF}.tped', BLOCK_SIZE, MAX_POSITIONS, root, 1)

#memory size
# number of runs - we are doing only 1
