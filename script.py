import os,csv

def fetch_details(command) : 
    print command
    os.system(command)

    with open("file.csv") as csvfile :
        dic={}
        reader = csv.DictReader(csvfile)
        for row in reader :
            if row["analyzerid"].isdigit() :
                dic[row["analyzerid"]] = {"analyzername" : row["analyzername"]}#,"analyzertype" : row["analyzertype"] }
 #       for key in sorted(dic.keys(),key=int) :
 #           print key,dic[key]["analyzername"]#,dic[key]["analyzertype"]
#    a = raw_input("do you want to fetch details\npress enter to yes\ntype any char to no")
#    if a == '' :
        ch = raw_input("Enter the analyzerid")
        if ch not in dic.keys() :
            print "analyzerid doesnt exist"
        else :
            return ch


def choose_qos_sm() :
    command = 'sql2 --csv --output=file.csv -q internal.dev.query.akadns.net "select analyzerid,analyzername from analytics_info where analyzertype=\'clientside_qos1_%s\' group by 1,2 order by 1 ";'
    choices  = { 1 : "sm", 2: "vod", 3: "live" }
    choices_ci  = { "sm" : {"c_c" : "288", "t_c" : "298"}, "vod" : {"c_c":"137","t_c":"138"} ,"live" : { "c_c" :"136", "t_c" : "139" }}
    lol = {1:"c_c",2:"t_c"}
    print "select 1 for clientside_qos1_sm\nselect 2 for clientside_qos1_vod\nselect 3 for clientside_qos1_live\n"
    choice = int(raw_input("enter your choice"))
    print "select 1 for console cube\nselect 2 for time cube\n"
    ch = int(raw_input("enter your choice\t"))
    command=command %choices[choice]
    cube_id=choices_ci[choices[choice]][lol[ch]]

    return fetch_details(command),cube_id

