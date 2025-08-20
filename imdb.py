from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")

movies = driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")

movie_list = []
for movie in movies:
    try:
        title = movie.find_element(By.CSS_SELECTOR, "h3").text
        year = movie.find_elements(By.CSS_SELECTOR, ".cli-title-metadata-item")[0].text
        rating = movie.find_element(By.CSS_SELECTOR, ".ipc-rating-star--rating").text
        movie_list.append([title, year, rating])
    
    except:
        continue

df = pd.DataFrame(movie_list, columns=["Title", "Year", "Rating"])
df.to_csv("imdb_top_.csv", index=False)

driver.quit()

print("All 250 movies saved ")
