import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/disvcg/projects/PyElementary']

# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup !!must be!! stored in a main backup directory
target_dir = '/Users/disvcg/projects/PyElementary/backup/' 

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
today = target_dir + time.strftime('%Y%m%d')

# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = raw_input('Enter a comment --> ')

if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'
    #Notice the backslash!

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'



