'''
how to use?
python make_summary_from_jmeter_log.py logdir outputcsvfname
'''




import sys
import csv
import os
import datetime

class LogAnalayzer:
    def load_files(self,target_dir,csv_fname):
        self.output=[]
        #        #start,end,test_time,avt,errro,throuput

        self.output.append(["fname","start","end","testing_time","avt","error","throuput","statuscode"])
        if not os.path.exists(target_dir):
            raise Exception("theres no such directory")
        #os.chdir(target_dir)
        fnames=os.listdir(target_dir)
        print(fnames)
        for fname in fnames:
            fname=os.path.join(target_dir,fname)

            self.load_file(fname)
        self.__write_csv(csv_fname)


    def __write_csv(self,fname):
        with open(fname,"w",newline="")as writer:
            csv_writer=csv.writer(writer)
            for ele in self.output:
                csv_writer.writerow(ele)




    def load_file(self,fname):
        '''

        :param domain:fileドメイン
        :param fname:
        :return:
        '''
        with open(fname,"r")as reader:
            csv_reader=csv.reader(reader)
            csv_list=list(csv_reader)
            if len(csv_list)>=2:
                st=datetime.datetime.fromtimestamp(int(csv_list[1][0])/1000)
                ed=datetime.datetime.fromtimestamp(int(csv_list[-1][0])/1000)
                #print(st)
                #print(ed)
                ele=Element(fname,st,ed)
                for i in range(1,len(csv_list)):
                    ele.count+=1
                    ele.total_response_time+=int(csv_list[i][1])
                    statuscode=(int(csv_list[i][3]))
                    if statuscode!=200:
                        ele.status_code_set.add(statuscode)
                        ele.error_count+=1

            self.output.append(ele.make_list())







class Element:
    def __init__(self,fname,st,ed):
        self.fname=fname
        self.count=0
        self.st=st
        self.ed=ed
        #second
        self.delta=(ed-st).total_seconds()

        self.total_response_time=0
        self.error_count=0
        self.error_rate=0
        self.response_time=0
        self.throughput=None
        self.status_code_set=set()
        self.testing_time=0
        #average resonse time
        self.avt=None

    def __summarize(self):
        if self.count>0:

            self.error_rate=float(self.error_count/self.count)
            #second
            self.throughput=self.count/self.delta
            self.avt=(self.total_response_time)/self.count


    def make_list(self):
        self.__summarize()
        #start,end,test_time,avt,errro,throuput
        output_list=[self.fname.split("/")[-1],self.st.strftime("%Y/%m/%d %H:%M"),self.ed.strftime("%Y/%m/%d %H:%M")
            ,int(self.delta/60),round(self.avt,2),round(self.error_rate*100,2),round(self.throughput,2),self.status_code_set]

        #print(output_list)
        return output_list






if __name__=="__main__":

    args=sys.argv
    print(args)
    if not len(args)==3:
        raise Exception("argslen must be 4")


    fname="/home/shibaken/IDEetc/apache-jmeter-3.2/bin/logs/kuber_r2s20_1m/1user_171102_30min.jtl"
    tester=LogAnalayzer()
    #tester.load_file(fname)
    log_dir=args[1]
    output_csv=args[2]
    tester.load_files(log_dir,output_csv)


