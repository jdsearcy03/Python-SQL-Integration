from servicenow_functions import *
from sql_functions import *

#Set Variables
pwd = input('Enter MySQL Password:\n')
instance = input('Enter ServiceNow Instance:\n')
user = input('Enter ServiceNow UserName:\n')
password = input('Enter ServiceNow Password:\n')

#Connect MySQL Database
connection = create_db_connection("localhost", "root", pwd, "ServiceNow")

#Send API Requests
users = snam_request('get', user, password, instance, 'sys_user', '')
departments = snam_request('get', user, password, instance, 'cmn_department', '')
locations = snam_request('get', user, password, instance, 'cmn_location', '')
incidents = snam_request('get', user, password, instance, 'incident', '')
user_groups = snam_request('get', user, password, instance, 'sys_user_group', '')

#Populate Departments Table
populate_departments = "INSERT INTO departments VALUES"
for department in departments:
    populate_departments += '\n'
    if department['sys_id'] != '':
        sys_id = "'" + department['sys_id'] + "'"
    else:
        sys_id = 'NULL'
    if department['name'] != '':
        name = "'" + department['name'] + "'"
    else:
        name = 'NULL'
    if department['description'] != '':
        description = "'" + department['description'] + "'"
    else:
        description = 'NULL'
    insert_str = '(' + sys_id + ', ' + name + ', ' + description + '),'
    populate_departments += insert_str

populate_departments = populate_departments.rsplit(',', 1)[0]
populate_departments += ';'
execute_query(connection, populate_departments)

#Populate Locations Table
populate_locations = "INSERT INTO locations VALUES"
for location in locations:
    populate_locations += '\n'
    if location['sys_id'] != '':
        sys_id = "'" + location['sys_id'] + "'"
    else:
        sys_id = 'NULL'
    if location['name'] != '':
        name = "'" + location['name'] + "'"
    else:
        name = 'NULL'
    if location['street'] != '':
        street = "'" + location['street'] + "'"
    else:
        street = 'NULL'
    if location['city'] != '':
        city = "'" + location['city'] + "'"
    else:
        city = 'NULL'
    if location['zip'] != '':
        zip = location['zip']
        if type(zip) != int:
            zip = 'NULL'
    else:
        zip = 'NULL'
    if location['country'] != '':
        country = "'" + location['country'] + "'"
    else:
        country = 'NULL'
    insert_str = '(' + sys_id + ', ' + name + ', ' + street + ', ' + city + ', ' + zip + ', ' + country + '),'
    populate_locations += insert_str
populate_locations = populate_locations.rsplit(',', 1)[0]
populate_locations += ';'
execute_query(connection, populate_locations)

#Populate Users Table
populate_users = "INSERT INTO users VALUES"
for user in users:
    populate_users += "\n"
    if user['sys_id'] != '':
        sys_id = "'" + user['sys_id'] + "'"
    else:
        sys_id = 'NULL'
    if user['user_name'] != '':
        user_name = "'" + user['user_name'] + "'"
    else:
        user_name = 'NULL'
    if user['first_name'] != '':
        first_name = "'" + user['first_name'] + "'"
    else:
        first_name = 'NULL'
    if user['last_name'] != '':
        last_name = "'" + user['last_name'] + "'"
    else:
        last_name = 'NULL'
    if user['email'] != '':
        email = "'" + user['email'] + "'"
    else:
        email = 'NULL'
    if user['department'] != '':
        department = "'" + user['department']['value'] + "'"
    else:
        department = 'NULL'
    if user['location'] != '':
        location = "'" + user['location']['value'] + "'"
    else:
        location = 'NULL'
    if user['vip'] != '':
        if user['vip'] == 'true':
            vip = "1"
        elif user['vip'] == 'false':
            vip = "0"
        else:
            vip = f"{user['vip']}"
    else:
        vip = 'NULL'
    if user['street'] != '':
        street = "'" + user['street'] + "'"
    else:
        street = 'NULL'
    if user['city'] != '':
        city = "'" + user['city'] + "'"
    else:
        city = 'NULL'
    if user['zip'] != '':
        zip = f"{user['zip']}"
    else:
        zip = 'NULL'
    if user['phone'] != '':
        phone = "'" + user['phone'] + "'"
    else:
        phone = 'NULL'
    if user['gender'] != '':
        gender = "'" + user['gender'] + "'"
    else:
        gender = 'NULL'
    if user['last_login'] != '':
        last_login = "'" + user['last_login'] + "'"
    else:
        last_login = 'NULL'
    insert_str = "(" + sys_id + ", " + user_name + ", " + first_name + ", " + last_name + ", " + email + ", " + department + ", " + location + ", " + vip + ", " + street + ", " + city + ", " + zip + ", " + phone + ", " + gender + ", " + last_login + "),"
    populate_users += insert_str

