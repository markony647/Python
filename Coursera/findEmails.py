import sys
import os
import re
 
def parse_options(*args):
    '''
    Parse options and make list of parsed options
    available to program
    '''
    email, text = '--email', '--text'
    options = {email:False,text:False}
    get_value = lambda a,x: a[a.index(x)+1]
 
    if args:
        for option in args[0]:
            if option == email and get_value(args[0],email) == 'yes':
                options[option] = True
            if option == text and get_value(args[0],text) == 'yes':
                options[option] = True
 
    return options[email], options[text]
 
def get_files(directory="current"):
    '''
    Get file names that are in directory
    @param directory: set directory to discover
    '''
    set_current_dir = os.getcwd() if directory=="current" else directory
    (root, dirs, files) = os.walk(set_current_dir).next()
    add = lambda f: root+"\\"+f
    return [add(file) for file in files]
 
def main():
    (is_email_stat, is_general_stat) = parse_options(sys.argv[1:])
 
    text_to_analyze = [line for file in get_files() for line in open(file)]
    emails = re.findall(r"\w+@\w+.\w+","".join(text_to_analyze))
 
    if is_email_stat:
        print "Found %d emails" % len(emails)
 
    if is_general_stat:
        print "%d word are analyzed" % len("".join(text_to_analyze))
 
    print "\n"+str(emails)
 
if __name__ == "__main__":
    main()