#!/usr/bin/env python

###############################################################################
#
#  pymitchell is a module to import data from mitchell manager shop software
#  into easier to use objects
#
#  pymitchell uses a sqlite database which is made from the original
#  SMCORE32.mdb database mitchell uses.
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
        self.part = mitch.searchPartNumber(self.partNumber, mitch)
        self.tech = mitch.searchTechNumber(self.techNumber)


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
        self.estimateHazmat = row[56]
        self.estPartsAmount = row[58]
        self.timeOut = row[59]
        self.estimateHours = row[63]
        self.vehicle = mitch.searchVehicle(self.vehicleID)
        self.orders = []
        self.tech = mitch.searchTechNumber(self.defaultTech)
        getOrders = mitch.searchEstimate('_OrderList', self.estimateNumber)
        for order in getOrders:
            self.orders.append(Order(order, mitch))


class Schedule(object):
    def __init__(self, row, mitch):
        self.sched = row[2]
        self.notes = row[4]
        self.datePosted = row[5]
        self.custName = row[6]
        self.custID = row[7]
        self.recordNumber = row[9]
        self.estimateNumber = row[10]
        self.category = row[0]
        self.custCompany = row[1]
        self.recordType = row[3]
        self.estLaborHours = row[8]
        self.recordNumber = row[9]
        self.keyUnique = row[11]
        self.orders = []
        getOrders = mitch.searchEstimate('_OrderList', self.estimateNumber)
        for order in getOrders:
            self.orders.append(Order(order, mitch))


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
        self.custID = row[2]
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
        self.custName = row[26]
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
        self.tech = mitch.searchTechNumber(self.defaultTech)
        self.vehicle = mitch.searchVehicle(self.vehicleID)
        custrows = mitch.searchUser('_Customers', self.custID)
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
        self.phone = Phone(mitch.searchUser('_PhoneNum', self.custID)[0])

    def getVehicles(self, mitch):
        self.vehicles = []
        for vehicle in mitch.searchUser('_Vehicle', self.custID):
            self.vehicles.append(Vehicle(vehicle))

    def getHistory(self, mitch):
        self.history = []
        for hist in mitch.searchUser('_History', self.custID):
            self.history.append(History(hist, mitch))

    def getOpenOrders(self, mitch):
        self.schedule = []
        for sched in mitch.searchUser('_Schedule', self.custID):
            self.schedule.append(Schedule(sched, mitch))


class Mitchell(object):
    def __init__(self, sqlitepath):
        self.dbConnection = sqlite3.connect(sqlitepath)
        self.dbCur = self.dbConnection.cursor()
        self.tables = self.getTables()

    def getTables(self):
        q = "SELECT name FROM sqlite_master WHERE type = 'table'"
        getTables = self.dbCur.execute(q)
        tables = []
        for i in getTables:
            tables.append(str(i)[3:][:-3])
        return tables

    def searchUser(self, table, user):
        result = []
        key = {
            '_Vehicle': 'Cust_ID_', '_Customers': 'cust_id_',
            '_Status': 'cust_id_', '_History': 'cust_id_',
            '_Schedule': 'nCustNo_', '_PhoneNum': 'Cust_ID_'
        }
        q = "SELECT * FROM "+table+" WHERE "+key[table]+"=?"
        query = self.dbCur.execute(q, (user,))
        for row in query:
            result.append(row)
        return result

    def getSchedule(self, mitch):
        schedule = []
        q = "SELECT * FROM _Status"
        query = self.dbCur.execute(q).fetchall()
        for sched in query:
            s = Status(sched, mitch)
            if s.customer:
                schedule.append(s)
        return schedule

    def searchEstimate(self, table, estimateNumber):
        result = []
        key = {'_History': 'lineno_', '_OrderList': 'workid_'}
        q = "SELECT * FROM "+table+" WHERE "+key[table]+"=?"
        query = self.dbCur.execute(q, (estimateNumber,))
        for row in query:
            result.append(row)
        return result

    def searchLastName(self, name):
        result = []
        q = "SELECT * FROM _Customers WHERE lastname_ LIKE ?"
        query = self.dbCur.execute(q, (name,))
        for row in query:
            result.append(row)
        return result

    def searchPartNumber(self, partNumber, mitch):
        result = None
        if partNumber:
            q = "SELECT * FROM _PartsList WHERE partno_=?"
            query = self.dbCur.execute(q, (partNumber,)).fetchone()
            if query:
                result = Part(query)
            else:
                result = mitch.searchAltPartNumber(partNumber, mitch)
            return result
        else:
            return None

    def searchAltPartNumber(self, partNumber, mitch):
        result = None
        q = "SELECT * FROM _Altpartno WHERE alt_partno_=?"
        query = self.dbCur.execute(q, (partNumber,)).fetchone()
        if query:
            altpart = AltPartNo(query)
            result = mitch.searchUniquePartNumber(altpart.partUnique)
            return result
        else:
            return None

    def searchUniquePartNumber(self, partNumber):
        result = None
        q = "SELECT * FROM _PartsList WHERE part_unique_=?"
        query = self.dbCur.execute(q, (partNumber,)).fetchone()
        if query:
            result = Part(query)
            return result
        else:
            return None

    def searchTechNumber(self, techNumber):
        result = None
        q = "SELECT * FROM _Technician WHERE TechNum_=?"
        query = self.dbCur.execute(q, (techNumber,)).fetchone()
        if query:
            result = Technician(query)
            return result
        else:
            return None

    def searchVendorName(self, search):
        result = []
        q = "SELECT * FROM _Vendors WHERE name_ LIKE ('%' || ? || '%')"
        query = self.dbCur.execute(q, (search,))
        for row in query:
            result.append(Vendor(row))
        return result

    def searchVehicle(self, vehicleID):
        result = None
        q = "SELECT * FROM _Vehicle WHERE Vehicle_ID_=?"
        query = self.dbCur.execute(q, (vehicleID,)).fetchone()
        if query:
            result = Vehicle(query)
            return result
        else:
            return None

    def __del__(self):
        self.dbConnection.close()
