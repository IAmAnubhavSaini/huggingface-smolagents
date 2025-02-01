from requests.cookies import RequestsCookieJar


COOKIES_LIST = [
    {
        "domain": ".youtube.com",
        "expirationDate": 1718884961,
        "hostOnly": False,
        "httpOnly": False,
        "name": "ST-xuwub9",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "session_logininfo=AFmmF2swRAIgf4gadACOuWOcipI1anW-dakEjtidNLkufnOC8uml7EECIDh2YisqWELDBJPTGUysCucJ3I0wjXxYjVHro1LHrdW0%3AQUQ3MjNmd2Jiajl3OWZYRnpFNnZlWWV5ZGJWZ0hpcmp4LVVPU280bk4zOS03Z0ozZG9fOFhWZ0dXaVo3NG1wTEg1b3hGaG10TFBlaFBnTlJfbER5bEp0aFhoNS1OLVhYNFRZT2F6ajgzOFpDbGhlUjZpMWRETlFFRjFfTTRiM0RnNTROSkdmMTFMVjFic1VuZ2trbGp4aktDa0JJUC1BWDh3",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753004444.745411,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__Secure-YEC",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "CgtRVnI5LW1zRHlQVSjbtNCzBjIhCgJGUhIbEhcSFRMLFBUWFwwYGRobHB0eHw4PIBAREiAk",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050824,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__Secure-3PSID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "g.a000kwibeLUu8Ea9Y-vLun7u3kU5VNJVuMAZl_jdfJaNm50JyDBB4ezJ_bdWu46a7YwObVn44wACgYKAakSARQSFQHGX2MicJcTzecTKH6bHzqU6TMbTxoVAUF8yKqQYK-MoI6Ql3vI2oYTB3E-0076",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1750420959.974642,
        "hostOnly": False,
        "httpOnly": False,
        "name": "SIDCC",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "AKEyXzWQZauHKOo8t87zoEcjaVNIYUX54ohoWXT-tX4aAhEuZzIIptxZAcNkHuG2oDXYL6t-lw",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050652,
        "hostOnly": False,
        "httpOnly": False,
        "name": "SID",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "g.a000kwibeLUu8Ea9Y-vLun7u3kU5VNJVuMAZl_jdfJaNm50JyDBB6VHrZcC3gBAsFPbCQ0gF5AACgYKAYkSARQSFQHGX2Mi9kt0gHg5CxCYSkLQGHWaeBoVAUF8yKre_V6r3jZVak6JV4o2Q0FL0076",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1750420958.397534,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__Secure-1PSIDTS",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "sidts-CjIB3EgAEkYL2L-GfrEzW5Dfy62S9oefGNLgst78S_986htCnGcfkxECch_9oz-qytSsZBAA",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753433494.44729,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga_M0180HEFCY",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GS1.1.1718871908.1.0.1718873494.0.0.0",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050933,
        "hostOnly": False,
        "httpOnly": False,
        "name": "SAPISID",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "mfeuiC-HraNJ-A03/ASXvCPNJSw7yTFgd6",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1750420959.974764,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__Secure-1PSIDCC",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "AKEyXzWHDSoXGCZpZhPxRrnC7B1s8zGIUjeMVyvgtQfsm1fs92lXPtFEI_td9LBUyqVUe0xK",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050881,
        "hostOnly": False,
        "httpOnly": True,
        "name": "SSID",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "AmlwXHnQvOQ10LVd-",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050959,
        "hostOnly": False,
        "httpOnly": False,
        "name": "__Secure-1PAPISID",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "mfeuiC-HraNJ-A03/ASXvCPNJSw7yTFgd6",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050795,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__Secure-1PSID",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "g.a000kwibeLUu8Ea9Y-vLun7u3kU5VNJVuMAZl_jdfJaNm50JyDBBrlk7lRpKQGywAHEon7WGQAACgYKAQsSARQSFQHGX2MirAmnSRdZl6GPG6KLd4hOihoVAUF8yKoV17Tcj1a_OenIOkf2wBjO0076",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050993,
        "hostOnly": False,
        "httpOnly": False,
        "name": "__Secure-3PAPISID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "mfeuiC-HraNJ-A03/ASXvCPNJSw7yTFgd6",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1750420959.974815,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__Secure-3PSIDCC",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "AKEyXzXM5UjKUEXwSHVmRAIo6hGHA4G63adj3EE1VdNriD0f38jZQbsUKiD4LQbA3BValmTFDg",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1750420958.397647,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__Secure-3PSIDTS",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "sidts-CjIB3EgAEkYL2L-GfrEzW5Dfy62S9oefGNLgst78S_986htCnGcfkxECch_9oz-qytSsZBAA",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050908,
        "hostOnly": False,
        "httpOnly": False,
        "name": "APISID",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "IlQWLPjdNqziwCrV/ANG7Z4x5FF-IBxbZk",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753434620.050855,
        "hostOnly": False,
        "httpOnly": True,
        "name": "HSID",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "AasA7hmRuTFv7vjoq",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753435873.577793,
        "hostOnly": False,
        "httpOnly": True,
        "name": "LOGIN_INFO",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "AFmmF2swRAIgf4gadACOuWOcipI1anW-dakEjtidNLkufnOC8uml7EECIDh2YisqWELDBJPTGUysCucJ3I0wjXxYjVHro1LHrdW0:QUQ3MjNmd2Jiajl3OWZYRnpFNnZlWWV5ZGJWZ0hpcmp4LVVPU280bk4zOS03Z0ozZG9fOFhWZ0dXaVo3NG1wTEg1b3hGaG10TFBlaFBnTlJfbER5bEp0aFhoNS1OLVhYNFRZT2F6ajgzOFpDbGhlUjZpMWRETlFFRjFfTTRiM0RnNTROSkdmMTFMVjFic1VuZ2trbGp4aktDa0JJUC1BWDh3",
    },
    {
        "domain": ".youtube.com",
        "expirationDate": 1753444956.555608,
        "hostOnly": False,
        "httpOnly": False,
        "name": "PREF",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "f4=4000000&f6=40000000&tz=Europe.Paris&f5=30000&f7=100",
    },
]

