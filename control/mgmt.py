from db_model.mongodb import conn_mongodb
from datetime import datetime

class ExplorerSession():
    explorer_page = {'A':'explorer_A.html', 'B':'explorer_B.html'}
    session_count = 0

    @staticmethod
    def save_session_info(session_ip):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")  # https://strftime.org/
        
        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip': session_ip,
            'access_time': now_time
        })

    @staticmethod # AB_test를 위한 static 메소드, 페이지 호출
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