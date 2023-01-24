from urllib.parse import urlparse,parse_qs,urlencode
import json


URL = 'https://api.bukalapak.com/multistrategy-products?keywords=laptop+gaming&sort=date&limit=30&offset=0&facet=true&page=1&shouldUseSeoMultistrategy=false&isLoggedIn=false&show_search_contexts=true&access_token=6pcEtc5OgZigIt9Wp--DPm8rQ9QFp1C95lSkzLzKkxRNkQ'


def parse_new_url(url,next_page_number,offset_page_increment):
    url_parsed = urlparse(url=url)
    query_string = parse_qs(url_parsed.query)
    page_query_state = json.loads(query_string.get('page')[0])
    offset_query_state = json.loads(query_string.get('offset')[0])

    page_query_state = next_page_number 
    offset_query_state = offset_page_increment

    query_string.get('page')[0] = page_query_state
    query_string.get('offset')[0] = offset_query_state
    
    encoded_qs=urlencode(query_string,doseq=1) 
    new_url = f'https://api.bukalapak.com/multistrategy-products?{encoded_qs}'

    print(encoded_qs)

    return new_url