COOKIES_LIST += [
    {
        "domain": ".www.researchgate.net",
        "hostOnly": False,
        "httpOnly": True,
        "name": "isInstIp",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "False",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1734423981,
        "hostOnly": False,
        "httpOnly": False,
        "name": "__eoi",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "ID=c26f752377373146:T=1718871981:RT=1718884914:S=AA-AfjZw-T_OOX2kW2LLaFzXImgc",
    },
    {
        "domain": ".www.researchgate.net",
        "expirationDate": 1753444909.646103,
        "hostOnly": False,
        "httpOnly": True,
        "name": "ptc",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "RG1.8947708639250500550.1718872043",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1750507578,
        "hostOnly": False,
        "httpOnly": False,
        "name": "euconsent-v2-didomi",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "CQAgmoAQAgmoAAHABBENA5EsAP_gAEPgAAYgJ2pB5G5UTWlBIG53YMskIAUFhFBoQEAgAACAAwIBSBIAIIwEAGAAIAgAICACAAIAIBIAIABAGAAAAAAAYIAAIAAIAAAQIAAKIAAAAAAAAgBQAAgIAgggEAAAgEBEABAAgAAAEIIAQNgACgAAACCAAAAAAAABAAAAAAAAQAAAAAAAYCQAAAJIAAAAACAIABAIAAAAAAAAAAAAAAAABBAAIJ2wPIAFAAXABQAFQALgAcAA8ACAAEgALwAZAA0ACIAEcAJgAUgAqgBcADEAGgAPQAfgBEACOAE4AMMAZYA0QBsgDkAHOAO4AfsBBwEIAItARwBHQC6gHUAO2Ae0A_4CHQEXgJ2AUOAo8BT4CpQFqALYAXmAwQBkgDLAGXANjAhCBG8CbAE3gJ1gTtAA.f_wACHwAAAAA",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1718885236,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_gat",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "1",
    },
    {
        "domain": "www.researchgate.net",
        "expirationDate": 1721477183,
        "hostOnly": True,
        "httpOnly": False,
        "name": "_pbjs_userid_consent_data",
        "path": "/",
        "sameSite": "lax",
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "3524755945110770",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1752567981,
        "hostOnly": False,
        "httpOnly": False,
        "name": "__gads",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "ID=eca2adb88969c830:T=1718871981:RT=1718884914:S=ALNI_MY2qZchynrhWX6hWMlaI87Pcj9riQ",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1718886709.646173,
        "hostOnly": False,
        "httpOnly": True,
        "name": "__cf_bm",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "IkQ_J4ciBzKQduRvjqsfSmQu8UygDWbHeROO5JVccfo-1718884909-1.0.1.1-qvNGEdbfI0HfhFP6kwe7R7mkTqODNhFuKhs72lLly6K2BOPMG3kbahpQFGvPK0U8FUfkznkq65gngd1sWj7sDA",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1752567981,
        "hostOnly": False,
        "httpOnly": False,
        "name": "__gpi",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "UID=00000e4e9aa2e6f2:T=1718871981:RT=1718884914:S=ALNI_MYFNrgzkKn7K6Bd2y8hC6GJCvDiSg",
    },
    {
        "domain": ".researchgate.net",
        "hostOnly": False,
        "httpOnly": True,
        "name": "_cfuvid",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "_GPmGZkBymiH3UiqTqzakEpi98br3nfFUWC2_u_wqkc-1718884909785-0.0.1.1-604800000",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1753445177.271667,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GA1.1.1525244793.1718885177",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1753445177.271482,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga_4P31SJ70EJ",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GS1.1.1718885177.1.0.1718885177.0.0.0",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1718971576,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_gid",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GA1.2.854907463.1718885177",
    },
    {
        "domain": ".www.researchgate.net",
        "expirationDate": 1750407982.506505,
        "hostOnly": False,
        "httpOnly": True,
        "name": "did",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "1dWLO3C6am8l667Q4VUlBo0O1LI49Qi2Vw21SJEXHavBDYT56DI9007W5rYGVFVH",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1750507578,
        "hostOnly": False,
        "httpOnly": False,
        "name": "didomi_token",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "eyJ1c2VyX2lkIjoiMTkwMzU4YTUtNWU2My02Y2UzLWJlNzAtZGFjNzVmYjdiY2ExIiwiY3JlYXRlZCI6IjIwMjQtMDYtMjBUMTI6MDY6MTYuODA2WiIsInVwZGF0ZWQiOiIyMDI0LTA2LTIwVDEyOjA2OjE4Ljc4MVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsidHdpdHRlciIsImdvb2dsZSIsImM6bGlua2VkaW4tbWFya2V0aW5nLXNvbHV0aW9ucyIsImM6b3duZXJpcSIsImM6b21uaXR1cmUtYWRvYmUtYW5hbHl0aWNzIiwiYzp0ZWNobm9yYXRpLW1lZGlhIiwiYzppbnRlcmNvbSIsImM6aW50ZW50LWlxIiwiYzppcHJvbSIsImM6bGlua2VkaW4iLCJjOmFtYXpvbmFkdi16Y1hGTEI2WCIsImM6bWVkaWFuZXQtY1V3YUtFNnoiLCJjOmluZGV4ZXhjaC1OWkNRTTY4UCIsImM6emVvdGFwZ21iLWQ3YndtdGp3IiwiYzp0cmlwbGVsaWYtZGRKSDM0clkiLCJjOnJ0YmhvdXNlLWI4Y2RIOHRNIiwiYzptZHByaW1pcy1lYU4yOVdjUCIsImM6bG9vcG1lbGktVGRhWXRCUHEiLCJjOm1hZ25pdGVpbi05d1RZTHFSRCIsImM6Ymlkc3dpdGNoLWQ2N0V3N1c5IiwiYzpvcmFjbGVhZHYtcUhlREptQUwiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiIsImM6bG90YW1lc29sLURIaTdMUmpNIiwiYzpuZXh0bWlsbGUtR0pyZlg4VWMiLCJjOm5yaWNodGVjLXFVVlEyUlFxIiwiYzpicml0ZXBvb2wtQldWeVdHeVUiLCJjOnRhcGFkaW5jLXFxY2tVN1BXIiwiYzppZDV0ZWNobi16Tk1KNGR3ZiIsImM6bWljcm9zb2Z0IiwiYzpwZXJtdXRpdmUtSjdpaHJlTWsiLCJjOm9wZXJhc29mdC1CY1hjRFZKTSIsImM6cG9zdGhvZy1Cakp4RmRGOSJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJnZW9sb2NhdGlvbl9kYXRhIiwiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyJdfSwidmVuZG9yc19saSI6eyJlbmFibGVkIjpbImdvb2dsZSIsImM6b3BlcmFzb2Z0LUJjWGNEVkpNIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkRIU0FvQUZrQWNnQTVnSHFnUUhBeGdCNndEMTRJR0FRTkFqMEJJd0NTY0VyQUtCd1YtZ3MxQmgwREc0R09nQUEuREhTQW9BRmtBY2dBNWdIcWdRSEF4Z0I2d0QxNElHQVFOQWowQkl3Q1NjRXJBS0J3Vi1nczFCaDBERzRHT2dBQSJ9",
    },
    {
        "domain": ".www.researchgate.net",
        "hostOnly": False,
        "httpOnly": True,
        "name": "hasPdpNext",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "False",
    },
    {
        "domain": ".researchgate.net",
        "expirationDate": 1750421183,
        "hostOnly": False,
        "httpOnly": False,
        "name": "ph_phc_ma1XTQyee96N1GML6qUTgLQRiDifnRcE9STiHTZ0CfZ_posthog",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "%7B%22distinct_id%22%3A%220190358a-56a1-7313-83b0-d13dddeac787%22%2C%22%24sesid%22%3A%5B1718885183223%2C%220190358a-56a1-7313-83b0-d13b2b87778d%22%2C1718885176993%5D%2C%22%24session_is_sampled%22%3Atrue%7D",
    },
    {
        "domain": ".www.researchgate.net",
        "hostOnly": False,
        "httpOnly": True,
        "name": "sid",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "qmH5Lc4f0CUJ3zeaxORcV0S8I8V1MuCFZtcIQqPYtv1XPejrbSLAQRbT50PL40TqeKQ1XsQDWt9gtYVzuL80bRmPjw6jn3cQ0ikNqW40maHcQ3JL2Vfa8ZZf0j7p35eJ",
    },
]

