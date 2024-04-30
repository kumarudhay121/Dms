from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import os
from django.core.files.storage import FileSystemStorage
import pymysql
from datetime import datetime

global uname

def parseDate(dd):
    arr = dd.split("-")
    yy = int(arr[2].strip())
    mm = int(arr[1].strip())
    dd = int(arr[0].strip())
    current_date = str(yy)+"-"
    if mm < 10:
        current_date += "0"+str(mm)+"-"
    else:
        current_date += str(mm)+"-"
    if dd < 10:
        current_date += "0"+str(dd)
    else:
        current_date += str(dd)
    print(current_date)    
    return current_date

def AddEmployeesAction(request):
    if request.method == 'POST':
        ssn = request.POST.get('t1', False)
        fname = request.POST.get('t2', False)
        lname = request.POST.get('t3', False)
        salary = request.POST.get('t4', False)
        hiredate = request.POST.get('t5', False)
        jobclass = request.POST.get('t6', False)
        street = request.POST.get('t7', False)
        city = request.POST.get('t8', False)
        state = request.POST.get('t9', False)
        zipcode = request.POST.get('t10', False)
        title = request.POST.get('t11', False)
        speciality = request.POST.get('t12', False)
        birthdate = request.POST.get('t13', False)
        certification = request.POST.get('t14', False)
        facility = request.POST.get('t15', False)
        hiredate = parseDate(hiredate)
        birthdate = parseDate(birthdate)
        output = "none"
        eid = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select max(emp_id) FROM employee")
            rows = cur.fetchall()
            for row in rows:
                eid = row[0]
                break
        if eid is not None:
            eid += 1
        else:
            eid = 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO employee VALUES('"+str(ssn)+"','"+str(eid)+"','"+fname+"','"+lname+"','"+salary+"','"+hiredate+"','"+jobclass+"','"+street+"','"+city+"','"+state+"','"+zipcode+"','"+title+"','"+speciality+"','"+birthdate+"','"+certification+"','"+facility+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Employee details added with Employee Id as : '+str(eid)
        context= {'data':output}
        return render(request, 'AddEmployees.html', context)      

def AddEmployees(request):
    if request.method == 'GET':
        output = '<tr><td><font size="3" color="black">Facility&nbsp;ID</b></td><td><select name="t15">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select facility_id FROM facility")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'
        context= {'data1':output}
        return render(request, 'AddEmployees.html', context)

def AddMedicalFacility(request):
    if request.method == 'GET':
        return render(request, 'AddMedicalFacility.html', {})

def EmployeeManage(request):
    if request.method == 'GET':
        return render(request, 'EmployeeManage.html', {})

def PatientManage(request):
    if request.method == 'GET':
        return render(request, 'PatientManage.html', {})    

def Reporting(request):
    if request.method == 'GET':
        return render(request, 'Reporting.html', {})

def Back(request):
    if request.method == 'GET':
        return render(request, 'AdminScreen.html', {})

def AdminLogin(request):
    if request.method == 'GET':
        return render(request, 'AdminLogin.html', {})  

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def AdminLoginAction(request):
    global uname
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if username == 'admin' and password == 'admin':
            context= {'data':'welcome '+username}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'login failed'}
            return render(request, 'AdminLogin.html', context)

