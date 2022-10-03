import requests, json, inspect, re

class NPSParks():

    #TODO NPS API can't handle symbols in GET URL

    def __init__(self, api_key):
        self.api_key = api_key

    def __call_api(self, url_ending, parameters=[]):
            base_url = "https://developer.nps.gov/api/v1/"
            endpoint = f"{base_url}{url_ending}" 
            parameter_str = '?'
            for item in parameters:
                key_value_split = re.split(r'=|;', item)
                if key_value_split[1] == "":
                    continue
                elif key_value_split[2] == 'True' and key_value_split[1] == '[]':
                    continue
                elif key_value_split[2] == 'True':
                    parameter_str += f"{key_value_split[0]}="
                    for word in key_value_split[1].split(','):
                        word = word.strip("[]' ")
                        parameter_str += f"{word.replace(' ', '%20')},"
                    parameter_str = parameter_str.rstrip(',')
                    parameter_str += '&'
                else:
                    parameter_str += f"{item.replace(' ', '%20')}&"
            endpoint += f"{parameter_str}api_key={self.api_key}"
            return json.loads(requests.get(endpoint).text)

    def __format_parameter_list(self, items, function):
        return_list = []
        counter = 0
        signature = inspect.signature(function)
        for param in signature.parameters.keys():
            isList = False
            if counter < len(items):
                if type(items[counter]) == list:
                    isList = True
                return_list.append(f"{param}={items[counter]};{isList}")
            counter += 1
        return return_list
            
    def get_activities(self, id="", q="", limit="", start="", sort=""):
        parameters = self.__format_parameter_list([id, q, limit, start, sort], self.get_activities)
        return self.__call_api("activities", parameters=parameters)
    
    def get_activities_parks(self, id=[], q="", limit="", start="", sort=[]):
        parameters = self.__format_parameter_list([id, q, limit, start, sort], self.get_activities_parks)
        return self.__call_api("activities/parks", parameters=parameters)

    def get_alerts(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_alerts)
        return self.__call_api("alerts", parameters=parameters)

    def get_amenities(self, id=[], q="", limit="", start=""):
        parameters = self.__format_parameter_list([id, q, limit, start], self.get_amenities)
        return self.__call_api("amenities", parameters=parameters)

    def get_amenities_parksplaces(self, parkCode=[], id=[], q="", limit="", start="", sort=""):
        parameters = self.__format_parameter_list([parkCode, id, q, limit, start, sort], self.get_amenities_parksplaces)
        return self.__call_api("amenities/parksplaces", parameters=parameters)

    def get_amenities_parksvisitorcentors(self, parkCode="", id="", q="", limit="", start="", sort=[]):
        parameters = self.__format_parameter_list([parkCode, id, q, limit, start, sort], self.get_amenities_parksvisitorcentors)
        return self.__call_api("amenities/parksvisitorcentors", parameters=parameters)

    def get_articles(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_articles)
        return self.__call_api("articles", parameters=parameters)

    def get_campgrounds(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode,stateCode, limit, start, q,], self.get_campgrounds)
        return self.__call_api("campgrounds", parameters=parameters)

    def get_events(self, parkCode=[], organization=[], subject=[], portal=[], tagsAll=[], tagsNone=[], stateCode=[], dateStart="", dateEnd="", eventType=[], id="", q="", pageSize="", pageNumber="", expandRecurring=""):
        parameters = self.__format_parameter_list([parkCode, organization, subject, portal, tagsAll, tagsNone, stateCode, dateStart, dateEnd, eventType, id, q, pageSize, pageNumber, expandRecurring], self.get_events)
        return self.__call_api("events", parameters=parameters)

    def get_lessonplans(self, parkCode=[], stateCode=[], limit="", start="", q="", sort=[]):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q, sort], self.get_lessonplans)
        return self.__call_api("lessonplans", parameters=parameters)

    def get_multimedia_audio(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_multimedia_audio)
        return self.__call_api("multimedia/audio", parameters=parameters)

    def get_multimedia_videos(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_multimedia_videos)
        return self.__call_api("multimedia/videos", parameters=parameters)

    def get_newsreleases(self, parkCode=[], stateCode=[], limit="", start="", q="", sort=[]):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q, sort], self.get_newsreleases)
        return self.__call_api("newsreleases", parameters=parameters)

    def get_parkinglots(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_parkinglots)
        return self.__call_api("parkinglots", parameters=parameters)

    def get_parks(self, parkCode=[], stateCode=[], limit="", start="", q="", sort=[]):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q, sort], self.get_parks)
        return self.__call_api("parks", parameters=parameters)

    def get_passportstamplocations(self, parkCode=[], stateCode=[], q="", limit="", start=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, q, limit, start], self.get_passportstamplocations)
        return self.__call_api("passportstamplocations", parameters=parameters)

    def get_people(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_people)
        return self.__call_api("people", parameters=parameters)

    def get_places(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_places)
        return self.__call_api("places", parameters=parameters)

    def get_thingstodo(self, id=[], parkCode=[], stateCode=[], q="", limit="", start="", sort=[]):
        parameters = self.__format_parameter_list([id, parkCode, stateCode, q, limit, start, sort], self.get_thingstodo)
        return self.__call_api("thingstodo", parameters=parameters)

    def get_topics(self, id=[], q="", limit="", start="", sort=[]):
        parameters = self.__format_parameter_list([id, q, limit, start, sort], self.get_topics)
        return self.__call_api("topics", parameters=parameters)

    def get_topics_parks(self, id=[], q="", limit="", start="", sort=[]):
        parameters = self.__format_parameter_list([id, q, limit, start, sort], self.get_topics_parks)
        return self.__call_api("topics/parks", parameters=parameters)

    def get_tours(self, id=[], parkCode=[], stateCode=[], q="", limit="", start=""):
        parameters = self.__format_parameter_list([id, parkCode, stateCode, q, limit, start], self.get_tours)
        return self.__call_api("tours", parameters=parameters)

    def get_visitorcenters(self, parkCode=[], stateCode=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, limit, start, q], self.get_visitorcenters)
        return self.__call_api("visitorcenters", parameters=parameters)

    def get_webcams(self, parkCode=[], stateCode=[], id=[], limit="", start="", q=""):
        parameters = self.__format_parameter_list([parkCode, stateCode, id, limit, start, q], self.get_webcams)
        return self.__call_api("webcams", parameters=parameters)


    
