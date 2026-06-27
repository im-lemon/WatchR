import requests #type:ignore
import bs4

def scrape(link):
    if link.endswith(".mp4") or link.endswith(".avi") or link.endswith(".webm") or link.endswith(".mov"):
        r=requests.get(link, stream=True)
        fn = r.headers.get("Content-Disposition")
        
        with open(fn, 'wb') as f:
            for ch in r.iter_content(chunk_size=8192):
                if ch:
                    f.write(ch)

    r = requests.get(link)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    print(r.status_code)
    
    video = soup.find("video")

    fn = r.headers.get("Content-Disposition")

    vid=requests.get(fn, stream=True)
    with open(fn, 'wb') as f:
        for ch in vid.iter_content(chunk_size=8192):
            f.write(ch)