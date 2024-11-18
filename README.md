# content-rating-function
Serverless function to return a rating of a text content, implemented in Python

# Content rating calculation function
Text content calculation function

<img width="766" alt="image" src="https://github.com/user-attachments/assets/0cac4c96-1014-4bd2-977d-a1ecec388d31">


To run the function, use this request example:

```
curl -X POST "function-URL/actions/content-rating-fn?result=true" \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic <TOKEN>"
  -d '{"content": "The text you want to analyze goes here."}'
```

