from database.connection import get_connection


class SuperServices:

    def open(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()   

    def execute_query(self, query, params, insert=None):
        self.open()

        try:
            self.cur.execute(query, params)
            self.conn.commit()

            if insert:
                return self.cur.fetchone()[0] # type: ignore
            
        except Exception as e:
            self.conn.rollback()
            print(e)
            
        finally:
            self.close()

    def select(self, query, fetch: str, params=None):
        self.open()

        try:
            if fetch == 'one':
                self.cur.execute(query, params)
                result = self.cur.fetchone()
            elif fetch =='all':
                self.cur.execute(query)
                result = self.cur.fetchall()

            return result

        except Exception as e:
            print(e)

        finally:
            self.close()