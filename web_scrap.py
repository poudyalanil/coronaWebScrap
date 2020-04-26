
import requests as req
from bs4 import BeautifulSoup as b4
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt 
import time

def scrap():
    src = req.get('https://www.worldometers.info/coronavirus/')
    sop = b4(src.content,'html.parser')


    when = datetime.now().strftime("%d-%b")
    print(when)



    main_div = sop.find_all(id='maincounter-wrap')

    cases = int((main_div[0].find('span').get_text()).replace(',',''))
    death = int(main_div[1].find('span').get_text().replace(',',''))
    recovered = int(main_div[2].find('span').get_text().replace(',',''))
    time_checked = time.strftime("%I:%M %p")
    print(time_checked)
    datas = pd.DataFrame(
        {
            'Date':[when],
            'Time':[time_checked],
            'Total Cases':[cases],
            'Deaths':[death],
            'Total Recovered':[recovered],
        })

    print(datas)
    
    datas.to_csv('corona.csv',mode='a', header=False)
    fil =  pd.read_csv('corona.csv')
    plt.plot(fil.Time,fil.Deaths)

    plt.grid(b=False, which='major', color='#666666', linestyle='-')
    
    plt.tight_layout(pad=0.000001, w_pad=0.0001, h_pad=1.0)
    plt.xlabel(f"{when}")
    plt.ylabel("Numbers")
    timees = str(int(time.time()))
    plt.savefig(f"images/{timees}", bbox_inches = "tight")
scrap()