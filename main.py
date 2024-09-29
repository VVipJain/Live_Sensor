from sensor.exception import SensorException
import os
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

#def test_exception():
   #     try:
   #         logging.info("error aayegi 0 vaali")
   #         a=1/0
     #   except Exception as e:
     #       raise SensorException(e,sys)

if __name__ == "__main__":
    file_path = r"C:\Users\VIPUL JAIN\Documents\Live_Sensor\sensor_data.csv"
    database_name = "vipul_jain"
    collection_name = "sensor_data"
    dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)


    #try:
    #    test_exception()
    #except Exception as e:
    #    print(e)