COOKIES_LIST += [
    {
        "domain": "github.com",
        "hostOnly": True,
        "httpOnly": True,
        "name": "_gh_sess",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "P%2Fmof1avuqwHaUQUIJR%2FZYn7jqbT7lgGuTGjp1BGAFIG5UpNDusEE3b8dRjz0eATE5xPdPjLYFqMs%2FI9AOalKX4YuYfSEEnxCMawU01099b4o9Xzzcv%2BmecrmO0Q8q%2Bdq1h8SIv6nvPP7HzlFesl8ysafb9b%2F0q6dTArKdSOurasza8UgLSYD08ofA50Pcm0IG7CTzF8ZCizrGgGTMi%2F%2B7L3E17jav5PM1Sf2vQKg15Gbg1QIOppJJHzlufgQoZigqFv%2BWznaws0Tt7Y2lSFCw%3D%3D--CJRhqMXJnwOaJgk4--DhUErlL4GdROikEjKD4O9g%3D%3D",
    },
    {
        "domain": ".github.com",
        "expirationDate": 1750408875.763785,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_octo",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "GH1.1.728652011.1718872875",
    },
    {
        "domain": ".github.com",
        "expirationDate": 1750408875.763926,
        "hostOnly": False,
        "httpOnly": True,
        "name": "logged_in",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": False,
        "storeId": None,
        "value": "no",
    },
    {
        "domain": ".github.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "preferred_color_mode",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "dark",
    },
    {
        "domain": ".github.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "tz",
        "path": "/",
        "sameSite": "lax",
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "Europe%2FParis",
    },
]

