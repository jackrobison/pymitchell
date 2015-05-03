#!/usr/bin/env python

###############################################################################
#
#  pymitchell is a module to import data from mitchell manager shop software
#  into easier to use objects
#
#  pymitchell uses a sqlite database which is made from the original
#  SMCORE32.mdb database that mitchell uses.
#
#  The table names in sqlite database have a preceding '_' before them, this
#  was done because sqlite didn't like  some of the original names. The key
#  names have a trailing '_' added to them for the same reason.
#
#  Jack Robison
#
###############################################################################

import sqlite3


class AccountClass(object):
    def __init__(self, row):
        self.classDescription = row[3]
        self.accountType = row[9]
        self.classNumber = row[10]


class AltPartNo(object):
    def __init__(self, row):
        self.altPartNumber = row[0]
        self.partUnique = row[1]
        self.mfgCode = row[2]


class Order(object):
    def __init__(self, row, mitch):
        self.vendorCode = row[0]
        self.techSel = row[2]
        self.partConfirm = row[4]
        self.qty = row[5]
        self.cost = row[8]
        self.performed = row[9]
        self.accountclass = row[12]
        self.category = row[13]
        self.partNumber = row[16]
        self.description = row[25]
        self.techNumber = row[26]
        self.hoursPay = row[27]
        self.seqNumber = row[28]
        self.price = row[29]
        self.hoursActual = row[30]
        self.estimateNumber = row[34]
        self.keyID = row[43]
        self.sale = row[48]
        self.listPrice = row[49]
        self.mfgCode = row[51]
        self.partUnique = row[52]
        self.hoursCharged = row[55]
        self.part = mitch.search_part_number(self.partNumber, mitch)
        self.tech = mitch.search_tech_number(self.techNumber)


class Vehicle(object):
    def __init__(self, row):
        self.vehicleID = row[2]
        self.make = row[6]
        self.owner = row[21]
        self.plate = row[27]
        self.model = row[35]
        self.vin = row[45]
        self.year = row[50]
        self.inspDate = row[0]
        self.engine = row[17]
        self.custID = row[21]
        self.subModel = row[23]
        self.license = row[27]
        self.memo = row[32]
        self.odometer1 = row[46]
        self.odometer2 = row[47]


class History(object):
    def __init__(self, row, mitch):
        self.custID = row[8]
        self.promised = row[9]
        self.orderType = row[11]
        self.defaultTech = row[12]
        self.reasonForVisit = row[20]
        self.recordNumber = row[21]
        self.writer = row[22]
        self.laborAmount = row[23]
        self.odometerIn = row[24]
        self.datePosted = row[25]
        self.hazwasteAmount = row[27]
        self.location = row[29]
        self.timeIn = row[30]
        self.estimateNumber = row[33]
        self.status = row[34]
        self.balanceDue = row[35]
        self.estimateShopSupplies = row[36]
        self.sched = row[37]
        self.hazWaste = row[41]
        self.estLaborAmount = row[42]
        self.partsAmount = row[43]
        self.shopSupplies = row[44]
        self.writerNumber = row[45]
        self.shopSuppliesAmount = row[46]
        self.odometerOut = row[49]
        self.vehicleID = row[50]
        self.defaultTechParts = row[51]
        self.printedDate = row[55]
        self.estimateHazmat = row[56]
        self.estPartsAmount = row[58]
        self.timeOut = row[59]
        self.estimateHours = row[63]
        self.vehicle = mitch.search_vehicle(self.vehicleID)
        self.orders = []
        self.tech = mitch.search_tech_number(self.defaultTech)
        getOrders = mitch.search_estimate('_OrderList', self.estimateNumber)
        self.orders = [Order(order, mitch) for order in getOrders]
        custrows = mitch.search_user('_Customers', self.custID)
        if custrows:
            self.customer = Customer(custrows[0], mitch)


