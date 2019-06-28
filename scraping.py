from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import csv

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://psleci.nic.in/default.aspx")

driver.maximize_window()

dropdown=driver.find_element_by_id("ddlState")
options = [x for x in dropdown.find_elements_by_tag_name("option")]

def refresh(t):
    driver.get("http://psleci.nic.in/default.aspx")
    select = Select(driver.find_element_by_id('ddlState'))
    select.select_by_index(t)
    time.sleep(2)
def refresh2(new):
    refresh(t)
    select_district=Select(driver.find_element_by_id("ddlDistrict"))
    select_district.select_by_index(new)
    time.sleep(2)

with open("polling.json","w") as f:
    for element in options[1:]:

        if element==1:
            time.sleep(2)               #Loop for printing States
        r=element.get_attribute("innerHTML")
        print('-->',r)
        f.write(json.dumps(r))

        for i in range(len(options)):                        #loop for Selecting a state
            time.sleep(2)
            select = Select(driver.find_element_by_id('ddlState'))
            select.select_by_index(i)
            district=driver.find_element_by_id("ddlDistrict")
            t=i


            options2=[x for x in district.find_elements_by_tag_name("option")]

            for ele in options2[1:]:

                select = Select(driver.find_element_by_id('ddlState'))
                select.select_by_index(i)
                district=driver.find_element_by_id("ddlDistrict")
                time.sleep(1)
                s=ele.get_attribute("innerHTML")
                print('----->',s)
                f.write(json.dumps(s))

                for j in range(len(options2)):
                                                        #Loop for selecting district
                    time.sleep(2)
                    select_district=Select(driver.find_element_by_id("ddlDistrict"))
                    select_district.select_by_index(j)
                    ac=driver.find_element_by_id("ddlAC")

                    options3=[x for x in ac.find_elements_by_tag_name("option")]
                    time.sleep(2)

                    for ele2 in options3[1:]:           #Loop for printing AC
                        time.sleep(2)
                        attr=ele2.get_attribute("innerHTML")
                        print('---------->',attr)
                        f.write(json.dumps(attr))

                        for k in range(len(options3)):
                                                                #Loop for selecting district
                            time.sleep(2)
                            select_ac=Select(driver.find_element_by_id("ddlAC"))
                            select_ac.select_by_index(k)
                            ps=driver.find_element_by_id("ddlPS")

                            options4=[x for x in ps.find_elements_by_tag_name("option")]
                            time.sleep(2)

                            for ele3 in options4[1:]:           #Loop for printing AC
                                if ele3==1:
                                    time.sleep(2)
                                polling=ele3.get_attribute("innerHTML")
                                print('--------------->',polling)
                                f.write(json.dumps(polling))
                                f.write('\n')
                            f.write('\n\n')
                        f.write('\n\n\n')
                        if k==len(options3)-1:
                            new=j
                            new+=1
                            refresh2(new)
                            break
                f.write('\n\n\n\n')

                t+=1
                refresh(t)
                break
