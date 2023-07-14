#_________PAYROLL    MANAGEMENT    SYSTEMS_____________
import mysql.connector as sqltor
import time
import datetime
from tkinter import *
from tkinter import messagebox
import subprocess

db=sqltor.connect(host='localhost',
                  user='root',
                  password='root',
                  database='payroll')
cursor=db.cursor()


root=Tk()
root.title('Payroll Systems')
root.geometry('1350x650+0+0')

Tops=Frame(root,width=1350,height=50,bd=8,relief='raise')
Tops.pack(side=TOP)
f1=Frame(root,width=600,height=600,bd=8,relief='raise')
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,relief='raise')
f2.pack(side=RIGHT)
f1a=Frame(f1,width=600,height=200,bd=20,relief='raise')
f1a.pack(side=TOP)
f1b=Frame(f1,width=600,height=600,bd=20,relief='raise')
f1b.pack(side=TOP)

lblinfo=Label(Tops,font=('arial',60,'bold'),text='  Payment Management Systems  ',bd=10,fg='purple')
lblinfo.grid(row=0,column=0)


def databeses():
    subprocess.call('calc.exe')
    
    
def iExit():
    qExit=messagebox.askyesno('Payroll Management Systems','Do You Want To Exit The System?')
    if qExit>0:
        root.destroy()
        return
    
def Reset():
    Name.set('')
    Address.set('')
    HoursWorked.set('')
    WagesHour.set('')
    Payable.set('')
    Taxable.set('')
    NetPayable.set('')
    GrossPayable.set('')
    OvertimeHours.set('')
    Employer.set('')
    WorkerID.set('')
    txtPaySlip.delete('1.0',END)
    
def EnterInfo():
    txtPaySlip.insert(END,'\t           PAY  SLIP  \n\n')
    txtPaySlip.insert(END,'Name : \t\t'+ Name.get() + '\n\n')
    txtPaySlip.insert(END,'Address : \t\t'+ Address.get() + '\n\n')
    txtPaySlip.insert(END,'Employer : \t\t'+ Employer.get() + '\n\n')
    txtPaySlip.insert(END,'Worker ID : \t\t'+ WorkerID.get() + '\n\n')
    txtPaySlip.insert(END,'Hours Worked : \t\t'+ HoursWorked.get() + '\n\n')
    txtPaySlip.insert(END,'Wages per Hour : \t\t'+ WagesHour.get() + '\n\n')
    txtPaySlip.insert(END,'Tax Paid : \t\t'+ NetPayable.get() + '\n\n')
    txtPaySlip.insert(END,'Net Payable : \t\t'+ Payable.get() + '\n\n')
    txtPaySlip.insert(END,'Gross Payable : \t\t'+ Taxable.get() + '\n\n')

def WeeklyWages():
    HoursWorkedPerWeek=float(HoursWorked.get())
    WagesPerHours=float(WagesHour.get())

    PayDue=WagesPerHours*HoursWorkedPerWeek
    PaymentDue=str('%.2f'%(PayDue))
    Payable.set(PaymentDue)
    
    Tax=PayDue-PayDue*1/6
    Taxables=str('%.2f'%(Tax))
    Taxable.set(Taxables)
    GrossPayable.set(Taxable)

    NetPay=PayDue-Tax
    NetPays=str('%.2f'%(NetPay))
    NetPayable.set(NetPays)
    
    if HoursWorkedPerWeek>40:
        overTimeHours=(HoursWorkedPerWeek-40)+WagesPerHours*1.5
        overtimehrs=str('%.2f'%(overTimeHours))
        OvertimeHours.set(overtimehrs)
    elif HoursWorkedPerWeek<=40:
        overtimePay=(HoursWorkedPerWeek-40)+WagesPerHours*1.5
        Overtimehrs=str('%.2f'%(overtimePay))
        OvertimeHours.set(Overtimehrs)
    return

