import os

import googleapiclient.discovery

title = 're zero'

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    with open("./token.txt") as f:
            api_key = f.read()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = api_key)

    request = youtube.search().list(
        part="snippet",
        q="обзор на аниме {}".format(title)
    )
    response = request.execute()

    for key in response:
        print(key, response[key])
    print(response['items'][0]['id']['videoId'])

if __name__ == "__main__":
    main()