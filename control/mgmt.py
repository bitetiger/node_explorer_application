from db_model.mongodb import conn_mongodb
from datetime import datetime

class ExplorerSession():
    explorer_page = {'A':'explorer_A.html', 'B':'explorer_B.html'}
    session_count = 0

    @staticmethod
    def save_session_info(session_ip, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%y %H:%M:%S") #https://strftime.org/
        
        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip' : session_ip,
            'page' : webpage_name,
            'access_time' : now_time
        })

    @staticmethod
    def get_explorer_page(page_id=None):
        if page_id == None:
            if ExplorerSession.session_count == 0:
                ExplorerSession.session_count = 1
                return ExplorerSession.explorer_page('A')
            else:
                ExplorerSession.session_count = 0
                return ExplorerSession.explorer_page('B')
        else:
            return ExplorerSession.explorer_page(page_id)