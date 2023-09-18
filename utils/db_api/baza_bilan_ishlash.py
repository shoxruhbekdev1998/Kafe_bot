import sqlite3

class Database:
    def __init__(self,baza_manzili):
        self.path_to_db = baza_manzili
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql:str,parameters:tuple = None, fetchone = False, fetchall = False, commit = False):
        if not parameters:
            parameters = ()

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    @staticmethod
    def format_args(sql,parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql , tuple(parameters.values())





    def user_qoshish(self, ism:str, tg_id:int, fam: str = None, username: str=None):

        sql = """ 
        INSERT INTO myfiles_subscribe(ism,tg_id,fam,username) Values( ?, ?, ?, ?)
        """
        self.execute(sql,parameters=(ism,tg_id,fam,username),commit=True)


    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_subscribe
        """
        return self.execute(sql,fetchall=True)

    def select_user(self,**kwargs):

        #SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
        SELECT * FROM myfiles_menu Where 
        """
        sql,parameters =self.format_args(sql,kwargs)

        return sql.execute(sql,parameters=parameters,fetchone=True)

    def select_types(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT * FROM myfiles_menu Where 
                """
        sql, parameters = self.format_args(sql, kwargs)

        return sql.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_subscribe;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM myfiles_subscribe WHERE TRUE",commit=True)

    def select_all_menu(self):
        sql = """
        SELECT * FROM myfiles_menu
        """
        return self.execute(sql,fetchall=True)



    def select_maxsulotlar(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT * FROM myfiles_maxsulotlar Where 
                """
        sql,parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)


    def select_maxsulotlar_from_korzinka(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                SELECT * FROM myfiles_korzinka Where 
                """
        sql,parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)


    def select_all_maxsulotlar(self):
        sql = """
        SELECT * FROM myfiles_maxsulotlar
        """
        return self.execute(sql,fetchall=True)

    def maxsulot_qoshish_to_korzinka(self, nomi: str,
                                     tg_id: int,
                                     narxi: int,
                                     rasm: str,
                                     turi: str,
                                     date: str,
                                     soni: int,
                                     status: bool = True,
                                     malumot: str = None,
                                     username: str = None):

        sql = """ 
           INSERT INTO myfiles_korzinka(nomi,soni,narxi,tg_id,rasm,malumot,turi,username,date,status) Values( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
           """
        self.execute(sql, parameters=(nomi,soni,narxi,tg_id,rasm,malumot,turi,username,date,status), commit=True)


    def select_maxsulot(self,**kwargs):

        #SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
        SELECT * FROM myfiles_maxsulotlar Where 
        """
        sql,parameters =self.format_args(sql,kwargs)

        return self.execute(sql,parameters=parameters,fetchone=True)

    def select_maxsulot_from_korzinka(self, **kwargs):

        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
           SELECT * FROM myfiles_korzinka Where 
           """
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)


    def update_korzinka(self,soni,tg_id,nomi):

        #SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
        UPDATE  myfiles_korzinka SET soni=?  Where tg_id=? and nomi=?
        """
        self.execute(sql, parameters=(soni,tg_id,nomi), commit=True)



    def delete_maxsulot_from_korzinka(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM user where id = 1 AND Name='John'"
        sql = """
                DELETE FROM myfiles_korzinka Where 
                """
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, commit=True)


def logger(statement):
    print(f"""
    _________________________________________________
    Executing:
    {statement}
    ___________________________________________________-
"""

    )