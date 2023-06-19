import requests
import streamlit as st

website_url = [
    'https://booking.miaherbalbeauty.in',
    'https://clickshare-lp.tltechnologies.net',
    'https://gopetz-lp.tltechnologies.net',
    'https://KeralaDrives.tltechnologies.net',
    'https://booking.KeralaDrives.com',
    'https://cactus-salonspa.tltechnologies.net',
    'https://booking.cactus-salonspa.com',
    'https://foodizone.shop',
    'https://theproteinhub.in',
    'https://apply.crayonsthecreativeschool.in',
    'https://crayonsthecreativeschool.in',
    'https://gopalmedicals.in',
    'https://apply.studyabroadnetworks.com',
    'https://studyabroadnetworks.com',
    'https://JobCard.tltechnologies.net',
    'https://champions.tltechnologies.net',
    'http://cp.tsoatchampions.com',
    'http://ams.tsoatchampions.com',
    'https://www.tsobriargrove.org',
    'https://cp.tsobriargrove.org',
    'https://ams.tsobriargrove.org',
    'http://tlclickshare.com',
    'https://KeralaDrives.com',
    'https://booking.KeralaDrives.com',
    'https://cactus-salonspa.com',
    'https://completeeyecarechampions.com',
    'http://cpadmin.completeeyecarechampions.com',
    'https://ams.completeeyecarechampions.com',
    'https://eyeloungebriargrove.com',
    'http://cpadmin.eyeloungebriargrove.com',
    'https://ams.eyeloungebriargrove.com',
    'https://booking.miaherbalbeauty.in',
    'https://KeralaDrives.com',
    'https://booking.KeralaDrives.com',
    'https://cactus-salonspa.com',
    'https://foodizone.shop',
    'https://theproteinhub.in',
    'https://apply.crayonsthecreativeschool.in',
    'https://crayonsthecreativeschool.in',
    'https://gopalmedicals.in',
    'https://apply.studyabroadnetworks.com',
    'https://studyabroadnetworks.com',
    'https://slp.tltechnologies.net',
    'https://bakery.tltechnologies.net'    
]

statuses = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable",
    403: "Forbidden response",
    522: "Connection Timeout Error",
    530: "The site is frozen"
}

status_counts = {status: 0 for status in statuses.values()}
status_counts['Request Exception'] = 0  # Initialize count for 'Request Exception'

st.title("Website Status Counts")

for index, url in enumerate(website_url, start=1):
    try:
        web_response = requests.get(url)
        status_code = web_response.status_code
        status = statuses.get(status_code, "Unknown Status")
        status_counts[status] += 1
        st.write(f"{index}. {url}: {status}")
    except requests.exceptions.RequestException:
        status = "Request Exception"
        status_counts[status] += 1
        st.write(f"{index}. {url}: {status}")

st.title("Website Status Counts")
for status, count in status_counts.items():
    st.write(f"{status}: {count}")
