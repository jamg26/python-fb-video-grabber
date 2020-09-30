import requests
from pySmartDL import SmartDL
from time import sleep


def main():
    link = ""

    link = input('Enter facebook video url: ')

    dest = "./"

    if "facebook" in link:
        url = "https://getvideo.p.rapidapi.com/"

        querystring = {
            "url": link}

        headers = {
            'x-rapidapi-host': "getvideo.p.rapidapi.com",
            'x-rapidapi-key': "fKF1gF6A8Hmshio5bYJ0MWDnKgRXp1HFSX7jsnmPs7rhcgCPmb"
        }
        try:
            response = requests.request(
                "GET", url, headers=headers, params=querystring)
            r = response.json()
        except:
            print('Link is not supported.')
            main()
        for x in r['streams']:
            if 'hd' in x['fmt_id']:
                obj = SmartDL(x['url'], dest)
                obj.start()
                path = obj.get_dest()
                res = input('Done!\ntry again? [y/n]: ')
                if 'y' in res:
                    main()
                else:
                    print('Created by: jamuel galicia')
                    sleep(3)
                    exit()
                # print(x['url'])
    else:
        print('Invalid fb link')


main()
