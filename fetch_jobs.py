
import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

if not APP_ID or not APP_KEY:
    raise ValueError("Check ADZUNA_APP_ID and ADZUNA_APP_KEY in your .env file.")

# Search terms covering different IT roles
SEARCH_TERMS = [
    "IT jobs",
    "software developer",
    "data analyst",
    "data scientist",
    "Python developer",
    "Java developer",
    "web developer",
    "software tester",
    "QA engineer",
    "DevOps engineer",
    "cloud engineer",
    "cybersecurity",
    "IT support",
    "network engineer",
    "database administrator",
    "data engineer",
    "machine learning engineer",
    "business intelligence analyst",
]

COUNTRY = "in"
RESULTS_PER_PAGE = 50
MAX_PAGES = 3  # Start small; increase after testing

all_jobs = []
seen_ids = set()

url_template = (
    "https://api.adzuna.com/v1/api/jobs/"
    + COUNTRY
    + "/search/{}"
)

for term in SEARCH_TERMS:
    print(f"\nSearching for: {term}")

    for page in range(1, MAX_PAGES + 1):
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": RESULTS_PER_PAGE,
            "what": term,
            "category": "it-jobs",
            "content-type": "application/json",
        }

        try:
            response = requests.get(
                url_template.format(page),
                params=params,
                timeout=30,
            )

            if response.status_code != 200:
                print(
                    f"Request failed for '{term}', page {page}: "
                    f"{response.status_code}"
                )
                print(response.text[:300])
                break

            data = response.json()
            jobs = data.get("results", [])

            print(f"Page {page}: {len(jobs)} results")

            if not jobs:
                break

            for job in jobs:
                job_id = job.get("id")

                # Skip duplicate listings
                if job_id is not None and str(job_id) in seen_ids:
                    continue

                if job_id is not None:
                    seen_ids.add(str(job_id))

                company = job.get("company") or {}
                location = job.get("location") or {}
                category = job.get("category") or {}

                all_jobs.append({
                    "job_id": job_id,
                    "search_term": term,
                    "title": job.get("title"),
                    "company": company.get("display_name"),
                    "location": location.get("display_name"),
                    "category": category.get("label"),
                    "created": job.get("created"),
                    "salary_min": job.get("salary_min"),
                    "salary_max": job.get("salary_max"),
                    "salary_is_predicted": job.get(
                        "salary_is_predicted"
                    ),
                    "contract_type": job.get("contract_type"),
                    "contract_time": job.get("contract_time"),
                    "description": job.get("description"),
                    "job_url": job.get("redirect_url"),
                })

            time.sleep(1)

        except requests.exceptions.RequestException as error:
            print(f"Network/API error: {error}")
            break

# Save the combined dataset
if all_jobs:
    df = pd.DataFrame(all_jobs)

    os.makedirs("data", exist_ok=True)
    output_file = "data/it_jobs_india.csv"

    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print("\n--- COLLECTION SUMMARY ---")
    print("Unique jobs collected:", len(df))
    print("Search terms used:", len(SEARCH_TERMS))
    print("Saved to:", output_file)
    print("\nSample job titles:")
    print(df["title"].head(10).to_string(index=False))

else:
    print("No jobs collected. Check the API response and credentials.")