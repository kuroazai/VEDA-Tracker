#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:27:11 2020

@author: fidelismwansa
"""
import shelve
import random
from fastapi import FastAPI
from pydantic import BaseModel


class DataBase(object):

    def __init__(self):
        # Open the database
        self.db = shelve.open('devices.db')
        self.n_devices = len(self.db)

    def create_device(self):
        # Get the current size
        size = len(self.db)
        # Generate ID
        ID = "VEDA-X" + str(size + 1)
        # For testing
        rf_id = random.randint(10000, 19999)
        gsm_id = random.randint(10000, 19999)
        alert = True
        y = random.uniform(-0.48065185546874994, 0.142822265625)
        x = random.uniform(51.32374658474385, 51.675961632740744)
        # Generate a device
        self.db[ID] = {  'ID': ID,
                         'Name': "",
                         'RF_ID': rf_id,
                         'GSM_ID': gsm_id,
                         'Status': alert,
                         "geometry": {"type": "Point", "coordinates": [x,y]}

                      }

    def get_devices(self):
        # Check if items exist
        if len(self.db) == 0:
            return
        else:
            devices = []
            for x in self.db:
                # Append each device to devices list
                devices.append(self.db[x])
            return devices


dm = DataBase()
app = FastAPI()

#************************************************************
#   Classes
#************************************************************


class Device(BaseModel):
    ID: str
    Name: str = None
    RF_ID = str
    GSM_ID = str
    Status: bool
    Journey_Log: list = []


@app.get("/")
async def root():
    # test = Device( ID='Veda-RX0', Name='Saber', RF_ID='12315', GSM_ID='123123')
    # dm.create_device()
    return dm.get_devices()
    # my_user: Device = Device(ID='Veda-RX0', Name='Saber', RF_ID='12315', GSM_ID='123123', Status=True, Journey_Log=[])
    # return {'Devices':{ '0':{"ID": "Veda-RX01", 'Radio Frequency':'30,000', "GSM Number":'0712312376', 'Stolen From':"Street name", "Time passed after theft":'01:00:00', 'Journey Log':[0,1,2,3,4,5,6,7,8,9], 'Stops POF':[0,9,8,7,6,5,4,3,2,1], "Refuel POF":[0,1,2]}}}


@app.put("/Devices/{id}")
async def add_device(item: Device):
    return item


@app.get("/Device/{ID}")
async def get_device(ID):
    return dm.db[ID]
