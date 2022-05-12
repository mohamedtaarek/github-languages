
from rest_framework import views, status
from rest_framework.response import Response
from datetime import date, timedelta
import requests
import json
class TrendingReposAPI(views.APIView):
    def get(self,request, *args,**kwargs):
        day = date.today() -timedelta(days=30)
        print("Today's date:", day)
        query = "created:>" + str(day)
        params = {
            'q': query,
            "sort": "stars",
            "order": "desc",
            "per_page": 100
        }
        response  = requests.get('https://api.github.com/search/repositories',params=params)
        data = json.loads(response.text)
        repos = data["items"]
        reshaped_data = {}
        for repo in repos:
            if reshaped_data.get(repo["language"]):
                reshaped_data[repo["language"]]["count"]= reshaped_data[repo["language"]]["count"] + 1
                reshaped_data[repo["language"]]["repositories"].append(repo)
            else:
                reshaped_data[repo["language"]]= {"count": 1}
                reshaped_data[repo["language"]]["repositories"]= [repo]
        return Response(reshaped_data,status=status.HTTP_200_OK)