populate_users = populate_users.rsplit(',', 1)[0]
populate_users += ';'
execute_query(connection, populate_users)

#Populate User Groups Table
populate_user_groups = "INSERT INTO user_groups VALUES"
for group in user_groups:
    populate_user_groups += '\n'
    if group['sys_id'] != '':
        sys_id = "'" + group['sys_id'] + "'"
    else:
        sys_id = 'NULL'
    if group['name'] != '':
        name = "'" + group['name'] + "'"
    else:
        name = 'NULL'
    if group['manager'] != '':
        manager = "'" + group['manager']['value'] + "'"
    else:
        manager = 'NULL'
    insert_str = '(' + sys_id + ', ' + name + ', ' + manager + '),'
    populate_user_groups += insert_str
populate_user_groups = populate_user_groups.rsplit(',', 1)[0]
populate_user_groups += ';'
execute_query(connection, populate_user_groups)

#Populate Incidents Table
populate_incidents = "INSERT INTO incidents VALUES"
for incident in incidents:
    populate_incidents += '\n'
    if incident['sys_id'] != '':
        sys_id = "'" + incident['sys_id'] + "'"
    else:
        sys_id = 'NULL'
    if incident['number'] != '':
        number = "'" + incident['number'] + "'"
    else:
        number = 'NULL'
    if incident['active'] != '':
        if incident['active'] == 'true':
            active = "1"
        elif incident['active'] == 'false':
            active = "0"
        else:
            active = "'" + incident['active'] + "'"
    else:
        active = 'NULL'
    if incident['priority'] != '':
        priority = f"{incident['priority']}"
    else:
        priority = 'NULL'
    if incident['state'] != '':
        state = f"{incident['state']}"
    else:
        state = 'NULL'
    if incident['opened_at'] != '':
        opened_at = "'" + incident['opened_at'] + "'"
    else:
        opened_at = 'NULL'
    if incident['caller_id'] != '':
        caller_id = "'" + incident['caller_id']['value'] + "'"
    else:
        caller_id = 'NULL'
    if incident['assignment_group'] != '':
        assignment_group = "'" + incident['assignment_group']['value'] + "'"
    else:
        assignment_group = 'NULL'
    if incident['assigned_to'] != '':
        assigned_to = "'" + incident['assigned_to']['value'] + "'"
    else:
        assigned_to = 'NULL'
    if incident['resolved_by'] != '':
        resolved_by = "'" + incident['resolved_by']['value'] + "'"
    else:
        resolved_by = 'NULL'
    if incident['resolved_at'] != '':
        resolved_at = "'" + incident['resolved_at'] + "'"
    else:
        resolved_at = 'NULL'
    insert_str = '(' + sys_id + ', ' + number + ', ' + active + ', ' + priority + ', ' + state + ', ' + opened_at + ', ' + caller_id + ', ' + assignment_group + ', ' + assigned_to + ', ' + resolved_by + ', ' + resolved_at + '),'
    populate_incidents += insert_str
populate_incidents = populate_incidents.rsplit(',', 1)[0]
populate_incidents += ';'
execute_query(connection, populate_incidents)