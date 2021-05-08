import time
from datetime import datetime
import requests
from flask import Flask, flash, request, redirect, send_from_directory
from flask_mysqldb import MySQL
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
import json
from flask import jsonify
import os
from urllib.request import urlopen

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = "rozgaar.cdtf8jnpr7a9.ap-south-1.rds.amazonaws.com"
app.config['MYSQL_USER'] = "admin"
app.config['MYSQL_PASSWORD'] = "987654321"
app.config['MYSQL_DB'] = "corona"

mysql = MySQL(app)


# *********************************************************************************************************************

@app.route('/input/raj', methods=['GET'])
def input_raj():
    now = datetime.now()
    dt_string = now.strftime("%B %d, %H:%M")
    del_all()
    file1 = open("raj.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO rajasthan (hos_name, last_up, va, oa, ia, iva, phn1, phn2, loca, district) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (p[0], dt_string, p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/raj', methods=['GET'])
def outweb_raj():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rajasthan")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Phone 2": i[8], "Location": i[9], "District": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/all', methods=['GET'])
def del_all():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE rajasthan")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/delhiall', methods=['GET'])
def input_delhiall():
    now = datetime.now()
    dt_string2 = now.strftime("%B %d, %H:%M")
    del_delhiall()
    file1 = open("delhi_all.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    x = json.dumps(data)
    for i in dic.keys():
        p = dic[i]
        cur = mysql.connection.cursor()
        # print(p)
        cur.execute(
            "INSERT INTO delhi_all (hos_name, hosp_type, last_up, va, phn1, phn2, loca, district) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (p[0], p[1], dt_string2, p[3], p[4], p[5], p[6], p[7]))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/delhiall', methods=['GET'])
def outweb_all():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM delhi_all")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Hospital Type": i[2], "Last Updated": i[3], "Vacant Beds": i[4],
               "Phone 1": i[5], "Phone 2": i[6], "Location": i[7], "District": i[8]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/delhiall', methods=['GET'])
def del_delhiall():
    cur2 = mysql.connection.cursor()
    cur2.execute("TRUNCATE TABLE delhi_all")
    mysql.connection.commit()
    cur2.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/delhioxy', methods=['GET'])
def input_delhioxy():
    now = datetime.now()
    dt_string3 = now.strftime("%B %d, %H:%M")
    del_delhioxy()
    file1 = open("delhi_oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    x = json.dumps(data)
    for i in dic.keys():
        p = dic[i]
        cur = mysql.connection.cursor()
        # print(p)
        cur.execute(
            "INSERT INTO delhi_oxy (hos_name, hosp_type, last_up, va, phn1, phn2, loca, district) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (p[0], p[1], dt_string3, p[3], p[4], p[5], p[6], p[7]))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/delhioxy', methods=['GET'])
def outweb_oxy():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM delhi_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Hospital Type": i[2], "Last Updated": i[3],
               "Vacant Oxygen Beds": i[4], "Phone 1": i[5], "Phone 2": i[6], "Location": i[7], "District": i[8]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/delhioxy', methods=['GET'])
def del_delhioxy():
    cur3 = mysql.connection.cursor()
    cur3.execute("TRUNCATE TABLE delhi_oxy")
    mysql.connection.commit()
    cur3.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/delhiicu', methods=['GET'])
def input_delhiicu():
    now = datetime.now()
    dt_string4 = now.strftime("%B %d, %H:%M")
    del_delhiicu()
    file1 = open("delhi_icu.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    x = json.dumps(data)
    for i in dic.keys():
        p = dic[i]
        cur = mysql.connection.cursor()
        # print(p)
        cur.execute(
            "INSERT INTO delhi_icu (hos_name, hosp_type, last_up, va, phn1, phn2, loca, district) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (p[0], p[1], dt_string4, p[3], p[4], p[5], p[6], p[7]))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/delhiicu', methods=['GET'])
def outweb_delhiicu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM delhi_icu")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Hospital Type": i[2], "Last Updated": i[3],
               "Vacant ICU Beds": i[4], "Phone 1": i[5], "Phone 2": i[6], "Location": i[7], "District": i[8]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/delhiicu', methods=['GET'])
def del_delhiicu():
    cur4 = mysql.connection.cursor()
    cur4.execute("TRUNCATE TABLE delhi_icu")
    mysql.connection.commit()
    cur4.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/uk', methods=['GET'])
def input_uk():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_uk()
    file1 = open("uk.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    x = json.dumps(data)
    for i in dic.keys():
        p = dic[i]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO uk (hos_name, last_up, va, oa, ia, phn1, loca, district) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/uk', methods=['GET'])
def outweb_uk():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM uk")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Phone 1": i[6], "Location": i[7], "District": i[8]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/uk', methods=['GET'])
def del_uk():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE uk")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/tn', methods=['GET'])
def input_tn():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_tn()
    file1 = open("tn.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO tn (hos_name, last_up, va, oa, ia, iva, phn1, loca, district) VALUES (%s,%s,%s,%s,%s,%s,%s,%s, %s)",
            (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/tn', methods=['GET'])
def outweb_tn():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tn")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/tn', methods=['GET'])
def del_tn():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE tn")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/telng', methods=['GET'])
def input_telng():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_telng()
    json_url = urlopen("https://covidtelangana.com/data/covidtelangana.com/bed_data.json")
    data = json.loads(json_url.read())
    for each in data:
        hosp = each['hospital_name']
        try:
            loca = each['hospital_address']
        except:
            loca = ""
        try:
            phn1 = each['hospital_phone']
        except:
            phn1 = 0
        try:
            district = each['district']
        except:
            district = ""
        try:
            va = each['available_beds_without_oxygen']
        except:
            va = each["available_beds_allocated_to_covid"]
        try:
            oa = each['available_beds_with_oxygen']
        except:
            oa = 0
        try:
            ia = each['available_icu_beds_without_ventilator']
        except:
            ia = 0
        try:
            iva = each['available_icu_beds_with_ventilator']
        except:
            iva = 0
        try:
            area = each['area']
        except:
            area = ""
        # print(district, hosp, loca, va, oa, ia, iva, phn1)
        if (0 == va) and (0 == oa) and (0 == ia) and (0 == iva):
            # print("me called")
            continue
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO telng (hos_name, last_up, va, oa, ia, iva, phn1, loca, district, area) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (hosp, dt_string5, va, oa, ia, iva, phn1, loca, district, area))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/telng', methods=['GET'])
def outweb_telng():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM telng")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9], "Area": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/telng', methods=['GET'])
def del_telng():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE telng")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/wb', methods=['GET'])
def input_wb():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_wb()
    json_url = urlopen("https://covidwb.com/data/covidwb.com/bed_data.json")
    data = json.loads(json_url.read())
    for each in data:
        hosp = each['hospital_name']
        try:
            loca = each['hospital_address']
        except:
            loca = ""
        try:
            phn1 = each['hospital_phone']
        except:
            phn1 = 0
        try:
            district = each['district']
        except:
            district = ""
        try:
            va = each['available_beds_without_oxygen']
        except:
            va = each["available_beds_allocated_to_covid"]
        try:
            oa = each['available_beds_with_oxygen']
        except:
            oa = 0
        try:
            ia = each['available_icu_beds_without_ventilator']
        except:
            ia = 0
        try:
            iva = each['available_icu_beds_with_ventilator']
        except:
            iva = 0
        try:
            area = each['area']
        except:
            area = ""
        # print(district, hosp, loca, va, oa, ia, iva, phn1)
        if (0 == va) and (0 == oa) and (0 == ia) and (0 == iva):
            # print("me called")
            continue
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO wb (hos_name, last_up, va, oa, ia, iva, phn1, loca, district, area) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (hosp, dt_string5, va, oa, ia, iva, phn1, loca, district, area))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/wb', methods=['GET'])
def outweb_wb():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM wb")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9], "Area": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/wb', methods=['GET'])
def del_wb():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE wb")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/mp', methods=['GET'])
def input_mp():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_mp()
    json_url = urlopen("https://covidmp.com/data/covidmp.com/bed_data.json")
    data = json.loads(json_url.read())
    for each in data:
        hosp = each['hospital_name']
        try:
            loca = each['hospital_address']
        except:
            loca = ""
        try:
            phn1 = each['hospital_phone']
        except:
            phn1 = 0
        try:
            district = each['district']
        except:
            district = ""
        try:
            va = each['available_beds_without_oxygen']
        except:
            va = each["available_beds_allocated_to_covid"]
        try:
            oa = each['available_beds_with_oxygen']
        except:
            oa = 0
        try:
            ia = each['available_icu_beds_without_ventilator']
        except:
            ia = 0
        try:
            iva = each['available_icu_beds_with_ventilator']
        except:
            iva = 0
        try:
            area = each['area']
        except:
            area = ""
        # print(district, hosp, loca, va, oa, ia, iva, phn1)
        if (0 == va) and (0 == oa) and (0 == ia) and (0 == iva):
            # print("me called")
            continue
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO mp (hos_name, last_up, va, oa, ia, iva, phn1, loca, district, area) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (hosp, dt_string5, va, oa, ia, iva, phn1, loca, district, area))
        mysql.connection.commit()
        cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/mp', methods=['GET'])
def outweb_mp():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mp")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9], "Area": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/mp', methods=['GET'])
def del_mp():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE mp")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/gujarat', methods=['GET'])
def input_gujarat():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_gujarat()
    list_of_link = ['https://covidgandhinagar.com/data/covidgandhinagar.com/bed_data.json',
                    'https://covidbaroda.com/data/covidbaroda.com/bed_data.json',
                    'https://covidamd.com/data/covidamd.com/bed_data.json']
    for link in list_of_link:
        json_url = urlopen(link)
        data = json.loads(json_url.read())
        for each in data:
            hosp = each['hospital_name']
            try:
                loca = each['hospital_address']
            except:
                loca = ""
            try:
                phn1 = each['hospital_phone']
            except:
                phn1 = 0
            try:
                district = each['district']
            except:
                district = ""
            try:
                va = each['available_beds_without_oxygen']
            except:
                va = each["available_beds_allocated_to_covid"]
            try:
                oa = each['available_beds_with_oxygen']
            except:
                oa = 0
            try:
                ia = each['available_icu_beds_without_ventilator']
            except:
                ia = 0
            try:
                iva = each['available_icu_beds_with_ventilator']
            except:
                iva = 0
            try:
                area = each['area']
            except:
                area = ""
            # print(district, hosp, loca, va, oa, ia, iva, phn1)
            if (0 == va) and (0 == oa) and (0 == ia) and (0 == iva):
                # print("me called")
                continue
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO gujarat (hos_name, last_up, va, oa, ia, iva, phn1, loca, district, area) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (hosp, dt_string5, va, oa, ia, iva, phn1, loca, district, area))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/gujarat', methods=['GET'])
def outweb_gujarat():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM gujarat")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9], "Area": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/gujarat', methods=['GET'])
def del_gujarat():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE gujarat")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/ap', methods=['GET'])
def input_ap():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_ap()
    list_of_link = ['https://covidaps.com/data/covidaps.com/bed_data.json']
    for link in list_of_link:
        json_url = urlopen(link)
        data = json.loads(json_url.read())
        for each in data:
            hosp = each['hospital_name']
            try:
                loca = each['hospital_address']
            except:
                loca = ""
            try:
                phn1 = each['hospital_phone']
            except:
                phn1 = 0
            try:
                district = each['district']
            except:
                district = ""
            try:
                va = each['available_beds_without_oxygen']
            except:
                va = each["available_beds_allocated_to_covid"]
            try:
                oa = each['available_beds_with_oxygen']
            except:
                oa = 0
            try:
                ia = each['available_icu_beds_without_ventilator']
            except:
                ia = 0
            try:
                iva = each['available_icu_beds_with_ventilator']
            except:
                iva = 0
            try:
                area = each['area']
            except:
                area = ""
            # print(district, hosp, loca, va, oa, ia, iva, phn1)
            if (0 == va) and (0 == oa) and (0 == ia) and (0 == iva):
                # print("me called")
                continue
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO ap (hos_name, last_up, va, oa, ia, iva, phn1, loca, district, area) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (hosp, dt_string5, va, oa, ia, iva, phn1, loca, district, area))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/ap', methods=['GET'])
def outweb_ap():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ap")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9], "Area": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/ap', methods=['GET'])
def del_ap():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE ap")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/maharashtra', methods=['GET'])
def input_maharashtra():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_maharashtra()
    list_of_link = ['https://covidnashik.com/data/covidnashik.com/bed_data.json',
                    'https://covidpune.com/data/covidpune.com/bed_data.json',
                    "https://covidbeed.com/data/covidbeed.com/bed_data.json"]
    for link in list_of_link:
        json_url = urlopen(link)
        data = json.loads(json_url.read())
        for each in data:
            hosp = each['hospital_name']
            try:
                loca = each['hospital_address']
            except:
                loca = ""
            try:
                phn1 = each['hospital_phone']
            except:
                phn1 = 0
            try:
                district = each['district']
            except:
                district = ""
            try:
                va = each['available_beds_without_oxygen']
            except:
                va = each["available_beds_allocated_to_covid"]
            try:
                oa = each['available_beds_with_oxygen']
            except:
                oa = 0
            try:
                ia = each['available_icu_beds_without_ventilator']
            except:
                ia = 0
            try:
                iva = each['available_icu_beds_with_ventilator']
            except:
                iva = 0
            try:
                area = each['area']
            except:
                area = ""
            # print(district, hosp, loca, va, oa, ia, iva, phn1)
            if (0 == va) and (0 == oa) and (0 == ia) and (0 == iva):
                # print("me called")
                continue
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO maharashtra (hos_name, last_up, va, oa, ia, iva, phn1, loca, district, area) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (hosp, dt_string5, va, oa, ia, iva, phn1, loca, district, area))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/maharashtra', methods=['GET'])
def outweb_maharashtra():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM maharashtra")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9], "Area": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/maharashtra', methods=['GET'])
def del_maharashtra():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE maharashtra")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/karnataka', methods=['GET'])
def input_karnataka():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_karnataka()
    list_of_link = ["https://covidbengaluru.com/data/covidbengaluru.com/bed_data.json"]
    for link in list_of_link:
        json_url = urlopen(link)
        data = json.loads(json_url.read())
        for each in data:
            hosp = each['hospital_name']
            try:
                loca = each['hospital_address']
            except:
                loca = ""
            try:
                phn1 = each['hospital_phone']
            except:
                phn1 = 0
            try:
                district = each['district']
            except:
                district = ""
            try:
                va = each['available_beds_without_oxygen']
            except:
                va = each["available_beds_allocated_to_covid"]
            try:
                oa = each['available_beds_with_oxygen']
            except:
                oa = 0
            try:
                ia = each['available_icu_beds_without_ventilator']
            except:
                ia = 0
            try:
                iva = each['available_icu_beds_with_ventilator']
            except:
                iva = 0
            try:
                area = each['area']
            except:
                area = ""
            # print(district, hosp, loca, va, oa, ia, iva, phn1)
            if (0 == va) and (0 == oa) and (0 == ia) and (0 == iva):
                # print("me called")
                continue
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO karnataka (hos_name, last_up, va, oa, ia, iva, phn1, loca, district, area) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (hosp, dt_string5, va, oa, ia, iva, phn1, loca, district, area))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/karnataka', methods=['GET'])
def outweb_karnataka():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM karnataka")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Hospital Name": i[1], "Last Updated": i[2], "Vacant General Beds": i[3],
               "Vacant Oxygen Beds": i[4], "Vacant ICU Beds": i[5], "Vacant ICU Vantilator Beds": i[6], "Phone 1": i[7],
               "Location": i[8], "District": i[9], "Area": i[10]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/karnataka', methods=['GET'])
def del_karnataka():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE karnataka")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/maharashtra_plasma', methods=['GET'])
def input_maharashtra_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_maharashtra_plasma()
    list_of_link = ['https://covidnashik.com/data/covidnashik.com/plasma_data.json',
                    'https://covidpune.com/data/covidpune.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO maharashtra_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/maharashtra_plasma', methods=['GET'])
def outweb_maharashtra_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM maharashtra_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/maharashtra_plasma', methods=['GET'])
def del_maharashtra_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE maharashtra_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/gujarat_plasma', methods=['GET'])
def input_gujarat_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_gujarat_plasma()
    list_of_link = ['https://covidgandhinagar.com/data/covidgandhinagar.com/plasma_data.json',
                    'https://covidbaroda.com/data/covidbaroda.com/plasma_data.json',
                    'https://covidamd.com/data/covidamd.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO gujarat_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/gujarat_plasma', methods=['GET'])
def outweb_gujarat_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM gujarat_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/gujarat_plasma', methods=['GET'])
def del_gujarat_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE gujarat_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/delhi_plasma', methods=['GET'])
def input_delhi_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_delhi_plasma()
    list_of_link = ['https://coviddelhi.com/data/coviddelhi.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO delhi_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/delhi_plasma', methods=['GET'])
def outweb_delhi_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM delhi_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/delhi_plasma', methods=['GET'])
def del_delhi_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE delhi_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/wb_plasma', methods=['GET'])
def input_wb_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_wb_plasma()
    list_of_link = ['https://covidwb.com/data/covidwb.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO wb_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/wb_plasma', methods=['GET'])
def outweb_wb_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM wb_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/wb_plasma', methods=['GET'])
def del_wb_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE wb_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/telng_plasma', methods=['GET'])
def input_telng_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_telng_plasma()
    list_of_link = ['https://covidtelangana.com/data/covidtelangana.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO telng_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/telng_plasma', methods=['GET'])
def outweb_telng_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM telng_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/telng_plasma', methods=['GET'])
def del_telng_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE telng_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/karnataka_plasma', methods=['GET'])
def input_karnataka_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_karnataka_plasma()
    list_of_link = ['https://covidbengaluru.com/data/covidbengaluru.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO karnataka_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/karnataka_plasma', methods=['GET'])
def outweb_karnataka_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM karnataka_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/karnataka_plasma', methods=['GET'])
def del_karnataka_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE karnataka_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/ap_plasma', methods=['GET'])
def input_ap_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_ap_plasma()
    list_of_link = ['https://covidaps.com/data/covidaps.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO ap_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/ap_plasma', methods=['GET'])
def outweb_ap_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ap_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/ap_plasma', methods=['GET'])
def del_ap_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE ap_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/mp_plasma', methods=['GET'])
def input_mp_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_mp_plasma()
    list_of_link = ['https://covidmp.com/data/covidmp.com/plasma_data.json']
    for link in list_of_link:
        try:
            json_url = urlopen(link)
            data = json.loads(json_url.read())
        except:
            continue
        for each in data:
            name = each['name']
            try:
                address = each['address']
            except:
                address = ""
            try:
                phone = each['phone']
            except:
                phone = 0
            try:
                fax = each['fax']
            except:
                fax = ""
            try:
                email = each['email']
            except:
                email = ""
            try:
                ot = each['org_type']
            except:
                ot = ""
            try:
                status = each['status']
            except:
                status = "not_available"
            try:
                plasma = each['availability']
                try:
                    abn = plasma["AB-Ve"]
                except:
                    abn = 0
                try:
                    abp = plasma["AB+Ve"]
                except:
                    abp = 0
                try:
                    an = plasma["A-Ve"]
                except:
                    an = 0
                try:
                    ap = plasma["A+Ve"]
                except:
                    ap = 0
                try:
                    onv = plasma["O-Ve"]
                except:
                    onv = 0
                try:
                    op = plasma["O+Ve"]
                except:
                    op = 0
                try:
                    bn = plasma["B-Ve"]
                except:
                    bn = 0
                try:
                    bp = plasma["B+Ve"]
                except:
                    bp = 0
            except:
                plasma = ""
                abn = 0
                abp = 0
                an = 0
                ap = 0
                onv = 0
                op = 0
                bn = 0
                bp = 0
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO mp_plasma (name, address, phone, fax, email, org_type, status, abn, abp, an, ap, onv, op, bn, bp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name, address, phone, fax, email, ot, status, abn, abp, an, ap, onv, op, bn, bp))
            mysql.connection.commit()
            cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/mp_plasma', methods=['GET'])
def outweb_mp_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mp_plasma")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Status": i[15], "Hospital Name": i[1], "AB-Ve": i[3], "AB+Ve": i[2], "A-Ve": i[4],
               "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9], "Address": i[10], "Phone": i[11],
               "Fax": i[12], "Email": i[13], "Organisation type": i[14]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/mp_plasma', methods=['GET'])
def del_mp_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE mp_plasma")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_raj', methods=['GET'])
def input_oxy_raj():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_raj()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "rajasthan":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO raj_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_raj', methods=['GET'])
def outweb_oxy_raj():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM raj_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_raj', methods=['GET'])
def del_oxy_raj():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE raj_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_maha', methods=['GET'])
def input_oxy_maha():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_maha()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "maharashtra":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO maha_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_maha', methods=['GET'])
def outweb_oxy_maha():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM maha_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_maha', methods=['GET'])
def del_oxy_maha():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE maha_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_guj', methods=['GET'])
def input_oxy_guj():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_guj()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "gujarat":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO guj_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_guj', methods=['GET'])
def outweb_oxy_guj():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM guj_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_guj', methods=['GET'])
def del_oxy_guj():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE guj_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_delhi', methods=['GET'])
def input_oxy_delhi():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_delhi()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "delhi":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO delhi_oxysup (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_delhi', methods=['GET'])
def outweb_oxy_delhi():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM delhi_oxysup")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_delhi', methods=['GET'])
def del_oxy_delhi():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE delhi_oxysup")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_mp', methods=['GET'])
def input_oxy_mp():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_mp()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "madhya pradesh":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO mp_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_mp', methods=['GET'])
def outweb_oxy_mp():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mp_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_mp', methods=['GET'])
def del_oxy_mp():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE mp_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_ap', methods=['GET'])
def input_oxy_ap():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_ap()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "andhra pradesh":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO ap_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_ap', methods=['GET'])
def outweb_oxy_ap():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ap_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_ap', methods=['GET'])
def del_oxy_ap():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE ap_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_uk', methods=['GET'])
def input_oxy_uk():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_uk()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "uttrakhand":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO uk_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_uk', methods=['GET'])
def outweb_oxy_uk():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM uk_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_uk', methods=['GET'])
def del_oxy_uk():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE uk_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_wb', methods=['GET'])
def input_oxy_wb():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_wb()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "west bengal":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO wb_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_wb', methods=['GET'])
def outweb_oxy_wb():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM wb_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_wb', methods=['GET'])
def del_oxy_wb():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE wb_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})


@app.route('/input/oxy_tn', methods=['GET'])
def input_oxy_tn():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    del_oxy_tn()
    file1 = open("oxy.json", 'r')
    data = file1.read()
    data = json.loads(data)
    dic = dict(data)
    for i in dic.keys():
        p = dic[i]
        if p[4] == "tamil nadu":
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO tn_oxy (name, phone, url, city, state) VALUES (%s,%s,%s,%s,%s)",
                (p[0], p[1], p[2], p[3], p[4]))
            mysql.connection.commit()
            cur.close()
        else:
            pass
    return jsonify({'result': "success", 'status': 200})


