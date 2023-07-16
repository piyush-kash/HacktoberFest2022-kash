import csv
import json
import datetime
import os
import ssl
import base64
import urllib.request
from java.security import KeyStore
from javax.net.ssl import SSLContext, TrustManagerFactory, HttpsURLConnection
from org.json import CDL
from org.json import JSONArray, JSONObject
from java.security.cert import X509Certificate
from javax.security.auth.x500 import X500Principal
from org.apache.commons.io import FileUtils
from java.io import BufferedReader, BufferedWriter, File, FileInputStream, FileWriter, InputStreamReader, OutputStreamWriter
from java.time.format import DateTimeFormatter
from java.time import LocalDateTime

class Cparty_TypeB:
    pfxPath = "//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//pfxcert.pfx"
    trustStoreSubPath = "/lib/security/cacerts"
    CountUrl = "https://sdsentityservice-s8t2.barcapint.com/counterparty/count"
    FindUrl = "https://sdsentityservice-s8t2.barcapint.com/counterparty/find"
    trustStorePassword = "changeit"

    @staticmethod
    def readFromStream(response):
        try:
            for line in response:
                print(line.decode())
        except Exception as e:
            print(e)

    @staticmethod
    def getCertificateFromStore(clientStore):
        alias = ""
        try:
            aliases = clientStore.aliases()
            while aliases.hasMoreElements():
                alias = aliases.nextElement()
                if clientStore.getCertificate(alias).getType() == "X.509":
                    cert = clientStore.getCertificate(alias)
                    expDate = cert.getNotAfter()
                    fromDate = cert.getNotBefore()
                    subject = cert.getSubjectX500Principal()
                    issuer = cert.getIssuerX500Principal()
                    sSubjectCN = subject.getName()
                    sIssuerCN = issuer.getName()
                    print("Following certificate will be used:")
                    print("Issuer: " + sIssuerCN)
                    print("CN: " + sSubjectCN)
                    print("Expiry Date: " + str(expDate))
                    print("From Date: " + str(fromDate))
                    break
        except Exception as e:
            print(e)
        return alias

    @staticmethod
    def main(args):
        dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss")
        now = LocalDateTime.now()
        print(dtf.format(now))

        clientStore = None

        Cparty_Branch = FileWriter("//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//JSON//Cparty_Branch.txt")
        Cparty_Branch.write("[")

        try:
            p12 = FileInputStream(Cparty_TypeB.pfxPath)
            cacerts = FileInputStream("//usr//java//latest//jre" + Cparty_TypeB.trustStoreSubPath.replace('/', os.path.sep))

            env = os.environ
            str = "Qxhpb21VS0BQUk9E"
            decoded = base64.b64decode(str).decode('utf-8')
            pfxPassword = decoded

            clientStore = KeyStore.getInstance(KeyStore.getDefaultType())
            clientStore.load(p12, pfxPassword.toCharArray())

            kmf = KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm())
            kmf.init(clientStore, pfxPassword.toCharArray())
            alias = Cparty_TypeB.getCertificateFromStore(clientStore)

            kms = kmf.getKeyManagers()
            cert = clientStore.getCertificate(alias)
            trustStoreEntry = KeyStore.TrustedCertificateEntry(cert)

            trustStore = KeyStore.getInstance(KeyStore.getDefaultType())
            trustStore.load(cacerts, Cparty_TypeB.trustStorePassword.toCharArray())

            tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm())
            tmf.init(trustStore)
            tms = tmf.getTrustManagers()

            sslContext = SSLContext.getInstance("TLSv1.2")
            sslContext.init(kms, tms, None)
            HttpsURLConnection.setDefaultSSLSocketFactory(sslContext.getSocketFactory())

            url_count = URL(Cparty_TypeB.CountUrl)
            urlConn_Branch_count = url_count.openConnection()
            urlConn_Branch_count.setRequestMethod("POST")
            urlConn_Branch_count.setRequestProperty("Content-Type", "application/json; charset=utf-8")
            urlConn_Branch_count.setRequestProperty("Accept", "application/json")
            urlConn_Branch_count.setDoOutput(True)

            jsonInputString_Branch_Count = "{\"criteria\": {\"operator\":  \"and\",\"items\": [{\"operator\": \"gte\",\"field\": \"id\",\"value\": \"0\"},{\"operator\": \"in\",\"field\": \"type\",\"value\": [\"B\"]}]}}"

            with OutputStreamWriter(urlConn_Branch_count.getOutputStream(), "utf-8") as os:
                input = jsonInputString_Branch_Count.encode("utf-8")
                os.write(input, 0, len(input))

            if urlConn_Branch_count.getResponseCode() == 200:
                with BufferedReader(InputStreamReader(urlConn_Branch_count.getInputStream(), "utf-8")) as br2:
                    response_Branch_count = StringBuilder()
                    responseLine_Branch_count = None
                    while (responseLine_Branch_count = br2.readLine()) != None:
                        response_Branch_count.append(responseLine_Branch_count.strip())
                    total_Branch_count = int(response_Branch_count.toString())
                    print("Total_Branch_count is " + str(total_Branch_count))

                    start_id = 0
                    readTimeout = ((total_Branch_count / 5000) * 10 * 1000) + 10 * 60 * 1000

                    i = 0
                    while i <= total_Branch_count / 5000:
                        url = URL(Cparty_TypeB.FindUrl)
                        urlConn_Branch_find = url.openConnection()
                        urlConn_Branch_find.setConnectTimeout(10000)
                        urlConn_Branch_find.setReadTimeout(readTimeout)
                        urlConn_Branch_find.setRequestMethod("POST")
                        urlConn_Branch_find.setRequestProperty("Content-Type", "application/json; charset=utf-8")
                        urlConn_Branch_find.setRequestProperty("Accept", "application/json")
                        urlConn_Branch_find.setDoOutput(True)

                        with OutputStreamWriter(urlConn_Branch_find.getOutputStream(), "utf-8") as os:
                            s1 = str(start_id)
                            jsonInputString_Branch_find = "{\"criteria\": {\"operator\": \"and\",\"items\": [{\"operator\": \"eq\",\"field\": \"type\",\"value\": \"B\"}]},\"afterid\": " + s1 + ",\"take\": 5000,\"fields\": [\"id\",\"ultimate_parent_id\",\"name\",\"type\", \"ownership.parent_id\",\"bic\", \"bta_code_of_accounts\",\"country_of_operation\",\"country_of_incorporation\", \"short_name\",\"updated_on\"]}"
                            input = jsonInputString_Branch_find.encode("utf-8")
                            os.write(input, 0, len(input))

                        if urlConn_Branch_find.getResponseCode() == 200:
                            with BufferedReader(InputStreamReader(urlConn_Branch_find.getInputStream(), "utf-8")) as br:
                                response = StringBuilder()
                                responseLine = None
                                while (responseLine = br.readLine()) != None:
                                    response.append(responseLine.strip())
                                temp = response.toString()

                                obj = JSONArray(temp)
                                last_cp = obj.get(obj.length() - 1)
                                m = last_cp.get("id").toString()
                                start_id = int(m)

                                temp = temp[1: -1]
                                Cparty_Branch.write(temp)

                        i += 1

                    Cparty_Branch.write(",")
            else:
                Cparty_TypeB.readFromStream(urlConn_Branch_count.getErrorStream())

        except SSLHandshakeException as e:
            print(e)
        except Exception as e:
            print(e)

        inputfile_Branch = "//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//JSON//Cparty_Branch.txt"
        fulljson_Branch = String(Files.readAllBytes(Paths.get(inputfile_Branch)))
        jsonArrayString_Branch = "{\"fileName\":" + fulljson_Branch + "}"
        output_Branch = None

        try:
            output_Branch = JSONObject(jsonArrayString_Branch)
            docs_Branch = output_Branch.getJSONArray("fileName")

            file_Branch = File("//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//JSON//Counterparty_TypeB.txt")
            csv_Branch = CDL.toString(docs_Branch)
            FileUtils.writeStringToFile(file_Branch, csv_Branch)

        except Exception as e:
            print(e)

        strFile = "//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//JSON//Counterparty_TypeB.txt"
        reader = CSVReader(FileReader(strFile))
        nextLine = None
        newFinal = "//apps//axiom_app//boe//batch//scripts//JAVA_CODE//sds//Files//Counterparty_TypeB.txt"
        writer = CSVWriter(FileWriter(newFinal), '|', CSVWriter.NO_QUOTE_CHARACTER)

        while (nextLine = reader.readNext()) != None:
            if nextLine != None:
                writer.writeNext(nextLine)

        writer.close()

        dtf2 = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss")
        now2 = LocalDateTime.now()
        print(dtf2.format(now2))


if __name__ == "__main__":
    Cparty_TypeB.main(None)
