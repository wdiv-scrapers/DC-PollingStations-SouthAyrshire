from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


search_url = "https://opendata.arcgis.com/api/v2/datasets?filter%5Bcatalogs%5D=maps-south-ayrshire.opendata.arcgis.com&include=organizations%2Cgroups&page%5Bnumber%5D=1&page%5Bsize%5D=10&q=polling&sort=-updatedAt"
stations_url = "https://opendata.arcgis.com/datasets/72bef698f90b4da7b28ee403598e4403_29.geojson"
districts_url = "https://opendata.arcgis.com/datasets/80572b43c4b24d73ad2c4851aaeb9151_30.geojson"
council_id = 'S12000028'


search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape()
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='objectid')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='objectid')
districts_scraper.scrape()
