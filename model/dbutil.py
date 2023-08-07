
import os
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery

basedir = os.path.dirname(__file__)


class DBUtil:
    db = QSqlDatabase("QSQLITE")

    @classmethod
    def init_db(self):
        DBUtil.db.setDatabaseName(os.path.join(basedir, "ledger.sqlite"))
        DBUtil.db.open()

    @classmethod
    def query_model(self, sql) -> QSqlQueryModel:
        result_model = QSqlQueryModel()
        result_query = QSqlQuery(
            sql, DBUtil.db)
        result_model.setQuery(result_query)
        return result_model

    @classmethod
    def query_byparam_model(self, sql, param_dict) -> QSqlQueryModel:
        result_model = QSqlQueryModel()
        query = QSqlQuery(DBUtil.db)
        query.prepare(sql)
        # print(sql)
        for key, value in param_dict.items():
            query.bindValue(key, value)
        query.exec()
        result_model.setQuery(query)
        return result_model