class Schedule(object):
    def __init__(self, row, mitch):
        self.sched = row[2]
        self.notes = row[4]
        self.datePosted = row[5]
        self.custID = row[7]
        self.recordNumber = row[9]
        self.estimateNumber = row[10]
        self.category = row[0]
        self.custCompany = row[1]
        self.recordType = row[3]
        self.estLaborHours = row[8]
        self.recordNumber = row[9]
        self.keyUnique = row[11]
        getOrders = mitch.search_estimate('_OrderList', self.estimateNumber)
        self.orders = [Order(order, mitch) for order in getOrders]
        custrows = mitch.search_user('_Customers', self.custID)
        if custrows:
            self.customer = Customer(custrows[0], mitch)


class Part(object):
    def __init__(self, row):
        self.comment = row[0]
        self.tireSize = row[1]
        self.tireFlag = row[2]
        self.category = row[7]
        self.partNumber = row[8]
        self.cost = row[9]
        self.catList = row[10]
        self.mfgCode = row[12]
        self.description = row[13]
        self.listPrice = row[19]
        self.fixedListPrice = row[20]
        self.partUnique = row[21]


class Phone(object):
    def __init__(self, row):
        self.phoneNumber = row[0]
        self.extensionNumber = row[3]


class Status(object):
    def __init__(self, row, mitch):
        self.createdAsEstimateFlag = row[1]
        self.refNumber = row[7]
        self.custID = row[8]
        self.promised = row[9]
        self.orderType = row[11]
        self.defaultTech = row[12]
        self.reasonForVisit = row[20]
        self.recordNumber = row[21]
        self.writer = row[22]
        self.laborAmount = row[23]
        self.odometerIn = row[24]
        self.datePosted = row[25]
        self.hazwasteAmount = row[27]
        self.location = row[29]
        self.timeIn = row[30]
        self.yearMakeModel = row[31]
        self.estimateNumber = row[33]
        self.status = row[34]
        self.balanceDue = row[35]
        self.estimateShopSupplies = row[36]
        self.sched = row[37]
        self.hazWaste = row[41]
        self.estLaborAmount = row[42]
        self.partsAmount = row[43]
        self.shopSupplies = row[44]
        self.writerNumber = row[45]
        self.shopSuppliesAmount = row[46]
        self.odometerOut = row[49]
        self.vehicleID = row[50]
        self.defaultTechParts = row[51]
        self.license = row[52]
        self.printedDate = row[55]
        self.estPartsAmount = row[58]
        self.timeOut = row[59]
        self.estimateHours = row[63]
        self.tech = mitch.search_tech_number(self.defaultTech)
        self.vehicle = mitch.search_vehicle(self.vehicleID)
        custrows = mitch.search_user('_Customers', self.custID)
        if custrows:
            self.customer = Customer(custrows[0], mitch)
        else:
            self.customer = None


class Technician(object):
    def __init__(self, row):
        self.city = row[0]
        self.zipCode = row[1]
        self.lastName = row[2]
        self.state = row[4]
        self.firstName = row[7]
        self.phoneNumber = row[10]
        self.address = row[12]
        self.techNumber = row[13]


class Vendor(object):
    def __init__(self, row):
        self.comment = row[0]
        self.extensionNumber2 = row[2]
        self.code = row[3]
        self.city = row[8]
        self.zipCode = row[9]
        self.state = row[12]
        self.extensionNumber1 = row[16]
        self.phoneNumber2 = row[17]
        self.phoneNumber1 = row[18]
        self.address = row[22]
        self.accountclass = row[23]
        self.name = row[25]
        self.contact = row[26]


