from sqlalchemy import MetaData, create_engine

engine = create_engine('postgresql://chef:yesyesye@localhost/chefaidb')

metadata = MetaData()
metadata.reflect(bind=engine)

print(metadata.tables.keys())

