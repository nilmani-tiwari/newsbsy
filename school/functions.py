from school.models import *
import datetime
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
from django.contrib import messages
import requests

def pydate(x):
	return parse(x).date()

def tdifferance(t1="10:00:41",t2="10:00:42"):
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(t2.strip(), FMT) - datetime.strptime(t1.strip(), FMT)
    return tdelta.seconds

def gps_data_update():
    gps_data={}
    num=Busapi.objects.values("rf_id").count()
    for one in range(num):
        first=Busapi.objects.first()
        machine_no=first.machine_no
        if 1==1:
            tran_gps=School_Transport.objects.get(school_code=first.school_code,reader_machine_no=machine_no)
            
            sim_no=tran_gps.gps_sim_no
            bus_no=tran_gps.transport_id
            rf_id=first.rf_id
            date=first.date
            time=first.time
            gps_data=gpsrestapi.values().filter(date__startswith=date,imei_no=sim_no)   #multiple datafilter(title__startswith=char)
            
            print(tran_gps,sim_no,bus_no,rf_id,date,time,gps_data)
            map_data=busmap(bus_no=bus_no,machine_no=machine_no,school_code=school_code,rf_id=rf_id,lat=gps_data.lat,log=gps_data.log,time=time,date=date)
            map_data.save()
            first.delete()
            gps_data.delete()
            
        else:
            pass
        





def attendance_update():
    std={}
    num = attendance_api.objects.values("rf_id").count()
    for i in range(num):
        first = attendance_api.objects.first()
        try:
            card = StudentMaster.objects.get(student_card_number=first.rf_id,school_code=first.school_code)
            
            try:
                outtime=first.attendance_timestamp[9:25]
                s = Attendance.objects.filter(rf_id=card.student_card_number,name=card.Full_name,user_name=card.user_name,
                									date=pydate(first.attendance_timestamp),school_code=first.school_code)
                if s.exists():
                    intime=s.first().intime
                    if tdifferance(intime,outtime)>60:
                        s.update(outtime=first.attendance_timestamp[9:25])
                        if s !=0:
                            first.delete() #truncate attendance_api
                    else:
                        first.delete() #truncate attendance_api
                else:
                    obj = Attendance(rf_id=card.student_card_number,name=card.Full_name,user_name=card.user_name,
                    							  date= pydate(first.attendance_timestamp),
                    							  intime=first.attendance_timestamp[9:25],gwId=first.gwId,
                    							  school_code=card.school_code, medium_name=card.medium_name,class_name=card.class_name,division_name=card.division_name,
                    				 group_id="4")


                    obj.save()
                    first.delete()


            except:
                print("i m here")

        except:
            try:
                card = StaffMaster.objects.get(staff_card_number=first.rf_id,staff_school_code=first.school_code)
                print("staff ********************************************** found")
                if 1==1:
                    outtime=first.attendance_timestamp[9:25]
                    s = Attendance.objects.filter(rf_id=card.staff_card_number, name=card.staff_First_name,user_name=card.staff_user_name,
                    							  date= pydate(first.attendance_timestamp),
                    							  school_code=first.school_code)
                    print("staff *******************atten*************************** update")
                    if s.exists():
                        intime=s.first().intime
                        if tdifferance(intime,outtime)>60:
                            s.update(outtime=first.attendance_timestamp[9:25])
                            if s !=0:
                                first.delete() #truncate attendance_api
                        else:
                            first.delete() #truncate attendance_api
                    
                    else:
                        obj = Attendance(rf_id=card.staff_card_number, name=card.staff_First_name,user_name=card.staff_user_name,
                        				 date= pydate(first.attendance_timestamp),
                        				 intime=first.attendance_timestamp[9:25], gwId=first.gwId,
                        				 school_code=first.school_code, medium_name=card.staff_medium_name,
                        				 class_name=card.staff_class_name, division_name=card.staff_division_name,
                        				 group_id="3")
                        obj.save()
                        first.delete()
                        print("staff *******************atten*************************** saved")
                else:
                    pass
            except:
                print(f"this card:{first} is not an authenticated by sbsy admin")
                first.delete()




import serial
def read_rfid():
    #data=input("enter rfid data ")
    ser = serial.Serial ("COM3")
    ser.baudrate = 9600
    data = ser.read(12)
    ser.close()
    return data.decode()




