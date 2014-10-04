from optparse import OptionParser
import sys

op = OptionParser()
op.add_option('--hello','-T',dest='hello',default= True)
opts, args = op.parse_args()

print args
