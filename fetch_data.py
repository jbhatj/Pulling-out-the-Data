from script import choose_qos_sm,fetch_details
import telnetlib
import time


def in_range(choice,ll,ul) :
    return True if choice>=ll and choice <=ul else False

def select_time() :
    pattern = "%d %m %Y %H %M %S"
    from_time = int(time.mktime(time.strptime(raw_input("\n*****FROM TIME******\nEnter  the date and time(give space btw each word(format: dd mm yy HH MM SS) ex: 30 06 2016 2 00 15 :\n"),pattern)))
    to_time = int(time.mktime(time.strptime(raw_input("\n*******TO TIME********\nEnter the date and time(give space btwn each word(fromat: dd mm yy HH MM SS) ex: 30 06 2016 4 00 15 :\n"),pattern)))
    return from_time,to_time

def do_connection(from_time,to_time,time_per_unit) :# arguments :(host,port),from_time,to_time,time_in=60(i.e set to per minute by default),
    port = "8159"
    hosts   = ["adbq1.other.dfw1.dna.akamai.com","adbq1.other.iad1.dna.akamai.com","adbq1.other.sjc1.dna.akamai.com" ]

    analyzer_id,cube_id =  choose_qos_sm()
    print analyzer_id,cube_id

    for host in hosts :
        try :
            connection = telnetlib.Telnet(host,port,timeout=10)
            time_now = int(time.time())
            string = "Select time - ((time - %s) %% %d) as time_1_min_bucket,sum(num_denied)+sum(num_warned)+0 as total_rules From qos.100154.288 Duration time >= %s and time <= %s Group By 1 Order By 1 ASC offset 0 with '{\"redirection\":\"off\"}' ;\n"%(from_time,time_per_unit,from_time,to_time)

            print string
            connection.write(string)
            l = connection.read_all()
            file_name = host.split('.')[2]+".csv" 
            with open(file_name,"w") as f :
                f.write(l)
        
            connection.close()
        except  :
            print "something went wrong while querying %s  and the error message is "%(host)

def main() :
    f_e,t_e = select_time()
    do_connection(f_e,t_e,60)


if __name__ == "__main__" :
    main()
