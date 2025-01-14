import subprocess
import logging

import os
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from .scraping import scrape_olx

def schedule_scraping():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_olx, 'interval', minutes=1)
    scheduler.add_job(daily_db_dump, 'cron', hour=12, minute=0)
    scheduler.start()
    print("Scheduler started.")

def daily_db_dump():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dump_filename = f"olx_db_dump_{timestamp}.sql"
    dump_path = os.path.join(os.getcwd(), "dumps", dump_filename)
    if not os.path.exists("dumps"):
        os.makedirs("dumps")
        
    dump_command = f"pg_dump -U user -h localhost olx_db > {dump_path}"
    
    subprocess.run(dump_command, check=True)
    logging.info(f"Database dump created: {dump_filename}")
    
    try:
        subprocess.run(dump_command, shell=True, check=True)
        print(f"Database dumped successfully: {dump_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during database dump: {e}")
    
    # try:
    #     dump_file = f"./dumps/olx_db_dump_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql"
        
    #     command = [
    #         "pg_dump",
    #         "--host=db",  
    #         "--username=user",  
    #         "--dbname=olx_db", 
    #         "--file", dump_file,  
    #     ]
    #     subprocess.run(command, check=True)
    #     logging.info(f"Database dump created successfully: {dump_file}")
    # except subprocess.CalledProcessError as e:
    #     logging.error(f"Error while creating database dump: {e}")
