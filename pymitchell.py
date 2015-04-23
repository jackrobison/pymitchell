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
    classDescription = None
    accountType = None
    classNumber = None

    def __init__(self, row):
        self.classDescription = row[3]
        self.accountType = row[9]
        self.classNumber = row[10]


class AltPartNo(object):
    altPartNumber = None
    partUnique = None
    mfgCode = None

    def __init__(self, row):
        self.altPartNumber = row[0]
        self.partUnique = row[1]
        self.mfgCode = row[2]


class Order(object):
    vendorCode = None
    techSel = None
    partConfirm = None
    qty = None
    cost = None
    performed = None
    accountclass = None
    category = None
    partNumber = None
    description = None
    techNumber = None
    hoursPay = None
    seqNo = None
    price = None
    hoursActual = None
    estimateNumber = None
    keyID = None
    sale = None
    listPrice = None
    mfgCode = None
    partUnique = None
    hoursCharged = None
    part = None

    def __init__(self, row, Mitchell):
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
        self.part = Mitchell.searchPartNumber(self.partNumber, Mitchell)


class Vehicle(object):
    vehicleID = None
    make = None
    owner = None
    plate = None
    model = None
    vin = None
    year = None
    inspDate = None
    engine = None
    custID = None
    subModel = None
    license = None
    memo = None
    odometer1 = None
    odometer2 = None

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
    custID = None
    promised = None
    orderType = None
    defaultTech = None
    reasonForVisit = None
    recordNumber = None
    writer = None
    laborAmount = None
    odometerIn = None
    odometerOut = None
    datePosted = None
    hazwasteAmount = None
    location = None
    timeIn = None
    yearMakeModel = None
    estimateNumber = None
    status = None
    balanceDue = None
    estimateShopSupplies = None
    sched = None
    hazWaste = None
    estLaborAmount = None
    partsAmount = None
    shopSupplies = None
    writerNumber = None
    shopSuppliesAmount = None
    odometerOut = None
    vehicleID = None
    defaultTechParts = None
    license = None
    printedDate = None
    estimateHazmat = None
    estPartsAmount = None
    timeOut = None
    estimateHours = None
    orders = []

    def __init__(self, row, Mitchell):
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
        self.orders = []
        getOrders = Mitchell.searchEstimate('_OrderList', self.estimateNumber)
        for order in getOrders:
            self.orders.append(Order(order, Mitchell))


class Schedule(object):
    sched = None
    notes = None
    datePosted = None
    custName = None
    custID = None
    recordNumber = None
    estimateNumber = None
    category = None
    custCompany = None
    recordType = None
    recordNumber = None
    keyUnique = None
    orders = []

    def __init__(self, row, Mitchell):
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
        getOrders = Mitchell.searchEstimate('_OrderList', self.estimateNumber)
        for order in getOrders:
            self.orders.append(Order(order, Mitchell))


class Manufacturer(object):
    mfgName = None
    mfgCode = None
    mfgUnique = None

    def __init__(self, row):
        self.mfgName = row[0]
        self.mfgCode = row[1]
        self.mfgUnique = row[2]


class Part(object):
    comment = None
    tireSize = None
    tireFlag = None
    category = None
    partNumber = None
    cost = None
    catList = None
    mfgCode = None
    description = None
    listPrice = None
    fixedListPrice = None
    partUnique = None

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
    phoneNumber = None
    extensionNumber = None
    custID = None

    def __init__(self, row):
        self.phoneNumber = row[0]
        self.custID = row[2]
        self.extensionNumber = row[3]