COOKIES_LIST += [
    {
        "domain": ".web.archive.org",
        "expirationDate": 1718886430,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_gat",
        "path": "/web/20201123221659/http://orcid.org/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "1",
    },
    {
        "domain": ".web.archive.org",
        "expirationDate": 1718972770,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_gid",
        "path": "/web/20201123221659/http://orcid.org/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GA1.2.402246368.1606169825",
    },
    {
        "domain": ".web.archive.org",
        "expirationDate": 1753446370.315621,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga",
        "path": "/web/20201123221659/http://orcid.org/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GA1.2.1301409987.1606169825",
    },
    {
        "domain": ".web.archive.org",
        "expirationDate": 1750422367,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_hjid",
        "path": "/web/20201123221659/http://orcid.org/",
        "sameSite": "lax",
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "07f80263-a631-4bf4-8ffd-8fc8912085e2",
    },
    {
        "domain": ".web.archive.org",
        "expirationDate": 1718888167,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_hjFirstSeen",
        "path": "/web/20201123221659/http://orcid.org/",
        "sameSite": "lax",
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "1",
    },
]
COOKIES_LIST += [
    {
        "domain": "orcid.org",
        "hostOnly": True,
        "httpOnly": False,
        "name": "AWSELBCORS",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "CBD1D7FF1216388FA48838CBCA4774FD22800B8FB548A40EF92BB0994D5B77A8410307CDEAA69C52236663F2BF89B252C17BC0FCDF790FD59771BDDF6EA8CA4CFD29D8733F",
    },
    {
        "domain": ".orcid.org",
        "expirationDate": 1753452454.637671,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga_9R61FWK9H5",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GS1.1.1718892454.1.0.1718892454.0.0.0",
    },
    {
        "domain": ".orcid.org",
        "expirationDate": 1753452454.63421,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "GA1.1.2021310691.1718892455",
    },
    {
        "domain": "orcid.org",
        "hostOnly": True,
        "httpOnly": False,
        "name": "AWSELB",
        "path": "/",
        "sameSite": None,
        "secure": False,
        "session": True,
        "storeId": None,
        "value": "CBD1D7FF1216388FA48838CBCA4774FD22800B8FB548A40EF92BB0994D5B77A8410307CDEAA69C52236663F2BF89B252C17BC0FCDF790FD59771BDDF6EA8CA4CFD29D8733F",
    },
    {
        "domain": ".orcid.org",
        "expirationDate": 1750428454,
        "hostOnly": False,
        "httpOnly": False,
        "name": "OptanonAlertBoxClosed",
        "path": "/",
        "sameSite": "lax",
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "2024-06-20T14:07:34.583Z",
    },
    {
        "domain": ".orcid.org",
        "expirationDate": 1750428454,
        "hostOnly": False,
        "httpOnly": False,
        "name": "OptanonConsent",
        "path": "/",
        "sameSite": "lax",
        "secure": False,
        "session": False,
        "storeId": None,
        "value": "isGpcEnabled=0&datestamp=Thu+Jun+20+2024+16%3A07%3A34+GMT%2B0200+(heure+d%E2%80%99%C3%A9t%C3%A9+d%E2%80%99Europe+centrale)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=False&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1",
    },
    {
        "domain": "orcid.org",
        "hostOnly": True,
        "httpOnly": False,
        "name": "XSRF-TOKEN",
        "path": "/",
        "sameSite": None,
        "secure": True,
        "session": True,
        "storeId": None,
        "value": "6957be7a-bcb4-4d59-a522-ea9b6b210ed9",
    },
]

# Create a RequestsCookieJar instance
COOKIES = RequestsCookieJar()

# Add cookies to the jar
for cookie in COOKIES_LIST:
    COOKIES.set(cookie["name"], cookie["value"], domain=cookie["domain"], path=cookie["path"])
