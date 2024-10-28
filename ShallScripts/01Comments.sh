#!/usr/bin/bash

# To find the location of installed bash use below command
#    $ which bash
#    output: /usr/bin/bash

# First line is a shebang line its #!<path>  for the programming language to be used by linux
#   eg #!/bin/bash                <--Used to execute shell script
#   eg #!/usr/bin/perl            <--Used to execute perl script

# Execute a shell script
#   $bash <path/filename>
#   $./<path/filename>
  

# this is single comment 

: '
Colons and single quotes.
This is another way
to create a multi-line
comment
'

<<-EOF
This is a 
multi-line 
comment
EOF

echo hello world
echo $0 # Prints the file name