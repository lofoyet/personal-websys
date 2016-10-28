#!/usr/bin/python
#
#  This is a cgi program (hw2.cgi) that can be used to list the contents of a users websys directory
#
#  It must be named hw2.cgi and have world read access in order to work.
# This is due o security restrictions on the Stern systems that
# will only allow execution of programs named .cgi
#
# the input is the netid of the user, provided by a form with a fieldname of userid
# The program then constructs the path to the users directory
# Stern student directories are located at:
# /homedir/grad/FCHAR/NETID/
# and their websys directories are located at:
# /homedir/grad/FCHAR/NETID/public_html/websys
# where FCHAR is the first character of the netid and NETID is the netid.
#
#
#  i.e. user aws2310 has their home directory at
# /homedir/grad/a/aws2310
# So their web pages are at
# /homedir/grad/a/aws2310/public_html
# and their websys page is at
# /homedir/grad/a/aws2310/public_html/websys
#
#

# import the cgi modules to be able to retrive the form parameters
import cgi, cgitb
#import the commands module to let us execute unix commands
# and retrieve the results

import commands
import random
        

# print the html headers to standard output
# This is what the browser will be sent in response to the CGI request

print "Content-type:text/html"
# The next blank line MUST be there
print ""
print 
print '<head>'
print '<title>'
print 'Contents of a users websys directory'
print '</title>'
print '<style type="text/css">'
print 'body {'
print 'font-family: Arial;'
print 'font-size: 16px;'
print '}'

print '</style>'

print '</head>'
print '<body>'
#
#  call the FieldStorage method to retrieve the parameters after the ? on the URL
#
form=cgi.FieldStorage()
# form should contain all of the key value pairs
# For debugging, we will print it out

# retrieve the value of the userid field from the form
Fchar=form["userid"].value[0]
Userid =form["userid"].value

# Now construct the full path to their websys directory
# it should be  /homedir/grad/fchar/userid/public_html/websys
# where FCHAR is the first character of the userid
# type 'pwd' at the unix prompt to see you full path

# Note that we can treat strings as an array of characters
# with the first element at location 0

webSysPath = "/homedir/grad/" + Fchar + "/"  + Userid + "/public_html/websys"
print "<h3>"
print 'List of user ' + Userid + "'s" + ' websys directory'
print "</h3>"

# create the ls command
#, i.e. ls /homedir/grad/fchar/userid/public_html/websys

lscommand = 'ls --sort=extension ' + webSysPath
#
# tell html the next stuff is preformatted
# otherwise it ignores line breaks and will ruin it all together
#
print '<pre>'
status,lsresults = commands.getstatusoutput(lscommand)

list = lsresults.split("\n")

count = dict()
ext = []
for i in list:
    ext.append(i.split(".")[1])

j = 0
for i in range(0,len(ext)):
    if i == 0:
        count[j] = 1
    else:
        if ext[i] == ext[i-1]:
            count[j] = count[j]+1
        else:
            j = j+1
            count[j] = 1

k = 0


for i in count.keys():
    c1 = str(random.randrange(0,256))
    c2 = str(random.randrange(0,256))
    c3 = str(random.randrange(0,256))
    for j in range(0,count[i]):
        print '<font style=";color:rgb(' + c1 + ',' + c2 + ',' + c3 + ')">'+list[k]+'</font>'
        k = k+1


print '<br><a href="http://people.stern.nyu.edu/tl1848/websys/">Click here to go to the directory to click around</a>'
print '</pre>'
print '</body>'
print '</html>'