import urllib.request
import urllib.parse
# def sendSMS(message, numbers):
# 	for i in numbers:
# 		data = urllib.parse.urlencode({'apikey': "D2HJ8G0JbY4-QQwKO8p9fwWqpBIAornkgO7dee8bh9", 'numbers': i,
# 									   'message': message, 'sender': "TXTLCL"})
# 		data = data.encode('utf-8')
# 		request = urllib.request.Request("https://api.textlocal.in/send/?")
# 		f = urllib.request.urlopen(request, data)
# 		fr = f.read()
#
# 	return (fr)





# def absentmsg(ch):
# 	for i in ch:
# 		data = urllib.parse.urlencode(
# 			{'apikey': "D2HJ8G0JbY4-QQwKO8p9fwWqpBIAornkgO7dee8bh9", 'numbers': i.split(":")[0],
# 			 'message': i.split(":")[1], 'sender': "TXTLCL"})
# 		data = data.encode('utf-8')
# 		request = urllib.request.Request("https://api.textlocal.in/send/?")
# 		f = urllib.request.urlopen(request, data)
# 		fr = f.read()
# 		print(fr)
# 	return True


def sendsms(request,school_code,date,message, numbers):
    msg=message_pack.objects.filter(school_code=school_code).last()
    if msg is not None :
        rem_msg=int(msg.total_msg)
        if rem_msg >0:
            data = urllib.parse.urlencode({'apikey': "D2HJ8G0JbY4-QQwKO8p9fwWqpBIAornkgO7dee8bh9", 'numbers': numbers,
                                           'message': message, 'sender': "TXTLCL"})
            data = data.encode('utf-8')
            request1 = urllib.request.Request("https://api.textlocal.in/send/?")
            f = urllib.request.urlopen(request1, data)
            fr = f.read()
            m=message_pack(school_code=school_code,total_msg=rem_msg-1,sent_msg_to=numbers,message=message,date=date)
            m.save()
            # messages.info(request, "you have insufficient ballance plz recharge.")
            messages.success(request, "Message send successfully.")
            # messages.success(request, "Successfully recieved")
            return True,rem_msg-1
        else:
            messages.info(request, "you have insufficient ballance plz recharge.")
    return



def absent_msg(request,school_code,date,ch):
  for i in ch:
    message=i.split(":")[1]
    numbers=i.split(":")[0]
    sendsms(request,school_code,date,message, numbers)
  return True
 
 
 
 
  
def manual_attendence_all(request,username,school_code):
    #if request.method == 'POST':
	user_name = username

	import datetime
	#date = datetime.datetime.now()
	date=datetime.datetime.now() + datetime.timedelta(seconds=19800)
	attendance_timestamp=date.strftime("%d-%b-%y %H:%M:%S")
	print(user_name,date, "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
	try:
		if User.objects.filter(groups=4, username=user_name).exists():  # student
			rf_id= StudentMaster.objects.get(user_name=user_name).student_card_number
			data = attendance_api(school_code=school_code, attendance_timestamp=attendance_timestamp, rf_id=rf_id,
								  gwId="manual", )
			data.save()
			messages.success(request, "Successfully attendance saved!! ")
			#return redirect('manual_attendence')
		elif User.objects.filter(groups=3, username=user_name).exists():
			rf_id = StaffMaster.objects.get(staff_user_name=user_name).staff_card_number
			data = attendance_api(school_code=school_code, attendance_timestamp=attendance_timestamp, rf_id=rf_id,
								  gwId="manual", )
			data.save()
			messages.success(request, "Successfully attendance saved!! ")
			#return redirect('manual_attendence')
		else:
			messages.info(request, "invalid Username!! "+str(user_name))
	except Exception as e:
		messages.info(request, f"Something went wrong!! {e}")




	#return render(request, 'SchoolDesign/manual-attendence.html')
	return


def manual_atten(request,school_code,date,ch):
    for i in ch:
        username=i.split(":")[0]
        manual_attendence_all(request,username,school_code)
    pass

def sbsy_absent_msg(request,school_code,date,ch):
    date = datetime.now().date()
    for i in ch:
        massage=i.split(":")[1]
        number=i.split(":")[0]
        sender_user_name=SchoolMaster.objects.values().filter(school_code=school_code).first()["email"]
        user, created = parents_msg.objects.get_or_create(school_code=school_code,date=date,user_name=number,message=massage,sender_user_name=sender_user_name)
        user.save()
    messages.success(request, "Message Successfully sent in SBSY smart school please suggest parents to download the app from play store")
    messages.success(request, "Parents username is their registered mobile number and default password is 12345 ")





