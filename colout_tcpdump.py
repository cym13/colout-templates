#encoding: utf-8

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