class Status(object):
    createdAsEstimateFlag = None
    refNumber = None
    custID = None
    promised = None
    orderType = None
    defaultTech = None
    reasonForVisit = None
    recordNumber = None
    writer = None
    laborAmount = None
    odometerIn = None
    datePosted = None
    custName = None
    hazwasteAmount = None
    location = None
    timeIn = None
    yearMakeModel = None
    estimateNumber = None
    status = None
    balanceDue = None
    estimateShopSupplies = None
    sched = None
    hazWaste = None
    estLaborAmount = None
    partsAmount = None
    shopSupplies = None
    writerNumber = None
    shopSuppliesAmount = None
    odometerOut = None
    vehicleID = None
    defaultTechParts = None
    license = None
    printedDate = None
    estPartsAmount = None
    timeOut = None
    estimateHours = None
    customer = None

    def __init__(self, row, Mitchell):
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

        custrows = Mitchell.searchUser('_Customers', self.custID)
        if custrows:
            self.customer = Customer(custrows[0], Mitchell)
        else:
            self.customer = None


class Technician(object):
    city = None
    zipCode = None
    lastName = None
    state = None
    firstName = None
    phoneNumber = None
    address = None
    techNumber = None

    def __init__(self, row):
        city = row[0]
        zipCode = row[1]
        lastName = row[2]
        state = row[4]
        firstName = row[7]
        phoneNumber = row[10]
        address = row[12]
        techNumber = row[13]


class Vendors(object):
    comment = None
    extensionNumber2 = None
    code = None
    city = None
    zipCode = None
    state = None
    extensionNumber1 = None
    phoneNumber2 = None
    phoneNumber1 = None
    address = None
    accountclass = None
    name = None
    contact = None

    def __init__(self, row):
        comment = row[0]
        extensionNumber2 = row[2]
        code = row[3]
        city = row[8]
        zipCode = row[9]
        state = row[12]
        extensionNumber1 = row[16]
        phoneNumber2 = row[17]
        phoneNumber1 = row[18]
        address = row[22]
        accountclass = row[23]
        name = row[25]
        contact = row[26]


class Customer(object):
    custID = None
    lastVisited = None
    balanceDue = None
    city = None
    zipCode = None
    state = None
    firstName = None
    lastName = None
    company = None
    address = None
    remarks = None
    emailAddress = None

    vehicles = []
    history = []
    phone = None
    schedule = []

    def __init__(self, row, Mitchell):
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
        self.phone = Phone(Mitchell.searchUser('_PhoneNum', self.custID)[0])

    def getVehicles(self, Mitchell):
        self.vehicles = []
        for vehicle in Mitchell.searchUser('_Vehicle', self.custID):
            self.vehicles.append(Vehicle(vehicle))

    def getHistory(self, Mitchell):
        self.history = []
        for hist in Mitchell.searchUser('_History', self.custID):
            self.history.append(History(hist, Mitchell))

    def getOpenOrders(self, Mitchell):
        self.schedule = []
        for sched in Mitchell.searchUser('_Schedule', self.custID):
            self.schedule.append(Schedule(sched, Mitchell))


class Mitchell(object):
    dbConnection = None
    dbCur = None
    tables = None

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

    def getSchedule(self, Mitchell):
        schedule = []
        q = "SELECT * FROM _Status"
        query = self.dbCur.execute(q).fetchall()
        for sched in query:
            s = Status(sched, Mitchell)
            if s.customer:
                schedule.append(s)
                print s.customer.custID
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

    def searchPartNumber(self, partNumber, Mitchell):
        result = None
        q = "SELECT * FROM _PartsList WHERE partno_=?"
        query = self.dbCur.execute(q, (partNumber,)).fetchone()
        if query:
            result = Part(query)
        else:
            result = Mitchell.searchAltPartNumber(partNumber, Mitchell)
        return result

    def searchAltPartNumber(self, partNumber, Mitchell):
        result = None
        q = "SELECT * FROM _Altpartno WHERE alt_partno_=?"
        query = self.dbCur.execute(q, (partNumber)).fetchone()
        if query:
            altpart = AltPartNo(query)
            result = Mitchell.searchUniquePartNumber(altpart.partUnique)
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

    def __del__(self):
        self.dbConnection.close()