@app.route('/outweb/oxy_tn', methods=['GET'])
def outweb_oxy_tn():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tn_oxy")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Supplier Name": i[1], "Phone": i[2], "Url Address": i[3], "City": i[4]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)


@app.route('/del/oxy_tn', methods=['GET'])
def del_oxy_tn():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE tn_oxy")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

# ####################################################################################################################

# *********************************************************************************************************************

@app.route('/input/m_plasma', methods=['POST'])
def input_plasma():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    each = request.get_json()

    try:
        name = each['name']
    except:
        name = ""
    try:
        phone = each['phone']
    except:
        phone = 0
    try:
        address = each['address']
    except:
        address = ""
    try:
        other = each['other']
    except:
        other = ""
    try:
        abn = each["AB-Ve"]
    except:
        abn = 0
    try:
        abp = each["AB+Ve"]
    except:
        abp = 0
    try:
        an = each["A-Ve"]
    except:
        an = 0
    try:
        ap = each["A+Ve"]
    except:
        ap = 0
    try:
        onv = each["O-Ve"]
    except:
        onv = 0
    try:
        op = each["O+Ve"]
    except:
        op = 0
    try:
        bn = each["B-Ve"]
    except:
        bn = 0
    try:
        bp = each["B+Ve"]
    except:
        bp = 0
    try:
        area = each["area"]
    except:
        area = 0
    try:
        email = each['email']
    except:
        email = ""

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO plasma_m (name, address, phone, other, area, abn, abp, an, ap, onv, op, bn, bp, email, uptime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (name, address, phone, other, area, abn, abp, an, ap, onv, op, bn, bp, email, dt_string5))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

