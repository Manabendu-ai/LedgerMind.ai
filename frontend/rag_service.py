from config import QUERY_API
import requests

class QueryService:
    def get_response(self, query:str):
        try:
            response = requests.post(QUERY_API, params={"query":query})
            if response.status_code == 200:
                return response.json()
            else:
                return {
                        "status": "error",
                        "status_code": response.status_code,
                        "message": response.text
                    }
        except Exception as e:
            print(f"Retrival Error {e}")