import requests

def test_index_page():
    # URL of the index page
    url = 'http://localhost:8000/index.html'
    
    try:
        # Send a GET request to the index page
        response = requests.get(url)

        # Check if the response status code is 200 (OK)
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

        # Check if the response contains specific content (modify as needed)
        assert "<title>Mohammed Umar</title>" in response.text, "Page title not found in index.html"

        print("Test passed: index.html is served correctly.")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, "Request to index.html failed"

if __name__ == "__main__":
    test_index_page()