class Customer(object):
    def __init__(self, row, mitch):
        self.custID = row[2]
        self.lastVisited = row[3]
        self.balanceDue = row[6]
        self.city = row[7]
        self.zipCode = row[9]
        self.state = row[13]
        self.firstName = row[17]
        self.lastName = row[19]
        self.company = row[20]
        self.address = row[25]
        self.remarks = row[26]
        self.emailAddress = row[37]
        self.vehicles = []
        self.history = []
        self.schedule = []
        self.phone = Phone(mitch.search_user('_PhoneNum', self.custID)[0])

    #get all vehicles belonging to the customer
    def get_vehicles(self, mitch):
        vehicleSearch = mitch.search_user('_Vehicle', self.custID)
        self.vehicles = [Vehicle(vehicle) for vehicle in vehicleSearch]

    #get past orders from the customer
    def get_history(self, mitch):
        historySearch = mitch.search_user('_History', self.custID)
        self.history = [History(hist, mitch) for hist in historySearch]

    #get presently open orders for the customer
    def get_open_orders(self, mitch):
        orderSearch = mitch.search_user('_Schedule', self.custID)
        self.schedule = [Schedule(sched, mitch) for sched in orderSearch]

    #search customer orders for a part number
    def search_cust_part_number(self, partNumber, mitch):
        if self.history == []:
            self.get_history(mitch)
        if self.schedule == []:
            self.get_open_orders(mitch)
        result = []
        for hist in self.history:
            for order in hist.orders:
                if (partNumber.lower() in order.partNumber.lower()):
                    result.append(order)
                else:
                    if order.part:
                        if (partNumber.lower() in order.part.partNumber.lower()):
                            result.append(order)
        for sched in self.schedule:
            for order in sched.orders:
                if (partNumber.lower() in order.partNumber.lower()):
                    result.append(order)
                else:
                    if order.part:
                        if (partNumber.lower() in order.part.partNumber.lower()):
                            result.append(order)
        return result

    #search customer orders for a part description
    def search_cust_part_description(self, description, mitch):
        if self.history == []:
            self.get_history(mitch)
        if self.schedule == []:
            self.get_open_orders(mitch)
        result = []
        for hist in self.history:
            for order in hist.orders:
                if (description.lower() in order.description.lower()):
                    result.append(order)
                else:
                    if order.part:
                        if (description.lower() in order.part.description.lower()):
                            result.append(order)
        for sched in self.schedule:
            for order in sched.orders:
                if (description.lower() in order.description.lower()):
                    result.append(order)
                else:
                    if order.part:
                        if (description.lower() in order.part.description.lower()):
                            result.append(order)
        return result


