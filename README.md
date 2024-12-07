# Content rating function
Text content rating function

To run the function, use this request example:

```
curl -X POST "https://function-url" \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic <TOKEN>" \
  -d '{"content": "The fucking text you want to analyze goes here."}'
```

Response example:
```
{"rating":2}
```