def Insert():
    WORKERID=WorkerID.get()
    NAME=Name.get()
    ADDRESS=Address.get()
    EMPLOYER=Employer.get()
    HOURSWORKED=HoursWorked.get()
    HOURLYRATE=WagesHour.get()
    TAX=NetPayable.get()
    OVERTIME=OvertimeHours.get()
    GROSSPAY=Taxable.get()
    NETPAY=Payable.get()
    cursor=db.cursor()
    cursor.execute('INSERT INTO payslips VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(WORKERID,NAME,ADDRESS,EMPLOYER,HOURSWORKED,HOURLYRATE,TAX,OVERTIME,GROSSPAY,NETPAY))
    db.commit()
    messagebox.showinfo('Payroll Management Systems','Your record is inserted into the Database')
    Reset()


Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
WagesHour=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable=StringVar()
OvertimeHours=StringVar()
Employer=StringVar()
WorkerID=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
DateOfOrder.set(time.strftime('%d/%m/%y'))


lblName=Label(f1a,text='Name',font=('arial',16,'bold'),bd=20,fg='green').grid(row=0,column=0)
lblAddress=Label(f1a,text='Address',font=('arial',16,'bold'),bd=20,fg='green').grid(row=0,column=2)
lblEmployer=Label(f1a,text='Employer',font=('arial',16,'bold'),bd=20,fg='green').grid(row=1,column=0)
lblWorkerID=Label(f1a,text='Worker ID',font=('arial',16,'bold'),bd=20,fg='green').grid(row=1,column=2)
lblHoursWorked=Label(f1a,text='Hours Worked',font=('arial',16,'bold'),bd=20,fg='green').grid(row=2,column=0)
lblHourlyRate=Label(f1a,text='Hourly Rate',font=('arial',16,'bold'),bd=20,fg='green').grid(row=2,column=2)
lblGrossPay=Label(f1a,text='Gross Pay',font=('arial',16,'bold'),bd=20,anchor='w',fg='green').grid(row=3,column=0)
lblOvertime=Label(f1a,text='Overtime',font=('arial',16,'bold'),bd=20,fg='green').grid(row=3,column=2)
lblNetPay=Label(f1a,text='Net Pay',font=('arial',16,'bold'),bd=20,fg='green').grid(row=4,column=0)
lblTaxPaid=Label(f1a,text='Tax Paid',font=('arial',16,'bold'),bd=20,fg='green').grid(row=4,column=2)


etxtName=Entry(f1a,textvariable=Name,font=('arial',16),bd=16,width=22,justify='left')
etxtName.grid(row=0,column=1)
etxtAddress=Entry(f1a,textvariable=Address,font=('arial',16),bd=16,width=22,justify='left')
etxtAddress.grid(row=0,column=3)
etxtEmployer=Entry(f1a,textvariable=Employer,font=('arial',16),bd=16,width=22,justify='left')
etxtEmployer.grid(row=1,column=1)
etxtHoursWorked=Entry(f1a,textvariable=HoursWorked,font=('arial',16),bd=16,width=22,justify='left')
etxtHoursWorked.grid(row=2,column=1)
etxtWagesPerHours=Entry(f1a,textvariable=WagesHour,font=('arial',16),bd=16,width=22,justify='left')
etxtWagesPerHours.grid(row=2,column=3)
etxtWorkerid=Entry(f1a,textvariable=WorkerID,font=('arial',16),bd=16,width=22,justify='left')
etxtWorkerid.grid(row=1,column=3)
etxtGrossPay=Entry(f1a,textvariable=Payable,font=('arial',16),bd=16,width=22,justify='left')
etxtGrossPay.grid(row=4,column=1)
etxtNetPay=Entry(f1a,textvariable=NetPayable,font=('arial',16),bd=16,width=22,justify='left')
etxtNetPay.grid(row=4,column=3)
etxtTax=Entry(f1a,textvariable=Taxable,font=('arial',16),bd=16,width=22,justify='left')
etxtTax.grid(row=3,column=1)
etxtOvertime=Entry(f1a,textvariable=OvertimeHours,font=('arial',16),bd=16,width=22,justify='left')
etxtOvertime.grid(row=3,column=3)


lblPaySlip=Label(f2,textvariable=DateOfOrder,font=('arial',21,'bold')).grid(row=0,column=0)
txtPaySlip=Text(f2,height=22,width=34,bd=16,font=('arial',12,'bold'))
txtPaySlip.grid(row=1,column=0)


btnSalary=Button(f1b,text='Calculate',padx=16,pady=16,bd=8,fg='black',
                 font=('arial',16,'bold'),width=10,height=1,command=WeeklyWages).grid(row=0,column=0)

btnReset=Button(f1b,text='Reset',padx=16,pady=16,bd=8,fg='black',
                 font=('arial',16,'bold'),width=10,height=1,command=Reset).grid(row=0,column=2)

btnPaySlip=Button(f1b,text='View PaySlip',padx=16,pady=16,bd=8,fg='black',
                 font=('arial',16,'bold'),width=10,height=1,command=EnterInfo).grid(row=0,column=1)

btnInsert=Button(f1b,text='Submit PaySlip',padx=16,pady=16,bd=8,fg='blue',
                 font=('arial',16,'bold'),width=10,height=1,command=Insert).grid(row=0,column=3)

btnExit=Button(f1b,text='EXIT SYSTEM',padx=16,pady=16,bd=8,fg='red',
                 font=('arial',16,'bold'),width=10,height=1,command=iExit).grid(row=0,column=4)

btnview=Button(f1b,text='CALCULATOR',padx=16,pady=16,bd=8,fg='green',
                 font=('arial',16,'bold'),width=10,height=1,command=databeses).grid(row=0,column=5)
root.mainloop()