
from mysql import connector
import datetime
class DbShop:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="321996",
                database="shop_db"
            )
            return self.connection
        except Exception as e:
            return None

class ProductManager(DbShop):
    def get_object(self,id=None):
        try:
            self.connection = super().get_connected()
            self.cursor = self.connection.cursor()
            query = "select * from product where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            products = self.cursor.fetchone()
            return products
        except Exception as e:
            return None
    def post(self,**kwargs):
        try:
            self.connection = super().get_connected()
            self.cursor = self.connection.cursor()
            query = "insert into product(product_name,category,brand,price,stock,supplier,added_date) values(%s,%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Product Added Successfully...!")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.connection=super().get_connected()
            self.cursor=self.connection.cursor()
            query ="select * from product"
            self.cursor.execute(query)
            products=self.cursor.fetchall()
            for i in products:
                print(i)
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            products = self.get_object(id=id)
            if products != None:
                self.connection = super().get_connected()
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k +"=%s,"
                placeholder =placeholder.rstrip(", ")
                query = f"update product set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Product Data updated Successfully...")

            else:
                print("Product Not Found..!")
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.connection = super().get_connected()
            self.cursor = self.connection.cursor()
            query = "delete from product where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            self.connection.commit()
            print('deleted success')

            if self.cursor.rowcount > 0:
                print("Deletion successful")
            else:
                print("Product not found")
        except Exception as e:
            print(e)

shop_instance =DbShop()
shop_instance.get_connected()
product_instance =ProductManager()
print(product_instance.get_object(1))
#product_instance.post(product_name="Computer",category="Electronics",brand="Dell",price=55000,stock=10,supplier="ABC Computers",added_date=datetime.datetime.today())
#product_instance.post(product_name="Laptop", category="Electronics", brand="HP", price=55000, stock=15, supplier="Tech World", added_date=datetime.datetime.today())
#product_instance.post(product_name="Smartphone", category="Electronics", brand="Samsung", price=28000, stock=20, supplier="Mobile Hub", added_date=datetime.datetime.today())
#product_instance.post(product_name="Keyboard", category="Electronics", brand="Logitech", price=1500, stock=30, supplier="Computer Zone", added_date=datetime.datetime.today())
#product_instance.post(product_name="Office Chair", category="Furniture", brand="Nilkamal", price=7500, stock=12, supplier="Home Mart", added_date=datetime.datetime.today())
#product_instance.post(product_name="Notebook", category="Stationery", brand="Classmate", price=80, stock=100, supplier="Stationery World", added_date=datetime.datetime.today())
#product_instance.post(product_name="T-Shirt", category="Clothing", brand="Puma", price=1800, stock=25, supplier="Fashion Hub", added_date=datetime.datetime.today())
product_instance.put(1,price=45000)
product_instance.delete(3)
product_instance.get()