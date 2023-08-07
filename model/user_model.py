
from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from model.dbutil import DBUtil

INSERT_USER_SQL = """
    insert into user(name) values(?)
    """
QUERY_USER_SQL = "SELECT id as 编号, name as 人员 FROM user "

QUERY_USER_BY_NAME_SQL = """
    SELECT id FROM user where name = :name
    """

QUERY_USERLIST_SQL = "SELECT name  FROM user "

DEL_BY_ID_SQL = "delete FROM user where id = :id"


class UserModel:
    def getUsers(self) -> QSqlQueryModel:
        userModel = DBUtil.query_model(QUERY_USER_SQL)
        return userModel

    def addUser(self, userName):
        q = QSqlQuery(INSERT_USER_SQL, DBUtil.db)
        q.addBindValue(userName)
        q.exec()
        return q.lastInsertId()

    def queryByName(self, userName) -> bool:
        q = QSqlQuery(DBUtil.db)
        q.prepare(QUERY_USER_BY_NAME_SQL)
        q.bindValue(":name", userName)
        q.exec()
        return q.next()

    def queryIdByName(self, userName) -> bool:
        q = QSqlQuery(DBUtil.db)
        q.prepare(QUERY_USER_BY_NAME_SQL)
        q.bindValue(":name", userName)
        q.exec()
        if q.next():
            return q.value(0)

    def del_pojo(self, id):
        q = QSqlQuery(DBUtil.db)
        q.prepare(DEL_BY_ID_SQL)
        q.bindValue(":id", id)
        q.exec()

    def queryUserList(self):
        user_list = ['']
        q = QSqlQuery(QUERY_USERLIST_SQL, DBUtil.db)
        q.exec()
        while q.next():
            user_list.append(q.value(0))
        return user_list
