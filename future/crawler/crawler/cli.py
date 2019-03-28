import sys 
from optparse import OptionParser

from .helper import date_difference


def main():
    
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    #parser.add_option("-f", "--file", dest="filename",
    #                  help="read data from FILENAME")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    #parser.add_option("-d", "--date", action="store_true", help="Date difference")                      
    parser.add_option("-d", "--date", action="store_true", help="Date difference 2019,1,9 2019,4,9 year,month,day")                      
                      
    (options, args) = parser.parse_args()
    print(len(args))
    print(options)
    print(args)
    #if len(args) != 1:
        #parser.error("incorrect number of arguments")
    #if options.verbose:
        #print("reading %s..." % options.filename)                      
    if options.date:
        print('date')
        # year, month, day
        print(len(args))
        if len(args) >= 2:
            result = date_difference(args[0], args[1])
            print(result)
        else:
            parser.print_help()
        #print("reading %s..." % options.filename)
        
    
	
    

if __name__ == '__main__':
    main()
    
    # https://pymotw.com/3/argparse/index.html
    # https://docs.python.org/3/library/optparse.html
    