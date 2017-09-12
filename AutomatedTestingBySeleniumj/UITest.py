from selenium import webdriver
import selenium
import datetime
import workdays
import unittest
from selenium.webdriver.support.ui import Select
from dateutil.relativedelta import relativedelta
import csv
import os

D_LIMIT=1400
CAPTURE_DIR="./capture_files/"

BOUNDARY1="boundary1"
BOUNDARY2="boundary2"
EXTERIOR1="exterior1"
EXTERIOR2="exterior2"
import time
'''
APIにリクエストを自動的に投げる
'''


#休暇がdddd/dd/dd　の形式で書かれたcsv
HOLIDAYS_FNAME="./holidays.csv"
TARGET_URL=""
MODE_LIST=["D","W","M","S"]
CODE_DICT={"valid":1332,"invalid":9999}
class RequestSender:
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.get(TARGET_URL)
        #
        self.driver.implicitly_wait(200)
        self.today=datetime.datetime.now()

    def load_test_case(self,fname):
        #parit　testの組み合わせを記したファイルを読み込む
        with open(fname,"r",encoding="utf8")as reader:
            self.driver.get(TARGET_URL)
            csv_read = csv.reader(reader)
            test_cases = list(csv_read)
            count=0
            for case in test_cases:
                count+=1
                if count==1:
                    continue
                print(count)
                self.set_case(case[0],case[1],case[2],case[3])
                time.sleep(3)
        self.driver.quit()






    def set_case(self,mode,start,end,code):

        if code == "valid":
            code = CODE_DICT[code]
        elif code == "invalid":
            code = CODE_DICT[code]
        else:
            raise Exception("codeはvalidかinvalidのどちらかです")

        if mode=="S":
            self.calc_s()
            self.send_request(code,mode,self.s_dict[start],self.s_dict[end])

        elif mode=="W":
            self.calc_week()
            self.send_request(code,mode,self.w_dict[start],self.w_dict[end])

        elif mode=="D":
            self.calc_day()
            self.send_request(code,mode,self.d_dict[start],self.d_dict[end])
        elif mode=="M":
            self.calc_month()
            self.send_request(code,mode,self.m_dict[start],self.m_dict[end])
        else:
            raise Exception("modeはS,W,D,Mのどれかです")






    def send_request(self,code,mode,start_time,end_time):
        print("{}:::{}~{}".format(mode,start_time,end_time))
        #write each parameter form
        self.input_stock_code(code)
        self.input_mode(mode)
        self.input_start(start_time)
        self.input_end(end_time)
        #send request
        #self.driver.find_element_by_xpath("//select[@class='btn btn-primary']")
        button=self.driver.find_element_by_tag_name("button")
        #button.click()


        #check response
        #output=self.driver.find_element_by_class_name("list")
        #if output.is_displayed():
         #   print("responseがかえってきました")
        self.take_capture()


    def input_start(self,start_time):
        '''

        :return:
        '''
        #        create_account_button=driver.find_element_by_xpath("//button[@title='Create an Account''")

        start_form=self.driver.find_element_by_name("start")
        start_form.clear()
        start_form.send_keys(start_time)

    def input_end(self,end_time):
        end_form=self.driver.find_element_by_name("end")
        end_form.clear()
        end_form.send_keys(end_time)

    def input_mode(self,mode):
        if not mode in MODE_LIST:
            raise Exception("modeはS,D,W,Mのどれかを選んでくらさい")
        mode_form=Select(self.driver.find_element_by_name("mode"))
        mode_form.select_by_value(mode)

    def input_stock_code(self,code):
        code_form=self.driver.find_element_by_name("code")
        code_form.clear()
        code_form.send_keys(code)

    def calc_s(self):
        self.s_dict={}

        boundary1=datetime.datetime(self.today.year,self.today.month,self.today.day,9,0,0)
        boundary2=datetime.datetime(self.today.year,self.today.month,self.today.day,15,0,0)
        exterior1=datetime.datetime(self.today.year,self.today.month,self.today.day,8,59,0)
        exterior2=datetime.datetime(self.today.year,self.today.month,self.today.day,15,1,0)


        self.s_dict[BOUNDARY1] = boundary1.strftime("%Y/%m/%d %H:%M")
        self.s_dict[BOUNDARY2] = boundary2.strftime("%Y/%m/%d %H:%M")
        self.s_dict[EXTERIOR1] = exterior1.strftime("%Y/%m/%d %H:%M")
        self.s_dict[EXTERIOR2] = exterior2.strftime("%Y/%m/%d %H:%M")
        




    def calc_week(self):
        self.w_dict={}
        #300週前
        boundary1=self.today-datetime.timedelta(weeks=300)
        #今週
        boundary2=self.today
        exterior1=self.today-datetime.timedelta(weeks=301)
        exterior2=self.today+datetime.timedelta(weeks=1)

        self.w_dict[BOUNDARY1] = boundary1.strftime("%Y/%m/%d")
        self.w_dict[BOUNDARY2] = boundary2.strftime("%Y/%m/%d")
        self.w_dict[EXTERIOR1] = exterior1.strftime("%Y/%m/%d")
        self.w_dict[EXTERIOR2] = exterior2.strftime("%Y/%m/%d")

    def load_holidays(self,fname):
        with open(fname,"r",encoding="utf8")as reader:
            csv_read=csv.reader(reader)
            examp_data=list(csv_read)[0]
            self.holidays=[datetime.datetime.strptime(ele,"%Y/%m/%d") for ele in examp_data ]
            #print(self.holidays)

   # def calc_work(self):
        #self.load_holidays(HOLIDAYS_FNAME)
        #start_date = datetime.datetime(2017, 5, 1)
        #end_date = datetime.datetime(2017, 5, 31)
        #return (workdays.workday(self.today, days=-D_LIMIT,holidays=self.holidays))



    def calc_day(self):
        self.d_dict={}
        self.load_holidays(HOLIDAYS_FNAME)
        boundary1= workdays.workday(self.today, days=-D_LIMIT,holidays=self.holidays)
        boundary2=self.today
        exterior1=workdays.workday(boundary1, days=-1,holidays=self.holidays)
        exterior2=workdays.workday(self.today,days=1,holidays=self.holidays)

        self.d_dict[BOUNDARY1] = boundary1.strftime("%Y/%m/%d")
        self.d_dict[BOUNDARY2] = boundary2.strftime("%Y/%m/%d")
        self.d_dict[EXTERIOR1] = exterior1.strftime("%Y/%m/%d")
        self.d_dict[EXTERIOR2] = exterior2.strftime("%Y/%m/%d")







    def calc_month(self):
        self.m_dict={}
        #120ヶ月前
        boundary1=self.today-relativedelta(months=120)
        #今月
        boundary2=self.today
        #121ヶ月前
        exterior1=boundary1- relativedelta(months=1)
        #来月
        exterior2=boundary2+relativedelta(months=1)
        self.m_dict[BOUNDARY1]=boundary1.strftime("%Y/%m/%d")
        self.m_dict[BOUNDARY2]=boundary2.strftime("%Y/%m/%d")
        self.m_dict[EXTERIOR1]=exterior1.strftime("%Y/%m/%d")
        self.m_dict[EXTERIOR2]=exterior2.strftime("%Y/%m/%d")





    def take_capture(self):
        #queryの内容をファイル名に反映させるようにする！！！！！！！！！！！！！！！！！！！！！！！！！！！
        today=datetime.datetime.now()
        fname="ui_test_capture_"+today.strftime("%Y%m%d_%H%M%S")+".png"
        fname=os.path.join(CAPTURE_DIR,fname)
        print(fname)

        self.driver.save_screenshot(fname)

if __name__=="__main__":
    tester=RequestSender()
    #tester.send_request(1332,"W","2017/01/01","2017/09/01")
    #tester.load_holidays("holidays.csv")
    #tester.calc_day()
    tester.load_test_case("test_case.csv")

    #tester.send_request()