def AddInsuranceAction(request):
    if request.method == 'POST':
        name = request.POST.get('t1', False)
        street = request.POST.get('t2', False)
        city = request.POST.get('t3', False)
        state = request.POST.get('t4', False)
        zipcode = request.POST.get('t5', False)
        output = "none"
        eid = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select max(insurance_id) FROM insurance")
            rows = cur.fetchall()
            for row in rows:
                eid = row[0]
                break
        if eid is not None:
            eid += 1
        else:
            eid = 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO insurance VALUES('"+str(eid)+"','"+name+"','"+street+"','"+city+"','"+state+"','"+zipcode+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Insurance details added with Insurance Id as : '+str(eid)
        context= {'data':output}
        return render(request, 'AddInsurance.html', context)              

def AddInsurance(request):
    if request.method == 'GET':
        return render(request, 'AddInsurance.html', {})        

def AddMedicalFacilityAction(request):
    if request.method == 'POST':
        ftype = request.POST.get('t1', False)
        size = request.POST.get('t2', False)
        street = request.POST.get('t3', False)
        city = request.POST.get('t4', False)
        state = request.POST.get('t5', False)
        zipcode = request.POST.get('t6', False)
        office = request.POST.get('t7', False)
        room = request.POST.get('t8', False)
        pcode = request.POST.get('t9', False)
        desc = request.POST.get('t10', False)
        output = "none"
        fid = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select max(facility_id) FROM facility")
            rows = cur.fetchall()
            for row in rows:
                fid = row[0]
                break
        if fid is not None:
            fid += 1
        else:
            fid = 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO facility VALUES('"+str(fid)+"','"+ftype+"','"+size+"','"+street+"','"+city+"','"+state+"','"+zipcode+"','"+office+"','"+room+"','"+pcode+"','"+desc+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Facility details added with Facility Id as : '+str(fid)
        context= {'data':output}
        return render(request, 'AddMedicalFacility.html', context)
      
def ViewEmployeeManage(request):
    if request.method == 'GET':
        return render(request, 'ViewEmployeeManage.html', {})

def ViewMedicalFacility(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Facility ID</th><th><font size="" color="black">Facility Type</th>'
        output += '<th><font size="" color="black">Size</th>'
        output+='<th><font size="" color="black">Street</th><th><font size="" color="black">City</th>'
        output+='<th><font size="" color="black">State</th><th><font size="" color="black">Zip Code</th>'
        output+='<th><font size="" color="black">Office Count</th><th><font size="" color="black">Room Count</th>'
        output+='<th><font size="" color="black">PCode</th><th><font size="" color="black">Description</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM facility")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+str(row[3])+'</td>'
                output+='<td><font size="" color="black">'+str(row[4])+'</td><td><font size="" color="black">'+str(row[5])+'</td>'
                output+='<td><font size="" color="black">'+str(row[6])+'</td><td><font size="" color="black">'+str(row[7])+'</td>'
                output+='<td><font size="" color="black">'+str(row[8])+'</td><td><font size="" color="black">'+str(row[9])+'</td>'
                output+='<td><font size="" color="black">'+str(row[10])+'</td></tr>'
        output += "</table><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'ViewEmployeeManage.html', context)

def ViewEmployees(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">SSN No</th><th><font size="" color="black">Employee ID</th>'
        output += '<th><font size="" color="black">First Name</th><th><font size="" color="black">Last Name</th><th><font size="" color="black">Salary</th>'
        output+='<th><font size="" color="black">Hire Date</th><th><font size="" color="black">Job Class</th>'
        output+='<th><font size="" color="black">Street</th><th><font size="" color="black">City</th>'
        output+='<th><font size="" color="black">State</th><th><font size="" color="black">Zip Code</th>'
        output+='<th><font size="" color="black">Job Title</th><th><font size="" color="black">Speciality</th>'
        output+='<th><font size="" color="black">Birth Date</th><th><font size="" color="black">Certification</th><th><font size="" color="black">Facility ID</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM employee")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+str(row[3])+'</td>'
                output+='<td><font size="" color="black">'+str(row[4])+'</td><td><font size="" color="black">'+str(row[5])+'</td>'
                output+='<td><font size="" color="black">'+str(row[6])+'</td><td><font size="" color="black">'+str(row[7])+'</td>'
                output+='<td><font size="" color="black">'+str(row[8])+'</td><td><font size="" color="black">'+str(row[9])+'</td>'
                output+='<td><font size="" color="black">'+str(row[10])+'</td><td><font size="" color="black">'+str(row[11])+'</td>'
                output+='<td><font size="" color="black">'+str(row[12])+'</td><td><font size="" color="black">'+str(row[13])+'</td>'
                output+='<td><font size="" color="black">'+str(row[14])+'</td><td><font size="" color="black">'+str(row[15])+'</td>'
        output += "</table><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'ViewEmployeeManage.html', context)

def InsuranceInvoice(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Insurance ID</th><th><font size="" color="black">Date</th>'
        output+='<th><font size="" color="black">Invoice Revenue</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select i.insurance_id,i.invoice_date, sum(id.cost) from invoice_details id, invoice i where id.invoice_id = i.invoice_id order by i.invoice_date")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+str(row[2])+'</td></tr>'
        output += "</table><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'ViewEmployeeManage.html', context)

def ViewInsurance(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Insurance ID</th><th><font size="" color="black">Insurance Name</th>'
        output+='<th><font size="" color="black">Street</th><th><font size="" color="black">City</th>'
        output+='<th><font size="" color="black">State</th><th><font size="" color="black">Zip Code</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM insurance")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+str(row[3])+'</td>'
                output+='<td><font size="" color="black">'+str(row[4])+'</td><td><font size="" color="black">'+str(row[5])+'</td></tr>'
        output += "</table><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'ViewEmployeeManage.html', context)


#==============================patient manage

def PatientManage(request):
    if request.method == 'GET':
        return render(request, 'PatientManage.html', {})    

def CreatePatient(request):
    if request.method == 'GET':
        output = '<tr><td><font size="3" color="black">Employee&nbsp;SSN</b></td><td><select name="t8">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select SSN FROM employee")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'
        output += '<tr><td><font size="3" color="black">Insurance&nbsp;ID</b></td><td><select name="t9">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select insurance_id FROM insurance")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'
        
        context= {'data1':output}
        return render(request, 'CreatePatient.html', context)
    
def CreatePatientAction(request):
    if request.method == 'POST':
        fname = request.POST.get('t1', False)
        initials = request.POST.get('t2', False)
        lname = request.POST.get('t3', False)
        street = request.POST.get('t4', False)
        city = request.POST.get('t5', False)
        state = request.POST.get('t6', False)
        zipcode = request.POST.get('t7', False)
        ssn = request.POST.get('t8', False)
        insurance = request.POST.get('t9', False)
        output = "none"
        pid = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select max(patient_id) FROM patient")
            rows = cur.fetchall()
            for row in rows:
                pid = row[0]
                break
        if pid is not None:
            pid += 1
        else:
            pid = 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO patient VALUES('"+str(pid)+"','"+fname+"','"+initials+"','"+lname+"','"+street+"','"+city+"','"+state+"','"+zipcode+"','"+ssn+"','"+insurance+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Patient details added with Patient Id as : '+str(pid)
        context= {'data':output}
        return render(request, 'PatientManage.html', context)

def Appointment(request):
    if request.method == 'GET':
        output = '<tr><td><font size="3" color="black">Employee&nbsp;SSN</b></td><td><select name="t1">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select SSN FROM employee")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'
        output += '<tr><td><font size="3" color="black">Patient&nbsp;ID</b></td><td><select name="t2">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select patient_id FROM patient")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'

        output += '<tr><td><font size="3" color="black">Facility&nbsp;ID</b></td><td><select name="t3">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select facility_id FROM facility")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'
        
        context= {'data1':output}
        return render(request, 'Appointment.html', context)
    
def AppointmentAction(request):
    if request.method == 'POST':
        ssn = request.POST.get('t1', False)
        patient = request.POST.get('t2', False)
        facility = request.POST.get('t3', False)
        appointment_date = request.POST.get('t4', False)
        appointment_date = parseDate(appointment_date)
        output = "none"
        iid = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select max(invoice_id) FROM make_appointment")
            rows = cur.fetchall()
            for row in rows:
                iid = row[0]
                break
        if iid is not None:
            iid += 1
        else:
            iid = 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO make_appointment VALUES('"+str(ssn)+"','"+patient+"','"+facility+"','"+str(iid)+"','"+appointment_date+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Appointment details added with Invoice Id as : '+str(iid)
        context= {'data':output}
        return render(request, 'PatientManage.html', context)


def UpdatePayment(request):
    if request.method == 'GET':
        output = '<tr><td><font size="3" color="black">Invoice&nbsp;ID</b></td><td><select name="t1">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select invoice_id FROM make_appointment")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'
        context= {'data1':output}
        return render(request, 'UpdatePayment.html', context)

def getPatientID(invoice):
    pid = None
    ssn = None
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select SSN, patient_id FROM make_appointment where invoice_id='"+invoice+"'")
        rows = cur.fetchall()
        for row in rows:
            ssn = row[0]
            pid = row[1]
            break
    insurance_id = None
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select insurance_id FROM patient where patient_id='"+str(pid)+"'")
        rows = cur.fetchall()
        for row in rows:
            insurance_id = row[0]
            break
    return str(pid), str(insurance_id), str(ssn)    
            
    

def UpdatePaymentAction(request):
    if request.method == 'POST':
        invoice = request.POST.get('t1', False)
        amount = request.POST.get('t2', False)
        treatment = request.POST.get('t3', False)
        pid, insurance_id, ssn = getPatientID(invoice)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO treatment VALUES('"+str(ssn)+"','"+pid+"','"+treatment+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        today = str(datetime.now())
        arr = today.split(" ")
        today = arr[0].strip()

        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO invoice VALUES('"+str(invoice)+"','"+today+"','"+insurance_id+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()

        invoice_num = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select max(invoice_num) FROM invoice_details")
            rows = cur.fetchall()
            for row in rows:
                invoice_num = row[0]
                break
        if invoice_num is not None:
            invoice_num += 1
        else:
            invoice_num = 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO invoice_details VALUES('"+str(invoice_num)+"','"+amount+"','"+invoice+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        context= {'data':"Invoice payment successfully updated with invoice number : "+str(invoice_num)}
        return render(request, 'PatientManage.html', context)

def Reporting(request):
    if request.method == 'GET':
        return render(request, 'Reporting.html', {})        
        
def DayWiseRevenue(request):
    if request.method == 'GET':
        return render(request, 'DayWiseRevenue.html', {})

def DateWiseRevenue(request):
    if request.method == 'GET':
        output = '<tr><td><font size="3" color="black">Physician&nbsp;SSN</b></td><td><select name="t1">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select SSN FROM employee")
            rows = cur.fetchall()
            for row in rows:
                output += '<option value="'+str(row[0])+'">'+str(row[0])+'</option>'
        output += '</select></td></tr>'
        context= {'data1':output}
        return render(request, 'DateWiseRevenue.html', context)
    
def InsuranceRevenue(request):
    if request.method == 'GET':
        return render(request, 'InsuranceRevenue.html', {})            
    
        
def DayWiseRevenueAction(request):
    if request.method == 'POST':
        dd = request.POST.get('t1', False)
        dd = parseDate(dd)
        output = ''
        output+='<table border=1 align=center width=100%><tr>'
        output+='<th><font size="" color="black">Revenue Date</th><th><font size="" color="black">Sub Total</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        total = 0
        with con:
            cur = con.cursor()
            cur.execute("select i.invoice_date, sum(id.cost) from invoice_details id, invoice i, make_appointment ma where i.invoice_date = '"+dd+"' and i.invoice_id = id.invoice_id and i.invoice_id = ma.invoice_id")
            #select ma.facility_id, i.insurance_id, i.invoice_date, sum(id.cost) from invoice_details id, invoice i, make_appointment ma where i.invoice_date = '"+dd+"' group by ma.facility_id")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td></tr>'
                #output+='<td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+str(row[3])+'</td></tr>'
                total += row[1]
        output+='<tr><td><font size="" color="black">Total = '+str(total)+'</td></tr>'        
        output += "</table><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'Reporting.html', context)

def DateWiseRevenueAction(request):
    if request.method == 'POST':
        ssn = request.POST.get('t1', False)
        dd = request.POST.get('t2', False)
        dd = parseDate(dd)
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Physician SSN</th><th><font size="" color="black">Patient ID</th>'
        output+='<th><font size="" color="black">Facility ID</th><th><font size="" color="black">Invoice ID</th><th><font size="" color="black">Appointment Date</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from make_appointment where appointment='"+dd+"' and SSN='"+ssn+"'")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+str(row[3])+'</td><td><font size="" color="black">'+str(row[4])+'</td></tr>'
        output += "</table><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'Reporting.html', context)


def InsuranceRevenueAction(request):
    if request.method == 'POST':
        from_date = request.POST.get('t1', False)
        from_date = parseDate(from_date)
        to_date = request.POST.get('t2', False)
        to_date = parseDate(to_date)
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Insurance ID</th><th><font size="" color="black">Average Revenue</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'dms',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select i.insurance_id, avg(id.cost) from invoice_details id, invoice i where i.invoice_id = id.invoice_id and i.invoice_date between '"+from_date+"' and '"+to_date+"' group by i.insurance_id")
            #select i.insurance_id, avg(id.cost) from invoice_details id, invoice i where i.invoice_date between '"+from_date+"' and '"+to_date+"' group by i.insurance_id")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td></tr>'                     
        output += "</table><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'Reporting.html', context)
        

    
