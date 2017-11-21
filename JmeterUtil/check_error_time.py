import datetime

def  sort_error_by_time(fname):
    with open(fname,"r")as reader:
        ouput_dict={}
        #first line only cotains variables names
        reader.readline()
        for line in reader:
            if line.__contains__("Non"):
                tmp_time=line.split(",")[0]
                tmp_resp=line.split(",")[1]
                error_time=datetime.datetime.fromtimestamp(int(tmp_time)/1000)

                time_str=(error_time.strftime("%Y/%m/%d %H:%M"))
                ouput_dict.setdefault(time_str,0)
                ouput_dict[time_str]+=1
                print(tmp_resp)

    print(sorted(ouput_dict.items()))



def calc_response_time(fname):
    with open(fname, "r")as reader:
        reader.readline()
        count_ok=0
        count_error=0
        res_time_ok=0
        res_time_error=0

        for line in reader:
            if line.__contains__("Non"):
                count_error+=1
                #print(line.split(",")[1])
                res_time_error+=float(line.split(",")[1])
            else:
                count_ok+=1
                #print(line.split(",")[1])

                res_time_ok+=float(line.split(",")[1])
    print("ok")

    print(float(res_time_ok)/float(count_ok))
    print("error")
    print(float(res_time_error/count_error))












if __name__=="__main__":
    #file_open("logs/7user_1mega_171116_elb_check_2.jtl")
    calc_response_time("logs/10user_171116_10min.jtl")

    ok
    210.6411371237458
    error
    2255.342979635584
ok
463.97408207343415
error
1771.090909090909