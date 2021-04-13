from sqlalchemy import create_engine, Column, Integer, Float, String, or_, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///cmstock.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float)
    stock = Column(Integer)

Base.metadata.create_all(engine)

# Insert
product1 = Product(name="Arduino", price=100.50, stock=10)
product2 = Product(name="NodeMCU", price=200, stock=11)
product3 = Product(name="LED", price=1, stock=211)
# session.add(product1)
session.add_all([product1, product2, product3])
session.commit()

# Query all
# products = session.query(Product)
# for product in products:
#     print(product.id, product.name, product.price, product.stock)

# Query with condition
# product = session.query(Product).filter(Product.id==2).first()
# print(product.id, product.name, product.price, product.stock)


# Query with or condition
products = session.query(Product).filter(or_(Product.name=='Arduino', Product.name=='LED'))
for product in products:
    print(product.id, product.name, product.price, product.stock)

# Update
# product = session.query(Product).filter(Product.id==1).first()
# product.name = "CodeMobiles"
# product.stock = 1
# product.price = 1
# session.commit()

# Update multi row
# products = session.query(Product).filter(Product.name=="LED")
# products.update({Product.name:"LCD"})
# session.commit()

# Delete
products = session.query(Product).filter(Product.name=="LCD")
products.delete()
session.commit()
