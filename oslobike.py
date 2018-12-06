
import requests

# this method will send the request to api endpoint and will return response
def get_api_response(url,header):
    return requests.get(url,headers=header)

def main():
    client_identifier={'Client-Identifier':'API_KEY'}
    url_stations = "https://oslobysykkel.no/api/v1/stations"
    url_avilabulity = "https://oslobysykkel.no/api/v1/stations/availability"
    
    # GET Calls are made to both stations and availability endpoints in order to retrieve 
    # station title,available bikes and locked bikes information
    try:
        req_stations = get_api_response(url_stations,client_identifier)
        req_stations.raise_for_status()
        req_availability = get_api_response(url_avilabulity,client_identifier)
        req_availability.raise_for_status()

        if (req_stations and req_availability):
            json_object_stations = req_stations.json()
            json_object_availability = req_availability.json()

            print('Station Name |      Available bikes    | Locked bikes ')

            for stn in json_object_stations["stations"]:
                for avl in json_object_availability["stations"]:
                    if stn["id"] == avl["id"]:
                        print(stn["title"] , '|', avl["availability"]["bikes"], '|', avl["availability"]["locks"])
        else:
            print("Error: Received empty response from api")

    except requests.exceptions.HTTPError as Errh:
        print ("Http Error:",Errh)
        return False
    except requests.exceptions.ConnectionError as Errc:
        print ("Error Connecting:",Errc)
        return False
    except requests.exceptions.Timeout as Errt:
        print ("Timeout Error:",Errt)
        return False
    except requests.exceptions.RequestException as Err:
        print ("Error: Something Else",Err)
        return False

if __name__ == '__main__':
    main()
