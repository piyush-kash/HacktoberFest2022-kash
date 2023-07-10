import csv
import json
import datetime
import os
import ssl
import base64
import urllib.request

from OpenSSL import crypto
from org.json import CDL

def read_from_stream(response):
    try:
        for line in response:
            print(line.decode())
    except Exception as e:
        print(e)

def get_certificate_from_store(client_store):
    alias = ""
    try:
        aliases = client_store.aliases()
        while aliases.hasMoreElements():
            alias = aliases.nextElement()
            if client_store.getCertificate(alias).getType() == "X.509":
                cert = client_store.getCertificate(alias)
                exp_date = cert.getNotAfter()
                from_date = cert.getNotBefore()
                subject = cert.getSubjectX500Principal()
                issuer = cert.getIssuerX500Principal()
                s_subject_cn = subject.getName()
                s_issuer_cn = issuer.getName()
                print("Following certificate will be used:")
                print(f"Issuer: {s_issuer_cn}")
                print(f"CN: {s_subject_cn}")
                print(f"Expiry Date: {exp_date}")
                print(f"From Date: {from_date}")
                break
    except Exception as e:
        print(e)
    return alias

pfx_path = "//apps//axion app//boe//batch//scripts//JAVA CODE//sds//ptxcert.pfx"
truststore_subpath = "/lib/security/cacerts"
count_url = "https://sdsdataservice.barcapint.com/counterparty/count"
find_url = "https://sdsdataservice.barcapint.com/counterparty/find"
truststore_password = "changeit"

dtf = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(dtf)

with open("//apps//axiom app//boe//batch//scripts//JAVA_CODE//sds//JSON//Cparty_Branch.txt", "w") as cparty_branch:
    cparty_branch.write("[")

    try:
        pass
    except ssl.SSLHandshakeException as e:
        print(e)
    except Exception as e:
        print(e)

inputfile_branch = "//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//JSON//Cparty_Branch.txt"
with open(inputfile_branch, "r") as file:
    fulljson_branch = file.read()
jsonArrayString_branch = "{\"fileName\":" + fulljson_branch + "}"

try:
    output_branch = json.loads(jsonArrayString_branch)
    docs_branch = output_branch["fileName"]

    with open("//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//JSON//Counterparty_TypeB.txt", "w") as file_branch:
        csv_branch = CDL.toString(docs_branch)
        file_branch.write(csv_branch)
except Exception as e:
    print(e)

str_file = "//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//JSON//Counterparty_TypeB.txt"
with open(str_file, "r") as file:
    reader = csv.reader(file)
    data = [line for line in reader]

new_final = "//apps//axiom app//boe//batch//Scripts//JAVA_CODE//sds//Files//Counterparty_TypeB.txt"
with open(new_final, "w", newline='') as file:
    writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_NONE)
    writer.writerows(data)

dtf2 = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(dtf2)
