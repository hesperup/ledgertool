from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from model.dbutil import DBUtil


QUERY_PRODUCT_SQL = "SELECT id as 管理编号 ,name as 仪器,fac_id as 厂家编号 ,spec as 规格 FROM product order by name"

INSERT_PRODUCT_SQL = """
    insert into product(id,name,spec,fac_id) values(?,?,?,?)
    """


QUERY_PRODUCT_BY_ID_SQL = "SELECT id   FROM product where id = :id"

QUERY_PRODLIST_SQL = "SELECT distinct name FROM product order by name"

QUERY_PIDLIST_SQL = "SELECT id  FROM product where name = :name "

DEL_BY_ID_SQL = "DELETE FROM product where id = :id"


class ProductModel:

    def getProducts(self):
        productModel = DBUtil.query_model(QUERY_PRODUCT_SQL)
        return productModel

    def addProduct(self, id, name, spec, fac_id):
        q = QSqlQuery(INSERT_PRODUCT_SQL, DBUtil.db)
        q.addBindValue(id)
        q.addBindValue(name)
        q.addBindValue(spec)
        q.addBindValue(fac_id)
        q.exec()
        return

    def queryById(self, id) -> bool:
        q = QSqlQuery(DBUtil.db)
        q.prepare(QUERY_PRODUCT_BY_ID_SQL)
        q.bindValue(":id", id)
        q.exec()
        return q.next()

    def del_prod(self, id):
        q = QSqlQuery(DBUtil.db)
        q.prepare(DEL_BY_ID_SQL)
        q.bindValue(":id", id)
        q.exec()

    def queryProdList(self):
        prod_list = ['']
        q = QSqlQuery(QUERY_PRODLIST_SQL, DBUtil.db)
        q.exec()
        while q.next():
            prod_list.append(q.value(0))
        return prod_list

    def queryPidList(self, name):
        pid_list = ['']
        q = QSqlQuery(DBUtil.db)
        q.prepare(QUERY_PIDLIST_SQL)
        q.bindValue(":name", name)
        q.exec()
        while q.next():
            # print(q.value(0))
            pid_list.append(q.value(0))
        return pid_list