class Mitchell(object):
    def __init__(self, sqlitepath):
        self.dbConnection = sqlite3.connect(sqlitepath)
        self.dbCur = self.dbConnection.cursor()
        self.tables = self.get_tables()

    #get all the table names in the sqlite db
    def get_tables(self):
        q = "SELECT name FROM sqlite_master WHERE type = 'table'"
        get_tables = self.dbCur.execute(q)
        tables = [str(i)[3:][:-3] for i in get_tables]
        return tables

    #search for rows containing a customer id in a given table
    def search_user(self, table, user):
        result = []
        key = {
            '_Vehicle': 'Cust_ID_', '_Customers': 'cust_id_',
            '_Status': 'cust_id_', '_History': 'cust_id_',
            '_Schedule': 'nCustNo_', '_PhoneNum': 'Cust_ID_'
        }
        q = "SELECT * FROM "+table+" WHERE "+key[table]+"=?"
        query = self.dbCur.execute(q, (user,))
        result = [row for row in query]
        return result

    #get the current scheduled jobs, returns a list of status objects
    def get_schedule(self, mitch):
        schedule = []
        q = "SELECT * FROM _Status"
        query = self.dbCur.execute(q).fetchall()
        for sched in query:
            s = Status(sched, mitch)
            if s.customer:
                schedule.append(s)
        return schedule

    #search for an estimate number in a table
    def search_estimate(self, table, estimateNumber):
        result = []
        key = {
            '_History': 'lineno_', '_OrderList': 'workid_',
            '_Status': 'lineno_', '_Schedule': 'lineno_'
        }
        q = "SELECT * FROM "+table+" WHERE "+key[table]+"=?"
        query = self.dbCur.execute(q, (estimateNumber,))
        result = [row for row in query]
        return result

    #search for a record number in a table
    def search_record(self, table, recordNumber):
        result = []
        key = {
            '_History': 'recno_', '_Status': 'recno_',
            '_Schedule': 'recno_'
        }
        q = "SELECT * FROM "+table+" WHERE "+key[table]+"=?"
        query = self.dbCur.execute(q, (recordNumber,))
        result = [row for row in query]
        return result

    #get customer table rows containing last names similar to the search
    def search_last_name(self, name):
        result = []
        q = "SELECT * FROM _Customers WHERE lastname_ LIKE ?"
        query = self.dbCur.execute(q, (name,))
        result = [row for row in query]
        return result

    #search for a part in the inventory list by description
    def search_part_description(self, search):
        result = []
        q = "SELECT * FROM _PartsList WHERE description_ LIKE ('%' || ? || '%')"
        query = self.dbCur.execute(q, (search,))
        if query:
            result = [Part(row) for row in query]
        return result

    #search for a part number in the inventory parts list
    def search_part_number(self, partNumber, mitch):
        result = None
        if partNumber:
            q = "SELECT * FROM _PartsList WHERE partno_=?"
            query = self.dbCur.execute(q, (partNumber,)).fetchone()
            if query:
                result = Part(query)
            else:
                result = mitch.search_alt_part_number(partNumber, mitch)
            return result
        else:
            return None

    #if the previous part search failed, see if the part has a unique ID
    def search_alt_part_number(self, partNumber, mitch):
        result = None
        q = "SELECT * FROM _Altpartno WHERE alt_partno_=?"
        query = self.dbCur.execute(q, (partNumber,)).fetchone()
        if query:
            altpart = AltPartNo(query)
            result = mitch.search_unique_part_number(altpart.partUnique)
            return result
        else:
            return None

    #search for a part in inventory based on unique ID
    def search_unique_part_number(self, partNumber):
        result = None
        q = "SELECT * FROM _PartsList WHERE part_unique_=?"
        query = self.dbCur.execute(q, (partNumber,)).fetchone()
        if query:
            result = Part(query)
            return result
        else:
            return None

    #get a technician object from a tech id
    def search_tech_number(self, techNumber):
        result = None
        q = "SELECT * FROM _Technician WHERE TechNum_=?"
        query = self.dbCur.execute(q, (techNumber,)).fetchone()
        if query:
            result = Technician(query)
            return result
        else:
            return None

    #search the vendor list
    def search_vendor_name(self, search):
        result = []
        q = "SELECT * FROM _Vendors WHERE name_ LIKE ('%' || ? || '%')"
        query = self.dbCur.execute(q, (search,))
        if query:
            result = [Vendor(row) for row in query]
        return result

    #get a vehicle object from a vehicle id
    def search_vehicle(self, vehicleID):
        result = None
        q = "SELECT * FROM _Vehicle WHERE Vehicle_ID_=?"
        query = self.dbCur.execute(q, (vehicleID,)).fetchone()
        if query:
            result = Vehicle(query)
            return result
        else:
            return None

    #convert an estimate number into a record number
    def est_number_to_rec_number(self, estimateNumber, mitch):
        hist = mitch.search_estimate('_History', estimateNumber)
        if hist != []:
            return History(hist[0], mitch).recordNumber
        stat = mitch.search_estimate('_Status', estimateNumber)
        if stat != []:
            return Status(stat[0], mitch).recordNumber
        sched = mitch.search_estimate('_Schedule', estimateNumber)
        if sched != []:
            return Schedule(Schedule[0], mitch).recordNumber

    #convert a record number into an estimate number
    def rec_number_to_est_number(self, recordNumber, mitch):
        hist = mitch.search_record('_History', recordNumber)
        if hist != []:
            return History(hist[0], mitch).estimateNumber
        stat = mitch.search_record('_Status', recordNumber)
        if stat != []:
            return Status(stat[0], mitch).estimateNumber
        sched = mitch.search_record('_Schedule', recordNumber)
        if sched != []:
            return Schedule(Schedule[0], mitch).estimateNumber

    def __del__(self):
        self.dbConnection.close()
