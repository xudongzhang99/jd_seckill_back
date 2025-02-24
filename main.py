
from datetime import datetime
import sys
from jd_spider_requests import JdSeckill
import signal, psutil
import time, os
from threading import Timer



jd_seckill = JdSeckill()
def kill_processes(parent_pid, sig=signal.SIGTERM):
    try:
        parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children(recursive=True)
    for process in children:
        process.send_signal(sig)
    parent.send_signal(sig)
    # 定义函数
def do_function( choice_function ):
   if choice_function == '1':
        jd_seckill.reserve()
   elif choice_function == '2':
        weekday = datetime.now().isoweekday()
        if weekday == 6 or weekday == 7:
            print('周末没有抢购')
            sys.exit(1)
        else:
            Timer(60 * 12, lambda:kill_processes(os.getpid()), ()).start()
            jd_seckill.seckill_by_proc_pool()      
   else:
        print('没有此功能')
        sys.exit(1)
    

if __name__ == '__main__':
    a = """
       oooo oooooooooo.            .oooooo..o                     oooo         o8o  oooo  oooo  
       `888 `888'   `Y8b          d8P'    `Y8                     `888         `"'  `888  `888  
        888  888      888         Y88bo.       .ooooo.   .ooooo.   888  oooo  oooo   888   888  
        888  888      888          `"Y8888o.  d88' `88b d88' `"Y8  888 .8P'   `888   888   888  
        888  888      888 8888888      `"Y88b 888ooo888 888        888888.     888   888   888  
        888  888     d88'         oo     .d8P 888    .o 888   .o8  888 `88b.   888   888   888  
    .o. 88P o888bood8P'           8""88888P'  `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o o888o 
    `Y888P                                                                                                                                                  
                                               
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
    """
    
    if len(sys.argv) == 2 :
        do_function(sys.argv[1])
    else:
       print(a)
       choice_function = input('请选择:')
       do_function(choice_function)