@app.route('/outweb/m_plasma', methods=['GET'])
def outweb_plasma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM plasma_m")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Name": i[1], "AB-Ve": i[2], "AB+Ve": i[3], "A-Ve": i[4], "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9],  "Address": i[10], "Phone": i[11], "Area": i[12], "Other": i[13]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)

@app.route('/del/m_plasma', methods=['GET'])
def del_plasma():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE plasma_m")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

@app.route('/input/m_oxygen', methods=['POST'])
def input_oxygen():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    each = request.get_json()

    try:
        name = each['name']
    except:
        name = ""
    try:
        phone = each['phone']
    except:
        phone = 0
    try:
        address = each['address']
    except:
        address = ""
    try:
        other = each['other']
    except:
        other = ""
    try:
        email = each["email"]
    except:
        email = 0
    try:
        area = each["area"]
    except:
        area = 0
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO oxygen_m (name, address, phone, other, area, email, uptime) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (name, address, phone, other, area, email, dt_string5))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

@app.route('/outweb/m_oxygen', methods=['GET'])
def outweb_oxygen():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM oxygen_m")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Name": i[1], "AB-Ve": i[2], "AB+Ve": i[3], "A-Ve": i[4], "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9],  "Address": i[10], "Phone": i[11], "Area": i[12], "Other": i[13]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)

