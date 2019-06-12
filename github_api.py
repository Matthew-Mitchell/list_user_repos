import requests
import datetime
import time

def print_repos(url, all_ = True):
    headers = "Accept: application/vnd.github.v3+json" #specify api for stability
    response = requests.get(url, params=headers)
    for item in response.json():
        print(item['name'])
    #Pagination Recursion
    if all_:
        try:
            url = response.links['next']['url']
            print("Next url: \n",url)
            #Check remaining requests
            remaining_requests = int(response.headers['X-RateLimit-Remaining'])
            print(remaining_requests)
            if remaining_requests > 0:
                print_repos(url)
            else:
                #Check reset time and wait accordingly
                reset_time = datetime.datetime.fromtimestamp(int(response.headers['X-RateLimit-Reset']))
                time_now = datetime.datetime.now()
                time_remaining = reset_time - time_now
                print("Rate Limiting Requests. Pausing for: ~{}".format(time_remaining))
                time.sleep(time_remaining.seconds + 5) #Wait remaining time plus 5 second buffer
        except:
            pass #No more links found

def print_usr_repos(username, all_ = True):
    url = "https://api.github.com/users/{}/repos".format(username)
    print_repos(url, all_ = all_)     #Pass to helper function

