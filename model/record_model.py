from PySide6.QtSql import QSqlQuery, QSqlQueryModel

from model.dbutil import DBUtil


QUERY_RECORD_SQL = "SELECT t.id 编号,m.name 人员,t.product_id as 仪器编号,p.name as 仪器 ,t.create_time 创建时间,t.start_date 借用开始日期,t.end_date 借用结束日期 FROM record t LEFT JOIN user m on m.id=t.people LEFT JOIN product p on p.id=t.product_id"

QUERY_BORROWFLAG_SQL = """SELECT t.id FROM record t where t.product_id = :pid and 
(date(:start) BETWEEN date(t.start_date) and date(t.end_date)
OR  date(:end) BETWEEN date(t.start_date) and date(t.end_date))"""

INSERT_RECORD_SQL = """
INSERT INTO "record" ("people", "create_time", "start_date", "end_date", "product_id") VALUES (?, datetime('now','localtime'), ?, ?, ?);
"""


class RecordModel:

    def getRecords(self) -> QSqlQueryModel:
        recordModel = DBUtil.query_model(QUERY_RECORD_SQL)
        return recordModel

    def getRecordsByQuery(self, user_name, prodt_name, query_date):
        QUERY_RECORD_BYPARAM_SQL = """SELECT t.id 编号,m.name 人员,t.product_id as 仪器编号,p.name as 仪器 ,t.create_time 创建时间,t.start_date 借用开始日期,t.end_date 借用结束日期 
                                    FROM record t 
                                    LEFT JOIN user m on m.id=t.people 
                                    LEFT JOIN product p on p.id=t.product_id
                                    where 1=1 
                                    """
        param_dict = {}
        if user_name:
            QUERY_RECORD_BYPARAM_SQL = QUERY_RECORD_BYPARAM_SQL+" and m.name=:uname"
            param_dict[":uname"] = user_name
        if prodt_name:
            QUERY_RECORD_BYPARAM_SQL = QUERY_RECORD_BYPARAM_SQL+" and p.name=:pname"
            param_dict[":pname"] = prodt_name
        if query_date:
            QUERY_RECORD_BYPARAM_SQL = QUERY_RECORD_BYPARAM_SQL + \
                " and t.create_time BETWEEN Datetime(:start_date|| '00:00:00') AND Datetime(:end_date|| '23:59:59')"
            param_dict[":start_date"] = query_date
            param_dict[":end_date"] = query_date

        recordModel = DBUtil.query_byparam_model(
            QUERY_RECORD_BYPARAM_SQL, param_dict)
        return recordModel

    def getRecordList(self, user_name, prodt_name, query_date):
        q = QSqlQuery(DBUtil.db)
        QUERY_RECORD_BYPARAM_SQL = """SELECT t.create_time 创建时间,m.name 人员,p.name as 仪器,t.product_id as 仪器编号 ,t.start_date 借用开始日期,t.end_date 借用结束日期 
                                    FROM record t 
                                    LEFT JOIN user m on m.id=t.people 
                                    LEFT JOIN product p on p.id=t.product_id
                                    where 1=1 
                                    """
        if user_name:
            QUERY_RECORD_BYPARAM_SQL = QUERY_RECORD_BYPARAM_SQL+" and m.name=:uname"
        if prodt_name:
            QUERY_RECORD_BYPARAM_SQL = QUERY_RECORD_BYPARAM_SQL+" and p.name=:pname"
        if query_date:
            QUERY_RECORD_BYPARAM_SQL = QUERY_RECORD_BYPARAM_SQL + \
                " and t.create_time BETWEEN Datetime(:start_date|| '00:00:00') AND Datetime(:end_date|| '23:59:59')"
        q.prepare(QUERY_RECORD_BYPARAM_SQL)
        if user_name:
            q.bindValue(":uname", user_name)
        if prodt_name:
            q.bindValue(":pname", prodt_name)
        if query_date:
            q.bindValue(":start_date", query_date)
            q.bindValue(":end_date", query_date)
        q.exec()
        record_list = [('登记时间', '人员', '仪器', '仪器编号', '借用开始日期', '借用结束日期')]
        while q.next():
            record = (q.value(0), q.value(1), q.value(2), q.value(
                3), q.value(4), q.value(5))
            record_list.append(record)
        return record_list

    def getBorrowFlag(self, pid, start, end):
        q = QSqlQuery(DBUtil.db)
        q.prepare(QUERY_BORROWFLAG_SQL)
        q.bindValue(":pid", pid)
        q.bindValue(":start", start)
        q.bindValue(":end", end)
        q.exec()
        return q.next()

    def saveBorrow(self, pid, people, start, end):
        q = QSqlQuery(INSERT_RECORD_SQL, DBUtil.db)
        q.addBindValue(people)
        q.addBindValue(start)
        q.addBindValue(end)
        q.addBindValue(pid)
        q.exec()
        return q.lastInsertId()
