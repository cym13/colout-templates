#encoding: utf-8

"""
TCPDUMP
=======

Colors the left side according to the kind of packet we are encountering:
    - blue   -> ICMP
    - purple -> UDP
    - red    -> ARP
    - cyan   -> IP
    - white  -> anything else

The layer 3 protocol is set in green, source and destination in yellow and
other important information in purple.
"""

def theme(context):
    return context,[
            [ "^([0-9]+:[0-9]+:[0-9.]+) (.*) ([^ ]+)\.[^. ]+ > ([^ ]+)\.[^.:]+(:) (ICMP6?).*$",
                "blue,green,yellow,yellow,green,purple", "" ],
            [ "^([0-9]+:[0-9]+:[0-9.]+) (.*) ([^ ]+)\.[^. ]+ > ([^ ]+)\.[^.:]+(:) (UDP).*$",
                "purple,green,yellow,yellow,green,purple", "" ],
            [ "^([0-9]+:[0-9]+:[0-9.]+) (ARP), Request who-has ([^ ]+) (.* )?tell ([^ ]+),.*$",
                "red,green,yellow,none,yellow,", "" ],
            [ "^([0-9]+:[0-9]+:[0-9.]+) (ARP), Reply ([^ ]+) is-at ([^ ]+) .*$",
                "red,green,yellow,yellow,", "" ],
            [ "^([0-9]+:[0-9]+:[0-9.]+) (IP6?) ([^ ]+)\.[^. ]+ > ([^ ]+)\.[^.:]+(:) .*$",
                "cyan,green,yellow,yellow,green", "" ],
        ]