@app.route('/del/m_oxygen', methods=['GET'])
def del_oxygen():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE oxygen_m")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

@app.route('/input/m_vacinj', methods=['POST'])
def input_vacinj():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    each = request.get_json()

    try:
        name = each['name']
    except:
        name = ""
    try:
        phone = each['phone']
    except:
        phone = 0
    try:
        address = each['address']
    except:
        address = ""
    try:
        other = each['other']
    except:
        other = ""
    try:
        email = each["email"]
    except:
        email = 0
    try:
        area = each["area"]
    except:
        area = 0
    try:
        inj_type = each["injection_type"]
    except:
        inj_type = 0
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO vacinj_m (name, address, phone, other, area, email, uptime, inj_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (name, address, phone, other, area, email, dt_string5, inj_type))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

@app.route('/outweb/m_vacinj', methods=['GET'])
def outweb_vacinj():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM vacinj_m")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Name": i[1], "AB-Ve": i[2], "AB+Ve": i[3], "A-Ve": i[4], "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9],  "Address": i[10], "Phone": i[11], "Area": i[12], "Other": i[13]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)

@app.route('/del/m_vacinj', methods=['GET'])
def del_vacinj():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE vacinj_m")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

@app.route('/input/m_ffood', methods=['POST'])
def input_ffood():
    now = datetime.now()
    dt_string5 = now.strftime("%B %d, %H:%M")
    each = request.get_json()

    try:
        name = each['name']
    except:
        name = ""
    try:
        phone = each['phone']
    except:
        phone = 0
    try:
        address = each['address']
    except:
        address = ""
    try:
        other = each['other']
    except:
        other = ""
    try:
        email = each["email"]
    except:
        email = 0
    try:
        area = each["area"]
    except:
        area = 0
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO ffood_m (name, address, phone, other, area, email, uptime) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (name, address, phone, other, area, email, dt_string5))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

@app.route('/outweb/m_ffood', methods=['GET'])
def outweb_ffood():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ffood_m")
    data = cur.fetchall()
    data = list(data)
    ls = []
    for i in data:
        dic = {"SN no.": i[0], "Name": i[1], "AB-Ve": i[2], "AB+Ve": i[3], "A-Ve": i[4], "A+Ve": i[5], "O-Ve": i[6], "O+Ve": i[7], "B-Ve": i[8], "B+Ve": i[9],  "Address": i[10], "Phone": i[11], "Area": i[12], "Other": i[13]}
        dic = dict(dic)
        ls.append(dic)
    return json.dumps(ls)

@app.route('/del/m_ffood', methods=['GET'])
def del_ffood():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE ffood_m")
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': "success", 'status': 200})

if __name__ == '__main__':
    app.run(debug=True)