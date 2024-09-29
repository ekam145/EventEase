import mysql.connector 

info = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="event_management"
)

value = info.cursor()


def admin_login(login_details):
    try:
        value.execute('SELECT * FROM `admin` WHERE `username`=%s and `password`=%s', login_details)
        return value.fetchone()
    except:
        return False


def department_login(login_details):
    try:
        value.execute('SELECT * FROM `department` WHERE `username`=%s and `password`=%s', login_details)
        return value.fetchone()
    except:
        return False


def add_department(department_details):
    try:
        print("Database : department details - ", department_details)
        value.execute("INSERT INTO `department` (department_name, username, password) VALUES (%s,%s,%s)",
                      department_details)
        info.commit()
        return True
    except:
        return False


def show_all_departments():
    try:
        value.execute('SELECT * FROM `department`')
        return value.fetchall()
    except:
        return False
    
def show_single_departments(data):
    try:
        value.execute('SELECT * FROM `department` where id=%s',data)
        return value.fetchone()
    except:
        return False



def delete_department_info(department_id):
    try:
        value.execute("DELETE FROM `department` WHERE id = %s", department_id)
        info.commit()
        return True
    except:
        return False


def update_department_info(department_details):
    try:
        print("Database : updated department details - ", department_details)
        value.execute("UPDATE `department` SET `department_name`= %s,`username`=%s,`password`=%s WHERE `id`=%s",
                      department_details)
        info.commit()
        return True
    except:
        return False


def add_venue(venue_details):
    try:
        print("Database : venue details - ", venue_details)
        value.execute("INSERT INTO `venue` (name,location,capacity) VALUES (%s,%s,%s)", venue_details)
        info.commit()
        return True
    except:
        return False



def show_all_venues():
    try:
        value.execute('SELECT * from `venue`')
        return value.fetchall()
    except:
        return False
def show_single_venues(data):
    try:
        value.execute('SELECT * from `venue` where id=%s',data)
        return value.fetchone()
    except:
        return False


def delete_venue_info(venue_id):
    try:
        value.execute("DELETE FROM `venue` WHERE id=%s", venue_id)
        info.commit()
        return True
    except:
        return False


def update_venue_info(venue_details):
    try:
        print("Database : Updated venue details - ", venue_details)
        value.execute("UPDATE `venue` SET `name`=%s,`location`=%s,`capacity`=%s WHERE `id`=%s", venue_details)
        info.commit()
        return True
    except:
        return False


def add_event(event_details):
    try:
        print("Database : event details - ", event_details)
        value.execute(
            "INSERT INTO `event` (dept_id,coordinator,event_name,date,duration,venue_id,status) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            event_details)
        info.commit()
        return True
    except Exception as e:
        print("Error is - ", e)
        return False


def show_all_events():
    value.execute("SELECT * FROM `event`")
    return value.fetchall()

def show_all_accepted_events():
    value.execute("SELECT * FROM `event` where status='ACCEPTED'")
    return value.fetchall()


def delete_event_info(event_id):
    try:
        value.execute("DELETE FROM `event` WHERE ID=%s", event_id)
        info.commit()
        return True
    except:
        return False


def update_event_info(event_details):
    try:
        print("Database : Updated event details - ", event_details)
        value.execute(
            "UPDATE `event` SET `dept_id`=%s,`coordinator`=%s,`event_name`=%s,`date`=%s,`duration`=%s,`venue_id`=%s,`status`=%s WHERE `id`=%s",
            event_details)
        info.commit()
        return True
    except Exception as e:
        print(e)
        return False


def reject_event(event_id):
    try:
        value.execute("UPDATE `event` set status='REJECTED' WHERE `id`=%s", event_id)
        info.commit()
        return True
    except:
        return False


def accept_event(event_id):
    try:
        value.execute("UPDATE `event` set `status`='ACCEPTED' WHERE `id`=%s", event_id)
        info.commit()
        return True
    except:
        return False
