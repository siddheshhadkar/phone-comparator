import mysql.connector

class FlipkartscraperPipeline(object):

    def __init__(self):
        self.link = mysql.connector.connect(host='localhost', user='<username_here>', passwd='<password_here>', database='scraperdb')
        self.cursor = self.link.cursor()
        self.cursor.execute("SHOW TABLES")
        self.flag=0
        for x in self.cursor:
            if 'flipkart' in x:
                self.flag = 1
        if self.flag!=1:
            self.cursor.execute("CREATE TABLE flipkart(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255), modelnumber VARCHAR(255), modelname VARCHAR(255), color VARCHAR(255), operatingsystem VARCHAR(255), displaysize VARCHAR(255), processortype VARCHAR(255), processorcore VARCHAR(255), internalstorage VARCHAR(255), resolution VARCHAR(255), gpu VARCHAR(255), ram VARCHAR(255), expandablestorage VARCHAR(255), primarycamera VARCHAR(255), secondarycamera VARCHAR(255), batterycapacity VARCHAR(255), warrantysummary VARCHAR(255))")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.query = "INSERT INTO flipkart(name , price , modelnumber , modelname , color , operatingsystem , displaysize , processortype , processorcore , internalstorage , resolution , gpu , ram , expandablestorage , primarycamera , secondarycamera , batterycapacity , warrantysummary) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for x in item:
            if item[x]==None:
                item[x]=""
        self.vals = (item['name'], item['price'], item['modelnumber'], item['modelname'], item['color'], item['operatingsystem'], item['displaysize'], item['processortype'], item['processorcore'], item['internalstorage'], item['resolution'], item['gpu'], item['ram'], item['expandablestorage'], item['primarycamera'], item['secondarycamera'], item['batterycapacity'], item['warrantysummary'])
        self.cursor.execute(self.query, self.vals)
        self.link.commit()
